
# identify comments (single Line Comment) in the line..

# here space is required to identify the comment
#i.e if abc#a is written then a will not be considered as comment.
def IsComments(comments, str):

    sep = (',', ' ')

    s = ""

    for char in str : 
        if char in sep:
            if s in comments :
                return True
            s = ""
        else :
            s += char
    
    return False

#here space is not required to identify the comment
def IsCommentsWithoutSpace(comments, str):

    sep = (',', ' ')

    s = ""

    for char in str :

        # print("current string : ", s)
        # print("current char : ", char)
        if s in sep :
            s = ""

        else :

            if s in comments :
                return True
            
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
        return True 

    return False

    


if __name__ == "__main__" :

    comments = []
   
    print("Enter Symbol for comment (press (enter) when you are done): ")
    print()

    while True: 
        com = input("Enter Symbol : ")

        if com == "":
            break

        comments.append(com)
    
    print()
    str = input("Enter a line : ")


    if IsCommentsWithoutSpace(comments,str) :
        print("Yes it contains Comment")
    else :
        print("No, it does not contains Comment")
