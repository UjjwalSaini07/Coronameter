from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import threading
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
def redirect1():
    pass
    os.system("%s %s" % (py, "coviddoctor.py"))
def redirect2():
    os.system("%s %s" % (py, "ChatBot.py"))
def startdotor():
    newthread = threading.Thread(target = redirect1)
    newthread.start()
def startchatbuddy():
    newthread = threading.Thread(target = redirect2)
    newthread.start()
# creating the window here.
window = Tk()
window.grab_set()
window.title("Covid-19 RealTime Data Tracker")
window.iconbitmap('iconfile.ico')
window.state("zoomed")
window.configure(bg = bright_background)
#creating the frame here.
window_frame1 = Frame(window, bg = bright_background, border = 0, borderwidth = 0, relief = FLAT)
window_frame1.pack(side = TOP, anchor = CENTER, padx = 500, pady = 10, fill = X)
#creating the labels text here.
label_text1 = "CoronaMeter"
label_text2 = "The Most Accurate Covid-19 Realtime Data Tracker"
label_text3 = "Take A Quick Virtual Covid-19 Risk Test Now"
label_text4 = 'Just Answer Some Simple Questions And Get Assured Of Your Health'
label_text5 = 'Get Every Information Of CoronaMeter From Your Personal Assistant'
label_text6 = 'DocBuddy (Talk To Your Doctor Buddy) [New]'
label_text7 = 'ChatBuddy (Talk To Your AI Robot Buddy) [New]'
#creating the text label here.
heading_label = Label(window_frame1, bg = bright_background, fg = bright_mainheading, font = "Jokerman 22 bold", text = label_text1)
subhead_label = Label(window, bg = bright_background, fg = bright_subheading, font = "Times 40 bold italic", text = label_text2)
#creating the image here.
virusimg = PhotoImage(file = "virus.png")
#creating the photo labels here.
virusimg_label = Label(window_frame1, bg = bright_background, border = 0, relief = FLAT, image = virusimg)
virusimg_label.grid(row = 0, column = 0, padx = 5, pady = 3)
heading_label.grid(row = 0, column = 1, padx = 3, pady = 3)
subhead_label.pack(side = TOP, padx = 5, pady  = 0, anchor = CENTER, fill = X)
label1 = Label(window, text = label_text3, fg = 'black', bg = '#ffeaa7', font = 'times 30 bold italic')
label2 = Label(window, text = label_text4, fg = 'black', bg = '#ffeaa7', font = 'times 30 bold italic')
label3 = Label(window, text = label_text5, fg = 'black', bg = '#ffeaa7', font = 'times 30 bold italic')
label1.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER, fill = X)
label2.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER, fill = X)
label3.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER, fill = X)
#creating the frames here.
window_frame = Frame(window, bg = bright_background, border = 5, relief = SOLID)
window_frame.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER, fill = X)
#creating the images here.
doctorimg = PhotoImage(file = 'doctor.png')
robotimg = PhotoImage(file = 'robot.png')
doctorimage = Button(window_frame, image = doctorimg, border = 0, relief = FLAT, bg = bright_background, fg = bright_background, command = startdotor)
robotimage = Button(window_frame, image = robotimg, border = 0, relief = FLAT, bg = bright_background, fg = bright_background, command = startchatbuddy)
doctorimage.image = doctorimg
robotimage.image = robotimg
doctorimage.grid(row = 0, column = 0, sticky = 'w', padx = 20, pady = 8)
robotimage.grid(row = 1, column = 0, sticky = 'w', padx = 20, pady = 8)
label4 = Label(window_frame, text = label_text6, fg = bright_mainheading, bg = bright_background, font = 'times 20 bold italic')
label5 = Label(window_frame, text = label_text7, fg = bright_mainheading, bg = bright_background, font = 'times 30 bold italic')
label4.grid(row = 0, column = 1, sticky = 'w', padx = 20, pady = 8)
label5.grid(row = 1, column = 1, sticky = 'w', padx = 20, pady = 8)
window.mainloop()