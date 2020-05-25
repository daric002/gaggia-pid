from flask import Flask
from tsic import TsicInputChannel, Measurement, TSIC306

import pigpio

app = Flask(__name__)

pi = pigpio.pi()
tsic = TsicInputChannel(pigpio_pi=pi, gpio=17, tsic_type=TSIC306)

@app.route('/temperature')
def get_temp():
    temperature = tsic.measure_once()
    return temperature

@app.route('/nothing/<input>')
def get_nothing(input):
    return "output is input: " + input

@app.route('/json')
def get_json():
    return {
        "oneThing": "the Thing",
        "nextThing": "the next thing"
    }