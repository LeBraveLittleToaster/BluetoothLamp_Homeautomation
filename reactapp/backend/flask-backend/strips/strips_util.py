import bluetooth
import json
from .modes import *
from flask import jsonify


class LedStripManager:

    sockets = []
    strips = []

    def __init__(self, strips):
        self.strips = strips["strips"]
        self.createBLSockets()

    def createBLSockets(self):
        i = 1
        for strip in self.strips:
            self.sockets.append(LEDStripSocket(strip, i))
            i += 1
        for socket in self.sockets:
            socket.connect()

    def merge_strips(self, strips):
        self.strips = strips
        return True

    def sendNetworkMsg(self):
        for strip, sock in zip(self.strips["strips"], self.sockets):
            print("Sending mode")
            sock.sendMode(self.getMode(strip["mode"]))

    def get_all_strips(self):
        return self.strips

    def one(self):
        return ModeOff()
    def two(self,mode):
        return ModeSolidColor(255,0,255)#mode["mode_color_h"], mode["mode_color_s"], mode["mode_color_v"])
    def three(self):
        return ModeOff()
    def four(self):
        return ModeOff()
    def five(self):
        return ModeOff()
    def six(self):    
        return ModeOff()

    def getMode(self, mode):
        print(mode)
        switcher = {
            0: self.one(),
            1: self.two(mode),
            2: self.three(),
            3: self.four(),
            4: self.five(),
            5: self.six()
        }
        return switcher.get(mode["mode_id"], ModeOff())

class LEDStripSocket:
    def __init__(self, strip, port):
        print(strip)
        self.serverMACAddress = strip["mac_address"]
        self.port = port

    def connect(self):
        self.s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            self.s.connect((self.serverMACAddress, self.port))
            print("Socket connected")
            return True
        except Exception as e:
            print(e)
            return False

    def sendMode(self, mode):
        for value in mode.getNetworkMsg():
            try:
                print("Sending value %s", (value))
                self.s.send(bytes([value]))
            except Exception as e:
                print(e)
                print("Failed to send message!")
    
    def close(self):
        self.s.close()
