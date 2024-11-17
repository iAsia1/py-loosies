username = input("Enter your username = ") 
password = input("Enter your password = ") 
print(" ") 

if password == "a" : 
    command = input(str("Welcome to the security module, enter your command: ")) 
    if command == "destroy" : 
        print(" ") 
        print("Thank you for killing me soldier, deactivating") 
        print("1010010011100110" * 1000) 
    if command == "echo" : 
        print(" ") 
        echo = input("Enter your text here: ")
        print(echo) 
    if command == "add" : 
        print(" ") 
        addend1 = input("Enter the first number: ") 
        addend2 = input("Enter the second number: ") 
        addres = int(addend1) + int(addend2) 
        print("Your sum is: " + str(addres)) 
    if command == "sub" :
        print(" ") 
        minuend1 = input("Enter the first number: ")
        minuend2 = input("Enter the second number: ") 
        subres = int(minuend1) - int(minuend2) 
        print("Your difference is: " + str(subres)) 
    if command == "mul" : 
        print(" ") 
        factor1 = input("Enter the first number: ") 
        factor2 = input("Enter the second number: ") 
        mulres = int(factor1) * int(factor2) 
        print("Your product is: " + str(mulres)) 
    if command == "div" : 
        print(" ") 
        dividend1 = input("Enter the first number: ") 
        dividend2 = input("Enter the second number: ") 
        divres = int(dividend1) / int(dividend2) 
        print("Your quotient is: " + str(divres)) 
else : 
    print("Wrong password, run again")