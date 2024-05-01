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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

user_input = ""

def start ():
    global user_input
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'report':
        report()
    elif user_input == 'espresso':
        espresso()
    elif user_input == 'cappuccino':
        cappuccino()
    elif user_input == 'latte':
        latte()

def report():
    print (f"water: {resources['water']}")
    print (f"milk: {resources['milk']}")
    print (f"coffee: {resources['coffee']}")

def latte():
    choice = MENU["latte"]
    ing = choice["ingredients"]
    water = ing["water"]
    coffee = ing["coffee"]
    milk = ing["milk"]
    money = choice["cost"]

    if (resources["water"] >= water and resources["coffee"] >= coffee and resources["milk"] >= milk):
        money_paid = pay()
        if (money_paid >= money ):
            money_left = money_paid - money
            print ("Here is your change: " + str(money_left))
            alter_resources()
            print("your espresso is ready!!")
        else:
            print ("not enough money")
    else :
        print ("not enough resources")

def cappuccino():
    choice = MENU["cappuccino"]
    ing = choice["ingredients"]
    water = ing["water"]
    coffee = ing["coffee"]
    milk = ing["milk"]
    money = choice["cost"]

    if (resources["water"] >= water and resources["coffee"] >= coffee and resources["milk"] >= milk):
        money_paid = pay()
        if (money_paid >= money ):
            money_left =   money_paid - money
            print ("Here is your change: " + str(money_left))
            alter_resources()
            print("your espresso is ready!!")
        else:
            print ("not enough money")
    else :
        print ("not enough resources")

def espresso():
    choice = MENU["espresso"]
    ing = choice["ingredients"]
    water = ing["water"]
    coffee = ing["coffee"]
    money = choice["cost"]

    if (resources["water"] >= water and resources["coffee"] >= coffee):
        money_paid = pay()
        if (money_paid >= money ):
            money_left = money_paid - money 
            print ("Here is your change: " + str(money_left))
            alter_resources()
            print("your espresso is ready!!")
        else:
            print ("not enough money")
    else :
        print ("not enough resources")

def pay():
    quater = int (input("Enter number of quater: "))
    dime  = int(input("Enter number of dime: "))
    nickel = int(input("Enter number of nickel: "))
    penny = int(input("Enter number of penny: "))
    return (0.25 * quater) + (dime * 0.10) +(nickel * 0.05) + (penny * 0.01)

def alter_resources ():
    global user_input
    present_water = resources["water"]
    present_milk = resources["milk"]
    present_coffee = resources["coffee"]
    if (user_input == 'espresso'):
        choice = MENU["espresso"]
        ing = choice["ingredients"]
        water = ing["water"]
        coffee = ing["coffee"]
        milk = 0
    elif (user_input == 'latte'):
        choice = MENU["latte"]
        ing = choice["ingredients"]
        water = ing["water"]
        coffee = ing["coffee"]
        milk = ing['milk']
    elif (user_input == 'cappuccino'):
        choice = MENU["cappuccino"]
        ing = choice["ingredients"]
        water = ing["water"]
        coffee = ing["coffee"]
        milk = ing['milk']

    resources["coffee"] = present_coffee - coffee
    resources["milk"] = present_milk - milk
    resources["water"] = present_water - water
  

while (user_input != 'off'):
    start() 

if (user_input == 'off'):
    resources["coffee"] = 100
    resources["milk"] = 200
    resources["water"] = 300

