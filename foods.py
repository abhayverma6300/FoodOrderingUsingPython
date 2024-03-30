# -*- coding: utf-8 -*-
"""
Foods Module

This module defines the Foods class, which inherits from Menu_Item class
and represents food items in a menu.

Author: Abhay
Date: Mon Apr 5 14:01:01 2021
"""

from menu_items import Menu_Item


class Foods(Menu_Item):
    """
    Foods Class

    Represents food items in a menu.

    Attributes:
        name (str): The name of the food item.
        price (float): The price of the food item.
    """

    def __init__(self, name, price):
        """
        Initializes a new Foods object.

        Args:
            name (str): The name of the food item.
            price (float): The price of the food item.
        """
        super().__init__(name, price)

    def info(self):
        """
        Get Food Information

        Returns:
            str: A formatted string containing the name and price of the food item.
        """
        return "{} : $ {}".format(self.name, str(self.price))
