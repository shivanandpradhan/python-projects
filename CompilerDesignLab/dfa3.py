#q4
#Construct a DFA with at least 2 a’s and 2b’s


#start Symbol
def start(c):
    if c == 'a':
        return 1
    elif c == 'b':
        return 5 

#first state
def state1(c):
    if c == 'a':
        return 8
    elif c == 'b':
        return 2

#second state
def state2(c):
    if c == 'a':
        return 3
    elif c == 'b':
        return 7 

#third state
def state3(c):
    if c == 'a':
        return -1
    elif c == 'b':
        return 4    

#four state -> final


#state no. 5
def state5(c):
    if c == 'a':
        return 6
    elif c == 'b':
        return 9   


#state no. 6
def state6(c):
    if c == 'a':
        return 3
    elif c == 'b':
        return 7   


#state no. 7
def state7(c):
    if c == 'a':
        return 4
    elif c == 'b':
        return -1   


# state no. 8
def state8(c):
    if c == 'a':
        return -1
    elif c == 'b':
        return 3  


#state no. 9
def state9(c):
    if c == 'a':
        return 7
    elif c == 'b':
        return -1   


# checking for valid string 
def isValid(str):

    state = 0

    print("State Traversal")

    for char in str:

        print(state,end=" -> ")

        if state == -1:
            print("trap")
            return False

        if state == 0 :
            state = start(char)

        elif state == 1 :
            state = state1(char) 

        elif state == 2 :
            state = state2(char)

        elif state == 3 :
            state = state3(char)
        
        elif state == 5 :
            state = state5(char)

        elif state == 6 :
            state = state6(char)

        elif state == 7 :
            state = state7(char)

        elif state == 8 :
            state = state8(char)

        elif state == 9 :
            state = state9(char)

    print("Accept")
    return True



if __name__ == "__main__":

    str = input("Enter a String : ")

    if isValid(str):
        print(str, "is accepted")
    else:
        print(str, "is not accepted")