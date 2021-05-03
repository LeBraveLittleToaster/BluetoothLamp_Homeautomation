import abc
import time
import paho.mqtt.client as mqtt
from abc import ABC
import bluetooth
from objprint import add_objprint

from stripper.config.Config import BluetoothConOptions, MqttConOptions, GpioConOptions, ConType
from stripper.model.modes import Mode


class ControllableStrip(metaclass=abc.ABCMeta):

    def __init__(self, name: str, location: str, s_id: int, con_type: ConType):
        self.name = name
        self.location = location
        self.s_id = s_id
        self.con_type: ConType = con_type

    @abc.abstractmethod
    def set_mode(self, mode: Mode):
        pass

    @abc.abstractmethod
    def send(self):
        pass

    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def reconnect(self):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

    @abc.abstractmethod
    def to_dict(self):
        pass


@add_objprint(exclude=["bl_socket", "mode"])
class BluetoothStrip(ControllableStrip, ABC):
    def __init__(self, name: str, location: str, s_id: int, con_options: BluetoothConOptions, init_mode: Mode):
        super().__init__(name, location, s_id, ConType.BLUETOOTH)
        self.con_options: BluetoothConOptions = con_options
        self.bl_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.mode: Mode = init_mode

    def to_dict(self):
        return {"id": self.s_id, "con_type": str(ConType.BLUETOOTH), "location": self.location, "name": self.name,
                "mode": self.mode.to_dict()}

    def set_mode(self, mode: Mode):
        self.mode = mode

    def send(self):
        print("Send mode called")
        for value in self.mode.get_network_msg():
            try:
                print("Sending value %s", value)
                self.bl_socket.send(bytes([value]))
            except Exception as e:
                print(e)
                print("Failed to send message!")

    def connect(self):
        try:
            self.bl_socket.connect((self.con_options.address, self.con_options.port))
            print("Socket connected")
            return True
        except Exception as e:
            print(e)
            try:
                print("Maybe not paired...retrying connection...")
                self.con_options.port = \
                    [_ for _ in bluetooth.find_service(address=self.con_options.address) if 'RFCOMM' in _['protocol']][
                        0][
                        'port']
                self.bl_socket.connect((self.con_options.address, self.con_options.port))
                print("successfully connected on retry")
                return True
            except Exception as e2:
                print(e2)
                return False

    def reconnect(self):
        self.disconnect()
        time.sleep(5)
        self.connect()

    def disconnect(self):
        self.bl_socket.close()


def on_connect_mqtt(client, user_data, flags, rc):
    print("Connected with result code " + str(rc))


@add_objprint(exclude=["mode"])
class MqttStrip(ControllableStrip, ABC):
    def __init__(self, name: str, location: str, s_id: int, con_options: MqttConOptions, init_mode: Mode):
        super().__init__(name, location, s_id, ConType.MQTT)
        self.con_options: MqttConOptions = con_options
        self.mqtt_client: mqtt.Client = mqtt.Client()
        self.mqtt_client.on_connect = on_connect_mqtt
        self.mqtt_client.username_pw_set(self.con_options.username, self.con_options.password)
        self.mode: Mode = init_mode

    def to_dict(self):
        return {"id": self.s_id, "con_type": str(ConType.MQTT), "location": self.location, "name": self.name,
                "mode": self.mode.to_dict()}

    def set_mode(self, mode: Mode):
        self.mode = mode

    def send(self):
        print("Mqtt send mode " + str(self.mode.get_network_msg()) + " to topic: " + self.con_options.topic)
        self.mqtt_client.publish(self.con_options.topic, payload=bytes(self.mode.get_network_msg()), qos=1,
                                 retain=False)

    def connect(self):
        self.mqtt_client.connect(
            host=self.con_options.url,
            port=self.con_options.port,
            keepalive=60, )

    def reconnect(self):
        self.disconnect()
        time.sleep(5)
        self.connect()

    def disconnect(self):
        print("MQTT disconnect called")
        self.mqtt_client.disconnect()


@add_objprint(exclude=["mode"])
class GpioStrip(ControllableStrip, ABC):
    def __init__(self, name: str, location: str, s_id: int, con_options: GpioConOptions, init_mode: Mode):
        super().__init__(name, location, s_id, ConType.GPIO)
        self.con_options: GpioConOptions = con_options
        self.mode: Mode = init_mode

    def to_dict(self):
        return {"id": self.s_id, "con_type": str(ConType.GPIO), "location": self.location, "name": self.name,
                "mode": self.mode.to_dict()}

    def set_mode(self, mode: Mode):
        self.mode = mode

    def send(self):
        print("GPIO send mode called")

    def connect(self):
        print("GPIO send called")

    def reconnect(self):
        self.disconnect()
        time.sleep(5)
        self.connect()

    def disconnect(self):
        print("GPIO disconnect called")
