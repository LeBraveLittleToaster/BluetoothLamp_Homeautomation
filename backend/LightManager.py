from LEDStrip import SingleStrip
from StripColorHSV import StripColorHSV
import uuid

class LightManager:
    def __init__(self):
        self.strips = {}

    def addStrip(self, ledStrip):
        stripID = uuid.uuid1()
        self.strips[stripID] = ledStrip
        return stripID

    def setStripTurnedOn(self, stripID, isOn):
        if stripID in self.strips:
            self.strips[stripID].setTurnedOn(isOn)
            return True
        else:
            return False

    def setStripColor(self, stripID, stripColorHSV):
        if stripID in self.strips:
            self.strips[stripID].setStripColor(stripColorHSV)
            return True
        else:
            return False
    
    def getAllStrips(self):
        return self.strips