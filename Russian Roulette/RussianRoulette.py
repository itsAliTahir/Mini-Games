import random
bullets = 6
bet = input("Enter Your Betting Amount: ")
bet = int(bet)
option = "y"
while bullets > 1:
    if option == "y":
        print("\nUser Risked His Life And Pulled The Pistol Trigger")
        num = random.randint(1,bullets)
        num = int(num)
        print(num)
        if num != 1:
            bet *= 1.5
            print("User Survived and Won", bet)
            bullets -= 1
            if bullets != 1:
                option = input("\nDo You Want To Pull The Trigger Again (y/n): ")
        else:
            print("User Died And Lost All Money")
            bullets = 0
    else:
        print("\nThanks For Participating!")
        bullets = 0