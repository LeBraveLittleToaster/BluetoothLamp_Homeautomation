import time
import unittest

from stripper.config.Config import MqttConOptions
from stripper.model.modes import ModeSolidColor, ModeOff
from stripper.model.strips import MqttStrip

con_opt = MqttConOptions("134.60.155.235", 1885, "topic/test/0", "admin", "omi-lul")
strip = MqttStrip(0, con_opt, ModeOff())


class TestStringMethods(unittest.TestCase):

    def test_strip_send(self):
        strip.connect()
        time.sleep(1)
        strip.set_mode(ModeSolidColor(255, 127, 0))
        strip.send()


if __name__ == '__main__':
    unittest.main()
