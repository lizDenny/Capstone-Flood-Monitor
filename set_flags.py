#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:57:10 2026
MIT License
"""

#if depth > const depth threshold
#flood flag = true
#else
#flood flag = false

#if flood flag
#wakeup interval = (5*60)-30 seconds
#else
#wakeup interval = (15*60)-30 seconds

#if flood flag
#road obstruction flag = check photo for similarities with previous photo
#via "check_similarity.py"
#else 
#road obstruction flag = 0