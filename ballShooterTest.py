"""Ball Shooter Test Suite"""

import ballShooter as bl
from time import sleep

import unittest

PAUSE = 2

shooter = bl.ballShooter()

print(shooter.idle)
print(shooter.lowLimit)
print(shooter.highLimit)

shooter.turnOn()
sleep(PAUSE)
print('Turned Off')
shooter.setSpeed(40)
sleep(PAUSE)
print('Turned On to' + str(40) + "%")
shooter.setSpeed(80)
sleep(PAUSE)
print('Turned On to' + str(80) + "%")
shooter.setSpeed(100)
sleep(PAUSE)
print('Turned On to' + str(100) + "%")
shooter.turnOff()
