import abc


def filter_start_parameter(valuelist):
    for i in range(1, len(valuelist)):
        if valuelist[i] == 35:
            valuelist[i] = 36
    return valuelist


class Mode:
    @abc.abstractmethod
    def get_network_msg(self):
        pass

    @abc.abstractmethod
    def to_dict(self):
        pass


class ModeOff(Mode):

    def __init__(self):
        self.networkMsg = [35, 0, 0, 0, 0, 0, 0, 0]

    def get_network_msg(self):
        print("NetworkMsg: %s", self.networkMsg)
        return filter_start_parameter(self.networkMsg)

    def to_dict(self):
        return {"type": "MODE_OFF"}


class ModeSolidColor(Mode):

    def __init__(self, hue, saturation, value):
        self.networkMsg = [35, 1]
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.networkMsg.extend((hue, saturation, value, 0, 0, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)

    def to_dict(self):
        return {"type": "SOLID_COLOR", "hue": self.hue, "saturation": self.saturation, "value": self.value}


class ModeColorrampSingleColor(Mode):

    def __init__(self, hue, saturation, value, speed):
        self.networkMsg = [35, 2]
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.speed = speed
        self.networkMsg.extend((hue, saturation, value, speed, 0, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)

    def to_dict(self):
        return {"type": "COLOR_RAMP_SINGLE_COLOR", "hue": self.hue, "saturation": self.saturation, "value": self.value,
                "speed": self.speed}


class ModeColorrampMulticolor(Mode):

    def __init__(self, color_move_speed, color_shift_speed):
        self.networkMsg = [35, 3]
        self.color_move_speed = color_move_speed
        self.color_shift_speed = color_shift_speed
        self.networkMsg.extend((255, 255, 255, color_move_speed, color_shift_speed, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)

    def to_dict(self):
        return {"type": "COLOR_RAMP_MULTI_COLOR", "hue": 255, "saturation": 255, "value": 255,
                "color_move_speed": self.color_move_speed, "color_shift_speed": self.color_shift_speed}


class ModeFlickerSingleColor(Mode):

    def __init__(self, hue, saturation, value, color_spawn_speed, color_spawn_amount):
        self.networkMsg = [35, 4]
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.color_spawn_speed = color_spawn_speed
        self.color_spawn_amount = color_spawn_amount
        self.networkMsg.extend((hue, saturation, value, color_spawn_speed, color_spawn_amount, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)

    def to_dict(self):
        return {"type": "COLOR_RAMP_MULTI_COLOR", "hue": self.hue, "saturation": self.saturation, "value": self.value,
                "color_spawn_speed": self.color_spawn_speed, "color_spawn_amount": self.color_spawn_amount}


class ModeFlickerMultiColor(Mode):

    def __init__(self, color_spawn_speed, color_spawn_amount):
        self.networkMsg = [35, 5]
        self.color_spawn_speed = color_spawn_speed
        self.color_spawn_amount = color_spawn_amount
        self.networkMsg.extend((255, 255, 255, color_spawn_speed, color_spawn_amount, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)

    def to_dict(self):
        return {"type": "COLOR_RAMP_MULTI_COLOR", "hue": 255, "saturation": 255, "value": 255,
                "color_spawn_speed": self.color_spawn_speed, "color_spawn_amount": self.color_spawn_amount}


class ModePulse(Mode):

    def __init__(self, hue, saturation, value, pulse_speed):
        self.networkMsg = [35, 6]
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.pulse_speed = pulse_speed
        self.networkMsg.extend((hue, saturation, value, pulse_speed, 0, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)

    def to_dict(self):
        return {"type": "COLOR_RAMP_MULTI_COLOR", "hue": self.hue, "saturation": self.saturation, "value": self.value,
                "pulse_speed": self.pulse_speed}


def get_mode(mode_options: dict):
    mode_id = mode_options["mode_id"]
    if mode_id == 0:
        return ModeOff()
    elif mode_id == 1:
        return ModeSolidColor(mode_options["mode_color_h"], mode_options["mode_color_s"],
                              mode_options["mode_color_v"])
    elif mode_id == 2:
        return ModeColorrampSingleColor(mode_options["mode_color_h"], mode_options["mode_color_s"],
                                        mode_options["mode_color_v"],
                                        mode_options["speed"])
    elif mode_id == 3:
        return ModeColorrampMulticolor(mode_options["speed"], mode_options["shift_speed"])
    elif mode_id == 4:
        return ModeFlickerSingleColor(mode_options["mode_color_h"], mode_options["mode_color_s"],
                                      mode_options["mode_color_v"],
                                      mode_options["spawn_speed"], mode_options["spawn_amount"])
    elif mode_id == 5:
        return ModeFlickerMultiColor(mode_options["spawn_speed"], mode_options["spawn_amount"])
    elif mode_id == 6:
        return ModePulse(mode_options["mode_color_h"], mode_options["mode_color_s"], mode_options["mode_color_v"],
                         mode_options["pulse_speed"])

    return ModeOff()
