from typing import List, Optional

import paho.mqtt.client as mqtt

from mqtt_stripper.config.runnerconfig import RunnerConfig
from mqtt_stripper.network.MqttMessages import MqttModeMessage, MqttOnOffMessage
from mqtt_stripper.strips.db.device import Device
from mqtt_stripper.strips.db.modes import Mode
from mqtt_stripper.strips.db.mongo_connector import MongoConnector


def on_connect_mqtt(client, user_data, flags, rc):
    print("Connected with result code " + str(rc))


class StripManager:
    def __init__(self, mongo_con: MongoConnector, runner_config: RunnerConfig):
        self.mongo_con: MongoConnector = mongo_con
        self.runner_config: RunnerConfig = runner_config
        self.mqtt_client: mqtt.Client = mqtt.Client()
        self.mqtt_client.on_connect = on_connect_mqtt
        self.mqtt_client.username_pw_set(self.runner_config.mqtt_username, self.runner_config.mqtt_password)

    def connect(self):
        self.mqtt_client.connect(self.runner_config.mqtt_ip, self.runner_config.mqtt_port)

    def print(self):
        print("+++++++++++++")
        print("DEVICE_TYPES:")
        for e in self.mongo_con.get_device_list():
            print(e)
        print("+++++++++++++")
        print("+++++++++++++")
        print("Mood_TYPES:")
        for e in self.mongo_con.get_mood_list():
            print(e)
        print("+++++++++++++")

    def set_mood_mode(self, mood_uuid: str):
        mood = self.mongo_con.get_mood(mood_uuid)
        if mood is not None:
            devices: List[Device] = self.mongo_con.get_devices_in_id_list(
                list(map(lambda x: x.strip_uuid, mood.manipulators))
            )
            for manipulator in mood.manipulators:
                for device in devices:
                    if device.uuid == manipulator.strip_uuid:
                        self.mongo_con.update_device_mode(device.uuid, manipulator.mode)
                        self.mqtt_client.publish(device.input_topic, str(manipulator.mode.to_dict()))

    def set_is_on(self, device_uuid: str, is_on:bool):
        device: Optional[Device] = self.mongo_con.get_device(device_uuid)
        if device is not None:
            self.mongo_con.update_device_is_on(device_uuid, is_on)
            self.mqtt_client.publish(device.input_topic, MqttOnOffMessage(is_on).to_json())

    def set_mode(self, strip_uuid: str, mode: Mode):
        device: Optional[Device] = self.mongo_con.get_device(strip_uuid)
        if device is not None:
            self.mongo_con.update_device_mode(device.uuid, mode)
            self.mqtt_client.publish(device.input_topic, MqttModeMessage(mode).to_json())
