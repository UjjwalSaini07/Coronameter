# this is the first window of my application
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import time
import sys
py = sys.executable
#storing the color code for bright theme here.
bright_background = "#F8EFBA"
bright_mainheading = "#6D214F"
bright_subheading = "#182C61"
bright_bottom = "darkblue"
bright_hover = "#ffda79"
bright_background = "#F8EFBA"
bright_hoverfg = "black"
#file-handling here.
themefile = open('savedtheme.txt')
readvalue = themefile.read()
if readvalue == "DarkThemeTRUE" or readvalue == "DarkTheme":
    # storing the color code for dark theme here.
    bright_background = "#30336b"
    bright_mainheading = "yellow"
    bright_subheading = "cyan"
    bright_bottom = "white"
    bright_hover = "yellow"
    bright_hoverfg = "black"
elif readvalue == "BrightThemeTRUE" or readvalue == "BrightTheme":
    #storing the color code for bright theme here.
    bright_background = "#F8EFBA"
    bright_mainheading = "#6D214F"
    bright_subheading = "#182C61"
    bright_bottom = "darkblue"
    bright_hover = "#ffda79"
    bright_hoverfg = "black"
elif readvalue == "BrightThemeFALSE":
    themefile = open("savedtheme.txt", "w")
    themefile.write("BrightThemeTRUE")
    themefile.close()
elif readvalue == "DarkThemeFALSE":
    bright_background = "#30336b"
    bright_mainheading = "yellow"
    bright_subheading = "cyan"
    bright_bottom = "white"
    bright_hover = "yellow"
    bright_hoverfg = "black"
    themefile = open("savedtheme.txt", "w")
    themefile.write("BrightThemeTRUE")
    themefile.close()
else:
    pass
#creating the functions...
def hoveron1(event):
    createbtn.config(bg = bright_hover, relief = SOLID, border = 2)
def hoveron2(event):
    loginbtn.config(bg = bright_hover, relief = SOLID, border = 2)
def hoveron4(event):
    setting.config(bg = bright_hover, relief = SOLID, border = 2, fg = bright_hoverfg)
def hoveroff1(event):
    createbtn.config(bg = bright_background, relief = FLAT, border = 0)
def hoveroff2(event):
    loginbtn.config(bg = bright_background, relief = FLAT, border = 0)
def hoveroff4(event):
    setting.config(bg = bright_background, relief = FLAT, border = 0, fg = bright_subheading)
def hoveron3(event):
    closebtn.config(bg = "red", relief = SOLID, border = 5)
def hoveroff3(event):
    closebtn.config(bg = bright_background, relief = FLAT, border = 0)
def createprocess(event):
    #redirected...
    first.destroy()
    os.system("%s %s" % (py, "sign_up_window.py"))
def loginprocess(event):
    # redirected...
    first.destroy()
    os.system("%s %s" % (py, "sign_in_window.py"))
def closeprocess(event):
    response = messagebox.askyesnocancel('Exit CoronaMeter Pro', "Are You Sure To Exit The Application ?")
    if response == True:
        messagebox.showinfo("GoodBye", "Thank You For Using :)")
        first.destroy()
    else:
        pass
#creating the setting window here.
def click4(event):
    #creating the theme apply function here.
    def applytheme():
        theme_get = themevalue.get()
        print(theme_get)
        default_get = defaultvalue.get()
        print(default_get)
        if theme_get:
            themefile = open('savedtheme.txt', 'w')
            themefile.writelines(theme_get)
            if default_get:
                savetheme = 'TRUE'
                themefile.writelines(savetheme)
                themefile.close()
                statusvar.set(f"Theme Status : Applying {theme_get}, please wait...")
                statusbar.update()
                time.sleep(2)
                statusvar.set(f"Theme Status : {theme_get} Applied, Please Wait...")
                statusbar.update()
                time.sleep(2)
                statusvar.set("Theme Status : Done, Restart Required...")
                doneimage.config(state="disabled")
            else:
                savetheme = "FALSE"
                themefile.writelines(savetheme)
                themefile.close()
                statusvar.set("Theme Status : Applying Settings...")
                statusbar.update()
                time.sleep(2)
                statusvar.set(f"Theme Status : {theme_get} Applied, Please Wait...")
                statusbar.update()
                time.sleep(2)
                statusvar.set("Theme Status : Done, Restart Required...")
                doneimage.config(state="disabled")
        else:
            messagebox.showerror("Theme Not Selected Error", "Please Select One Theme To Apply !")
    # creating the small window here for the theme here.
    window = Toplevel(first)
    window.title("Theme Customization Window")
    window.configure(bg=bright_background)
    window.geometry("500x500+400+100")
    window.grab_set()
    window.iconbitmap("iconfile.ico")
    window.resizable(False, False)
    #creating the variables here.
    statusvar = StringVar(window)
    themevalue = StringVar(window)
    defaultvalue = IntVar(window, "1")
    statusvar.set("Theme Status : No Theme Selected Yet")
    #creating the labels and button here.
    list_of_themes = ['Dark Mode   (New)', "Bright Mode (New)", 'Select Theme', "Save Selected Theme As My Default Theme ?"]
    if readvalue == 'DarkTheme' or readvalue == 'DarkThemeTRUE' or readvalue == 'DarkThemeFALSE':
        bright_hoverfg = bright_hover
    else:
        bright_hoverfg = "black"
    theme = Label(window, bg = bright_background, fg = bright_subheading, text = list_of_themes[2],
                  font = "Algerian 40 bold underline")
    theme1 = Radiobutton(window, bg = bright_background, fg = bright_hoverfg, variable = themevalue,value = "DarkTheme",
                         text = list_of_themes[0], font = "Times 20 bold italic")
    theme2= Radiobutton(window, bg = bright_background, fg = bright_hoverfg, variable = themevalue,value = "BrightTheme",
                        text = list_of_themes[1], font = "Times 20 bold italic")
    doneimg = PhotoImage(file = "tick(1).png")
    doneimage = Button(window, bg = bright_background, fg = bright_background, image = doneimg, border = 0,
                       relief = FLAT, command = applytheme)
    statusbar = Label(window, bg = bright_background, fg = bright_hoverfg, textvariable = statusvar,
                      font = 'Times 15 bold italic')
    default = Checkbutton(window, bg = bright_background, fg = bright_subheading, variable = defaultvalue,
                          font = "Times 18 bold italic", text = list_of_themes[3])
    theme.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
    theme1.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
    theme2.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
    default.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
    doneimage.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
    statusbar.pack(side = BOTTOM, padx = 5, pady =5, anchor = CENTER)
    window.mainloop()
#creating the window...
first = Tk()
first.title("CoronaMeter Pro v2.o")
first.configure(bg = bright_background)
first.iconbitmap("iconfile.ico")
first.state("zoomed")
#creating the widgets...
headtext = "Welcome To CoronaMeter"
createtext = "Create Account"
logintext = "Login Account"
headlbl = Label(first, bg = bright_background, fg = bright_mainheading, font = "Jokerman 80 bold", text = headtext)
createlbl = Label(first, bg = bright_background, fg = bright_subheading, font = "Times 60 bold", text = createtext)
loginlbl = Label(first, bg = bright_background, fg = bright_subheading, font = "Times 60 bold", text = logintext)
createimg = PhotoImage(file = "login(1).png")
loginimg = PhotoImage(file = "login.png")
closeimg = PhotoImage(file = "close.png")
createbtn = Button(first, bg = bright_background, image = createimg, border = 0, relief = FLAT)
loginbtn = Button(first, bg = bright_background, image = loginimg, border = 0, relief = FLAT)
closebtn = Button(first, bg = bright_background, image = closeimg, border = 0, relief = FLAT)
createbtn.image = createimg
loginbtn.image = loginimg
closeimg.image = closebtn
#packing the widgets...
headlbl.pack(side = TOP, padx = 5, pady = 10, fill = X)
createlbl.pack(side = TOP, padx = 5, pady = 10, fill = X)
createbtn.pack(side = TOP, padx = 5, pady = 10)
loginlbl.pack(side = TOP, padx = 5, pady = 5, fill = X)
loginbtn.pack(side = TOP, padx = 5, pady = 5)
closebtn.pack(side = BOTTOM, padx = 5, pady = 5)
#binding the buttons...
createbtn.bind("<Enter>", hoveron1)
loginbtn.bind("<Enter>", hoveron2)
createbtn.bind("<Leave>", hoveroff1)
loginbtn.bind("<Leave>", hoveroff2)
closebtn.bind("<Enter>", hoveron3)
closebtn.bind("<Leave>", hoveroff3)
createbtn.bind("<Button-1>", createprocess)
loginbtn.bind("<Button-1>", loginprocess)
closebtn.bind("<Button-1>", closeprocess)
#creating productive labels...
text1 = "CoronaMeter v2.0 Pro"
text2 = "Created & Managed By : ABHIJIT MANDAL"
text3 = "© 2020-2021 All Rights Reserved"
text4 = "Powered By : Python"
text5 = "Theme Settings"
l1 = Label(first, bg = bright_background, fg = bright_bottom, font = "Times 30 bold italic", text = text1)
l2 = Label(first, bg = bright_background, fg = bright_bottom, font = "Times 20 bold italic", text = text2)
l3 = Label(first, bg = bright_background, fg = bright_bottom, font = "Times 20 bold italic", text = text4)
l4 = Label(first, bg = bright_background, fg = bright_bottom, font = "Times 20 bold italic", text = text3)
mylist = [l4, l3, l2, l1]
for i in mylist:
    i.pack(side = BOTTOM, padx = 5, pady = 3, anchor = CENTER)
setting = Button(first, bg = bright_background, fg = bright_subheading, text = text5,
                 font = "Times 30 bold italic underline", border = 3, relief = FLAT)
setting.pack(side = BOTTOM, padx = 0, pady = 3, anchor = CENTER)
setting.bind('<Enter>', hoveron4)
setting.bind('<Leave>', hoveroff4)
setting.bind('<Button-1>', click4)
first.mainloop()
