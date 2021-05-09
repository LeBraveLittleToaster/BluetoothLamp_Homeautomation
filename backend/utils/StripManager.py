from typing import List, Optional, Mapping, Dict
import paho.mqtt.client as mqtt
from utils.Config import Config, Strip, MqttConOptions
from utils.runnerconfig import RunnerConfig


class StripValue:

    def __init__(self, strip_id: int, hue=0, brightness=0, speed=0, mode_id=0):
        self.hue = hue
        self.brightness = brightness
        self.speed = speed
        self.strip_id = strip_id
        self.mode_id = mode_id

    def update_all_values(self, hue: int, brightness: int, speed: int, mode_id: int):
        self.hue = hue
        self.brightness = brightness
        self.speed = speed
        self.mode_id = mode_id


def on_connect_mqtt(client, user_data, flags, rc):
    print("Connected with result code " + str(rc))


class StripManager:
    def __init__(self, strips: List[Strip], runner_config: RunnerConfig, strip_values=None):
        self.strips: List[Strip] = strips
        self.runner_config = runner_config
        self.selected_id: Optional[int] = None
        self.strip_values: Dict[int, StripValue] = strip_values \
            if strip_values is not None \
            else self.generate_empty_values(self.strips)
        self.mqtt_client: mqtt.Client = mqtt.Client()
        self.mqtt_client.on_connect = on_connect_mqtt
        self.mqtt_client.username_pw_set(self.runner_config.mqtt_username, self.runner_config.mqtt_password)

    def connect(self):
        self.mqtt_client.connect(self.runner_config.mqtt_ip, self.runner_config.mqtt_port)

    def select_id(self, strip_id: int) -> None:
        self.selected_id = strip_id

    @staticmethod
    def get_str_from_mode(mode_id:int):
        if mode_id == 1:
            return "Mode1"
        elif mode_id == 2:
            return "Mode2"
        elif mode_id == 3:
            return "Mode3"
        elif mode_id == 4:
            return 4
        else:
            return "Mode0"

    @staticmethod
    def get_mode_from_str(mode: str):
        if mode == "Mode1":
            return 1
        elif mode == "Mode2":
            return 2
        elif mode == "Mode3":
            return 3
        elif mode == "Mode4":
            return 4
        else:
            return 0

    def set_strip_value(self, strip_id: int, hue: int, brightness: int, speed: int, mode: str):
        strip_value = self.strip_values.get(strip_id, StripValue(strip_id))
        strip_value.update_all_values(hue, brightness, speed, self.get_mode_from_str(mode))
        self.send_to_mqtt(strip_id, hue, brightness, speed, self.get_mode_from_str(mode))

    def send_to_mqtt(self, strip_id: int, hue: int, brightness: int, speed: int, mode_id: int):
        strip = self.get_strip_by_id(strip_id)
        options: MqttConOptions = strip.options
        if self.mqtt_client.is_connected() is False:
            self.reconnect_mqtt()
        self.mqtt_client.publish(options.output_topic, str({
            "mode_id": mode_id,
            "hue": hue,
            "brightness": brightness,
            "speed": speed
        }))

    def reconnect_mqtt(self):
        self.mqtt_client.disconnect()
        self.connect()

    def get_or_add_strip_value_by_id(self, strip_id: int) -> StripValue:
        strip_value: Optional[StripValue] = self.strip_values.get(strip_id, None)
        if strip_value is None:
            strip_value = StripValue(strip_id)
            self.strip_values[strip_id] = strip_value
        return strip_value

    def get_strip_by_id(self, strip_id: int) -> Optional[Strip]:
        for strip in self.strips:
            if strip.strip_id == strip_id:
                return strip
        return None

    @staticmethod
    def generate_empty_values(strips: List[Strip]):
        values: Dict[int, StripValue] = dict()
        for strip in strips:
            values[strip.strip_id] = StripValue(strip.strip_id)
        return values
