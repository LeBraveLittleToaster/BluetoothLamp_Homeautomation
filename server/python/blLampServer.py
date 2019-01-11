import bluetooth
import sys
import struct
import argparse
import time
import requests

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
  
def sendMessageTo(targetBluetoothMacAddress,r,g,b,m):
  print "Sending message "
  msg = parseMsg(r,g,b,m)
  print msg
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send(msg)
  sock.close()
  
def lookUpNearbyBluetoothDevices():
  nearby_devices = bluetooth.discover_devices()
  for bdaddr in nearby_devices:
    print str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]"
    if bdaddr == "98:D3:31:FC:79:0C":
      print "Sending ->hello!!<-" + " [" + str(bdaddr) + "]"
      sendMessageTo(bdaddr)

def sendToAllDevices(r,g,b,m):
  for address in allowed_devices:
    print str(bluetooth.lookup_name( address )) + " [" + str(address) + "]"
    sendMessageTo(address, r,g,b,m)

def parseMsg(r,g,b,m):
  l = 4
  x = "#" + fill(str(r), l) + fill(str(g), l) + fill(str(b), l) + fill(str(m), l)
  print x
  return buffer(x)

def fill(v, width):
  print v
  while len(v) < width:
    v = "0" + v;
  print v
  print "++++++++++"
  return v

def parseArgs():
  parser = argparse.ArgumentParser()
  parser.add_argument('-r', required = True)
  parser.add_argument('-g', required = True)
  parser.add_argument('-b', required = True)
  parser.add_argument('-m', required = True)
  args = parser.parse_args()
  r = int(args.r)
  g = int(args.g)
  b = int(args.b)
  m = int(args.m)

  run(r,g,b,m)

def collectData():
  r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
  print r.json()

def run(r,g,b,m):
  while True:
    time.sleep(2)
    collectData()
    sendToAllDevices(r,g,b,m);


parseArgs()