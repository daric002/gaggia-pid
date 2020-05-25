from time import sleep
from random import randrange

def PID():
    previous_error = 0
    integral = 0
    measured_value = randrange(70, 99)

    goal_temperature = 93
    SLEEP_TIME = 0.05
    KP = SLEEP_TIME  / 2
    KD = KP / 2
    KI = KD / 2
    i = 1

    while True:
        _error = goal_temperature - measured_value
        integral = integral + _error * SLEEP_TIME
        _derivate = (_error + previous_error) / SLEEP_TIME
        output = KP * _error + KI * integral + KD * _derivate

        previous_error = _error
        if output > 0 :
            measured_value += 0.5

        if i == 200:
            measured_value -=20
        measured_value -= 0.2
        i+=1

        print("measured_valie {} _error {} output {}".format(measured_value, _error, output))