# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 10:19:59 2025

@author: pooji
"""

from item import Item
from exceptions import ItemNotFoundError
"""
    Shopping Cart class that manages a collection of items.
    This class provides functionality for adding and removing items
    from a shopping cart. It uses a list to store Item objects.
    """

class ShoppingCart:
    def __init__(self):
        """
       Initialize an empty shopping cart.
       Uses a list to store Item objects.
       """

        self.items=[]

    def add_item(self, item):
        #add item to the list
        self.items.append(item)
            

    def remove_item(self, item_name):
        for item in self.items:
            if item_name==item.name:
                self.items.remove(item)
                return 
        raise ItemNotFoundError(f"{item_name} not found in shopping cart")
        
        # Hint: Search for item by name and remove it
        

    def total_price(self):
        return sum(item.price*item.quantity for item in self.items)
    
        # Hint: Sum of (item.price * item.quantity) for all items
        

    def __len__(self):
        return len(self.items)
        # Hint: return number of items
        

    def __getitem__(self, index):
        return self.items[index]
        # Hint: return item at given index
        
    def __contains__(self, item_name):
        return any(item.name==item_name for item in self.items)
        # Hint: return True if any item.name == item_name
        

    def __add__(self, other):
        """
        Overload + operator:
        - If other is Item → add to cart
        - If other is ShoppingCart → merge items
        """
        if isinstance(other,Item):
            self.add_item(other)
        elif isinstance(other,ShoppingCart):
            self.items.extend(other.items)
        else:
            raise TypeError("Can only add item or shopping cart to the ShoppingCart")
        return self

    def __str__(self):
        # Hint: Show all items in cart + total price
        if not self.items:
            return "Your ShoppingCart is empty"
        details="\n".join(str(item) for item in self.items)
        return f"Items in your cart:\n{details}\nTotalprice:{self.total_price()}"

