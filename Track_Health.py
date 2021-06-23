# importing the libs here
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sys
py = sys.executable
#creating the button action function here.
def testing_start():
    print("testing start.")
def closeapp():
    verify = messagebox.askyesnocancel("EXIT CoronaMeter", "Are You Sure To EXIT ?")
    print(verify)
    if verify == True:
        messagebox.showinfo("GoodBye User", "Come Again :)")
        window.destroy()
    elif verify == False:
        pass
    else:
        pass
#creating the hover effect function here.
def hoveron1(event):
    doctor_image_label.configure(bg = "#fff200", border = 5)
def hoveroff1(event):
    doctor_image_label.configure(bg = "#ffeaa7", border = 3)
#creating the window screen here.
window = Tk()
window.title("Covid-19 Health Tracker")
window.iconbitmap('iconfile.ico')
window.attributes("-fullscreen", True)
window.configure(bg = "#ffeaa7")
#creating the frame here.
window_frame1 = Frame(window, bg = "#ffeaa7", border = 0, borderwidth = 0, relief = FLAT)
window_frame1.pack(side = TOP, anchor = CENTER, padx = 300, pady = 10, fill = X)
#creating the labels text here.
label_text1 = "CoronaMeter"
label_text2 = "The Best Offline Covid-19 Risk Detector"
label_text3 = "Just Answer Some Simple Questions And Get Assured Of Your Health"
label_text4 = "Take A Quick Test Now"
#creating the text label here.
heading_label = Label(window_frame1, bg = "#ffeaa7", fg = "#273c75", font = "Jokerman 60 bold", text = label_text1)
subhead_label = Label(window, bg = "#ffeaa7", fg = "#e74c3c", font = "Times 40 bold italic", text = label_text2)
#creating the image here.
virusimg = PhotoImage(file = "virus.png")
#creating the photo labels here.
virusimg_label = Label(window_frame1, bg = "#ffeaa7", border = 0, relief = FLAT, image = virusimg)
virusimg_label.grid(row = 0, column = 0, padx = 5, pady = 3)
heading_label.grid(row = 0, column = 1, padx = 5, pady = 3)
subhead_label.pack(side = TOP, padx = 5, pady  = 0, anchor = CENTER, fill = X)
#creating more mid labels here.
label_1 = Label(window, bg = "#ffeaa7", fg = "#273c75", font = "Times 30 bold", text = label_text3)
label_2 = Label(window, bg = "#ffeaa7", fg = "#273c75", font = "Times 35 bold italic", text = label_text4)
#packing the system.
label_1.pack(side = TOP, padx = 5, pady = 20, anchor = CENTER)
label_2.pack(side = TOP, padx = 5, pady = 20, anchor = CENTER)
#creating the photo here.
doctor_image = PhotoImage(file = "doctor.png")
doctor_image_label = Button(window, bg = "#ffeaa7", border = 3, relief = SOLID, image = doctor_image, activebackground = "lightgreen", command = testing_start)
doctor_image_label.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
closeimg = PhotoImage(file = "close.png")
closeimg_label = Button(window, bg = "#ffeaa7", image = closeimg, relief = FLAT, border = 0, activebackground = "red", command = closeapp)
closeimg_label.pack(side = BOTTOM, padx = 5, pady = 10, anchor = CENTER)
#creating the slider here.
def slider():
    global count, text
    if count >=len(slider_text):
        count = -1
        text = ''
        slider_label.configure(text = text)
    else:
        text  = text + slider_text[count]
        slider_label.configure(text = text)
    count += 1
    slider_label.after(300, slider)
slider_text = "Developed By Abhijit Mandal"
inspire_text = "Inspired By Arogya Setu"
count = 0
text = ''
inspire_label = Label(window, text = inspire_text, bg = "#ffeaa7", fg = "black", font = "Times 25 bold italic")
inspire_label.pack(side = BOTTOM, padx = 5, pady = 10, anchor = CENTER)
slider_label = Label(window, text = slider_text, bg = "#ffeaa7", fg = "black", font = "Times 30 bold italic")
slider_label.pack(side = BOTTOM, padx = 5, pady = 10, anchor = CENTER)
slider()
#creating the hover effect here.
doctor_image_label.bind("<Enter>", hoveron1)
doctor_image_label.bind("<Leave>", hoveroff1)
window.mainloop()
