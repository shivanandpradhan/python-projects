# importing random for getting the random number.
from random import randint

if __name__ == "__main__" :
    
    print("{a:^60}\n".format(a = "Random Number Guessing Game"))
    print("Enter range of Number to Guess")

    # setting the range for the guessing game
    low = int(input("Enter the lowest number to Guess : "))
    high = int(input("Enter the highest number to Guess : "))

    # initial scores
    user_score = 0
    comp_score = 0


    while True : 
        # displaying message to start of end the Game.
        print("\n\nEnter :\n1 -> start the Game")
        print("0 or other no. -> end the Game")

        if (int(input("\tEnter your choice : "))) == 1 :

            # computer guessing random no. from [low,high]
            comp_guess = randint(low,high) 

            # gettig the input from user
            user_guess = int(input("\nGuess Number from [{0}, {1}] :- ".format(low, high)))


            # incrementing user_score if user guess the right number
            if user_guess == comp_guess :
                print("\n\tYou Guess it Right.")
                user_score += 1
            else : 
                print("You Guess : {0}\nComputer Guess : {1}".format(user_guess, comp_guess));
                comp_score += 1

            # printing the score at each time.
            print("\n\nUser Score : ", user_score)
            print("Computer Score : ", comp_score)

        else :
            print("\nTotal Played : ", user_score + comp_score)
            print("User Score : ", user_score)
            print("Computer Score : ", comp_score)
            break
    