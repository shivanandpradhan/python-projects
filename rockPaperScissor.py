from random import choice

if __name__ == "__main__":

    """ Game of Rock Paper and Scissor 
        where rock beats scissor
              scissor beats paper
                    and 
              paper beats rock"""

    print("{a:^60}".format(a = "Rock, Paper and Scissor Game"))
   

    # 3 items - rock, paper and scissor
    items = ("rock", "paper", "scissor")


    # initial scores
    user_score = 0
    comp_score = 0

    # total matches
    total_match = 0

    # draw match
    draw_match = 0

    while True : 
        # displaying message to start of end the Game.
        print("\n\nEnter :\n1 -> start the Game")
        print("0 or other no. -> end the Game")


        if (int(input("\tEnter your choice : "))) == 1 :


            print("\n\n\tEnter for selecting : ")
            print("\t\tRock -> 1")
            print("\t\tPaper -> 2")
            print("\t\tScissor -> 3")

            # randomly item selected by computer
            comp_select = items.index(choice(items)) + 1

            # gettig the input from user
            user_select = int(input("\nEnter your Choice : "))


            # print the selection....
            print("\n\nUser selected : ",items[user_select - 1])
            print("Computer selected : ",items[comp_select - 1])

            # user - rock and comp - scissor
            # user - scissor and comp - paper
            # user - paper and comp - rock
            if (user_select == 1 and comp_select == 3) or (user_select == 3 and comp_select == 2) or (user_select == 2 and comp_select == 1):
                print("\"nYou Won")
                print("\t{0} beats {1}".format(items[user_select - 1], items[comp_select - 1]))
                user_score += 1

            elif (user_select == comp_select):
                print("Game Draw ")
                draw_match += 1

            else : 
                print("\nYou loss")
                print("\t{1} beats {0}".format(items[user_select - 1], items[comp_select - 1]))
                comp_score += 1

            total_match += 1 

            # printing the score at each time.
            print("\n\nUser Score : ", user_score)
            print("Computer Score : ", comp_score)
            print("Draw : ", draw_match)

        else :
            print("\nTotal Played : ", total_match)
            print("User Score : ", user_score)
            print("Computer Score : ", comp_score)
            print("Draw : ", draw_match)
            break
    

    
