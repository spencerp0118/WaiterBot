#Computer Science: Proposal WaiterBot
#Spencer P
foodMenu = ["0- Cheesebuger", "1- Salad", "2- Chicken Strips", "3- Soup", "4- Steak"]
#I want to make it so people can choose the type of soup and salad, then also give them a change to make a change to the food, ex: they can ask for no pickles on their bugar and the WaiterBot will read it back
drinkMenu = ["0- Water", "1- Soda", "2- Juices"]
#like with foods I wanna give options with the type of soda and jucies they can pick
sideDishes = ["0- French Fries", "1- Beans", "2- Mini Salad"]

print("Hello! Welcome to the beta test of WaiterBot\nThank you for helping test this system to help make customers dining experience easier and more efficient.\n First can I please get your name?")
usersName = input()
print("Hello, " + str(usersName) + ". What can I get for you as a starting drink?")

print("To make your easier please input the corresponding number assigned to your drink of choice.")
print(drinkMenu)
usersDrink = (input("Please input your drinks number here: "))