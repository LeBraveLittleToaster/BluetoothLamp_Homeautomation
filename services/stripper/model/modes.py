def filter_start_parameter(valuelist):
    for i in range(1, len(valuelist)):
        if valuelist[i] == 35:
            valuelist[i] = 36
    return valuelist


class Mode:
    def get_network_msg(self):
        pass


class ModeOff(Mode):

    def __init__(self):
        self.networkMsg = [35, 0, 0, 0, 0, 0, 0, 0]

    def get_network_msg(self):
        print("NetworkMsg: %s", self.networkMsg)
        return filter_start_parameter(self.networkMsg)


class ModeSolidColor(Mode):

    def __init__(self, hue, saturation, value):
        self.networkMsg = [35, 1]
        self.networkMsg.extend((hue, saturation, value, 0, 0, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)


class ModeColorrampSingleColor(Mode):

    def __init__(self, hue, saturation, value, speed):
        self.networkMsg = [35, 2]
        self.networkMsg.extend((hue, saturation, value, speed, 0, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)


class ModeColorrampMulticolor(Mode):

    def __init__(self, color_move_speed, color_shift_speed):
        self.networkMsg = [35, 3]
        self.networkMsg.extend((255, 255, 255, color_move_speed, color_shift_speed, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)


class ModeFlickerSingleColor(Mode):

    def __init__(self, hue, saturation, value, color_spawn_speed, color_spawn_amount):
        self.networkMsg = [35, 4]
        self.networkMsg.extend((hue, saturation, value, color_spawn_speed, color_spawn_amount, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)


class ModeFlickerMultiColor(Mode):

    def __init__(self, color_spawn_speed, color_spawn_amount):
        self.networkMsg = [35, 5]
        self.networkMsg.extend((255, 255, 255, color_spawn_speed, color_spawn_amount, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)


class ModePulse(Mode):

    def __init__(self, hue, saturation, value, pulse_speed):
        self.networkMsg = [35, 6]
        self.networkMsg.extend((hue, saturation, value, pulse_speed, 0, 0))  # mode

    def get_network_msg(self):
        return filter_start_parameter(self.networkMsg)


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
