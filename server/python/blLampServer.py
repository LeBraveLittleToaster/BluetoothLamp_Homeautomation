import bluetooth
import sys
import struct
import argparse

allowed_devices = ["98:D3:31:FC:79:0C"]
port = 1

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
  print "Sending message " + genMsg(r,g,b)
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send(genMsg(r,g,b))
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

def genMsg(r,g,b):
  return "#" + fillTo4Bytes(r) + fillTo4Bytes(g) + fillTo4Bytes(b)

def fillTo4Bytes(v):
  return struct.unpack("4b", struct.pack("I", v))

def parseArgs():
  parser = argparse.ArgumentParser()
  parser.add_argument('-r', required = True)
  parser.add_argument('-g', required = True)
  parser.add_argument('-b', required = True)
  args = parser.parse_args()
  r = int(args.r)
  g = int(args.g)
  b = int(args.b)


  sendToAllDevices(r,g,b)

parseArgs()