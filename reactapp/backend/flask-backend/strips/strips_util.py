import bluetooth
import json
import time
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
        self.strips.clear()
        self.strips = strips
        return True

    def sendNetworkMsg(self):
        for strip, sock in zip(self.strips, self.sockets):
            sock.sendMode(self.getMode(strip["mode"]))

    def get_all_strips(self):
        return self.strips

    def getMode(self, mode):
        mode_id = mode["mode_id"]
        if mode_id == 0:
            return ModeOff()
        elif mode_id == 1: 
            return ModeSolidColor(mode["mode_color_h"], mode["mode_color_s"], mode["mode_color_v"])
        elif mode_id == 2:
            return ModeColorrampSingleColor(mode["mode_color_h"], mode["mode_color_s"], mode["mode_color_v"], mode["speed"])
        elif mode_id == 3:
            return ModeColorrampMultiColor(mode["speed"], mode["shift_speed"])
        elif mode_id == 4:
            return ModeFlickerSingleColor(mode["mode_color_h"], mode["mode_color_s"], mode["mode_color_v"], mode["spawn_speed"],mode["spawn_amount"])
        elif mode_id == 5:
            return ModeFlickerMultiColor(mode["spawn_speed"],mode["spawn_amount"])
        elif mode_id == 6:
            return ModePulse(mode["mode_color_h"], mode["mode_color_s"], mode["mode_color_v"], mode["pulse_speed"])
            
        return ModeOff()

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
        print("Send mode called")
        for value in mode.getNetworkMsg():
            try:
                print("Sending value %s", (value))
                self.s.send(bytes([value]))
            except Exception as e:
                print(e)
                print("Failed to send message!")
    
    def close(self):
        self.s.close()
