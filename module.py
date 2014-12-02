# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 09:10:40 2014

@author: Sierra
"""

class module:
    # Simple representation of a module as a set of KOs 

    def __init__(self, name, description, filename=None):
        self.name = name # i.e. M00001
        self.description = description
        self.kos = [] #KOs actually present in the sample, subset of all_kos
        self.all_kos = [] # all KOs known to exist in module (names only)
        self.module_abundances_t2d = []
        self.module_abundance_control = []
    
    def add_ko(self, k):
        # Add a KO to the list of KOs composing this module
        self.kos.append(k)

    def add_ko_all(self, ko_name):
        # Add a KO to the list of KOs composing this module
        self.all_kos.append(ko_name)    