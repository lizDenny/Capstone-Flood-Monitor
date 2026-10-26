#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:36:18 2026
MIT License
"""
import poll_sensors
#import estimate_depth
#import set_flags
#import cloud_sync

#Poll witty pi via gpio for current time

#Poll sensors via "poll_sensors.py"
sensor_data = poll_sensors.read_all()
#Calculate the depth from sensor data via "estimate_depth.py"

#Set alert flags via "set_flags.py"

#Append depth estimate, depth error, site photo, flood flag, and road 
#obstruction flag to timestamped archive in storage

#Sync archive to cloud via "cloud_sync.py"

#Negotiate next wakeup with witty pi via gpio

#Shutdown pi
