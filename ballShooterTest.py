"""Ball Shooter Hardware Test Suite"""

import ballShooter as bl
from time import sleep

import unittest

PAUSE = 2

shooter = bl.ballShooter()

print(shooter.idle)
print(shooter.lowLimit)
print(shooter.highLimit)

shooter.turnOn()
print('Turned On')
sleep(PAUSE)

shooter.setSpeed(0)
print('Set speed to ' + str(0) + "%")
sleep(PAUSE)

print('Set speed to ' + str(40) + "%")
shooter.setSpeed(40)
sleep(PAUSE)

print('Set speed to ' + str(80) + "%")
shooter.setSpeed(80)
sleep(PAUSE)

print('Set speed to ' + str(100) + "%")
shooter.setSpeed(100)
sleep(PAUSE)

print('Turned Off')
shooter.turnOff()
