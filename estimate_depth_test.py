#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File: estimate_depth_test.py
@Brief: Unit tests for estimate_depth.py containing the module used to 
convert sensor readings into water depth measurements
@Copyright: 2026 MIT License
@Version: 1.0
"""

#Local module
from estimate_depth import estimate_depth

def test_estimate_flood_depth():
    average, error = estimate_depth(102.82, 5.025)
    assert average >= 6.045 and average <= 6.055 #~6.05 in
    assert error >= 0.0475 and error <= 0.0485 #~0.048 in
    
def test_estimate_dry_depth():
    average, error = estimate_depth(101.326, 5.1795)
    assert average >= 0.005 and average <= 0.015 #~0.01 in
    assert error >= 0.005 and error <= 0.015 #~0.01 in