from flask import Flask
from tsic import TsicInputChannel, Measurement, TSIC306
from test import PID

app = Flask(__name__)

@app.route('/temperature')
def get_temp():
    PID()
    return 5

@app.route('/nothing/<input>')
def get_nothing(input):
    return "output is input: " + input

@app.route('/json')
def get_json():
    return {
        "oneThing": "the Thing",
        "nextThing": "the next thing"
    }