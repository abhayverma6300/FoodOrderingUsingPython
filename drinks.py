# -*- coding: utf-8 -*-

"""
Drinks Module

This module defines the Drinks class, which inherits from Menu_Item class
and represents drinks in a menu.

Author: Abhay
Date: Mon Apr 5 14:00:33 2021
"""

from menu_items import Menu_Item


class Drinks(Menu_Item):
    """
    Drinks Class

    Represents drinks in a menu.

    Attributes:
        name (str): The name of the drink.
        price (float): The price of the drink.
        volume (float): The volume of the drink.
    """

    def __init__(self, name, price, volume):
        """
        Initializes a new Drinks object.

        Args:
            name (str): The name of the drink.
            price (float): The price of the drink.
            volume (float): The volume of the drink.
        """
        super().__init__(name, price)
        self.volume = volume

    def info(self):
        """
        Get Drink Information

        Returns:
            str: A formatted string containing the name and price of the drink.
        """
        return "{} : $ {}".format(self.name, str(self.price))
