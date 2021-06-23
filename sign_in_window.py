# login program for the user is completed
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sys
import mysql.connector
#init the color code for bright theme here.
bright_background = "#F8EFBA"
bright_mainheading = "#6D214F"
bright_subheading = 'black'
bright_entryfg = 'darkblue'
#file-handling here.
themefile = open('savedtheme.txt')
readvalue = themefile.read()
if readvalue == "DarkThemeTRUE" or readvalue == "DarkTheme":
    # storing the color code for dark theme here.
    bright_background = "#30336b"
    bright_mainheading = "yellow"
    bright_subheading = "cyan"
    bright_mainheading1 = 'yellow'
elif readvalue == "BrightThemeTRUE" or readvalue == "BrightTheme":
    #storing the color code for bright theme here.
    bright_background = "#F8EFBA"
    bright_mainheading = "#6D214F"
    bright_subheading = 'black'
    bright_entryfg = 'darkblue'
    bright_mainheading1 = bright_subheading
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
#creating the func.
#creating the database here
global mydb, mycursor
mydb = mysql.connector.connect(host="localhost", user='root', password="ujjwal2003", database="Coronameter")
def backprocess():
    third.destroy()
    os.system(("%s %s") % (py, "StartPageCV.py"))
def forgotprocess():
    mailget = mailvar1.get()
    squesget = selectvar.get()
    sansget = answervar.get()
    print(f"forgotdata is here = {squesget}")
    print(f"forgotdata is here = {sansget}")
    if squesget and sansget:
        mycursor = mydb.cursor()
        query = "select Id from users where UserMail = ('{}')".format(mailget)
        mycursor.execute(query)
        idget = mycursor.fetchone()
        print(idget)
        if idget:
            mycursor.execute("select UserQuestion, UserAnswer from USERS where Id = {}".format(idget[0]))
            datatuple = mycursor.fetchone()
            print(datatuple)
            ques = datatuple[0]
            ans = datatuple[1]
            if ques == squesget:
                print('ques verified.')
                if ans == sansget:
                    print('answer verified.')
                    third.destroy()
                    os.system(("%s %s") % (py, "Track_Data.py"))
                else:
                    messagebox.showwarning("Wrong Answer Detected", "Please Answer Correctly !")
            else:
                messagebox.showwarning("Invaid Question Selected !", "Please Select That Question, Which You Have Selected\nWhile Creating New Account !")
        else:
            messagebox.showerror("User Not Found :(", "Please Check Your E-Mail ID!")
    else:
        if squesget:
            if squesget != "Verify Yourself":
                pass
                if sansget:
                    pass
                else:
                    messagebox.showerror("Answer Error", "Please Fill Your Answer !")
            else:
                messagebox.showerror("Question Error", "Please Select Your Question !")
        else:
            pass
def submitprocess():
    #fetching the values
    mailget = mailvar1.get()
    passwordget = confirmpassvar1.get()
    list2 = [mailget, passwordget]
    for data in list2:
        print(f"data is here = {data}")
    if mailget and passwordget:
        print("all data inserted successfully")
        mycursor = mydb.cursor()
        query = "select Id from users where UserMail = ('{}')".format(mailget)
        mycursor.execute(query)
        idget = mycursor.fetchone()
        if idget:
            query = "select UserPassword from USERS where UserMail = ('{}')".format(mailget)
            mycursor.execute(query)
            passget = mycursor.fetchone()
            if passget[0] == passwordget:
                messagebox.showinfo("Login Successful :)", "Click OK And Go Ahead :)")
                third.destroy()
                os.system(("%s %s") % (py, "Track_Data.py"))
            else:
                messagebox.showinfo("Login Failed :(", "Your Password Is Incorrect !")
        else:
            messagebox.showwarning("User Not Found :(", "Please Check Your E-Mail ID !")
    else:
        if mailget:
            pass
            if passwordget:
                pass
            else:
                messagebox.showerror("Password Error", "Please Fill Your Password !")
        else:
            messagebox.showerror("Mail Error", "Please Fill Your Mail-ID !")
py = sys.executable
#creating the window...
third = Tk()
third.state("zoomed")
third.title("Login Account")
third.iconbitmap("iconfile.ico")
third.configure(bg = bright_background)
#creating the widgets...
headtext = "Login Your Account"
headlbl = Label(third, bg = bright_background, fg = bright_mainheading, font = "Jokerman 50 bold", text = headtext)
headlbl.pack(side = TOP, anchor = CENTER, padx = 5, pady = 5)
thirdframe = Frame(third, bg = bright_background, border = 0, relief = SOLID)
thirdframe.pack(side = TOP, anchor = CENTER, padx = 600, pady = 10, fill = X)
#creating the labels and images...
mailimg = PhotoImage(file = "email.png")
confirmpassimg = PhotoImage(file = "ui.png")
mailphoto = Label(thirdframe, bg = bright_background, image = mailimg, border = 0, relief = FLAT)
confirmpassphoto = Label(thirdframe, bg = bright_background, image = confirmpassimg, border = 0, relief = FLAT)
mailphoto.image = mailimg
confirmpassphoto.image = mailimg
maillbl = Label(thirdframe, bg = bright_background, fg = bright_subheading, font = "Times 15 bold italic", text = "Enter E-Mail")
confirmpasslbl = Label(thirdframe, bg = bright_background, fg = bright_subheading, font = "Times 13 bold italic", text = "Enter Password")
mailvar1 = StringVar()
confirmpassvar1 = StringVar()
mailentry = Entry(thirdframe, bg = "white", fg = bright_entryfg, font = "Times 20 bold", width = 20, textvariable = mailvar1)
mailentry.focus()
confirmpassentry = Entry(thirdframe, bg = "white", fg = bright_entryfg, font = "Times 20 bold", width = 20, textvariable = confirmpassvar1)
#packing the system...
mailphoto.grid(row = 0, column = 0, sticky = 'w', padx = 5, pady = 5)
confirmpassphoto.grid(row = 1, column = 0, sticky = 'w', padx = 5, pady = 5)
maillbl.grid(row = 0, column = 1, sticky = 'w', padx = 5, pady = 5)
confirmpasslbl.grid(row = 1, column = 1, sticky = 'w', padx = 5, pady = 5)
mailentry.grid(row = 0, column = 2, sticky = 'w', padx = 5, pady = 5)
confirmpassentry.grid(row = 1, column = 2, sticky = 'w', padx = 5, pady = 5)
#creating the buttons...
submitimg = PhotoImage(file = "tick(1).png")
submitbtn = Button(third, bg = bright_background, image = submitimg, border = 0, relief = FLAT, fg = bright_background, command = submitprocess)
submitbtn.image = submitimg
submitbtn.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
#for the case of forgot the password...
forgottext = "Forgot Password ? Don't Worry !"
questext = "Select Question"
anstext = "Give Answer"
squesimg = PhotoImage(file = "first2.png")
sansimg = PhotoImage(file = "first2.png")
thirdframe1 = Frame(third, bg = bright_background, border = 0, relief = SOLID)
squesphoto = Label(thirdframe1, bg = bright_background, image = squesimg, border = 0, relief = FLAT)
sansphoto = Label(thirdframe1, bg = bright_background, image = sansimg, border = 0, relief = FLAT)
squesphoto.image = squesimg
sansphoto.image = sansimg
selectvar = StringVar()
answervar = StringVar()
selectlist = ["What is Your Father Name ?", "What is Your Pet Name ?", "What is Your Home Name ?", "Where Is Your MotherLand ?"]
selectentry = ttk.Combobox(thirdframe1, font = "Times 20 bold italic", textvariable = selectvar, state = "readonly")
selectentry.set("Verify Yourself")
selectentry["values"] = selectlist
forgotlbl = Label(third, bg = bright_background, text = forgottext, font = "Times 25 bold", fg = bright_mainheading1)
givelbl = Label(thirdframe1, bg = bright_background, text = anstext, font = "Times 16 bold italic", fg = bright_subheading)
selectlbl = Label(thirdframe1, bg = bright_background, fg = bright_subheading, font = "Times 13 bold italic", text = questext)
giveentry = Entry(thirdframe1, bg = "white", font = "Times 20 bold", width = 22, textvariable = answervar, fg = bright_entryfg)
#packing the system...
forgotlbl.pack(side = TOP, anchor = CENTER, padx = 5, pady = 10)
thirdframe1.pack(side = TOP, anchor = CENTER, padx = 600, pady = 10, fill = X)
squesphoto.grid(row = 0, column = 0, sticky = 'w', padx = 5, pady = 5)
sansphoto.grid(row = 1, column = 0, sticky = 'w', padx = 5, pady = 5)
selectlbl.grid(row = 0, column = 1, sticky = 'w', padx = 5, pady = 5)
selectentry.grid(row = 0, column = 2, sticky = 'w', padx = 5, pady = 5)
givelbl.grid(row = 1, column = 1, sticky = 'w', padx = 5, pady = 5)
giveentry.grid(row = 1, column = 2, sticky = 'w', padx = 5, pady = 5)
#creating forgot submit button...
forgotimg = PhotoImage(file = "tick(1).png")
forgotbtn = Button(third, bg = bright_background, image = forgotimg, border = 0, relief = FLAT, fg = bright_background, command = forgotprocess)
forgotbtn.image = forgotimg
forgotbtn.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
backbtn = Button(third, bg = bright_background, fg = bright_subheading, font = "Comicsansms 20 bold underline", command = backprocess, text = "Back To HomePage", relief = FLAT)
backbtn.pack(side = BOTTOM, padx = 5, pady = 5, anchor = CENTER)
third.mainloop()
