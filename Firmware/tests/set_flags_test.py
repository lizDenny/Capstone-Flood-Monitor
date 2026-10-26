#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File: set_flags_test.py
@Brief: Unit tests for set_flags.py containing the module used to set the alerts and appropriate wakeup window based on sensor data
@Copyright: 2026 MIT License
@Version: 1.0
ToDo: Modify expected results to test obstruction flag when check_similarity is implemented
"""

#Standard library
import sys, os
#Add source directory to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
#Local module
from set_flags import set_flags
import const

def test_set_flags_flood_with_obstruction():
    flood_flag, obstruction_flag, wakeup_interval = set_flags(6.1, [-1], [-1])
    assert flood_flag == True
    assert obstruction_flag == True
    assert wakeup_interval == (const.FLOOD_INTERVAL*60)-const.FLOOD_EXECUTION_TIME #seconds
    
def test_set_flags_flood_without_obstruction():
    flood_flag, obstruction_flag, wakeup_interval = set_flags(6, [-1], [-2])
    assert flood_flag == True
    assert obstruction_flag == True
    assert wakeup_interval == (const.FLOOD_INTERVAL*60)-const.FLOOD_EXECUTION_TIME #seconds
    
def test_set_flags_normal_operation():
    flood_flag, obstruction_flag, wakeup_interval = set_flags(0.01, [-1], [-2])
    assert flood_flag == False
    assert obstruction_flag == False
    wakeup_interval == (const.NORMAL_INTERVAL*60)-const.NORMAL_EXECUTION_TIME #seconds