# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 09:06:32 2014

@author: Sierra
"""

class pathway:
    # Simple representation of a pathway as a set of KOs    
    
    def __init__(self, name, description, filename=None):
        self.name = name # i.e. ko00001
        self.description = description
        self.kos = [] # KOs actually in the sample, subset of all_kos
        self.all_kos = [] # all KOs known to exist in pathway (names only)
    
    def add_ko(self, k):
        # Add a KO to the list of KOs composing this pathway
        self.kos.append(k)
    
    def add_ko_all(self, ko_name):
        # Add a KO to the list of KOs composing this pathway
        self.all_kos.append(ko_name)