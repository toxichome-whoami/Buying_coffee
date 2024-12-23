def check_customer(customer_name, blacklisted_names):
    """
    Checks if a customer is on the blacklisted_names list. If they are, they are asked if they are evil. If they answer yes, they are asked how many good deeds they have done today. If it is 4 or more, they are let in. If not, they are not allowed in. If they answer no, they are let in.
    """
    if customer_name in blacklisted_names:
        while True:
            evil_status = str(input("Are you Evil: ")).lower()
            if evil_status == "yes":
                while True:
                    try:
                        positive_actions = int(
                            input("How many good deeds have you done in a day: ")
                        )
                        if positive_actions >= 4:
                            print(f"\nCome on in {customer_name}")
                            return
                        elif positive_actions < 4:
                            print(
                                f"\nYour are not welcome here, Evil {customer_name}\n"
                            )
                            exit()
                    except ValueError:
                        print("Your actions must be an integer. Please try again.\n")
            elif evil_status == "no":
                print(
                    f"\nOh, so you're one of those good {customer_name}s. Come on in!!!"
                )
                break
            else:
                print("Invalid input try again!!!")
    else:
        print(f"\nHello {customer_name}, Thank you so much for coming in today...")


def get_order(menu):
    """
    Asks the customer what they would like from the menu. If they enter a valid menu item, it returns the name of the item and its price. If they enter an invalid item, it asks them to try again.
    """
    print("What would you like from our menu today?")
    print("\nHere is what we are serving:")
    for item in menu:
        print(f"{1 + list(menu.keys()).index(item)}. {item}")
    while True:
        order_name = str(input("\nOrder name: ")).title()
        if order_name in menu:
            return order_name, menu[order_name]
        else:
            print("Sorry, we don't have that here. Please try again.")


def main():
    """
    The main function of the program. It asks the customer for their name, checks if they are on the blacklisted_names list, asks them what they would like from the menu, asks them how many of the item they would like, calculates the total cost, and prints out a message with the total cost.
    """
    print("\nHello, welcome to Toxic_Home.coffee")

    customer_name = str(input("What is your name: ")).title()
    blacklisted_names = ["Tasbir", "Ben", "Sadik"]
    check_customer(customer_name, blacklisted_names)

    menu = {
        "Black Coffee": 7,
        "Espresso": 10,
        "Latte": 5,
        "Cappuccino": 5,
        "Frappuccino": 6,
    }

    drink_name, drink_price = get_order(menu)

    while True:
        try:
            quantity = int(input("What is the quantity of coffee you would like: "))
            if quantity >= 1:
                break
            else:
                print("Your quantity must be greater than 0. Please try again.\n")
        except ValueError:
            print("Your quantity must be an integer. Please try again.\n")

    total_cost = quantity * drink_price
    print(f"Your total is: ${total_cost}")
    print(
        f"\nSounds good {customer_name}, we'll have your {quantity} {drink_name}(s) ready in a moment.\n"
    )


if __name__ == "__main__":
    main()

# Toxic Home.coffee 😊
