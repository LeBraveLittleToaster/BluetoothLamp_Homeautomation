def filterStartParameter(valuelist):
    for i in range(1, len(valuelist)):
        if valuelist[i] == 35:
            valuelist[i] = 36
    return valuelist
 
 
class ModeOff:
 
    def __init__(self):
        self.networkMsg = [35,0,0,0,0,0,0,0]
 
    def getNetworkMsg(self):
        print("NetworkMsg: %s" , (self.networkMsg))
        return filterStartParameter(self.networkMsg)
 
class ModeSolidColor:
 
    def __init__(self, hue, saturation, value):
        self.networkMsg = [35,1]
        self.networkMsg.extend((hue, saturation, value,0,0,0)) # mode
 
    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)
 
class ModeColorrampSingleColor:
 
    def __init__(self, hue, saturation, value, speed):
        self.networkMsg = [35,2]
        self.networkMsg.extend((hue, saturation, value, speed,0,0)) # mode
 
    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)
 
class ModeColorrampMulticolor:
 
    def __init__(self, color_move_speed, color_shift_speed ):
        self.networkMsg = [35,3]
        self.networkMsg.extend((255,255,255,color_move_speed, color_shift_speed,0)) # mode
 
    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)
 
class ModeFlickerSingleColor:
 
    def __init__(self, hue, saturation, value, color_spawn_speed, color_spawn_amount):
        self.networkMsg = [35,4]
        self.networkMsg.extend((hue, saturation, value, color_spawn_speed, color_spawn_amount,0)) # mode
 
    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)
 
class ModeFlickerMultiColor:
 
    def __init__(self, color_spawn_speed, color_spawn_amount):
        self.networkMsg = [35,5]
        self.networkMsg.extend((255,255,255, color_spawn_speed, color_spawn_amount,0)) # mode
 
    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)
 
class ModePulse:
 
    def __init__(self, hue, saturation, value, pulse_speed):
        self.networkMsg = [35,6]
        self.networkMsg.extend((hue, saturation, value, pulse_speed,0,0)) # mode
 
    def getNetworkMsg(self):
        return filterStartParameter(self.networkMsg)