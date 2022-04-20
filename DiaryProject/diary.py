import tkinter as tk
from tkinter import Frame, Listbox, PhotoImage, StringVar, ttk
from tkinter import messagebox
import datetime as dt
from tkinter.constants import END
from typing import Text


from PIL import ImageTk, Image


import sqlite3

# this is for creating a data base
# for first Time.......

# creating a database diary.db and 
# creating a table having field id, date and content.

# establishing a connection...
conn = sqlite3.connect("diary.db")

try:
    #creating a Table....
    conn.execute('''CREATE TABLE DIARY
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DATE TEXT NOT NULL,
                CONTENT TEXT NOT NULL);''')
except:
    pass



# getting the today date
dateObj = dt.datetime.now()

# formating the date object into required form
date = dateObj.strftime("%d-%m-%Y")


class FirstPage(tk.Frame):

    def __init__(self, parent, controller)  :
        tk.Frame.__init__(self, parent)

        # Frame for first page
        f1 = tk.Frame(self, background="#8DD9BB")

        f2 = tk.Frame(f1, width=100, height=100, highlightbackground="white", highlightthickness=2, background = "#8DD9BB")

        f1.pack(fill="both", expand=True)
        f2.place(in_=f1, anchor="c", relx=.5, rely=.5)


        f3 = tk.Frame(f2, background = "#8DD9BB")
        f3.pack(side = "left")

        f4 = tk.Frame(f2,  background = "#8DD9BB")
        f4.pack(side="left", padx = 20)

        # canvas = tk.Canvas(f3, width = 400, height=300, bg = "#8DD9BB")
        # canvas.pack(padx = 20)


        img = Image.open("./diary.png")
        resize_image = img.resize((250,250), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resize_image)

        # # img = ImageTk.PhotoImage(Image.open("./diary.png"))
        # canvas.create_image(20,20, anchor="nw", image = new_image)
        # canvas.image = new_image
        img_label = tk.Label(f3, image=new_image, bg = "#8DD9BB")
        img_label.image = new_image

        img_label.pack(side ="left", padx = 40, pady = 20)

        #------------------- heading of Frame -------
        tk.Label(f1, text= "Diary Application", bg = "#8DD9BB", fg="#160A3F", font = ("Helvetica", 22, "bold")).pack(padx = 50, pady = 20)

        # Write Button...
        writeBtn = tk.Button(f4, text = "Write In Diary", bg = "white", fg = "#FF4B1A", font = ("Helvetica", 12, "bold"), command= lambda : controller.show_frame(WritePage))

        # Read Button....
        readBtn = tk.Button(f4, text="Read Diary", bg = "white", fg = "#FF4B1A", font = ("Helvetica", 12, "bold"), command = lambda : controller.show_frame(ReadPage))
        
        # Close Button...
        closeBtn = tk.Button(f4, text= "Close", bg = "white", fg = "#FF4B1A", font = ("Helvetica", 12, "bold"), command = lambda : controller.close_window())
        
        # packing buttons...
        writeBtn.pack(pady = 10, fill = "x")
        readBtn.pack(pady = 10, fill = "x")
        closeBtn.pack(pady = 10, fill = "x")


# ------------------------- write Page :-------------------------- 

class WritePage(tk.Frame):

    def __init__(self, parent, controller)  :
        tk.Frame.__init__(self, parent)


        # frame for write page..
        f1 = tk.Frame(self, background = "#8DD9BB")
        f1.pack(fill = "both", expand = True)

        # frame for top -- heading...
        f2 = tk.Frame(f1, background = "#8DD9BB")
        f2.pack()

        #heading of the header...
        tk.Label(f2, text = "Write In Diary", bg = "#8DD9BB", fg="#160A3F", font = ("Helvetica", 22, "bold")).pack(side = "left", padx = 50, pady = 20)
        
        #button to go to home Page..
        tk.Button(f2, text = "Home Page", bg = "white", fg = "#E34B1A", font = ("Helvetica", 12, "bold"), command = lambda : controller.show_frame(FirstPage)).pack(side = "right")


        # -------------- middle frame ----------

        # creating a Frame
        f3 = tk.Frame(f1, background = "white")
        f3.pack(pady = 20)

        #label for middle frame.
        tk.Label(f3, text = "Write Whatever You Want ? ",bg = "white", fg = "#000702", font = ("Helvitica", 14, "bold")).pack(pady = 5)

        # var = StringVar()
        content = tk.Text(f3, height = 15, bg = "white", fg = "blue", font = ("Helvitica", 12, "bold"))
        content.pack(expand = True)

        f4 = tk.Frame(f1,background="#8DD9BB")
        f4.pack()


        #  a method for checking whether today data is posted  by user or not.
        def checkForTodayPost():
            """check whether user already posted data or not"""
            
            # checking for today date...
            checkDate = conn.execute(f"select DATE from DIARY where date == '{date}'")

            # if check date is not none..
            # means data is already posted for today :- return false.
            
            sum = 0
            
            for x in checkDate:
                sum += 1
                break
        
            return True if sum == 0 else False  # means data is posted already.



        # add the content in the diary with field as date and content.. written.
        def addInDiary():

            # getting the content written by user 
            # inside the text box...
            data = content.get("1.0", END)

            if data == "\n" :
                # show warning message.
                messagebox.showwarning("Warning", f"Enter The Text First.")
                return

            # checking for whether user
            # has posted something inside the db or not.
            if not checkForTodayPost():

                # displaying the message to the user.....
                # if he already posted...
                messagebox.showwarning("Warning","Today Diary is already Written.")
                return

            # data should not be empty..
            if data != "\n" :
                
                #insert date and content inside diary table in diary.db.
                conn.execute(f"Insert into DIARY ( date, content) values ( '{date}', '{data}')")
                
                # commit so that data should be saved....
                conn.commit()

                # displaying message to the user..
                # data is saved in the table..
                messagebox.showinfo("Information",f"Text Saved for today :- {date}")

                # deleting the text inside the text box..
                # make it empty..
                content.delete(1.0,END)
            
        

        # action done on submit by the user....   
        def handleSubmit():
            
            # getting the response from the user.
            response  = messagebox.askyesno("Save In DB or not","Are you done with today's Diary ? ")

            # if user is agreed, then save inside the database...
            if response : 
                addInDiary()
            
        
        # update the diary for today..
        def updateInDiary(append):
            
            # getting the data from the text box
            data = content.get("1.0", END)

            # if data is not empty inside the text box...
            if data != "\n" :

                #query
                query = ""

                if append:

                    # getting the previous data.
                    todayData = conn.execute(f"select content from DIARY where date = '{date}'")

                    # store the previous data inside new data
                    newData = ""
                    for x in todayData:
                        newData += x[0]
                    
                    newData += data

                    query = f"update DIARY set content = '{newData}' where date = '{date}'; "
                else:
                    query = f"update DIARY set content = '{data}' where date = '{date}'; "

                # update the entry for the current date...
                conn.execute(query)
                
                # make the changes permanent..
                conn.commit()

                # displaying the message... of Text Updated.
                messagebox.showinfo("Information", f"Text Updated for today :- {date}")

                # finally deleting the content from the text box..
                content.delete(1.0,END)

            else:
                # show warning message.
                messagebox.showwarning("Warning", f"Enter The Text First.")


        # Buttons ................
        tk.Button(f4, text = "Submit", bg = "green", fg = "white", font = ("Helvetica", 12, "bold"), command = lambda : addInDiary()).pack(side = "left")
        tk.Button(f4, text = "Update For Today", bg = "white", fg = "#E34B1A", font = ("Helvetica", 12, "bold"), command = lambda : updateInDiary(False)).pack(side = "left", padx = 15)
        tk.Button(f4, text = "Append For Today", bg = "blue", fg = "white", font = ("Helvetica", 12, "bold"), command = lambda : updateInDiary(True)).pack(side = "left")


# ------------------------------------- read page ----------------------------

class ReadPage(tk.Frame):

    def __init__(self, parent, controller)  :
        tk.Frame.__init__(self, parent)

        #frame for read page...
        f1 = tk.Frame(self, background = "#8DD9BB")
        f1.pack(fill = "both", expand = True)

        # ----------------- top header ------------------

        #frame for top header...
        f2 = tk.Frame(f1, background = "#8DD9BB")
        f2.pack()

        #heading of the header...
        tk.Label(f2, text = "Read Diary", bg = "#8DD9BB", fg="#160A3F", font = ("Helvetica", 22, "bold")).pack(side = "left", padx = 50, pady = 20)
        
        #button to go to home Page..
        tk.Button(f2, text = "Home Page", bg = "white", fg = "#E34B1A", font = ("Helvetica", 12, "bold"), command = lambda : controller.show_frame(FirstPage)).pack(side = "right")


        # ------------ ------ middle frame ---------------


        # frame for date display.. combo box.
        f3 = tk.Frame(f1, background = "#8DD9BB")
        f3.pack()

        #display the text
        tk.Label(f3, text="Select Date :- ", font = ("Helvetica", 10, "bold")).pack(side = "left")


        #database handling...

       

        #get all dates from the database...
        def getDates():
            """ Get all dates from the Data Base.. """

            #query for selecting date from the database.
            datesEntry = conn.execute("SELECT DATE FROM DIARY")

            # storing dates in the date 
            dates = []

            for each in datesEntry :
                dates.append(each)
            
            
            return dates

        
        # method for storing text inside the text box.
        # on selecting the item inside the combo box.
        def addInTextBox(event = None):

            # deleting the content from the text box..
            content.delete(1.0, END)

            # if event happended..
            if event:
                
                #requried Query...
                selectedDateData = conn.execute(f"Select content from DIARY where date = '{var.get()}'")

                # displaying the data inside the text box..
                for x in selectedDateData:
                    content.insert(1.0,x[0])

        #getting the dates 
        dates = getDates()



        #var for storing the selected data inside the list.
        var = tk.StringVar()

        # ComboBox for selecting the dates.
        list = ttk.Combobox(f3,width=10,textvariable = var, font = ("Helvetica", 10, "bold"))
        list.pack(side = "left")

        #storing the dates inside the list.
        list['values'] = dates

        # binding an event with the combobox..
        list.bind('<<ComboboxSelected>>', addInTextBox)

        # function for reloading dates 
        # required after entering the today text..
        def reloadDates():
            # fetching new dates...
            dates = getDates()
            list['values'] = dates

            messagebox.showinfo("Information", "Dates are reloaded......")

        tk.Button(f3, text = "Reload", bg = "brown", fg = "white", font = ("Helvetica", 10, "bold"), command = lambda : reloadDates()).pack(side = "right", padx=10)



        
        # frame for text box ........
        f4 = tk.Frame(f1, background = "white")
        f4.pack(pady = 20)


        #label for text..
        tk.Label(f4, text = "Display Area",bg = "white", fg = "#000702", font = ("Helvitica", 14, "bold")).pack(pady = 5)

        # text box
        content = tk.Text(f4, height = 15, fg = "blue", font=("Helvitica", 12, "bold"))
        content.pack(expand = True)  

     
# Main Application........

class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs) :
        tk.Tk.__init__(self, *args, **kwargs)

        #setting title of the application.
        # setting the icon as well..
        self.winfo_toplevel().title("Diary App")
        self.winfo_toplevel().iconbitmap("./diary.ico")


        self.window = tk.Frame(self)
        self.window.pack()

        self.window.grid_rowconfigure(0, minsize = 500)
        self.window.grid_columnconfigure(0, minsize = 800)

        self.frames = {}
        for F in (FirstPage, WritePage, ReadPage) :
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0,sticky='nsew')
        self.show_frame(FirstPage)

    def show_frame(self, page) :
        frame = self.frames[page]
        frame.tkraise()
    
    def close_window(self):
        self.winfo_toplevel().destroy()


app = Application()
app.mainloop()

# closing the connection...
conn.close()