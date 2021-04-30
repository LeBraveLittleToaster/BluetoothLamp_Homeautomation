import bluetooth
import time
from stripper.model.modes import *


class LedStripManager:
    sockets = []
    strips = []

    def __init__(self, strips):
        self.strips = strips["strips"]
        self.create_bl_sockets()
        time.sleep(2)

    def create_bl_sockets(self):
        i = 1
        for strip in self.strips:
            self.sockets.append(LEDStripSocket(strip, 1))
            i += 1
        for socket in self.sockets:
            socket.connect()

    def reconnect_all(self):
        for socket in self.sockets:
            socket.reconnect()

    def merge_strips(self, strips):
        self.strips.clear()
        self.strips = strips
        return True

    def send_network_msg(self):
        for strip, sock in zip(self.strips, self.sockets):
            sock.send_mode(self.get_mode(strip["mode"]))

    def get_all_strips(self):
        return self.strips

    def get_mode(self, mode_options: dict):
        mode_id = mode_options["mode_id"]
        if mode_id == 0:
            return ModeOff()
        elif mode_id == 1:
            return ModeSolidColor(mode_options["mode_color_h"], mode_options["mode_color_s"],
                                  mode_options["mode_color_v"])
        elif mode_id == 2:
            return ModeColorrampSingleColor(mode_options["mode_color_h"], mode_options["mode_color_s"],
                                            mode_options["mode_color_v"],
                                            mode_options["speed"])
        elif mode_id == 3:
            return ModeColorrampMulticolor(mode_options["speed"], mode_options["shift_speed"])
        elif mode_id == 4:
            return ModeFlickerSingleColor(mode_options["mode_color_h"], mode_options["mode_color_s"],
                                          mode_options["mode_color_v"],
                                          mode_options["spawn_speed"], mode_options["spawn_amount"])
        elif mode_id == 5:
            return ModeFlickerMultiColor(mode_options["spawn_speed"], mode_options["spawn_amount"])
        elif mode_id == 6:
            return ModePulse(mode_options["mode_color_h"], mode_options["mode_color_s"], mode_options["mode_color_v"],
                             mode_options["pulse_speed"])

        return ModeOff()


class LEDStripSocket:
    def __init__(self, strip, port):
        self.s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        print(strip)
        self.serverMACAddress = strip["mac_address"]
        self.port = port

    def connect(self):
        try:
            self.s.connect((self.serverMACAddress, self.port))
            print("Socket connected")
            return True
        except Exception as e:
            print(e)
            try:
                print("Maybe not paired...retrying connection...")
                self.port = \
                    [_ for _ in bluetooth.find_service(address=self.serverMACAddress) if 'RFCOMM' in _['protocol']][0][
                        'port']
                self.s.connect((self.serverMACAddress, self.port))
                print("successfully connected on retry")
                return True
            except Exception as e2:
                print(e2)
                return False

    def send_mode(self, mode):
        print("Send mode called")
        for value in mode.get_network_msg():
            try:
                print("Sending value %s", value)
                self.s.send(bytes([value]))
            except Exception as e:
                print(e)
                print("Failed to send message!")

    def close(self):
        self.s.close()

    def reconnect(self):
        self.close()
        time.sleep(5)
        self.connect()
