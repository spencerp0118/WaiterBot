#Computer Science: Proposal WaiterBot
#Spencer P

foodMenu = ["Cheesebuger", "Chicken Strips", "Soup", "Pizza"]

drinkMenu = ["0- Water", "1- Coke", "2- Pepsi"]

sideDishes = ["French Fries", "Beans", "Mini Salad"]

print("Hello! Welcome to the beta test of WaiterBot\nThank you for helping test this system to help make customers dining experience easier and more efficient.\n First can I please get your name?")
usersName = input()
print("Hello, " + str(usersName) + ". What can I get for you as a starting drink?")

print("To pick your drink please enter the drink's number'.")
print(drinkMenu)
usersDrink = int((input("Please input your drink's number here: ")))
print("You picked, " +drinkMenu[usersDrink]+ ", it will arrive to your table soon.")

#if usersDrink in drinkMenu:
 #print("wow") 

print("Great now that you ordered your drink, would you like to see the Menu or the Special for today?")
usersChoice = input()

if usersChoice == "Menu":
  print(foodMenu)
  usersMeal = str(input("What would you like to order?\nPlease insert here: "))
  while not usersMeal in foodMenu:
    print("Hmm I don't see what you are trying to order please try again.")
    print(foodMenu)
    usersMeal = str(input("What would you like to order?\nPlease insert here: "))

  if usersMeal in foodMenu:
    print("Great it looks like you ordered a " +usersMeal+ ". If you have any special instructions for your food please insert here, if not leave blank:\n")
    menuMealInstructions = str(input())
    print("Great it looks like you have ordered " +str(usersMeal)+ ", " +str(menuMealInstructions)+ " . It will be brought to you soon.")

if usersChoice == "Special":
  print("Great today special is, Sloppy Joes.\nWould you like to order this?")
  specialOption = str(input())
  if specialOption == "yes":
    print("Great! You order has been sent to the kitchen, do you have any special instructions, if not leave blank.")
    speicalsMealInstructions = str(input())
    print("Awesome, your Sloppy Joes, " +str(speicalsMealInstructions)+ " will be there soon.")
  
  else:
    print("Alrighty, I will take you back to the main menu.")
    print(foodMenu)
    print("What would you like to order?")
    userMeal2 = input()

    if not userMeal2 in foodMenu:
      print("I don't see what you tried to order please try again.")
      print(foodMenu)
      userMeal2 = input("What would you like to order:\n")

    if userMeal2 in foodMenu:
      print("Great you ordered, " +str(userMeal2)+ ", is there any special instructions you have? If so type them below:\n")
      specialInstructions = input()

    print("Great it looks like you ordered, " +str(userMeal2)+ ", " +str(specialInstructions)+ " it will be at your table soon.")

print("Nice, your food and drink will arrive at your table soon, in the mean time would you like to rate your time with WaiterBot?")
whatToRate = input("-Yes\n-No\n")

if whatToRate == "Yes":
  print("Thank you for helping improve WaiterBot.")
  rating = input("Please put your input here:")
  print("Thank you for saying, " +str(rating)+ " hope you enjoy your meal.")
  exit()

if whatToRate == "No":
  print("That's okay, I hope you enjoy your meal.")
  exit()

else:
  print("Not to sure what you said, but your meal will arrive soon so enjoy.")
  exit()
    
  

