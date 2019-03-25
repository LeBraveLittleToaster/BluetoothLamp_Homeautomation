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
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            self.socket.connect((self.macAddress, port))
            print("Connected to " + self.macAddress)
        except bluetooth.btcommon.BluetoothError as e:
            print("Failed to connect to " + self.macAddress)
            print(e)
            self.isConnected = True

    # r/g/b/mode (0-127)
    def sendColorValueWithMode(self,values):
        #if not self.isConnected:
        #    self.close()
        #    self.connect()
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
    print("Sending data")
    for socket in bluetoothSockets:
        socket.sendColorValueWithMode(v0)
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
    return render_template('colorchooser.html', data = dict)

@app.route("/regal/", methods=['POST'])
def move_forward():
    print(request.form.get('modeslc'))
    dict = {}
    dict['regalC'] = request.form.get('input')
    dict['regalM'] = request.form.get('modeslc')
    session['regalValues'] = dict
    sendRegalData(dict)
    return redirect('/colors')

if __name__ == '__main__':
    readConfigFile()
    startAndRunSockets()
    app.secret_key = 'raaaaandom'
    app.run(host='0.0.0.0', debug = True)