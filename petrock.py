import time
def gap():
    print("")

pet_rock_sim = True
print("Welcome to the Pet Rock Simulator!\n")
name = input("What would you like to name your pet rock?: ")
while len(name) > 10:
    print("This name is invalid, please use a name that is 10 or less characters in length\n")
    name = input("What would you like to name your pet rock?: ") # Gets the name of the rock from the user and checks that it is less than 10 characters in length
gap()
print("Starting Pet Rock Simulator...")
gap()
time.sleep(0.5)
day = 0
health = 10
hunger = 0
happiness = 10
anger = 0
age = 0
while pet_rock_sim:
    day += 1
    print(f"--Pet rock ({name}) stats--\n-Health = {health}/10\n-Hunger = {hunger}/10\n-Happiness = {happiness}/10\n-Anger = {anger}/10\n-Age = {age}\n---------------------\n")
    gap() # Tells the user the current game stats
    time.sleep(1)
    print(f"--What do you want to do with {name} the rock today?\n1.) Nothing\n2.) Play with {name}\n3.) Feed {name}\n4.) Pet {name}\n5.) Take {name} on walk\n6.) Take {name} to the vet\n7.) End game\n") #Tells the user their choices for the day
    temp_choice = input(f"Choose an option from 1 - 7 using the above options: ") # Asks the user for their action choice
    act_choice = 0
    invalid_name = True
    while invalid_name:
        if temp_choice.isdigit() == False:
            print(f"\nThe option {temp_choice} is not a valid option, please type a number from 1 to 6 and try again.")
            temp_choice = input(f"Choose an option from 1 - 6 using the above options: ")
        elif int(temp_choice) > 7 or int(temp_choice) < 1:
            print(f"\nThe option {temp_choice} is not a valid option, please type a number from 1 to 7 and try again.")
            temp_choice = input(f"Choose an option from 1 - 6 using the above options: ")
        else:
            invalid_name = False # Loop to verify that the user provided a valid input for the action choice
    act_choice = int(temp_choice)
    gap()
    print("Performing selected action...")
    time.sleep(0.5)
    gap()
    if act_choice == 1:
        print(f"You do nothing, {name} the rock is dissapointed..")
        happiness -= 1
        anger += 1
        hunger += 1
    elif act_choice == 2:
        print(f"You spend the day playing with {name}, {name} seems happy!")
        happiness += 3
        hunger += 1
        anger -= 1
    elif act_choice == 3:
        print(f"You decide to feed {name} the rock, it seems... satisfied?")
        happiness += 1
        anger -= 1
        hunger -= 4
    elif act_choice == 4:
        print(f"You spend the day relaxing and petting {name}, it seems relaxed.")
        happiness += 2
        anger -= 2
        health += 1
    elif act_choice == 5:
        print(f"You spend a while taking {name} for a walk, it seems tired but happy.")
        health -= 1
        hunger += 2
        happiness += 2
        anger -= 2
    elif act_choice == 6:
        print(f"You deicide that you need to take {name} to the vet, it seems angry")
        health += 5
        anger += 4
        happiness -= 4 # Changes stats based on the chosen action
    else:
        pet_rock_sim = False
    age += 1
    hunger += 1
    gap()
    time.sleep(0.5)

    if health > 10:
        health = 10
    elif health < 1:
        print(f"Your rock, {name} has run out of Hp, try taking the rock to the vet if it's Hp gets low")
        gap()
        pet_rock_sim = False
    elif health < 6:
        print(f"Your rock, {name}, has low hp, try taking it to the vet.")
        gap()
    
        
    if hunger < 1:
        hunger = 0
    elif hunger > 9:
        print(f"Your rock pet {name} is starving, feed them or they will take damage every day")
        gap()
        hunger = 10
        health -= 3

    if happiness > 10:
        happiness = 10
    elif happiness < 1:
        happiness = 0
        print(f"Your rock, {name}, is extremely unhappy, do something to cheer them up or they will continue to take damage")
        health -= 2
    
    if anger < 0:
        anger = 0
    elif anger > 9:
        print(f"Your pet rock, {name}, is furious with you, try doing something to cheer them up or they will continue to take damage")
        gap()
        anger = 10
        health -= 3
    
        
    if age == 100:
        print(f"Your rock {name} has died of old age after {day} days")
        gap()
        health -= 10
    elif age == 70:
        print(f"{name} is growing old, {name} will now take 1 damage every turn")
        gap()
    elif age == 18:
        print(f"{name} has reached adulthood")
        gap()
    elif age > 70:
        health -= 1
        print(f"Another day passes by, you are on day {day}")
        gap()
    else:
        print(f"Another day passes by, you are on day {day}")
        gap() # all age related events
    time.sleep(1)
