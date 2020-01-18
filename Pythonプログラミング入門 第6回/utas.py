#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 19:40:43 2018

@author: yohei
"""

class UTCourse:
    def __init__(self,dic):
        for k, v in dic.items():
            if "year" in k:
                setattr(self,k,int(v))
            else:
                setattr(self,k,v)