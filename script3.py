import random

command = str(input("Would you like to input your number, or generate one? "))

while True :
    if command == "input" : 
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
    if command == "generate" :
        print("")
        numa = random.randint(1, 6)
        numb = random.randint(1, 6)
        print("First number: " + str(numa))
        print("Second number: " + str(numb))

        outcome3 = numa % 2
        outcome4 = numb % 2

        if outcome3 == 0 or outcome4 == 0 :
            even2 = True
        else :
            even2 = False

        print("")
        print("Rolled evens? " + str(even2))
        break
    if command == "" :
        break