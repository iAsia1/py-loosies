import time

age = int(input("Enter your age: "))

if age >= 18:
  print("You are old enough to vote in the U.S.!")
else :
  print("You are so young please dont go to a voting booth or deal with politics")
  party = input("Anyways which political party where you going to vote for if you grow up: ")
  
  if party == "D" :
    print("Ok good choice good choice")
  if party == "R" :
    print("Ok BAD choice HORRID choice, vote for someone else")
  if party == "Chappell Roan Party" :
    print("WOW BEAUTIFUL CHOICE....  Here is $100000 dollars and flowers coming in 3 seconds")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")

    print("$100 " * 1000)
    print("Pick the dollar bills up now!!!!")