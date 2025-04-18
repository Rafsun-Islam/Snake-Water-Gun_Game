import random


computer = random.choice([-1,0,1])

youDict = {'s' : 1, 'w' : -1 , 'g' : 0}

revDict = {1 : "Snake" , -1 : "Water" , 0 : "Gun"}

youChoice = input("Enter Your Choice : ")

you = youDict[youChoice]

print(f"You Chose {revDict[you]} and Computer Chose {revDict[computer]} ")

if(computer == you):
    print("It is a DRAW!")
else:
    
    if(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Loss!")
    elif(computer == 1 and you == -1):
        print("You Loss!")
    elif(computer == -1 and you == 0):
        print("You Loss!")
    else:
        print("Something went Wrong!")