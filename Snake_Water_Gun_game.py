import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1, -1, 0])

you = input("Enter your choice (s/w/g): ")

youDict = {"s": 1, "w": -1, "g": 0}
younum = youDict[you]

print("Computer chose:", computer)

if computer == younum:
    print("Draw")

elif computer == -1 and younum == 1:
    print("You win")

elif computer == -1 and younum == 0:
    print("You lose")

elif computer == 1 and younum == 0:
    print("You win")

elif computer == 1 and younum == -1:
    print("You lose")

elif computer == 0 and younum == 1:
    print("You lose")

elif computer == 0 and younum == -1:
    print("You win")