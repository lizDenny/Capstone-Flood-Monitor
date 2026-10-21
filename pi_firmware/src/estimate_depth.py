#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File: estimate_depth.py
@Brief: Returns a depth estimate in inches averaged between a pressure (kPa) 
and ultrasonic (m) reading and the percent error between the two readings.
@Copyright: 2026 MIT License
@Version: 1.0
"""
def estimate_depth(pressure, ultrasonic):
    #Declare physical constants
    WATER_DENSISTY = 1000 #kg/m^3
    GRAVITY_ACCEL = 9.8 #m/s^2
    ATM_PRESSURE = 101.325 #kpa
    SENSOR_HEIGHT = 5.18 #m
    
    #Calculate depth estimate from pressure reading
    pressure_depth = 1000 * (pressure - ATM_PRESSURE) / (WATER_DENSISTY * GRAVITY_ACCEL)
    
    #Calculate depth estimate from ultrasonic returns
    ultrasonic_depth = SENSOR_HEIGHT - ultrasonic
    
    #Average both depth estimates to obtain final depth estimate
    average_depth = (pressure_depth + ultrasonic_depth) / 2
    
    #Calculate absolute error between the two estimates
    error = abs(average_depth - pressure_depth)
    
    #Convert final average and error to inches
    average_depth *= 39.37
    error *= 39.37

    return average_depth, error