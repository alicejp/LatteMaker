# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


offStr = "Off"
reportStr = "report"
machineIsOn = True
resources = {
    "water": 100,
    "milk": 200,
    "coffee": 100,
}
coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


# TODO: also shows the money, Money: £2.5
def print_report():
    for key, value in resources.items():
        unit = "ml"
        if key.lower() == "water" or key.lower() == "milk":
            unit = "ml"
        else:
            unit = "g"
        print(f'{key}: {value}{unit}')


def check_resource(coffeeKey):
    for key, value in MENU[coffeeKey]["ingredients"].items():
        isEnough = (int(value) <= int(resources[key]))
        print(f'{key}: {value}, isEnough {isEnough}')
        if not isEnough:
            print(f'Sorry there is not enough {key} for {coffeeKey}')
            return False
    # TODO 5: if it is enough, we should use the ingredient, but we might need to check the cash first
    print(f'We have everything you need for {coffeeKey}, please insert coins ')
    q, d, n, p = input("Enter 4 values: ").split()
    coins = process_coins(float(q),float(d),float(n),float(p))
    isEnoughCoins = coins >= MENU[coffeeKey]["cost"]
    print(f'money coins: {coins}, cost: {MENU[coffeeKey]["cost"]}')
    if not isEnoughCoins:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def process_coins(quarter, dime, nickel, pennie):
    total = quarter*coins["quarters"] + dime*coins["dimes"] + nickel*coins["nickles"] + pennie*coins["pennies"]
    print(f'quarter: {quarter}*{coins["quarters"]}')
    print(f'dimes: {dime}*{coins["dimes"]}')
    print(f'nickel: {nickel}*{coins["nickles"]}')
    print(f'pennie: {pennie}*{coins["pennies"]}')
    # print(f'total: {total}')
    print(f'rounded total: {round(total, 2)}')
    return round(total, 2)


# What would you want? (espresso/latte/cappuccino)?
def question():
    desire_coffee = input("What would you want? (espresso/latte/cappuccino) ")
    print("You desire: " + desire_coffee)
    if desire_coffee.lower() == offStr.lower():
        turn_off()
    elif desire_coffee.lower() == reportStr.lower():
        print_report()
    check_resource(desire_coffee)


# Turn off the coffee machine
def turn_off():
    # TODO 4, is this how we use the global variables?
    global machineIsOn
    machineIsOn = False
    print("Machine is off, see you tomorrow")


# execution
def start_hosting():
    while machineIsOn:
        question()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_hosting()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




