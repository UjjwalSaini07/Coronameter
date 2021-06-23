from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import pygame
from pygame import mixer
py = sys.executable
#creating the hover effect funciton here.
def hover_on_1(event):
    mid_label1.config(bg = "yellow")
def hover_on_2(event):
    mid_label2.config(bg = "yellow")
def hover_off_1(event):
    mid_label1.config(bg = "#ffeaa7")
def hover_off_2(event):
    mid_label2.config(bg = "#ffeaa7")
#creating the process function here.
def go_to_data(event):
    print("user redirected to the data file")
    os.system("%s %s" % (py, "Track_Data.py"))
def go_to_health(event):
    print("user redirected to the health file")
    os.system("%s %s" % (py, "Track_Health.py"))
def close_app(event):
    verify = messagebox.askyesnocancel("EXIT CoronaMeter", "Are You Sure To EXIT ?")
    if verify == True:
        messagebox.showinfo("GoodBye User", "Thanks For Using Me :)\nCome Again :)")
        window.destroy()
    elif verify == False:
        pass
    else:
        pass
def play_audio(audio_file):
    audio = audio_file
    mixer.init()
    mixer.music.load(audio)
    mixer.music.play()
#creating the window here for the screen.
window = Tk()
window.title("CoronaMeter")
window.attributes("-fullscreen", True)
window.iconbitmap("iconfile.ico")
window.configure(bg = "#ffeaa7")
#creating the frame here.
window_frame1 = Frame(window, bg = "#ffeaa7", border = 0, borderwidth = 0, relief = FLAT)
window_frame1.pack(side = TOP, anchor = CENTER, padx = 300, pady = 10, fill = X)
#creating the labels text here.
label_text1 = "CoronaMeter"
label_text2 = "The Most Accurate Covid-19 Realtime Data Tracker"
label_text3 = "HomePage"
label_text4 = "Close App"
label_text5 = "Track Your Health"
label_text6 = "Track Realtime Data"
label_text7 = 'Developed & Managed By Ujjwal Saini'
label_text8 = "Powered By Python 3.8"
label_text9 = "You Can Choose Any One Option From Above"
#creating the text label here.
heading_label = Label(window_frame1, bg = "#ffeaa7", fg = "#273c75", font = "Jokerman 60 bold", text = label_text1)
subhead_label = Label(window, bg = "#ffeaa7", fg = "#e74c3c", font = "Times 40 bold italic", text = label_text2)
#creating the bottom frame here.
bottom_frame = Frame(window, bg = "#ffeaa7", border = 0, borderwidth = 0, relief = FLAT)
bottom_frame.pack(side = BOTTOM, padx = 450, pady = 0, anchor = CENTER, fill = X)
bottom_label1 = Label(bottom_frame, bg = "#ffeaa7", fg = "#0652DD", font = "Times 18 bold italic", text = label_text7)
bottom_label2 = Label(bottom_frame, bg = "#ffeaa7", fg = "#0652DD", font = "Times 18 bold italic", text = label_text8)
pythonimg = PhotoImage(file = "python.png")
coderimg = PhotoImage(file = "user.png")
closeimg = PhotoImage(file = "close.png")
pythonimg_label = Label(bottom_frame, bg = "#ffeaa7", border = 0, relief = FLAT, image = pythonimg)
coderimg_label = Label(bottom_frame, bg = "#ffeaa7", border = 0, relief = FLAT, image = coderimg)
bottom_label1.grid(row = 0, column = 0, padx = 0, pady = 2)
coderimg_label.grid(row = 0, column = 1, padx = 0, pady = 2)
bottom_label2.grid(row = 1, column = 0, padx = 0, pady = 2)
pythonimg_label.grid(row = 1, column = 1, padx = 0, pady = 2)
#creating the image here.
virusimg = PhotoImage(file = "virus.png")
welcomeimg = PhotoImage(file = "welcome.png")
#creating the photo labels here.
virusimg_label = Label(window_frame1, bg = "#ffeaa7", border = 0, relief = FLAT, image = virusimg)
welcomeimg_label = Label(window, bg = "#ffeaa7", border = 0, relief = FLAT, image = welcomeimg)
virusimg_label.grid(row = 0, column = 0, padx = 5, pady = 3)
heading_label.grid(row = 0, column = 1, padx = 5, pady = 3)
#creating the mid labels here for the mid frame here.
mid_frame = Frame(window, bg = "#ffeaa7", border = 0, borderwidth = 0, relief = FLAT)
bot_frame = Frame(window, bg = "#ffeaa7", border = 0, borderwidth = 0, relief = FLAT)
mid_label1 = Button(mid_frame, text = label_text6, font = "Times 30 bold italic", bg = "#ffeaa7", fg = "#192a56", border = 0, relief = FLAT, activebackground = "#4cd137")
mid_label2 = Button(mid_frame, text = label_text5, font = "Times 32 bold italic", bg = "#ffeaa7", fg = "#192a56", border = 0, relief = FLAT, activebackground = "#4cd137")
dataimg = PhotoImage(file = "analysis.png")
healthimg = PhotoImage(file = "doctor.png")
botimg = PhotoImage(file = "chatbot.png")
dataimg_label = Label(mid_frame, bg = "#ffeaa7", image = dataimg, border = 0, relief = FLAT)
healthimg_label = Label(mid_frame, bg = "#ffeaa7", image = healthimg, border = 0, relief = FLAT)
botimg_label = Label(bot_frame, bg = "#ffeaa7", image = botimg, border = 0, relief = FLAT)
botlabel = Label(bot_frame, bg = "#ffeaa7", text = label_text9, font = "Times 25 bold italic", fg = "black")
close_btn = Button(window, bg = "#ffeaa7", image = closeimg, border = 5, relief = FLAT, activebackground = "#ffeaa7",pady=4)
#packing the system here.
subhead_label.pack(side = TOP, padx = 5, pady  = 0, anchor = CENTER, fill = X)
welcomeimg_label.pack(side = TOP, padx = 0,pady = 0, fill = X, anchor = CENTER)
mid_frame.pack(side = TOP, padx = 430, pady= 5, anchor = CENTER, fill = X)
bot_frame.pack(side = TOP, padx = 300, pady= 3, anchor = CENTER, fill = X)
dataimg_label.grid(row = 0, column = 0, padx = 0, pady = 0)
mid_label1.grid(row = 0, column = 1, padx = 0, pady = 0)
healthimg_label.grid(row = 1, column = 0, padx = 0, pady = 0)
mid_label2.grid(row = 1, column = 1, padx = 0, pady = 0)
botimg_label.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
botlabel.grid(row = 0, column = 1, sticky = "w", padx = 5, pady = 0)
close_btn.pack(side = BOTTOM, padx = 5, pady = 5, anchor = CENTER, fill = X)
#to prevent the image garbage disposal in python.
pythonimg_label.image = pythonimg
coderimg_label.image = coderimg
close_btn.image = closeimg
virusimg_label.image = virusimg
welcomeimg_label.image = welcomeimg
dataimg_label.image = dataimg
healthimg_label.image = healthimg
botimg_label.image = botimg
#binding the functions here.
mid_label1.bind("<Button-1>", go_to_data)
mid_label2.bind("<Button-1>", go_to_health)
close_btn.bind("<Button-1>", close_app)
mid_label1.bind("<Enter>", hover_on_1)
mid_label1.bind("<Leave>", hover_off_1)
mid_label2.bind("<Enter>", hover_on_2)
mid_label2.bind("<Leave>", hover_off_2)
# play_audio("Welcomeenglishdavid.mp3")
window.mainloop()