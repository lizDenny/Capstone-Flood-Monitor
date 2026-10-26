#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File: set_flags.py
@Brief: Sets alerts and appropriate operation intervals based on sensor data. Depth is assumed to be in inches, current_photo and previous_photo are assumed to be in jpegs, flood_flag and obstruction_flag are returned as bools, and wakeup interval is returned in seconds
@Copyright: 2026 MIT License
ToDo: Use check_similarity to determine the obstruction flag during flood mode once it's implemented
"""

#Local modules
from const import THRESHOLD_DEPTH, FLOOD_INTERVAL, FLOOD_EXECUTION_TIME, NORMAL_INTERVAL, NORMAL_EXECUTION_TIME

def set_flags(depth, current_photo, previous_photo):    
    #Flood mode operation
    if depth >= THRESHOLD_DEPTH:
        #Condition already checked during if statement
        flood_flag = True
        #Set ostruction alert if similarities found in the photos taken both in the current interval and previous interval
        obstruction_flag = True #check_similarity(current_photo, previous_photo)
        wakeup_interval = (FLOOD_INTERVAL*60)-FLOOD_EXECUTION_TIME #seconds
    #Non-Flood mode operation
    else:
        #Condition already checked during if statement
        flood_flag = False
        #Don't check for obstructions during normal operation to save power
        obstruction_flag = False
        wakeup_interval = (NORMAL_INTERVAL*60)-NORMAL_EXECUTION_TIME #seconds
        
    return flood_flag, obstruction_flag, wakeup_interval