# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



machineIsOn = True
resources = {
    "water": 100,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
dollar_coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}
coins = {
    "two_pound": 2,
    "one_pound": 1,
    "fifty_pence": 0.5,
    "twenty_pence": 0.2,
    "ten_pence": 0.1,
    "five_pence": 0.05,
}

display_coins = {
    "two_pound": "£2",
    "one_pound": "£1",
    "fifty_pence": "£0.5",
    "twenty_pence": "£0.2",
    "ten_pence": "£0.1",
    "five_pence": "£0.05",
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


def get_unit(key):
    if key.lower() == "water" or key.lower() == "milk":
        unit = "ml"
    elif key.lower() == "coffee":
        unit = "g"
    else:
        unit = "£"
    return unit


def print_report():
    for key, value in resources.items():
        unit = get_unit(key)
        if key.lower() == "money":
            print(f'{key}: {unit}{value}')
        else:
            print(f'{key}: {value}{unit}')


def check_coffee_resource(coffee_key, print_dev_log=True):
    if coffee_key in MENU:
        # check ingredients
        for key, value in MENU[coffee_key]["ingredients"].items():
            is_enough = (int(value) <= int(resources[key]))
            shorter = int(value) - int(resources[key])
            # print(f'Dev Log: {key}: {value}, isEnough {is_enough}')
            if not is_enough:
                unit = get_unit(key)
                if print_dev_log:
                    print(f'Dev Log: Sorry there is not enough {key} for {coffee_key}, we need {shorter}{unit} more')
                return False
        return True
    else:
        return False


user_coins = {
    "two_pound": 0.0,
    "one_pound": 0.0,
    "fifty_pence": 0.0,
    "twenty_pence": 0.0,
    "ten_pence": 0.0,
    "five_pence": 0.0,
}


def get_money_from_the_client(coffee_cost, total):
    for key in coins:
        user_input = float(input("How many {} do you have? ".format(display_coins[key])))
        if not user_input == 0.0:
            # Cache the user input
            user_coins[key] += user_input
            # we count the money from input but not from the cache, because it had already been added into the total
            total += coins[key] * user_input

        print(f'Total inserted money:  £{round(total, 2)}')
        has_enough_coins = total >= coffee_cost
        if has_enough_coins:
            print("You had already put enough coins to make the coffee, let's make the coffee")
            break

    # It is nice to show the user, how much they put it in.
    for key in coins:
        if int(user_coins[key]) == 0:
            continue
        print(f'You have {int(user_coins[key])} of {display_coins[key]}')
    return total


def has_input_enough_coins(coffee_cost):
    # indicate how to insert coins
    total = 0
    total = get_money_from_the_client(coffee_cost, total)
    has_enough_coins = total >= coffee_cost

    while not has_enough_coins:
        print(f'You gave me this much: {round(total, 2)}, but the coffee cost: {coffee_cost}')
        user_choice = int(input("Sorry that's not enough money. "
                                "Do you want to (1. put more money in, or 2. not having coffee today)? "))
        if user_choice == 1:
            total = get_money_from_the_client(coffee_cost, total)
            has_enough_coins = total >= coffee_cost
        else:
            print(f'Sorry to see you go, Money refund {round(total, 2)}')
            break

    if not has_enough_coins:
        return False

    # Add the money into the resource
    resources["money"] += coffee_cost

    # Return the change
    if total == coffee_cost:
        print(f'The coffee costs £{coffee_cost}, perfect here is no change.')
    else:
        print(f'The coffee costs £{coffee_cost}, you gave me £{round(total, 2)}, here is £{round(total - coffee_cost, 2)} in change.')
    return True


def check_resource(coffee_key):
    # check ingredients
    have_enough_ingredients = check_coffee_resource(coffee_key)
    if not have_enough_ingredients:
        return False

    # get the price
    coffee_cost = MENU[coffee_key]["cost"]
    # print out how much to the user
    print(f'That will be £{coffee_cost} for the {coffee_key}, please insert coins 🪙 '
          f'(we only accept coins at the moment) ')
    # check money
    # if it is enough, we should use the ingredient, but we might need to check the cash first
    if not has_input_enough_coins(coffee_cost):
        return False
    return True


def strike_through(text):
    return '\u0336'.join(text) + '\u0336'


def format_question():
    show_espresso = "espresso"
    if not check_coffee_resource("espresso", False):
        show_espresso = strike_through("espresso")

    show_latte = "latte"
    if not check_coffee_resource("latte", False):
        show_latte = strike_through("latte")

    show_cappuccino = "cappuccino"
    if not check_coffee_resource("cappuccino", False):
        show_cappuccino = strike_through("cappuccino")

    return "Hello my friend 😆 !! What ☕ would you want? " + show_espresso + " " + show_latte + " " + show_cappuccino


def check_valid_input(user_input):
    valid_input = [
        "report",
        "off",
        "espresso",
        "latte",
        "cappuccino"
    ]
    if user_input in valid_input:
        return True
    else:
        print(f'{user_input} is not a valid input, please try again')
        return False


# What would you want? (espresso/latte/cappuccino)?
def question():
    for_fun = True

    while for_fun:
        # check the coffee resource before print this out :)
        desire_coffee = input(format_question() + " (report or off)" + " ")

        print("You desire: " + desire_coffee)
        if check_valid_input(desire_coffee):
            for_fun = False

            if desire_coffee.lower() == "off":
                turn_off()
            elif desire_coffee.lower() == "report":
                print_report()
            else:
                # Report before purchasing the coffee
                print(f'=======Report: {desire_coffee} =======')
                print_report()
                print("================================================")
                make_coffee(desire_coffee)


def make_coffee(desire_coffee):
    has_enough = check_resource(desire_coffee)
    # transaction is successful and have enough resources
    if has_enough:
        # make coffee, use the ingredient
        for key, value in MENU[desire_coffee]["ingredients"].items():
            resources[key] -= int(value)
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





