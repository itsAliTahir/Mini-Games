import random
import msvcrt
score1 = 0
score2 = 0
user = 4
while(user!=0):
    comp = random.randint(1,3)
    print("\nUser Scores:", score1, "\t\t||\t Computer Scores:", score2)
    print("Press 1 To Select Rock\nPress 2 To Select Paper\nPress 3 To Select Scissors")
    user = msvcrt.getch()
    user = int(user)
    tools = ["Rock", "Paper", "Scissors"]
    if (user > 0 and user < 4):
        print("\n\nUser Selected: ",tools[user-1], "\nComputer Selected: ",tools[comp-1],"")        
        if comp==user:
            print("Tied")
        elif comp!=user:
            if (user == 2 and comp == 1) or (user == 3 and comp == 2) or (user == 1 and comp == 3):
                score1 += 1
                print("User Won")
            else:
                score2 += 1
                print("Computer Won")
    else: 
        print("Invalid Option, Retry \n")