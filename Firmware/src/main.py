#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:36:18 2026
MIT License
"""
#Local modules
from rtc_sync import rtc_sync
from poll_sensors import poll_sensors
from set_flags import set_flags
from archive_data import archive_data
from cloud_sync import cloud_sync
from negotiate_wakeup import negotiate_wakeup
from shutdown import shutdown

#Poll witty pi for current time via "rtc_sync"
rtc_sync()

#Poll sensors via "poll_sensors.py"
[average_depth, depth_error, site_photo, timestamp] = poll_sensors()

#Set alert flags via "set_flags.py"
[flood_flag, wakeup_interval] = set_flags(average_depth)

#Append depth estimate, depth error, site photo, flood flag, and road 
#obstruction flag to timestamped archive in storage via "archive_data.py"
#archive_data(average_depth, depth_error, site_photo, timestamp, flood_flag)

#Sync archive to cloud via "cloud_sync.py"
#cloud_sync()

#Negotiate next wakeup with witty pi via "negotiate_wakeup.py"
negotiate_wakeup(wakeup_interval)

#Shutdown pi
shutdown()
