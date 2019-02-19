import bluetooth
import time

v0 = [0,127,0,0]
v1 = [127,0,0,1]
v2 = [0,0,127,2]

serverMACAddress = '98:d3:31:fd:89:ca'
port = 1

def sendValues(values):
    text = "#".join(map(chr, values))
    s.send(text)

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    time.sleep(5)
    sendValues(v0)
    time.sleep(5)
    sendValues(v1)
    time.sleep(5)
    sendValues(v2)
sock.close()