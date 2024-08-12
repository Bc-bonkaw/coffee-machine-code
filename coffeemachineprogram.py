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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(resource):
    """ takes a dictionary and generates a report that shows the current resource values"""
    for key in resource:
        print(f"{key}: {resource[key]}ml")


def check_sufficient_resources(drinkType):
    """Check if there are sufficient resources"""
    # Resources required to make whatever type of coffee required
    if drinkType == "espresso":
        water = MENU[drinkType]["ingredients"]["water"]
        milk = 0
        coffee = MENU[drinkType]["ingredients"]["coffee"]
    else:
        water = MENU[drinkType]["ingredients"]["water"]
        milk = MENU[drinkType]["ingredients"]["milk"]
        coffee = MENU[drinkType]["ingredients"]["coffee"]

    # checking if any of the resources required is more than the available resources
    if water > resources["water"] or milk > resources["milk"] or coffee > resources["coffee"]:
        print(f"\nThey are not enough ingredients to make your {drinkType}")
        return False
    else:
        return True


def process_coins(quarters, dimes, nickles, pennies):
    """Processes the coins entered in dollars"""
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def update_resources(resources, drinkType):
    """Get 2 dictionaries:  Resources in the coffee and the user's chosen drink
    updates the resources dictionary depending on what type of coffee the user has taken"""
    resources["water"] -= drinkType["water"]
    resources["milk"] -= drinkType["milk"]
    resources["coffee"] -= drinkType["coffee"]

def update_espresso(resources, espresso):
    """Get 2 dictionaries:  Resources in the coffee and the user's chosen drink
    updates the resources dictionary if user chooses espresso since espresso does not have milk in it"""
    resources["water"] -= espresso["water"]
    resources["coffee"] -= espresso["coffee"]

# turn off the coffee machine once the user enters "off"
coffee_machine = True

# Buy coffee as long as the user has sufficient cash and
# as long as there is enough resources in the coffee machine
while coffee_machine:
    drinkType = input("What would you like? espresso/latte/cappuccino: ").lower()
    # check the user's input and decide what to do next
    if check_sufficient_resources(drinkType) == True:
        # prompt user for breakdown of how much they have:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        # calculate how much in dollars the user has entered
        total_in_cash = process_coins(quarters, dimes, nickles, pennies)

        # check if user's cash is sufficient to buy what he desires
        if total_in_cash > MENU[drinkType]["cost"]:
            # creating an empty space before printing the total amount
            print()

            print(f"${round(total_in_cash - MENU[drinkType]["cost"], 2)} in change.")
            print(f"Here is your {drinkType}. Enjoy!")
            print()
            # update the resources available on the coffee machine
            if drinkType == "espresso":
                update_espresso(resources, MENU[drinkType]["ingredients"])
            else:
                update_resources(resources, MENU[drinkType]["ingredients"])
        else:
            # if user has not enough money end the program
            coffee_machine = False
    else:
        coffee_machine = False

    # print report
    print_report(resources)
    print()
# prompt the user again once the coffee has been dispensed



