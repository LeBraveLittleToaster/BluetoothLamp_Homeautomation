class SingleStrip:
    def __init__(self, stripColorHSV):
        self.id = id
        self.isOn = True
        self.stripColorHSV = stripColorHSV
    
    def setColor(self, stripColorHSV):
        self.stripColorHSV = stripColorHSV
        self.sendUpdate()

    def setStripTurnedOn(self, isOn):
        self.isOn = isOn

    def sendUpdate(self):
        print("Writing to bluetoothcon")