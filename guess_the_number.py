import random

play_again = True

while play_again:
    com_num = random.randint(1,100)
    status = True
    count = 5
    while status:
        if count>0:
            user_num = int(input("Guess the number : "))
            if user_num > com_num:
                print("You choose a greater number!!!!")
            elif user_num < com_num:
                print("You choose a smaller number!!!!")
            else:
                print("You choose the correct number!!!!")
                status = False
            count-=1
        else:
            print("All Tries over")
            status = False
    choice = input("Choose y to continue and press n to exit : ")
    choice = choice.lower()
    if choice=="n":
        play_again = False
        print("Game Over!!!!")
    else:
        play_again = True
        print("Lets play again")