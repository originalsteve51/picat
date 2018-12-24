
import time
import random

SONAR_SERVO = 2
TILT_SERVO = 4
ROTATE_SERVO = 3

SONAR_HOME_HEADING = 65
TILT_HOME_HEADING = 90
ROTATE_HOME = 45

TILT_MAX = 45
TILT_MIN = 0

ROTATE_MAX = 120
ROTATE_MIN = 0

HOME_HEADING = 65

class Dancer(object):

    def __init__(self, pivotpi):
        self.__pivotpi = pivotpi

    def goto_home_position(self):
        self.__pivotpi.angle(SONAR_SERVO, HOME_HEADING)


    def turn_to_heading(self, heading):
        self.__pivotpi.angle(SONAR_SERVO, heading)

    def test_tilt_servo(self, step_size):
        for phi in range(TILT_MIN,TILT_MAX,step_size):
            self.__pivotpi.angle(TILT_SERVO, phi)
            time.sleep(0.2)

    def test_rotate_servo(self, step_size):
        for theta in range(ROTATE_MIN,ROTATE_MAX,step_size):
            self.__pivotpi.angle(ROTATE_SERVO, theta)
            time.sleep(0.2)

    def dance(self):
        pp = self.__pivotpi
        for i in range(0,3):
            pp.angle(TILT_SERVO, random.randrange(TILT_MIN, TILT_MAX))
            time.sleep(0.5)
            pp.angle(ROTATE_SERVO, random.randrange(ROTATE_MIN, ROTATE_MAX))
            time.sleep(0.5)



