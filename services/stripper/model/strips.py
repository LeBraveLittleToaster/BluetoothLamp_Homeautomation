import abc
from abc import ABC

from stripper.model.modes import Mode


class ControllableStrip(metaclass=abc.ABCMeta):

    def __init__(self, uuid: str):
        self.uuid = uuid

    @abc.abstractmethod
    def set_mode(self, mode: Mode):
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


class BluetoothStrip(ControllableStrip, ABC):
    def __init__(self, uuid: str, address_hex: str, ):
        super().__init__(uuid)

    def set_mode(self, mode: Mode):
        pass

    def connect(self):
        pass

    def reconnect(self):
        pass

    def disconnect(self):
        pass

