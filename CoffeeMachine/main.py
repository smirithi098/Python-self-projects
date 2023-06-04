from data import MENU
from data import resources

flag = True
profit = 0

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


def check_for_resources(drink):
    for item in drink['ingredients']:
        if resources[item] < drink['ingredients'][item]:
            print(f"Sorry there is not enough {item}")
            return False

    return True


def payment_transaction(drink, amount):
    if amount < MENU[drink]['cost']:
        print(f"Sorry, That's not enough money. Money Refunded ${amount:.2f}")

    else:
        change = amount - MENU[drink]['cost']
        print(f"Here is ${change:.2f} in change")
        return True


def insert_coins():
    print("Please insert coins.")
    no_of_quarters = float(input("How many quarters: "))
    no_of_dimes = float(input("How many dimes: "))
    no_of_nickles = float(input("How many nickles: "))
    no_of_pennies = float(input("How many pennies: "))

    total = (no_of_quarters*QUARTERS) + (no_of_dimes*DIMES) + (no_of_nickles*NICKLES) + (no_of_pennies*PENNIES)
    return total


def update_report(drink):
    global profit
    for item in drink['ingredients']:
        resources[item] -= drink['ingredients'][item]

    profit += drink['cost']


def print_report():
    print(f"Milk: {resources['milk']}ml\n"
          f"Water: {resources['water']}ml"
          f"\nCoffee: {resources['coffee']}g"
          f"\nMoney: ${profit}")


while flag:
    print("OUR MENU: \n")
    print(f"Espresso: {MENU['espresso']['cost']}\nLatte: {MENU['latte']['cost']}\nCappuccino: {MENU['cappuccino']['cost']}\n")

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print_report()

    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        resource_status = check_for_resources(drink=MENU[choice])
        if resource_status:
            total_amount = insert_coins()
            transaction_status = payment_transaction(drink=choice, amount=total_amount)
            if transaction_status:
                update_report(drink=MENU[choice])
                print(f"Here is your ☕ {choice}. Enjoy!")

    elif choice == "off":
        print("Oh No.. Coffee machine under maintenance:( Sorry for the inconvenience.")
        flag = False

    else:
        print("You have entered an invalid choice. Please try again.")
        flag = False
