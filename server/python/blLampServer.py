import bluetooth
import sys
import struct
import argparse

allowed_devices = ["98:D3:31:FC:79:0C"]
port = 1

class DataStream(bytearray):

    def append(self, v, fmt='>B'):
        self.extend(struct.pack(fmt, v))

def receiveMessages():
  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
  port = 1
  server_sock.bind(("",port))
  server_sock.listen(1)
  
  client_sock,address = server_sock.accept()
  print "Accepted connection from " + str(address)
  
  data = client_sock.recv(1024)
  print "received [%s]" % data
  
  client_sock.close()
  server_sock.close()
  
def sendMessageTo(targetBluetoothMacAddress,r,g,b):
  print "Sending R=" + r + " G=" + g + " B=" + b
  x = DataStream()
  x.append(r)
  x.append(g)
  x.append(b)
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send(x)
  sock.close()
  
def lookUpNearbyBluetoothDevices():
  nearby_devices = bluetooth.discover_devices()
  for bdaddr in nearby_devices:
    print str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]"
    if bdaddr == "98:D3:31:FC:79:0C":
      print "Sending ->hello!!<-" + " [" + str(bdaddr) + "]"
      sendMessageTo(bdaddr)

def sendToAllDevices(r,g,b):
  for address in allowed_devices:
    print str(bluetooth.lookup_name( address )) + " [" + str(address) + "]"
    sendMessageTo(address, r,g,b)

def parseArgs():
  parser = argparse.ArgumentParser()
  parser.add_argument('-r', '--red')
  parser.add_argument('-g', '--green')
  parser.add_argument('-b', '--blue')
  args = parser.parse_args()
  r = None
  g = None
  b = None
  for o, a in args:
    print (o + " " + a)
    if o in ("-r", "--red"):
      r = a
    elif o in ("-g", "--green"):
      g = a
    elif o in ("-b", "--blue"):
      b = a
    else:
      assert False, "unhandled option"

  sendToAllDevices(r,g,b)

parseArgs()