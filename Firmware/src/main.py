#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:36:18 2026
MIT License
"""
# Local modules
import rtc_sync, poll_sensors, set_flags, archive_data, cloud_sync, negotiate_wakeup

#Poll witty pi for current time via "rtc_sync"

#Poll sensors via "poll_sensors.py"
[average_depth, depth_error, site_photo, timestamp] = poll_sensors()

#Set alert flags via "set_flags.py"

#Append depth estimate, depth error, site photo, flood flag, and road 
#obstruction flag to timestamped archive in storage via "archive_data.py"

#Sync archive to cloud via "cloud_sync.py"

#Negotiate next wakeup with witty pi via "negotiate_wakeup.py"

#Shutdown pi
