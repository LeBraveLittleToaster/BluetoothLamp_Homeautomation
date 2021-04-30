import abc
import time
from abc import ABC

import bluetooth
from objprint import add_objprint

from stripper.config.Config import BluetoothConOptions, MqttConOptions, GpioConOptions, ConType
from stripper.model.modes import Mode


class ControllableStrip(metaclass=abc.ABCMeta):

    def __init__(self, s_id: int, con_type: ConType):
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


@add_objprint(exclude=["bl_socket", "mode"])
class BluetoothStrip(ControllableStrip, ABC):
    def __init__(self, s_id: int, con_options: BluetoothConOptions, init_mode: Mode):
        super().__init__(s_id, ConType.BLUETOOTH)
        self.con_options: BluetoothConOptions = con_options
        self.bl_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.mode: Mode = init_mode

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


@add_objprint(exclude=["mode"])
class MqttStrip(ControllableStrip, ABC):
    def __init__(self, s_id: int, con_options: MqttConOptions, init_mode: Mode):
        super().__init__(s_id, ConType.MQTT)
        self.con_options: MqttConOptions = con_options
        self.mode: Mode = init_mode

    def set_mode(self, mode: Mode):
        self.mode = mode

    def send(self):
        print("Mqtt send mode called")

    def connect(self):
        print("MQTT send called")

    def reconnect(self):
        self.disconnect()
        time.sleep(5)
        self.connect()

    def disconnect(self):
        print("MQTT disconnect called")


@add_objprint(exclude=["mode"])
class GpioStrip(ControllableStrip, ABC):
    def __init__(self, s_id: int, con_options: GpioConOptions, init_mode: Mode):
        super().__init__(s_id, ConType.GPIO)
        self.con_options: GpioConOptions = con_options
        self.mode: Mode = init_mode

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
