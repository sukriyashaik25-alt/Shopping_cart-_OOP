# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 10:20:39 2025

@author: pooji
"""

from shopping_cart import ShoppingCart
from item import Item
from exceptions import ItemNotFoundError

def main():
    """Main program to interact with the Shopping Cart system."""
    cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Show Cart Length")
        print("5. Check if Item Exists")
        print("6. Total Price")
        print("7. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            item = Item(name, price, quantity)
            cart.add_item(item)
            print(f"{name} added to cart successfully.")

        elif choice == "2":
            name = input("Enter item name to remove: ")
            try:
                cart.remove_item(name)
                print(f"{name} removed from cart.")
            except ItemNotFoundError as e:
                print(e)

        elif choice == "3":
            print(cart)

        elif choice == "4":
            print(f"Number of items in cart: {len(cart)}")

        elif choice == "5":
            name = input("Enter item name to check: ")
            if name in cart:
                print(f"{name} is in your cart.")
            else:
                print(f"{name} not found in your cart.")

        elif choice == "6":
            print(f"Total price: ₹{cart.total_price()}")

        elif choice == "7":
            print("Exiting the Shopping Cart. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
