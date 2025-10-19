# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 10:19:36 2025

@author: pooji
"""

class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return f'Name:{self.name},Price:{self.name} and Quantity:{self.quantity}'
        
