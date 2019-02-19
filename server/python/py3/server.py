import bluetooth
import time
import json

v0 = [0,127,0,0]
v1 = [127,0,0,1]
v2 = [0,0,127,2]

bluetoothSockets = []
port = 1

def readConfigFile():
    with open("led_strip_config.json") as f:
        json_data = json.load(f)
        for strip in json_data["strips"]:
            bluetoothSockets.append(LEDConnection(strip["mac_address"], strip["id"]))


class LEDConnection:
    def __init__(self, macAddress, id):
        self.macAddress = macAddress
        self.id = id
        self.isConnected = False

    def connect(self):
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            self.socket.connect((self.macAddress, port))
        except bluetooth.btcommon.BluetoothError:
            self.isConnected = True

    # r/g/b/mode (0-127)
    def sendColorValueWithMode(self,values):
        if not self.isConnected:
            close()
            connect()
        text = "#" + "".join(map(chr, values))
        try:
            self.socket.send(text)
        except bluetooth.btcommon.BluetoothError:
            self.isConnected = False

    def close(self):
        try:
            self.socket.close()
        except bluetooth.btcommon.BluetoothError:
            print ("Error closing socket...")
            
        
def startAndRunSockets():
    for socket in bluetoothSockets:
        socket.connect()
    time.sleep(3)
    while 1:
        for sock in bluetoothSockets:
            if sock.isConnected:
                sendColorValueWithMode(v0)
                time.sleep(3)
                sendColorValueWithMode(v1)
                time.sleep(3)
                sendColorValueWithMode(v2)
                time.sleep(3)


readConfigFile()
startAndRunSockets()

# try:
#     con1 = LEDConnection(serverMACAddress)
#     con1.connect()
#     while 1:
#         time.sleep(5)
#         con1.sendColorValueWithMode(v0)
#         time.sleep(5)
#         con1.sendColorValueWithMode(v1)
#         time.sleep(5)
#         con1.sendColorValueWithMode(v2)

# except bluetooth.btcommon.BluetoothError:
#     print ("Host down")

# con1.close()