import random
num = random.randint(1,100)
chances = 5
print("Guess The Random Generated Number From 1 to 100 (Chances:",chances,")\n")
while chances > 0:
    guess = input("Enter Your Number: ")
    guess = int(guess)
    if guess == num:
        print("You Have Guessed The Number Correctly!")
        print("Your Score:", chances*20)
        chances = 0
    else:
        chances-=1        
        print("Incorrect Answer!")
        if num > guess: print("Your Number ",guess, " is Smaller Than That Number" )
        else: print("Your Number ",guess, " is Greater Than That Number" )
        print("Chances Left:", chances, "\n")
if guess != num:
    print("You Lost!")
    print("The Number Was ", num)    
    print("Your Score: 0")
