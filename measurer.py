import RPi.GPIO as GPIO
import time

#TRIG = 23  # black for rh sensor
#ECHO = 24  # white for rh sensor

#TRIG = 14
#ECHO = 15

SCAN_SERVO = 2
STEP_TIME = 0.00
STEP_INCREMENT = 10
HOME_HEADING = 65
ACTIVE_HEADING = 30


SCAN_R_TO_L = 1
SCAN_L_TO_R = 2

class Measurer(object):

    def __init__ (self, pp, trigger_pin, echo_pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trigger_pin,GPIO.OUT)
        GPIO.setup(echo_pin,GPIO.IN)
        self.__last_scan_direction = SCAN_R_TO_L
        self.__pivotpi = pp
        self.__trigger_pin = trigger_pin
        self.__echo_pin = echo_pin

    def goto_home_position(self):
        self.__pivotpi.angle(SCAN_SERVO, HOME_HEADING)

    def goto_active_position(self):
        self.__pivotpi.angle(SCAN_SERVO, HOME_HEADING)

    def measure_cm(self):
        GPIO.output(self.__trigger_pin, False)
        time.sleep(0.1)
        GPIO.output(self.__trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.__trigger_pin, False)

        try:

            while GPIO.input(self.__echo_pin) == 0:
                pulse_start = time.time()

            while GPIO.input(self.__echo_pin) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            pulse_duration = None
            distance = round(distance, 2)
        except Exception as ex:
            print('Measurer::measure_cm Exception: ', ex)
            distance = 50000

        return distance

    def heading_to_target(self):
        heading_to_target = None
        closest_distance = 50000

        if self.__last_scan_direction == SCAN_L_TO_R:
            scan_range = range(120, 10, 0-STEP_INCREMENT)
            self.__last_scan_direction = SCAN_R_TO_L
        else:
            scan_range = range(20, 120, STEP_INCREMENT)
            self.__last_scan_direction = SCAN_L_TO_R

        for theta in scan_range:
            time.sleep(STEP_TIME)
            self.__pivotpi.angle(SCAN_SERVO, theta)
            distance = self.measure_cm()
            if distance < closest_distance:
                closest_distance = distance
                heading_to_target = theta
        return (heading_to_target, closest_distance)


