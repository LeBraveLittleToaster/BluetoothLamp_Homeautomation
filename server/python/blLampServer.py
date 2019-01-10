import bluetooth
import sys
import getopt

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
  
def sendMessageTo(targetBluetoothMacAddress):
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send(sys.argv[0] + sys.argv[1] + sys.argv[2])
  sock.close()
  
def lookUpNearbyBluetoothDevices():
  nearby_devices = bluetooth.discover_devices()
  for bdaddr in nearby_devices:
    print str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]"
    if bdaddr == "98:D3:31:FC:79:0C":
      print "Sending ->hello!!<-" + " [" + str(bdaddr) + "]"
      sendMessageTo(bdaddr)

def sendToAllDevices():
  for address in allowed_devices:
    print str(bluetooth.lookup_name( address )) + " [" + str(address) + "]"
    sendMessageTo(address)

sendToAllDevices()