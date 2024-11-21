import random

input = str(input("Would you like to input your number, or generate one? "))

while True :
    if input == "input" : 
        print("")
        roll1 = int(input("First die? "))
        roll2 = int(input("Second die? "))

        outcome1 = roll1 % 2
        outcome2 = roll2 % 2

        if outcome1 == 0 or outcome2 == 0 :
            even = True
        else :
            even = False
        
        print("")
        print("Rolled evens? " + str(even))
    if input == "generate" :
        print("")
        roll3 = print("First number: " + random.randint(1, 6))
        roll4 = print("Second number: " + random.randint(1, 6))

        outcome3 = roll3 % 2
        outcome4 = roll4 % 2

        if outcome3 == 0 or outcome4 == 0 :
            even2 = True
        else :
            even2 = False

        print("")
        print("Rolled evens? " + str(even2))
    if input == "" :
        break