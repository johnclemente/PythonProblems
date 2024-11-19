import math
import sys
# requirements

"""1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    a. Check the user’s input to decide what to do next.
    b. The prompt should show every time action has completed, e.g. once the drink is
    dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
    the current resource values. e.g.
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
4. Check resources sufficient?
    a. When the user chooses a drink, the program should check if there are enough
    resources to make that drink.
    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    not continue to make the drink but print: “ Sorry there is not enough water. ”
    c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
    a. If there are sufficient resources to make the drink selected, then the program should
    prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
    a. Check that the user has inserted enough money to purchase the drink they selected.
    E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
    program should say “ Sorry that's not enough money. Money refunded. ”.
    b. But if the user has inserted enough money, then the cost of the drink gets added to the
    machine as the profit and this will be reflected the next time “report” is triggered. E.g.
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
    c. If the user has inserted too much money, the machine should offer change. """

machineResources = {'milk':0, 'water':100, 'coffee': 76, 'money': 2.5}

cappiccinoCost = {'milk':5, 'water':10, 'coffee': 10, 'money': 1}
latteCost = {'milk':20, 'water':0, 'coffee': 10, 'money': 1}
espressoCost = {'milk':0, 'water':10, 'coffee': 10, 'money': 1}

def main():
    print("Welcome to the coin-operated coffee machine. Would you like a (c)appiccino, a (l)atte, or a (e)spresso?")
    userInput = "" 
    while userInput not in ["report","off","add resources","e","l","c"]:
        userInput = input("what do you want? ")
    if userInput == "report":
        report()
    if userInput == "e":
        for resource in espressoCost.keys():
            if espressoCost[resource] > machineResources[resource]:
                print(f'not enough of {resource} for espresso')
                main()
            else:
                paymentProcess()
                print("Enjoy your espresso!")
                print("Returning back to main menu")
                main()
    if userInput == "l":
        for resource in latteCost.keys():
            if latteCost[resource] > machineResources[resource]:
                print(f'not enough of {resource} for latte')
                main()
            else:
                paymentProcess()
    if userInput == "c":
        for resource in cappiccinoCost.keys():
            if cappiccinoCost[resource] > machineResources[resource]:
                print(f'not enough of {resource} for cappiccino')
            if cappiccinoCost[resource] > machineResources[resource]:
                main()
            else:
                paymentProcess()
    if userInput == "add resources":
        addResources()
        main() 
    if userInput == "off":
        print("goodbye")
        sys.exit()
        
def addResources():
    resource = ""
    amount = ""
    print("Welcome machine maintainer person")
    while resource not in ["milk", "water"]:
        resource = input("what would you like to add? ")
    if resource == "milk":
        amount = input("how much?: ")
        amount = int(amount)
        machineResources["milk"] = machineResources["milk"] + amount
    if resource == "water":
        amount = input("how much?: ")
        amount = int(amount)
        machineResources["water"] = machineResources["water"] + amount
            
def paymentProcess():
    quartersStr = input("Please provide your number of quarters: ")
    dimesStr = input("Please provide your number of dimes: ")
    nickelsStr = input("Please provide your number of nickels: ")
    penniesStr = input("Please provide your number of pennies: ")
    
    quarters = int(quartersStr)
    dimes = int(dimesStr)
    nickels = int(nickelsStr)
    pennies = int(penniesStr) 
    
    totalPennies = (quarters*25) + (dimes*10) + (nickels*5) + (pennies)
    totalMoney = totalPennies/100

    drinkCost = int(machineResources["money"])
    if totalMoney >= drinkCost:
        change = totalMoney - drinkCost
        actualChnage = round()
        print(f"you provided {totalMoney}")
        print(f"cost of drink is: {drinkCost}")
        print(f"{change} is your change")
    else:
        print("That is not enough money")
        print(f"you provided {totalMoney}")
        print(f"cost of drink is: {drinkCost}")
        print(f"{change} has been returned, please provide enough next time")
        print("returning to menu")
        main()


    
                    
                
        
def report():
    print(machineResources.items()) 
    main()
    
        
main() 