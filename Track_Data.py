from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import mysql.connector
import sys
py = sys.executable
#storing the color code for bright theme here.
bright_background = "#ffeaa7"
bright_mainheading = "#273c75"
bright_subheading = "#e74c3c"
bright_sublabels = "black"
bright_hoverbg = "#fbc531"
#file-handling here.
themefile = open('savedtheme.txt')
readvalue = themefile.read()
if readvalue == "DarkThemeTRUE" or readvalue == "DarkTheme":
    # storing the color code for dark theme here.
    bright_background = "#30336b"
    bright_mainheading = "yellow"
    bright_subheading = "cyan"
    bright_sublabels = bright_mainheading
    bright_hoverbg = bright_subheading
    bright_hoveroff = bright_background
elif readvalue == "BrightThemeTRUE" or readvalue == "BrightTheme":
    #storing the color code for bright theme here.
    bright_background = "#ffeaa7"
    bright_mainheading = "#273c75"
    bright_subheading = "#e74c3c"
    bright_sublabels = "black"
    bright_hoverbg = "#fbc531"
    bright_hoveroff = bright_background
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
#creating the button effects here.
def hover_on_effect1(event):
    first_button1.config(border = 5, relief = SOLID, bg = bright_hoverbg)
def hover_on_effect2(event):
    first_button2.config(border = 5, relief = SOLID, bg = bright_hoverbg)
def hover_on_effect3(event):
    second_button1.config(border = 5, relief = SOLID, bg = bright_hoverbg)
def hover_on_effect4(event):
    second_button2.config(border = 5, relief = SOLID, bg = bright_hoverbg)
def hover_on_effect5(event):
    third_button1.config(border = 5, relief = SOLID, bg = bright_hoverbg)
def hover_on_effect6(event):
    third_button2.config(border = 5, relief = SOLID, bg = bright_hoverbg)
#creating the hoveroff effect for the buttons here.
def hover_off_effect1(event):
    first_button1.config(border = 0, relief = FLAT, bg = bright_hoveroff)
def hover_off_effect2(event):
    first_button2.config(border = 0, relief = FLAT, bg = bright_hoveroff)
def hover_off_effect3(event):
    second_button1.config(border = 0, relief = FLAT, bg = bright_hoveroff)
def hover_off_effect4(event):
    second_button2.config(border = 0, relief = FLAT, bg = bright_hoveroff)
def hover_off_effect5(event):
    third_button1.config(border = 0, relief = FLAT, bg = bright_hoveroff)
def hover_off_effect6(event):
    third_button2.config(border = 0, relief = FLAT, bg = bright_hoveroff)
# creating the button click effect here.
def click_effect1(event):
    first_button1.config(border = 3, relief = FLAT, activebackground = bright_hoverbg)
    window.destroy()
    os.system("%s %s" % (py, "Track_Data_1.py"))
def click_effect2(event):
    first_button2.config(border = 3, relief = FLAT, activebackground = bright_hoverbg)
    window.destroy()
    os.system("%s %s" % (py, "Track_Data_2.py"))
def click_effect3(event):
    second_button1.config(border = 3, relief = FLAT, activebackground = bright_hoverbg)
    window.destroy()
    os.startfile('Countries.pdf')
def click_effect4(event):
    second_button2.config(border = 3, relief = FLAT, activebackground = bright_hoverbg)
    window.destroy()
    os.system("%s %s" % (py, "risk_detection.py"))
def click_effect5(event):
    third_button1.config(border = 3, relief = FLAT, activebackground = bright_hoverbg)
    window.destroy()
    os.system("%s %s" % (py, "Track_Data_5.py"))
def click_effect6(event):
    third_button2.config(border = 3, relief = FLAT, activebackground = bright_hoverbg)
    window.destroy()
    os.system("%s %s" % (py, "Track_Data_6.py"))
def close_app(event):
    verify = messagebox.askyesnocancel("EXIT CoronaMeter", "Are You Sure To EXIT ?")
    print(verify)
    if verify == True:
        messagebox.showinfo("GoodBye User", "Thanks For Using :)")
        window.destroy()
    elif verify == False:
        pass
    else:
        pass
# creating the main window here.
window = Tk()
window.title("Covid-19 RealTime Data Tracker")
window.iconbitmap('iconfile.ico')
window.attributes("-fullscreen", True)
window.configure(bg = bright_background)
#creating the frame here.
window_frame1 = Frame(window, bg = bright_background, border = 0, borderwidth = 0, relief = FLAT)
window_frame1.pack(side = TOP, anchor = CENTER, padx = 500, pady = 10, fill = X)
#creating the labels text here.
label_text1 = "CoronaMeter"
label_text2 = "The Most Accurate Covid-19 Realtime Data Tracker"
label_text3 = "Data By Country Name"
label_text4 = "Data By Country ID"
label_text5 = "View Available Countries"
label_text6 = "Health Test"
label_text7 = "Visualaize Data By Graphs"
label_text8 = "Get World Data"
#creating the text label here.
heading_label = Label(window_frame1, bg = bright_background, fg = bright_mainheading, font = "Jokerman 80 bold", text = label_text1)
subhead_label = Label(window, bg = bright_background, fg = bright_subheading, font = "Times 60 bold italic", text = label_text2)
#creating the image here.
closeimg = PhotoImage(file = "close.png")
virusimg = PhotoImage(file = "virus.png")
#creating the photo labels here.
virusimg_label = Label(window_frame1, bg = bright_background, border = 0, relief = FLAT, image = virusimg)
virusimg_label.grid(row = 0, column = 0, padx = 5, pady = 3)
heading_label.grid(row = 0, column = 1, padx = 5, pady = 3)
subhead_label.pack(side = TOP, padx = 5, pady  = 0, anchor = CENTER, fill = X)
#creating all the frames here.
first_frame = Frame(window, border = 0, relief = FLAT, bg = bright_background)
second_frame = Frame(window, border = 0, relief = FLAT, bg = bright_background)
third_frame = Frame(window, border = 0, relief = FLAT, bg = bright_background)
#creating the photo object for the images here.
first_photo1 = PhotoImage(file = "world.png")
first_photo2 = PhotoImage(file = "worldwide.png")
second_photo1 = PhotoImage(file = "flag-variant.png")
second_photo2 = PhotoImage(file = "recovered.png")
third_photo1 = PhotoImage(file = "graph.png")
third_photo2 = PhotoImage(file = "data-center.png")
#creating the buttons here.
first_button1 = Button(first_frame, bg = bright_background, font = "Times 30 bold italic", image = first_photo1, border = 0, borderwidth = 0, relief = SOLID)
first_button2 = Button(first_frame, bg = bright_background, font = "Times 30 bold italic", image = first_photo2, border = 0, borderwidth = 0, relief = SOLID)
second_button1 = Button(second_frame, bg = bright_background, font = "Times 30 bold italic", image = second_photo1, border = 0, borderwidth = 0, relief = SOLID)
second_button2 = Button(second_frame, bg = bright_background, font = "Times 30 bold italic", image = second_photo2, border = 0, borderwidth = 0, relief = SOLID)
third_button1 = Button(third_frame, bg = bright_background, font = "Times 30 bold italic", image = third_photo1, border = 0, borderwidth = 0, relief = SOLID)
third_button2 = Button(third_frame, bg = bright_background, font = "Times 30 bold italic", image = third_photo2, border = 0, borderwidth = 0, relief = SOLID)
#creating the new labels for the frame here.
first_label1 = Label(first_frame, bg = bright_background, fg = bright_sublabels, font = "Times 20 bold", text = label_text3)
first_label2 = Label(first_frame, bg = bright_background, fg = bright_sublabels, font = "Times 20 bold", text = label_text4)
first_frame.pack(side = TOP, padx = 0, pady = 0, anchor = CENTER)
second_frame.pack(side = TOP, padx = 0, pady = 0, anchor = CENTER)
second_label1 = Label(second_frame, bg = bright_background, fg = bright_sublabels, font = "Times 20 bold", text = label_text5)
second_label2 = Label(second_frame, bg = bright_background, fg = bright_sublabels, font = "Times 20 bold", text = label_text6)
third_frame.pack(side = TOP, padx = 0, pady = 0, anchor = CENTER)
third_label1 = Label(third_frame, bg = bright_background, fg = bright_sublabels, font = "Times 20 bold", text = label_text7)
third_label2 = Label(third_frame, bg = bright_background, fg = bright_sublabels, font = "Times 20 bold", text = label_text8)
#packing the entire system here.
first_button1.grid(row = 0, column = 0, sticky = 'w', padx = 200, pady = 0)
first_button2.grid(row = 0, column = 1, sticky = 'w', padx = 200, pady = 0)
first_label1.grid(row = 1, column = 0, padx = 0, pady = 0)
first_label2.grid(row = 1, column = 1, padx = 0, pady = 0)
second_button1.grid(row = 0, column = 0, sticky = 'w', padx = 200, pady = 0)
second_button2.grid(row = 0, column = 1, sticky = 'w', padx = 200, pady = 0)
second_label1.grid(row = 1, column = 0, padx = 0, pady = 0)
second_label2.grid(row = 1, column = 1, padx = 0, pady = 0)
third_button1.grid(row = 0, column = 0, sticky = 'w', padx = 200, pady = 0)
third_button2.grid(row = 0, column = 1, sticky = 'w', padx = 200, pady = 0)
third_label1.grid(row = 1, column = 0, padx = 0, pady = 0)
third_label2.grid(row = 1, column = 1, padx = 0, pady = 0)
# binding the btns for hover on effects
first_button1.bind("<Enter>", hover_on_effect1)
first_button2.bind("<Enter>", hover_on_effect2)
second_button1.bind("<Enter>", hover_on_effect3)
second_button2.bind("<Enter>", hover_on_effect4)
third_button1.bind("<Enter>", hover_on_effect5)
third_button2.bind("<Enter>", hover_on_effect6)
# binding the btns for hover off effects
first_button1.bind("<Leave>", hover_off_effect1)
first_button2.bind("<Leave>", hover_off_effect2)
second_button1.bind("<Leave>", hover_off_effect3)
second_button2.bind("<Leave>", hover_off_effect4)
third_button1.bind("<Leave>", hover_off_effect5)
third_button2.bind("<Leave>", hover_off_effect6)
# binding the btns for click effects.
first_button1.bind("<Button-1>", click_effect1)
first_button2.bind("<Button-1>", click_effect2)
second_button1.bind("<Button-1>", click_effect3)
second_button2.bind("<Button-1>", click_effect4)
third_button1.bind("<Button-1>", click_effect5)
third_button2.bind("<Button-1>", click_effect6)
#creating the close button here.
closeimg_label = Button(window, bg = bright_background, image = closeimg, relief = FLAT, border = 0, activebackground = "yellow")
closeimg_label.pack(side = BOTTOM, padx = 5, pady = 0, anchor = CENTER)
closeimg_label.bind("<Button-1>", close_app)
window.mainloop()
