from flask import Flask, render_template, request, redirect, jsonify,session, url_for, escape
from flask_material import Material
import json

app = Flask(__name__)
Material(app)

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

@app.route("/forward/", methods=['POST'])
def move_forward():
    print(request.form.get('modeslc'))
    dict = {}
    dict['regalC'] = request.form.get('input')
    dict['regalM'] = request.form.get('modeslc')
    session['regalValues'] = dict
    return redirect('/colors')

if __name__ == '__main__':
    app.secret_key = 'raaaaandom'
    app.run(host='0.0.0.0', debug = True)