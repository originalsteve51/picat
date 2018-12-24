import RPi.GPIO as GPIO
import pivotpi

import time

import measurer
import dancer

ACTIVITY_THRESHOLD = 30
running = True

RH_TRIGGER_PIN = 23
RH_ECHO_PIN = 24

LH_TRIGGER_PIN = 14
LH_ECHO_PIN = 15

distances = []
all_distances = []

def is_valid_distance(distance, all_distances):
    # a long distance is considered valid only if several have
    # occurred in a row
    all_distances.append(distance)
    if len(all_distances)>5:
        all_distances.pop(0)

    valid = True
    if distance > 1000:
        for i in range(0, len(all_distances)):
            if all_distances[i]<1000:
                valid = False
                break
    if not valid:
        print('invalid distance being ignored')
    return valid

def get_running_average(distance):

    if is_valid_distance(distance, all_distances):
        distances.append(distance)
        if len(distances)>5:
            distances.pop(0)
    print(distances)
    # compute average of the items in the list
    average = sum(distances)/len(distances)
    return average

try:
    pp = pivotpi.PivotPi()
    a_measurer = measurer.Measurer(pp, RH_TRIGGER_PIN, RH_ECHO_PIN)
    a_dancer = dancer.Dancer(pp)

    # center the scanner
    a_measurer.goto_home_position()
    a_dancer.goto_home_position()

    # wait until something approaches head-on
    while a_measurer.measure_cm() > ACTIVITY_THRESHOLD:
        pass


    while running:
        #target_heading = a_measurer.heading_to_target()
        #a_dancer.turn_to_heading(target_heading[0])
        running_average = get_running_average(a_measurer.measure_cm())
        time.sleep(1.0)
        print(running_average)
        if running_average > 80:
            running = False

        a_dancer.dance()

except Exception as ex:
    print('picat::__main__ caught an Exception: ', ex)
finally:
    GPIO.cleanup()

