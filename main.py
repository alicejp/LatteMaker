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
    "money": 0,
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


def print_report():
    for key, value in resources.items():
        unit = "ml"
        if key.lower() == "water" or key.lower() == "milk":
            unit = "ml"
            print(f'{key}: {value}{unit}')
        elif key.lower() == "coffee":
            unit = "g"
            print(f'{key}: {value}{unit}')
        else:
            unit = "£"
            print(f'{key}: {unit}{value}')


def check_coffee_resource(coffee_key):
    # check ingredients
    for key, value in MENU[coffee_key]["ingredients"].items():
        is_enough = (int(value) <= int(resources[key]))
        print(f'{key}: {value}, isEnough {is_enough}')
        if not is_enough:
            print(f'Sorry there is not enough {key} for {coffee_key}')
            return False
    return True


def check_resource(coffeeKey):
    # check ingredients
    is_enough = check_coffee_resource(coffeeKey)
    if not is_enough:
        return False

    # check money
    # if it is enough, we should use the ingredient, but we might need to check the cash first
    print(f'We have everything you need for {coffeeKey}, please insert coins ')
    q, d, n, p = input("Enter 4 values with a space in between: ").split()
    input_coins = process_coins(float(q),float(d),float(n),float(p))
    coffee_cost = MENU[coffeeKey]["cost"]
    has_enough_coins = input_coins >= coffee_cost
    print(f'money coins: {input_coins}, cost: {coffee_cost}')
    if not has_enough_coins:
        print("Sorry that's not enough money. Money refunded.")
        return False

    # TODO: move out here
    # make coffee
    for key, value in MENU[coffeeKey]["ingredients"].items():
        resources[key] -= int(value)

    # TODO: add the money into the resource, move out there
    resources["money"] += coffee_cost

    # Return the change
    if input_coins == coffee_cost:
        print(f'The coffee costs £{coffee_cost}, perfect here is no change.')
    else:
        print(f'The coffee costs £{coffee_cost}, here is £{round(input_coins - coffee_cost, 2)} in change.')
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


def strike_through(text):
    return '\u0336'.join(text) + '\u0336'


def format_question():
    show_espresso = "espresso"
    if not check_coffee_resource("espresso"):
        show_espresso = strike_through("espresso")

    show_latte = "latte"
    if not check_coffee_resource("latte"):
        show_latte = strike_through("latte")

    show_cappuccino = "cappuccino"
    if not check_coffee_resource("cappuccino"):
        show_cappuccino = strike_through("cappuccino")

    return "What would you want? " + show_espresso + " " + show_latte + " " + show_cappuccino


# What would you want? (espresso/latte/cappuccino)?
def question():
    # check the coffee resource before print this out :)
    desire_coffee = input(format_question()+ " ")

    print("You desire: " + desire_coffee)
    if desire_coffee.lower() == offStr.lower():
        turn_off()
    elif desire_coffee.lower() == reportStr.lower():
        # report before purchasing the coffee
        print_report()
    else:
        print(f'=======Report before purchasing {desire_coffee}=======')
        print_report()
        print("================================================")
        has_enough = check_resource(desire_coffee)
        # transaction is successful and have enough resources
        if has_enough:
            # report the money into the resource
            print(f'=======Report after purchasing {desire_coffee}=======')
            print_report()
            print("===============================================")
            print(f'Here is your {desire_coffee}. Enjoy!')


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





