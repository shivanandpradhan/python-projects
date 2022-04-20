
#q3
"""dfa for length of stringis odd"""


# start state
def start(c):

    # based on char input 
    # return state to move on it..
    if c == 'a' or c == 'b' :
        return 1

#first state
def state1(c):
    if c == 'a' or c == 'b' :
        return 0

#func for checking valid String or not...
def isValid(str):
    state = 0

    print("state Traversal : ")
    for char in str:

        print(state, "->" , end = " ")

        if state == 0:
            state = start(char)
        
        elif state == 1:
            state = state1(char)

    print(state)
    if state == 0 :
        return False

    return True



if __name__ == "__main__":

    # 
    str = input("Enter a String with (a,b) : ")

    if isValid(str):
        print(str, "is accepted by dfa")
    else :
        print(str,"is not accepted by dfa")