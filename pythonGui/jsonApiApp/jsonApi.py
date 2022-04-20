from tkinter import *
from tkinter import messagebox
import json


api = [] #container for api

if __name__ == "__main__" :

    # getting the input from the users

    inputs = []

    n = int(input("Enter total no. of fields (< 10) : "))

    for i in range(n):
        inputs.append(input("Enter Field Name : ").capitalize())


    #---------------------------- creating an App -----------------------------

    win = Tk()

    # setting icons,title, background, and geometry of window...
    win.title("Json Gui")
    win.iconbitmap("./json.ico")
    win.geometry("1000x1000")
    win['bg'] = "#CEE7EF"
    

    #---------------------------------------- top of the app----------------

    #heading
    topFrame = Frame(win, bg = "#CEE7EF")
    topFrame.pack(side = TOP, fill = X)

    Label(topFrame, text = "Welcome To Json Api App", bg = "#CEE7EF", font = ("Arial", 24, "bold"), fg = "red").pack()



    #--------------------------------------- middle part of the App -------------------------------


    #storing the data type for each input field..
    # a dictionary for storing all the data type of input field.

    var_type = dict()

    #printing information on the console..
    print("\nEnter Data Type : ")
    print("\tstring -> for StringVar()")
    print("\tint -> for IntVar()")
    print("\tdouble -> for DoubleVar()")
    print("\tboolean-> for BooleanVar()\n")
       

    for field in inputs :

        data_type = input("\n Enter data type for {} : ".format(field))

        if data_type == "int" :
            var_type[field] = IntVar()
        elif data_type == "double":
            var_type[field] = DoubleVar()
        elif data_type == "boolean" :
            var_type[field] = BooleanVar()
        # default data type
        else :
            var_type[field] = StringVar() 

    
    # displaying all the field inside the middle Frame..

    frame = Frame(win,  bg = "#CEE7EF")
    frame.pack(padx = 10, pady = 10)

    # storing all the entries..
    entryList = []
        

    #displaying label and entry

    for i in range(len(inputs)) :
        
        label = Label(frame, text = inputs[i], bg = "#CEE7EF", font = ("Arial", 13, "bold"))
        label.grid(row = i, column = 0, padx = 10, pady = 10)

        entry = Entry(frame, textvariable = var_type[inputs[i]], bd = 3, font = ("Arial", 15, "bold"), width = 40)
        entry.grid(row = i, column = 1, padx = 10, pady = 10)

        entryList.append(entry)


    # ------------------------------------ add data in the Api -----------------------------------
    
    def addInApi() :
        """  adding current data entered in the local api list"""

        data_values = dict()

        flag = True

        for i in range(len(inputs)) :

            try : 
                data  = var_type[inputs[i]].get()
            
            except :

                data = ""

            if data == "" :
                flag = False 
                messagebox.showwarning("Warning", "All fields are Required")
                break
            else :
                data_values[inputs[i]] = data
        
        if flag :
            for entry in entryList :
                entry.delete(0, END)

            api.append(data_values)
                

    # creating a json File abc.json
    def createSampleJsonFile() :
        """ create a sample abc. json file"""

        if len(api) == 0:
            messagebox.showwarning("Warning" , "No data in Api")
            return
            
        response = messagebox.askyesno("Do you want to Create a file", "abc.json")
        if response:
            with open("abc.json", "w") as file :
                file.write(json.dumps(api, indent = 4))


    
    #adding buttons
    btnContainer = Frame(win, bg = "#CEE7EF")
    btnContainer.pack()

    #button for storing data in the api
    Button(btnContainer, text = "Add in the Api", command = addInApi).grid(row = 0, column = 0, padx = 10, pady = 10)

    #button for creating a json File abc.json
    Button(btnContainer, text= "Save Api in abc.json", command = createSampleJsonFile).grid(row = 0, column= 1, padx = 10, pady = 10)


    #---------------for creating and saving file and let user type name of the file -----------------

    userFileFrame = Frame(win, bg = "#C337EF")
    userFileFrame.pack(padx = 10, pady = 10)

    #creating a label and entry for user to write the name of the file
    Label(userFileFrame, text ="Enter the name of file : ",bg = "#CEE7EF").grid(row = 0, column = 0, padx = 10, pady = 10)

    varFile = StringVar()
    entryFile = Entry(userFileFrame, textvariable = varFile, width= 30, font = ("Arial", 12, "italic"))
    entryFile.grid(row = 0, column = 1, padx = 10, pady = 10)


    #function
    def createAndSaveJsonFile():

        file = varFile.get()

        if file == "" :
            messagebox.showwarning("Warning", "No name is written for file")
            return 

        if file.find(".json") == -1 :
            file += ".json"

        response  = messagebox.askyesno("Do you want to create file :",file)

        if response : 
            with open(file, "w") as f :
                f.write(json.dumps(api, indent = 4))
            entryFile.delete(0,END)


    #btn for create and save a json file
    Button(userFileFrame, text = "Create and Save (.json File)", command = createAndSaveJsonFile).grid(row = 1, column = 1, padx = 5, pady = 5)


    win.mainloop()