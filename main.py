import random

# Randomly select the computer's choice
computer = random.choice([-1, 0, 1])

# Dictionary for user input
youDict = {'s': 1, 'w': -1, 'g': 0}

# Reverse dictionary for showing results
revDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get user's choice
youChoice = input("Enter Your Choice (s = Snake, w = Water, g = Gun): ").lower()

# Convert the user's choice to corresponding integer value
you = youDict[youChoice]

# Print the choices
print(f"You Chose {revDict[you]} and Computer Chose {revDict[computer]}")

# Check for draw
if computer == you:
    print("It is a DRAW!")
else:
    # Check the win/loss conditions
    if (computer == 1 and you == 0) or (computer == -1 and you == 1) or (computer == 0 and you == -1):
        print("You Win!")
    elif (computer == 0 and you == 1) or (computer == 1 and you == -1) or (computer == -1 and you == 0):
        print("You Loss!")
    else:
        print("Something went wrong!")
