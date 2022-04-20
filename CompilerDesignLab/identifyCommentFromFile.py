
#here space is not required to identify the comment
def IsCommentsWithoutSpace(comments, str):
    """return tuple of (boolean contains comment, current position)"""

    # for empty line
    if str == " ":
        return False

    # for seperator
    sep = (',', ' ')

    # initial string for scanning
    s = ""

    # curr_pos : will use for displaying comment
    curr_pos = -1

    for char in str :

        # print("current string : ", s)
        # print("current char : ", char)

        #incrementing the current postion
        curr_pos += 1

        if s in sep :
            s = ""

        else :

            #if comment is found
            if s in comments :
                return True,curr_pos
            
            #finding whether current s is in any 
            
            res = 0 
            for comment in comments :
                if s in comment : 
                    res = 1
                    break

            if res == 1:
                s += char
            else :
                s = char 

    if s in comments : 
        return True, curr_pos 

    return False, curr_pos

    


if __name__ == "__main__" :

    comments = []
   
    print("\nEnter Symbol for comment (press (enter) when you are done): ")
    print()

    while True: 
        com = input("Enter Symbol : ")

        if com == "":
            break

        comments.append(com)
    
    print()
    
    with open("abc.txt", 'r') as file :
        
        commentsInCode = []

        for line in file :

            res = IsCommentsWithoutSpace(comments, line) 
            #res will store tuple (boolean, pos where we got false or true)


            if res[0] == True:
                commentsInCode.append(line[res[1]:])

    if len(commentsInCode)  == 0 :
        print("No comments in the file")

    else :
        print("comments :- ")
        for line in commentsInCode:
            print(line,end="")
