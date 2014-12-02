# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 10:34:07 2014

@author: Sierra
"""

class sample:
    
    def __init__(self, t2d, name):
        self.t2d = t2d
        self.name = name
        self.kos = dict() # keys = ko name, values = ko relative abundance
        self.pathways = dict()
        self.modules = dict()
        
    def add_dict(self, ko_dictionary):
        self.kos = ko_dictionary