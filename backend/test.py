from time import sleep
from random import randrange
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

previous_error = 0
integral = 0
measured_value = randrange(70, 99)

goal_temperature = 93
SLEEP_TIME = 0.05
KP = SLEEP_TIME  / 2
KD = KP / 2
KI = KD / 2
i=1
t_axel = list()
temp_axel = list()

fig = plt.figure()
plt.grid()
plt.axis('auto')

while True:
    _error = goal_temperature - measured_value
    integral = integral + _error * SLEEP_TIME
    _derivate = (_error + previous_error) / SLEEP_TIME
    output = KP * _error + KI * integral + KD * _derivate

    previous_error = _error
    if output > 0 :
        measured_value += 0.5

    t_axel.append(i)
    temp_axel.append(measured_value)
    if i == 200:
        measured_value -=20
    measured_value -= 0.2
    i+=1

    print("measured_valie {} _error {} output {}".format(measured_value, _error, output))

    plt.plot(t_axel, temp_axel)
    plt.pause(SLEEP_TIME)

plt.show()