import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"} #Converts the numbers back into names for printing.

you = youDict[youstr] #Your input string is converted into a number using youDict.

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}") #Shows what both you and the computer chose.

if(computer == you):
    print("Its a draw") #If both chose the same thing — it's a draw.

else:
    if(computer == 1 and you == 0):
        print("Yoy lose")

    elif(computer == 1 and you == -1):
        print("You lose")

    elif(computer == -1 and you == 0):
        print("You Loos")

    elif(computer == -1 and you == 1):
        print("You Won")

    elif(computer == 0 and you == 1):
        print("You Won")

    elif(computer == 0 and you == -1):
        print("You Lose")

    else:
        print("Somthing went wrong")

    
  
