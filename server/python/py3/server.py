import bluetooth
import time

v0 = [0,127,0,0]
v1 = [127,0,0,1]
v2 = [0,0,127,2]

serverMACAddress = '98:d3:31:fd:89:ca'
port = 1

class LEDConnection:
    def __init__(self, macAddress):
        self.macAddress = macAddress

    def connect(self):
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        s.connect((self.macAddress, port))

    def sendValues(values):
        text = "#" + "".join(map(chr, values))
        s.send(text)

con1 = LEDConnection(serverMACAddress)
con1.connect()

while 1:
    time.sleep(5)
    con1.sendValues(v0)
    time.sleep(5)
    con1.sendValues(v1)
    time.sleep(5)
    con1.sendValues(v2)
sock.close()