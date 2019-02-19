import bluetooth
import time

serverMACAddress = '98:d3:31:fd:89:ca'
port = 1
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    text = "".join(map(chr, [112,52,52,250]))
    if text == "quit":
        break
    s.send(text)
    time.sleep(.4);
sock.close()
