# -*- coding: utf-8 -*-
"""
Menu Item Module

This module defines the Menu_Item class, which represents an item in a menu.

Author: Abhay
Date: Mon Apr 5 14:00:49 2021
"""

class Menu_Item():
    """
    Menu_Item Class

    Represents an item in a menu.

    Attributes:
        name (str): The name of the menu item.
        price (float): The price of the menu item.
    """

    def __init__(self, name, price):
        """
        Initializes a new Menu_Item object.

        Args:
            name (str): The name of the menu item.
            price (float): The price of the menu item.
        """
        self.name = name
        self.price = price
        
    def info(self):
        """
        Get Menu Item Information

        Returns:
            str: A formatted string containing the name and price of the menu item.
        """
        return "{} : ${}".format(self.name, str(self.price))

    def get_total_price(self, count):
        """
        Calculate Total Price

        Args:
            count (int): The quantity of the menu item.

        Returns:
            float: The total price of the menu item based on the quantity.
        """
        total_price = self.price * count
        
        if count >= 4:
            total_price *= 0.9
        return round(total_price)

    def getx_total_price(self, count):
        """
        Calculate Total Price with Discount

        Args:
            count (int): The quantity of the menu item.

        Returns:
            float: The total price of the menu item with discount based on the quantity.
        """
        total_price = self.price * count
        
        if count >= 2:
            total_price *= 0.6
        return round(total_price)
