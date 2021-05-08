import abc


class Mode:

    def __init__(self, mode_id: int):
        self.mode_id = mode_id

    @abc.abstractmethod
    def to_dict(self):
        pass

    @staticmethod
    def from_dict(data:dict):
        print("DATA:" + str(data))
        return get_mode(data)

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())

class ModeOff(Mode):

    def __init__(self):
        super().__init__(0)

    def to_dict(self):
        return {
            "mode_id": self.mode_id
        }


class ModeSolidColor(Mode):

    def __init__(self, hue, saturation, value):
        super().__init__(1)
        self.hue = hue
        self.saturation = saturation
        self.value = value

    def to_dict(self):
        return {"mode_id": self.mode_id, "hue": self.hue, "saturation": self.saturation, "value": self.value}


class ModeColorrampSingleColor(Mode):

    def __init__(self, hue, saturation, value, speed):
        super().__init__(2)
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.speed = speed

    def to_dict(self):
        return {"mode_id": self.mode_id, "hue": self.hue, "saturation": self.saturation, "value": self.value,
                "speed": self.speed}


class ModeColorrampMulticolor(Mode):

    def __init__(self, color_move_speed, color_shift_speed):
        super().__init__(3)

        self.color_move_speed = color_move_speed
        self.color_shift_speed = color_shift_speed

    def to_dict(self):
        return {"mode_id": self.mode_id, "hue": 255, "saturation": 255, "value": 255,
                "color_move_speed": self.color_move_speed, "color_shift_speed": self.color_shift_speed}


class ModeFlickerSingleColor(Mode):

    def __init__(self, hue, saturation, value, color_spawn_speed, color_spawn_amount):
        super().__init__(4)
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.color_spawn_speed = color_spawn_speed
        self.color_spawn_amount = color_spawn_amount

    def to_dict(self):
        return {"mode_id": self.mode_id, "hue": self.hue, "saturation": self.saturation, "value": self.value,
                "color_spawn_speed": self.color_spawn_speed, "color_spawn_amount": self.color_spawn_amount}


class ModeFlickerMultiColor(Mode):

    def __init__(self, color_spawn_speed, color_spawn_amount):
        super().__init__(5)

        self.color_spawn_speed = color_spawn_speed
        self.color_spawn_amount = color_spawn_amount

    def to_dict(self):
        return {"mode_id": self.mode_id, "hue": 255, "saturation": 255, "value": 255,
                "color_spawn_speed": self.color_spawn_speed, "color_spawn_amount": self.color_spawn_amount}


class ModePulse(Mode):

    def __init__(self, hue, saturation, value, pulse_speed):
        super().__init__(6)
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.pulse_speed = pulse_speed

    def to_dict(self):
        return {"mode_id": self.mode_id, "hue": self.hue, "saturation": self.saturation, "value": self.value,
                "pulse_speed": self.pulse_speed}


def get_mode(mode_options: dict) -> Mode:
    mode_id = mode_options["mode_id"]
    if mode_id == 0:
        return ModeOff()
    elif mode_id == 1:
        return ModeSolidColor(mode_options["hue"], mode_options["saturation"],
                              mode_options["value"])
    elif mode_id == 2:
        return ModeColorrampSingleColor(mode_options["hue"], mode_options["saturation"],
                                        mode_options["value"],
                                        mode_options["speed"])
    elif mode_id == 3:
        return ModeColorrampMulticolor(mode_options["speed"], mode_options["shift_speed"])
    elif mode_id == 4:
        return ModeFlickerSingleColor(mode_options["hue"], mode_options["saturation"],
                                      mode_options["value"],
                                      mode_options["spawn_speed"], mode_options["spawn_amount"])
    elif mode_id == 5:
        return ModeFlickerMultiColor(mode_options["spawn_speed"], mode_options["spawn_amount"])
    elif mode_id == 6:
        return ModePulse(mode_options["hue"], mode_options["saturation"], mode_options["value"],
                         mode_options["pulse_speed"])

    return ModeOff()
