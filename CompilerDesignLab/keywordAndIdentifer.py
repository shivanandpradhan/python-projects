
# adding keywords :- global var for storing all keywords..
keywords = ("int", "float", "double", "long", "short", "byte","if","for","while","struct","do","switch","else")

# global variable for storing all operators and separator 
operator = ('+', '-', '=', '+=','', '^',' ', ',', ';', '-=', '*', '/')


def printKeywordIdentifier(str):

    s = "" #empty string
    kw = [] #keyword list
    id = [] #identifier list

    # iterating through the string...
    for i in str : 
        if i not in operator:
            s += i
        else :
            if s in keywords:
                kw.append(s)
            elif s != "" :
                id.append(s)
            
            s = ''
    
    if s in keywords:
        kw.append(s)
    elif s != "" :
        id.append(s)
            

    print("Keywords :- ", kw)
    print("Identifier : ", id)

    return kw, id
        


if __name__ == "__main__":

    str = input("Enter the string : ")

    printKeywordIdentifier(str)
