import random as rand
num=rand.randint(1,10)
guess = None
Score = 10
while guess!=num:
    guess=int(input("Enter a number in range 1-10:"))
    if guess == num:
        print("Congratulations,you have won the game")
        Score+=5
        print("Your score is:",Score)
    else:
        print("Sorry,please try again")
        Score+=-2
        print("Your score is:",Score)
        if Score<=0:
            print("Game over")
            break
