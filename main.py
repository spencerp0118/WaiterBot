#Computer Science: Proposal WaiterBot
#Spencer P
foodMenu = ["Cheesebuger", "Salad", "Chicken Strips", "3Soup", "Steak"]
#I want to make it so people can choose the type of soup and salad, then also give them a change to make a change to the food, ex: they can ask for no pickles on their bugar and the WaiterBot will read it back
drinkMenu = ["Water", "Soda", "Juices"]
#like with foods I wanna give options with the type of soda and jucies they can pick
sideDishes = ["French Fries", "Beans", "Mini Salad"]

print("Hello! Welcome to the beta test of WaiterBot\nThank you for helping test this system to help make customers dining experience easier and more efficient.\n First can I please get your name?")
usersName = input()
print("Hello, " + str(usersName) + ". What can I get for you as a starting drink?")

print("To pick your drink please enter the drink name.")
print(drinkMenu)
usersDrink = (input("Please input your drink here: "))


