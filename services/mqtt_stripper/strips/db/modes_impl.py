from mqtt_stripper.strips.db.modes import Mode


class ModeSolidColor(Mode):

    def __init__(self, h, s, v, brightness):
        super().__init__(1)
        self.h = h
        self.s = s
        self.v = v
        self.brightness = brightness

    def to_dict(self):
        return {"mode_id": self.mode_id, "h": self.h, "s": self.s, "v": self.v, "brightness": self.brightness}

    def to_mqtt_dict(self):
        return {"mode_id": self.mode_id,
                "color": {"h": self.h, "s": self.s, "v": self.v, "brightness": self.brightness}, "options": {}}


class ModeSingleColorPulse(Mode):

    def __init__(self, h, s, v, brightness_start, brightness_end, speed):
        super().__init__(2)
        self.h = h
        self.s = s
        self.v = v
        self.brightness = brightness_start
        self.brightness_start = brightness_start
        self.brightness_end = brightness_end
        self.speed = speed

    def to_dict(self):
        return {"mode_id": self.mode_id, "h": self.h, "s": self.s, "v": self.v, "brightness": self.brightness_start,
                "brightness_start": self.brightness_start, "brightness_end": self.brightness_end, "speed": self.speed
                }

    def to_mqtt_dict(self):
        return {"mode_id": self.mode_id, "h": self.h, "s": self.s, "v": self.v, "brightness": self.brightness_start,
                "options": {
                    "brightness_start": self.brightness_start,
                    "brightness_end": self.brightness_end,
                    "speed": self.speed
                }}
