# -*- coding: utf-8 -*-
"""
@File: const.py
@Brief: Contains global contants
@Copyright: 2026 MIT License
"""

#Declare physical constants
WATER_DENSISTY = 1000 #kg/m^3
GRAVITY_ACCEL = 9.8 #m/s^2
ATM_PRESSURE = 101.325 #kpa
METERS_TO_INCHES = 39.37 #unitless

#Declare program constants
THRESHOLD_DEPTH = 6 #inches, depth at which pi switches to flood mode
FLOOD_INTERVAL = 5 #minutes, time interval between samples in flood mode
FLOOD_EXECUTION_TIME = 45 #seconds, estimated period the pi runs for to execute full program in flood mode, measured from boot to shutdown
NORMAL_INTERVAL = 15 #minutes, time interval between samples in normal operation
NORMAL_EXECUTION_TIME = 30 #seconds, estimated period the pi runs for to execute full program in normal operation, measured from boot to shutdown
SENSOR_HEIGHT = 5.18 #m, parallel distance between ultrasonic sensor and ground for this deployment
MINIMUM_ACCEPTABLE_DEPTH = -0.005 #inches, lowest measurement of water depth deemed within measurement tolerances
MAX_REPS = 10 #unitless, max number of repetitions allowed for while loops to prevent excessive execution time

#Declare IO pin names as constants
SENSOR_PWR_CTL_PIN = -1 #board number, GPIO pin used to control the power switch of the sensors