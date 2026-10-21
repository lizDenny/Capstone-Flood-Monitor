#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File: estimate_depth.py
@Brief: Returns a depth estimate in inches averaged between a pressure (kPa) and ultrasonic (m) reading and the percent error between the two readings.
@Copyright: 2026 MIT License
@Version: 1.0
"""

#Local modules
import const

def estimate_depth(pressure, ultrasonic):
    #Calculate depth estimate from pressure reading
    pressure_depth = 1000 * (pressure - const.ATM_PRESSURE) / (const.WATER_DENSISTY * const.GRAVITY_ACCEL)
    
    #Calculate depth estimate from ultrasonic returns
    ultrasonic_depth = const.SENSOR_HEIGHT - ultrasonic
    
    #Average both depth estimates to obtain final depth estimate
    average_depth = (pressure_depth + ultrasonic_depth) / 2
    
    #Calculate absolute error between the two estimates
    error = abs(average_depth - pressure_depth)
    
    #Convert final average and error to inches
    average_depth *= const.METERS_TO_INCHES
    error *= const.METERS_TO_INCHES

    return average_depth, error