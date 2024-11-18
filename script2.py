import random

def numbergame() :
    print("Hi baby, Welcome to Number game ")
    number = random.randint(1, 100)
    attempts = 0
    
    while True :
        try : 
            guess = int(input("Guess the number: "))
            attempts += 1
            
            if guess < 1 or guess > 100 :
                print("Try again ")
            elif guess < number :
                print("Too low ")
            elif guess > number :
                print("Too high ")
            else :
                print(f"You guessed the number after {attempts} attempts! Good Job!! ")
                break
        except ValueError :
            print("Yay ")
        
numbergame()