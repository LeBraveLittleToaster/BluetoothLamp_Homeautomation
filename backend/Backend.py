from flask import Flask, request
from LightManager import LightManager
from StripColorHSV import StripColorHSV
import json

app = Flask(__name__)

lightManager = LightManager()


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/strips')
def getAllStrips():
    return json.dumps(lightManager.getAllStrips())

@app.route('/strips/<stripID>')
def setStripData(stripID):
    print("Accessed stripid= " + stripID)
    
    isSuccess = True

    isOn = request.args.get('isOn', type = bool)
    if isOn is not None:
        print("Setting isOn to=%s" % (isOn))
        isSuccess = lightManager.setStripTurnedOn(stripID, isOn)

    hue = request.args.get('hue', type=int)
    saturation = request.args.get('saturation', type=int)
    value = request.args.get('value', type=int)
    
    if hue is not None and saturation is not None and value is not None:
        print("Setting color to = h: %s , s: %s, v: %s" % (hue, saturation, value))
        isSuccess = lightManager.setStripColor(stripID, StripColorHSV(hue, saturation, value))
        
    return json.dumps({"success":isSuccess})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=54321, debug=True)