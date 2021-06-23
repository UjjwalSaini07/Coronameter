from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sys
import mysql.connector
import random
#initializing the color code for bright theme here.
bright_background = "#F8EFBA"
bright_mainheading = "#6D214F"
bright_subheading = "black"
#file-handling here.
themefile = open('savedtheme.txt')
readvalue = themefile.read()
if readvalue == "DarkThemeTRUE" or readvalue == "DarkTheme":
    # storing the color code for dark theme here.
    bright_background = "#30336b"
    bright_mainheading = "yellow"
    bright_subheading = "cyan"
    dark_entry_back = 'white'
    dark_entry_fore = 'black'
elif readvalue == "BrightThemeTRUE" or readvalue == "BrightTheme":
    #storing the color code for bright theme here.
    bright_background = "#F8EFBA"
    bright_mainheading = "#6D214F"
    bright_subheading = "black"
    dark_entry_back = 'white'
    dark_entry_fore = 'black'
elif readvalue == "BrightThemeFALSE":
    themefile = open("savedtheme.txt", "w")
    themefile.write("BrightThemeTRUE")
    themefile.close()
elif readvalue == "DarkThemeFALSE":
    themefile = open("savedtheme.txt", "w")
    themefile.write("BrightThemeTRUE")
    themefile.close()
else:
    pass
#creating the database func here
global mydb, mycursor
mydb = mysql.connector.connect(host="localhost", user='root', password="ujjwal2003", database="Coronameter")
def adddata(nameval, ageval, phoneval, mailval, passwordval, quesval, ansval, idvalue):
    mycursor = mydb.cursor()
    query = "insert into USERS(UserName, UserAge, UserPhone, UserMail, UserPassword, UserQuestion, UserAnswer, Id) values ('{}',{},{},'{}','{}','{}','{}', {})".format(nameval, ageval, phoneval, mailval, passwordval, quesval, ansval, idvalue)
    mycursor.execute(query)
    mydb.commit()
#creating the func.
def backprocess():
    second.destroy()
    os.system(("%s %s") % (py, "StartPageCV.py"))
def process():
    global nameget, ageget, phoneget, mailget, confirmpassget, squesget, sansget, idvalue
    # fetching the values
    nameget = namevar.get().lower()
    ageget = agevar.get()
    phoneget = phonevar.get()
    mailget = mailvar.get()
    confirmpassget = confirmpassvar.get()
    createpassget = createpassvar.get()
    squesget = squesvar.get()
    sansget = sansvar.get()
    # logic for Id...
    id_value = random.randint(1, 300)
    list1 = [nameget, ageget, phoneget, mailget, createpassget, confirmpassget,squesget,sansget]
    for data in list1:
        print(f"Data is here = {data}")
    # checking the values when all are submitted
    if nameget and ageget and phoneget and mailget and createpassget and confirmpassget and sansget:
        if createpassget == confirmpassget:
            if squesget != "Your Question":
                if len(phoneget) == 10:
                    if ageget.isdigit() == True:
                        mycursor = mydb.cursor()
                        query = "SELECT Id FROM USERS WHERE UserMail = ('{}')".format(mailget)
                        mycursor.execute(query)
                        idget = mycursor.fetchone()
                        if idget:
                            messagebox.showerror("E-Mail Exists !", "You Are Already Registered, Try Login !")
                            print("user redirected.")
                            second.destroy()
                            os.system(("%s %s") % (py, "sign_in_window.py"))
                        else:
                            # from here the data is added to the database
                            adddata(nameget, ageget, phoneget, mailget, confirmpassget, squesget, sansget, id_value)
                            print("data addded successfully :)")
                            second.destroy()
                            print("window destroyed")
                            os.system(("%s %s") % (py, "sign_in_window.py"))
                    else:
                        messagebox.showerror("Invalid Age Detected", "Your Age Is Invalid !")
                else:
                    messagebox.showerror("Invalid Phone Detected", "Your Phone Number Is Invalid !")
            else:
                messagebox.showerror("Question Error", "Please Select Your Question !")
        else:
            messagebox.showerror("Password Verification Failed", "Please Confirm Your Password !")
    #checking the values as they are null or not separately
    else:
        if list1[0]:
            pass
            if list1[1]:
                pass
                if list1[2]:
                    pass
                    if list1[3]:
                        pass
                        if list1[4]:
                            pass
                            if list1[5]:
                                pass
                                if list1[7]:
                                    pass
                                #exception handling done...
                                else:
                                    messagebox.showwarning("Answer Error", "Please Fill Your Answer !")
                            else:
                                messagebox.showwarning("Password Error", "Please Confirm Your Password !")
                        else:
                            messagebox.showwarning("Password Error", "Please Create Your Password !")
                    else:
                        messagebox.showwarning("Mail Error", "Please Fill Your Mail-ID !")
                else:
                    messagebox.showwarning("Phone Error", "Please Fill Your Phone Number !")
            else:
                messagebox.showwarning("Age Error", "Please Fill Your Age !")
        else:
            messagebox.showwarning("Name Error", "Please Fill Your Name !")
py = sys.executable
#creating the window...
second = Tk()
second.state("zoomed")
second.title("Create Account")
second.iconbitmap("iconfile.ico")
second.configure(bg = bright_background)
#creating the widgets...
headtext = "Create Your Account"
headlbl = Label(second, bg = bright_background, fg = bright_mainheading, font = "Jokerman 80 bold", text = headtext)
headlbl.pack(side = TOP, anchor = CENTER, padx = 5, pady = 5)
secframe = Frame(second, bg = bright_background, border = 0, relief = SOLID)
secframe.pack(side = TOP, anchor = CENTER, padx = 600, pady = 10, fill = X)
nameimg = PhotoImage(file = "user.png")
ageimg = PhotoImage(file = "age(2).png")
phoneimg = PhotoImage(file = "telephone(1).png")
mailimg = PhotoImage(file = "email.png")
createpassimg = PhotoImage(file = "lock.png")
confirmpassimg = PhotoImage(file = "ui.png")
squesimg = PhotoImage(file = "first2.png")
sansimg = PhotoImage(file = "first2.png")
namephoto = Label(secframe, bg = bright_background, image = nameimg, border = 0, relief = FLAT)
agephoto = Label(secframe, bg = bright_background, image = ageimg, border = 0, relief = FLAT)
phonephoto = Label(secframe, bg = bright_background, image = phoneimg, border = 0, relief = FLAT)
mailphoto = Label(secframe, bg = bright_background, image = mailimg, border = 0, relief = FLAT)
createpassphoto = Label(secframe, bg = bright_background, image = createpassimg, border = 0, relief = FLAT)
confirmpassphoto = Label(secframe, bg = bright_background, image = confirmpassimg, border = 0, relief = FLAT)
squesphoto = Label(secframe, bg = bright_background, image = squesimg, border = 0, relief = FLAT)
sansphoto = Label(secframe, bg = bright_background, image = sansimg, border = 0, relief = FLAT)
namephoto.image = nameimg
agephoto.image = ageimg
phonephoto.image = phoneimg
mailphoto.image = mailimg
createpassphoto.image = createpassimg
confirmpassphoto.image = confirmpassimg
squesphoto.image = squesimg
sansphoto.image = sansimg
#creating the labels...
namelbl = Label(secframe, bg = bright_background, fg = bright_subheading, font = "Times 30 bold italic", text = "Enter Name")
agelbl = Label(secframe, bg = bright_background, fg = bright_subheading, font = "Times 30 bold italic", text = "Enter Age")
phonelbl = Label(secframe, bg = bright_background, fg = bright_subheading, font = "Times 30 bold italic", text = "Enter Phone")
maillbl = Label(secframe, bg = bright_background, fg = bright_subheading, font = "Times 30 bold italic", text = "Enter E-Mail")
createpasslbl = Label(secframe, bg = bright_background, fg = bright_subheading, font = "Times 30 bold italic", text = "Create Password")
confirmpasslbl = Label(secframe, bg = bright_background, fg = bright_subheading, font = "Times 30 bold italic", text = "Confirm Password")
squeslbl = Label(secframe, bg = bright_background, fg = bright_subheading, font = "Times 30 bold italic", text = "Security Question")
sanslbl = Label(secframe, bg = bright_background, fg = bright_subheading, font = "Times 30 bold italic", text = "Security Answer")
#packing the widgets...
namephoto.grid(row = 0, column = 0, sticky = 'w', padx= 5, pady= 5)
agephoto.grid(row = 1, column = 0, sticky = 'w', padx= 5, pady= 5)
phonephoto.grid(row = 2, column = 0, sticky = 'w', padx= 5, pady= 5)
mailphoto.grid(row = 3, column = 0, sticky = 'w', padx= 5, pady= 5)
createpassphoto.grid(row = 4, column = 0, sticky = 'w', padx= 5, pady= 5)
confirmpassphoto.grid(row = 5, column = 0, sticky = 'w', padx= 5, pady= 5)
squesphoto.grid(row = 6, column = 0, sticky = 'w', padx= 5, pady= 5)
sansphoto.grid(row = 7, column = 0, sticky = 'w', padx= 5, pady= 5)
namelbl.grid(row = 0, column = 1, sticky = 'w', padx= 5, pady= 5)
agelbl.grid(row = 1, column = 1, sticky = 'w', padx= 5, pady= 5)
phonelbl.grid(row = 2, column = 1, sticky = 'w', padx= 5, pady= 5)
maillbl.grid(row = 3, column = 1, sticky = 'w', padx= 5, pady= 5)
createpasslbl.grid(row = 4, column = 1, sticky = 'w', padx= 5, pady= 5)
confirmpasslbl.grid(row = 5, column = 1, sticky = 'w', padx= 5, pady= 5)
squeslbl.grid(row = 6, column = 1, sticky = 'w', padx= 5, pady= 5)
sanslbl.grid(row = 7, column = 1, sticky = 'w', padx= 5, pady= 5)
#creating the entry boxes...
namevar = StringVar()
agevar = StringVar()
phonevar = StringVar()
mailvar = StringVar()
createpassvar = StringVar()
confirmpassvar = StringVar()
squesvar = StringVar()
sansvar = StringVar()
queslist = ["What is Your Father Name ?", "What is Your Pet Name ?", "What is Your Home Name ?", "Where Is Your MotherLand ?"]
nameentry = Entry(secframe, bg = dark_entry_back, fg = dark_entry_fore, font = "Times 20 bold", width = 20, textvariable = namevar)
ageentry = Entry(secframe, bg = dark_entry_back, fg = dark_entry_fore, font = "Times 20 bold", width = 20, textvariable = agevar)
phoneentry = Entry(secframe, bg = dark_entry_back, fg = dark_entry_fore, font = "Times 20 bold", width = 20, textvariable = phonevar)
mailentry = Entry(secframe, bg = dark_entry_back, fg = dark_entry_fore, font = "Times 20 bold", width = 20, textvariable = mailvar)
createpassentry = Entry(secframe, bg = dark_entry_back, fg = dark_entry_fore, font = "Times 20 bold", width = 20, textvariable = createpassvar)
confirmpassentry = Entry(secframe, bg = dark_entry_back, fg = dark_entry_fore, font = "Times 20 bold", width = 20, textvariable = confirmpassvar)
squesentry = ttk.Combobox(secframe, font = "Times 16 bold", width = 25, textvariable = squesvar, state = "readonly")
squesentry["values"] = queslist
squesentry.set("Your Question")
sansentry = Entry(secframe, bg = "white", fg = "black", font = "Times 20 bold", width = 20, textvariable = sansvar)
nameentry.focus()
#packing the entry widgets...
nameentry.grid(row =0 , column = 2, sticky = 'w', padx = 5, pady = 5)
ageentry.grid(row = 1, column = 2, sticky = 'w', padx = 5, pady = 5)
phoneentry.grid(row =2 , column = 2, sticky = 'w', padx = 5, pady = 5)
mailentry.grid(row = 3, column = 2, sticky = 'w', padx = 5, pady = 5)
createpassentry.grid(row =4 , column =2 , sticky = 'w', padx = 5, pady = 5)
confirmpassentry.grid(row =5 , column = 2, sticky = 'w', padx = 5, pady = 5)
squesentry.grid(row = 6, column = 2, sticky = 'w', padx = 5, pady = 5)
sansentry.grid(row =7 , column = 2, sticky = 'w', padx = 5, pady = 5)
#creating the buttons...
submitimg = PhotoImage(file = "tick(1).png")
submitbtn = Button(second, bg = bright_background, image = submitimg, border = 0, relief = FLAT, fg = bright_background, command = process)
submitbtn.image = submitimg
submitbtn.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
backbtn = Button(second, bg = bright_background, fg = bright_subheading, font = "Comicsansms 20 bold underline", command = backprocess, text = "Back To HomePage", relief = FLAT)
backbtn.pack(side = BOTTOM, padx = 5, pady = 5, anchor = CENTER)
second.mainloop()
