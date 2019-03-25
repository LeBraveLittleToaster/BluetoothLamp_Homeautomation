from flask import Flask, render_template, request, redirect, jsonify,session, url_for, escape
from flask_material import Material
import json

import bluetooth
import time

app = Flask(__name__)
Material(app)


v0 = [0,127,0,0]
v1 = [127,0,0,1]
v2 = [0,0,127,2]

bluetoothSockets = []
port = 1

def readConfigFile():
    with open("led_strip_config.json") as f:
        json_data = json.load(f)
        for strip in json_data["strips"]:
            print("Adding strip " + strip["mac_address"])
            bluetoothSockets.append(LEDConnection(strip["mac_address"], strip["id"]))


class LEDConnection:
    def __init__(self, macAddress, id):
        self.macAddress = macAddress
        self.id = id
        self.isConnected = False

    def close(self):
        try:
            self.socket.close()
        except bluetooth.btcommon.BluetoothError:
            print ("Error closing socket...")

    def connect(self):
        print("Trying to connect to " + self.macAddress)
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            self.socket.connect((self.macAddress, port))
            print("Connected to " + self.macAddress)
            self.isConnected = True
        except bluetooth.btcommon.BluetoothError as e:
            print("Failed to connect to " + self.macAddress)
            print(e)
            self.isConnected = False

    # r/g/b/mode (0-127)
    def sendColorValueWithMode(self,values):
        if not self.isConnected:
            self.close()
            self.connect()
        if self.isConnected:
            text = "#" + "".join(map(chr, values))
            try:
                self.socket.send(text)
                print("Sended data")
            except bluetooth.btcommon.BluetoothError as e:
                print("Send data failed")
                print(e)
                self.isConnected = False
            
        
def startAndRunSockets():
    for socket in bluetoothSockets:
        socket.connect()

def sendRegalData(dict):
    h_full_range = int(dict['regalC'])
    h = int((h_full_range * (256.0/360.0)) / 2.0)
    s = int(255/2.0)
    v = int(255/2.0)
    m = int(dict['regalM'])
    data = [h,s,v,m]
    print(data)
    for socket in bluetoothSockets:
        socket.sendColorValueWithMode(data)
    pass

@app.route('/colors')
def default_colors():
    dict = {
        "regalC" : "50",
        "regalM" : "2"
    }
    try:
        dict = session['regalValues']
    except:
        print('session missing')
    print("Rendering template now...")
    return render_template('colorchooser.html', data = dict)

@app.route("/regal/", methods=['POST'])
def move_forward():
    print(request.form.get('modeslc'))
    dict = {}
    dict['regalC'] = request.form.get('input')
    dict['regalM'] = request.form.get('modeslc')
    session['regalValues'] = dict
    sendRegalData(dict)
    print("Redirecting now...")
    return redirect('/colors')

if __name__ == '__main__':
    print("+++Reading config file+++")
    readConfigFile()
    print("+++Creating sockets++++++")
    startAndRunSockets()
    app.secret_key = 'raaaaandom'
    app.jinja_env.cache = {}
    app.run(host='0.0.0.0')