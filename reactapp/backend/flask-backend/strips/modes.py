def filterStartParameter(valuelist):
    for i in range(1, len(valuelist)):
        if valuelist[i] == 35:
            valuelist[i] = 36
    return valuelist


class ModeOff:

    networkMsg = [35,0,0,0,0,0,0]

    def __init__(self):
        pass

    def getNetworkMsg(self):
        print("NetworkMsg: %s" , (self.networkMsg))
        return filterStartParameter(self.networkMsg)

class ModeSolidColor:

    networkMsg = [35,1]

    def __init__(self, hue, saturation, value):
        self.networkMsg.extend((hue, saturation, value,0,0,0)) # mode

    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)

class ModeColorrampSingleColor:

    networkMsg = [35,2]

    def __init__(self, hue, saturation, value, speed):
        self.networkMsg.extend((hue, saturation, value, speed,0,0)) # mode

    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)

class ModeColorrampMulticolor:

    networkMsg = [35,3]

    def __init__(self, color_move_speed, color_shift_speed ):
        self.networkMsg.extend((0,0,0,color_move_speed, color_shift_speed,0)) # mode

    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)

class ModeFlickerSingleColor:

    networkMsg = [35,4]

    def __init__(self, hue, saturation, value, color_spawn_speed, color_spawn_amount):
        self.networkMsg.extend((hue, saturation, value, color_spawn_speed, color_spawn_amount,0)) # mode

    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)

class ModeFlickerMultiColor:

    networkMsg = [35,5]

    def __init__(self, color_spawn_speed, color_spawn_amount):
        self.networkMsg.extend((0,0,0, color_spawn_speed, color_spawn_amount,0)) # mode

    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)

class ModePulse:

    networkMsg = [35,6]

    def __init__(self, hue, saturation, value, pulse_speed):
        self.networkMsg.extend((hue, saturation, value, pulse_speed,0,0)) # mode

    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)