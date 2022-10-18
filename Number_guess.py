import random as rand
num=rand.randint(0,10)
guess = None
Score = 10
while Score!=0:
    if Score<=0:
        print("Game over")
        break
    guess=int(input("Enter a number in range 1-10:"))
    if guess == num:
        print("Congratulations,you have won the game")
        Score+=5
        print("Your score is:",Score)
    elif guess<num:
        print("Your number is less than the random number")
        Score+=-2
        print("Your score is:",Score)
        if Score<=0:
            print("Game over")
            break
    elif guess>num:
        print("Your number is greater than the random number")
        Score+=-2
        print("Your score is:",Score)
        if Score<=0:
            print("Game over")
            break
