import time

import bluetooth

class LEDStripSocket:
    def __init__(self, address, port):
        self.s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.address = address
        self.port = port

    def connect(self):
        try:
            self.s.connect((self.address, self.port))
            print("Socket connected")
            return True
        except Exception as e:
            print(e)
            try:
                print("Maybe not paired...retrying connection...")
                self.port = \
                    [_ for _ in bluetooth.find_service(address=self.address) if 'RFCOMM' in _['protocol']][0][
                        'port']
                self.s.connect((self.address, self.port))
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
