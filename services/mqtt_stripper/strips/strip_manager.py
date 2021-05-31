from typing import List, Optional

import paho.mqtt.client as mqtt

from mqtt_stripper.config.runnerconfig import RunnerConfig
from mqtt_stripper.network.MqttMessages import MqttModeMessage, MqttOnOffMessage
from mqtt_stripper.strips.db.device import Device
from mqtt_stripper.strips.db.mongo_connector import MongoConnector
import logging as log


def on_connect_mqtt(client, user_data, flags, rc):
    log.info("Connected with result code " + str(rc))


def on_disconnect_mqtt(client, user_data, rc):
    log.info("Disconnected with result code " + str(rc))


class DeviceManager:
    def __init__(self, mongo_con: MongoConnector, runner_config: RunnerConfig):
        self.mongo_con: MongoConnector = mongo_con
        self.runner_config: RunnerConfig = runner_config
        self.mqtt_client: mqtt.Client = mqtt.Client()
        self.mqtt_client.on_connect = on_connect_mqtt
        self.mqtt_client.on_disconnect = on_disconnect_mqtt
        self.mqtt_client.username_pw_set(self.runner_config.mqtt_username, self.runner_config.mqtt_password)

    def connect(self):
        log.info("Starting MQTT client...")
        self.mqtt_client.loop_start()
        log.info("Connecting to MQTT broker...")
        self.mqtt_client.connect(self.runner_config.mqtt_ip, self.runner_config.mqtt_port)

    def print(self):
        log.info("+++++++++++++")
        log.info("DEVICE_TYPES:")
        for e in self.mongo_con.get_device_list():
            log.info(e)
        log.info("+++++++++++++")
        log.info("+++++++++++++")
        log.info("Mood_TYPES:")
        for e in self.mongo_con.get_mood_list():
            log.info(e)
        log.info("+++++++++++++")

    def set_mood_mode(self, mood_uuid: str):
        log.info("Setting mood with mood_uuid: " + mood_uuid)
        mood = self.mongo_con.get_mood(mood_uuid)
        if mood is not None:
            devices: List[Device] = self.mongo_con.get_devices_in_id_list(
                list(map(lambda x: x.strip_uuid, mood.manipulators))
            )
            for manipulator in mood.manipulators:
                for device in devices:
                    if device.uuid == manipulator.strip_uuid:
                        log.info("Setting manipulator " + str(manipulator.to_dict()) + " to device_uuid: " + device.uuid)
                        self.mongo_con.update_device_mode(device.uuid, manipulator.mode)
                        self.mqtt_client.publish(device.input_topic, str(manipulator.mode.to_dict()))
        else:
            log.warning("Mood [" + mood_uuid + "] is not available")

    def set_is_on(self, device_uuid: str, is_on: bool):
        log.info("Setting is_on=" + str(is_on) + " to device_uuid: " + device_uuid)
        device: Optional[Device] = self.mongo_con.get_device(device_uuid)
        if device is not None:
            self.mongo_con.update_device_is_on(device_uuid, is_on)
            self.mqtt_client.publish(device.input_topic, MqttOnOffMessage(is_on).to_json())
        else:
            log.warning("No device: " + device_uuid + " in database")

    def set_mode(self, device_uuid: str, mode: dict):
        log.info("Setting mode: " + str(str(mode) + " to device_uuid: " + device_uuid))
        device: Optional[Device] = self.mongo_con.get_device(device_uuid)
        if device is not None:
            self.mongo_con.update_device_mode(device.uuid, mode)
            self.mqtt_client.publish(device.input_topic, MqttModeMessage(mode).to_json())
        else:
            log.warning("No device: " + device_uuid + " in database")