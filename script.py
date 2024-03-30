# -*- coding: utf-8 -*-
"""
Order Management System

This script simulates an order management system for foods and drinks.

Author: Abhay
Date: Mon Apr 5 14:01:08 2021
"""

from foods import Foods
from drinks import Drinks

def buy():
    """
    Order Menu

    Displays the menu options for foods and drinks, takes user input for order,
    calculates the total amount, and prints the total amount.

    """
    # Initialize food and drink items
    food1 = Foods("Burger", 5)
    food2 = Foods("Sandwich", 4) 
    food3 = Foods("Pizza", 10)

    drink1 = Drinks("Coke", 2, "Small")
    drink2 = Drinks("Pepsi", 2, "Small")
    drink3 = Drinks("Cold Coffee", 5, "Small")

    foods = [food1, food2, food3]
    drinks = [drink1, drink2, drink3]

    # Display menu options
    index = 1
    list_index = 1
    item_list = [foods, drinks]
    disp_list = ['Foods', 'Drinks']
    
    for x in disp_list:
        print("{}. {}\n".format(list_index, x))
        list_index += 1

    choice_cat = int(input("Choose a category: (Use the numbers to choose) "))
    
    # Validate category choice
    if choice_cat in range(1, len(item_list) + 1):
        for x in item_list[choice_cat - 1]:
            print("{}. {}".format(index, x.info()))
            index += 1

        choice = int(input("Choose: "))
        choice_count = int(input("How many(10% off for more than 4): "))
        price = item_list[choice_cat - 1][choice - 1].get_total_price(choice_count)

        global total_amount
        total_amount += price
        print('Your amount is :$ ', price)
        print('------------------------------------')
        again = input("You want something else (Y/N): ")
        
        if again == 'Y':
            buy()
        else:
            price = 0
    else:
        print("Wrong Choice.")

print('\n\nHello, what do you want to eat: ')
total_amount = 0
buy()
print("\nYour Total amount is: $", total_amount)
print("\nThank You for Ordering!!\n")
