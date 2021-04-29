from typing import List

from stripper.config.Config import ConfigStrip, BluetoothConOptions, ConType, MqttConOptions, GpioConOptions
from stripper.model.modes import ModeOff
from stripper.model.strips import ControllableStrip, BluetoothStrip, MqttStrip, GpioStrip


def config_to_controllable_strip(config_strip: ConfigStrip) -> ControllableStrip:
    if config_strip.con_type == ConType.BLUETOOTH:
        return BluetoothStrip(
            config_strip.strip_id,
            config_strip.options,
            ModeOff())
    elif config_strip.con_type == ConType.MQTT:
        return MqttStrip(
            config_strip.strip_id,
            config_strip.options,
            ModeOff())
    elif config_strip.con_type == ConType.GPIO:
        return GpioStrip(
            config_strip.strip_id,
            config_strip.options,
            ModeOff())
    else:
        return BluetoothStrip(
            config_strip.strip_id,
            config_strip.options,
            ModeOff())


def convert_config_to_controllable_strips(config_strips: List[ConfigStrip]) -> List[ControllableStrip]:
    control_strips: List[ControllableStrip] = list(map(config_to_controllable_strip, config_strips))
    return control_strips
