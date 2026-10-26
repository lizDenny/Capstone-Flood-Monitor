#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:54:37 2026
MIT License
"""

#Third party modules
from RPI import GPIO
from time import strftime

#Local modules
from poll_sensors.poll_pressure import poll_pressure
from poll_sensors.poll_ultrasonic import poll_ultrasonic
from poll_sensors.poll_camera import poll_camera
from poll_sensors.estimate_depth import estimate_depth
from const import SENSOR_PWR_CTL_PIN, MINIMUM_ACCEPTABLE_DEPTH, MAX_REPS

def poll_sensors():
    #Initialize variables for loop control
    average_depth = -1
    rep_count = 0

    #Power sensors
    GPIO.output(SENSOR_PWR_CTL_PIN, GPIO.HIGH)

    # Poll depth until reasonable return is recieved (positive within measurement tolerances). Rep count prevents exessive sampling during poor conditions to save power
    while average_depth < MINIMUM_ACCEPTABLE_DEPTH and rep_count < MAX_REPS:
        #Poll connection to pressure sensor
        pressure = poll_pressure()

        #Poll uart connection to ultrasonic sensor
        ultrasonic = poll_ultrasonic()
    
        #Calculate depth reading from sensor data
        average_depth, depth_error = estimate_depth(pressure, ultrasonic)
        
        rep_count += 1

    #Poll usb connection to camera
    site_photo = poll_camera()

    #Save measurement timestamp (ex. 01/15/2027 at 06:30:04pm CST)
    timestamp = strftime("%m/%d/%Y at %I:%M%p %Z")

    #Cut power to sensors
    GPIO.output(SENSOR_PWR_CTL_PIN, GPIO.LOW)
    return average_depth, depth_error, site_photo, timestamp