from covid import *
from covid import Covid
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sys
py = sys.executable
# init the values for the color codes.
bright_background = "#ffeaa7"
bright_mainheading = "#273c75"
bright_subheading = "#e74c3c"
bright_sublabels = "black"
bright_sublabel = "darkblue"
#file-handling here.
themefile = open('savedtheme.txt')
readvalue = themefile.read()
if readvalue == "DarkThemeTRUE" or readvalue == "DarkTheme":
    # storing the color code for dark theme here.
    bright_background = "#30336b"
    bright_mainheading = "yellow"
    bright_subheading = "cyan"
    bright_sublabel = 'yellow'
    bright_sublabels = 'white'
elif readvalue == "BrightThemeTRUE" or readvalue == "BrightTheme":
    #storing the color code for bright theme here.
    bright_background = "#ffeaa7"
    bright_mainheading = "#273c75"
    bright_subheading = "#e74c3c"
    bright_sublabels = "black"
    bright_sublabel = "darkblue"
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
#creating the functions here.
def close_app(event):
    verify = messagebox.askyesnocancel("EXIT CoronaMeter", "Are You Sure To EXIT ?")
    print(verify)
    if verify == True:
        messagebox.showinfo("GoodBye User", "Thanks For Using :)")
        window.destroy()
        os.system("%s %s" % (py, "Track_Data.py"))
    elif verify == False:
        pass
    else:
        pass
#fetching the data here.
def display_data(confirmed, active, recovered, deaths):
    #getting the values from here
    confirmed_cases_value, active_cases_value, recovered_cases_value, death_cases_value = confirmed, active, recovered, deaths
    new = Toplevel(window)
    new.grab_set()
    new.title("World-Wide Covid-19 Data")
    new.iconbitmap('iconfile.ico')
    new.geometry("800x600")
    new.resizable(0,0)
    new.configure(bg=bright_background)
    #creating the labels and images here.
    confirmed_cases_image = PhotoImage(file="confirmed.png")
    active_cases_image = PhotoImage(file="active.png")
    death_cases_image = PhotoImage(file="death.png")
    recovered_cases_image = PhotoImage(file="recovered.png")
    #creating the images label here.
    confirmed_cases_label = Label(new, bg=bright_background, fg=bright_background, image=confirmed_cases_image, border=0,relief=FLAT)
    active_cases_label = Label(new, bg=bright_background, fg=bright_background, image=active_cases_image, border=0, relief=FLAT)
    death_cases_label = Label(new, bg=bright_background, fg=bright_background, image=death_cases_image, border=0, relief=FLAT)
    recovered_cases_label = Label(new, bg=bright_background, fg=bright_background, image=recovered_cases_image, border=0,relief=FLAT)
    #creating the text for the labels here.
    confirmed_cases_text = "Confirmed Cases\n" + str(confirmed_cases_value)
    active_cases_text = "Active Cases\n" + str(active_cases_value)
    recovered_cases_text = "Recovered Cases\n" + str(recovered_cases_value)
    death_cases_text = "Death Cases\n" + str(death_cases_value)
    #creating the text labels here.
    confirmed_cases_tlabel = Label(new, bg=bright_background, fg=bright_sublabel, font="Times 30 bold italic",text=confirmed_cases_text)
    active_cases_tlabel = Label(new, bg=bright_background, fg=bright_sublabel, font="Times 30 bold italic",text=active_cases_text)
    recovered_cases_tlabel = Label(new, bg=bright_background, fg=bright_sublabel, font="Times 30 bold italic",text=recovered_cases_text)
    death_cases_tlabel = Label(new, bg=bright_background, fg=bright_sublabel, font="Times 30 bold italic",text=death_cases_text)
    #packing the system here.
    confirmed_cases_label.place(x = 100, y = 20)
    confirmed_cases_tlabel.place(x = 20, y = 150)
    active_cases_label.place(x = 500, y = 20)
    active_cases_tlabel.place(x = 480, y = 150)
    recovered_cases_label.place(x = 100, y = 300)
    recovered_cases_tlabel.place(x = 20, y = 430)
    death_cases_label.place(x = 500, y = 300)
    death_cases_tlabel.place(x = 480, y = 430)
    new.mainloop()
def get_world_data():
    covid = Covid()
    total_active = covid.get_total_active_cases()
    total_recovered = covid.get_total_recovered()
    total_deaths = covid.get_total_deaths()
    total_confirmed = covid.get_total_confirmed_cases()
    display_data(total_confirmed, total_active, total_recovered, total_deaths)
    return total_confirmed, total_active, total_recovered, total_deaths
def hoveron(event):
    button.config(border = 5, relief = RAISED)
def hoveroff(event):
    button.config(border = 5, relief = SOLID)
#creating the window here.
window = Tk()
window.grab_set()
window.title("Covid-19 RealTime Data Tracker")
window.iconbitmap('iconfile.ico')
window.attributes("-fullscreen", True)
window.configure(bg = bright_background)
#creating the frame here.
window_frame1 = Frame(window, bg = bright_background, border = 0, borderwidth = 0, relief = FLAT)
window_frame1.pack(side = TOP, anchor = CENTER, padx = 500, pady = 20, fill = X)
#creating the labels text here.
label_text1 = "CoronaMeter"
label_text2 = "The Most Accurate Covid-19 Realtime Data Tracker"
label_text3 = "Get All The World-Wide Covid-19 Data"
#creating the text label here.
heading_label = Label(window_frame1, bg = bright_background, fg = bright_mainheading, font = "Jokerman 80 bold", text = label_text1)
subhead_label = Label(window, bg = bright_background, fg = bright_subheading, font = "Times 60 bold italic", text = label_text2)
#creating the image here.
virusimg = PhotoImage(file = "virus.png")
#creating the photo labels here.
virusimg_label = Label(window_frame1, bg = bright_background, border = 0, relief = FLAT, image = virusimg)
virusimg_label.grid(row = 0, column = 0, padx = 5, pady = 3)
heading_label.grid(row = 0, column = 1, padx = 5, pady = 3)
subhead_label.pack(side = TOP, padx = 5, pady  = 0, anchor = CENTER, fill = X)
label1 = Label(window, text = label_text3, fg = 'black', bg = '#ffeaa7', font = 'times 30 bold italic underline')
label1.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER, fill = X)
worldimg = PhotoImage(file = "data-center.png")
worldimg_label = Label(window, image = worldimg, borderwidth = 0, bd = 0, relief= FLAT, bg = bright_background, fg = '#ffeaa7')
worldimg_label.pack(side = TOP, padx =5, pady = 5, anchor= CENTER)
#creating the button for the next process.
button = Button(window, text = "Show World Data", border = 5, relief = SOLID, bg= bright_background, fg = bright_sublabels, command = get_world_data, font = "Times 30 bold", activebackground = "yellow", activeforeground = 'black')
button.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
button.bind('<Enter>', hoveron)
button.bind('<Leave>', hoveroff)
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
count = 0
text = ''
slider_label = Label(window, text = slider_text, bg = bright_background, fg = bright_sublabels, font = "Times 30 bold italic")
slider_label.pack(side = BOTTOM, padx = 5, pady = 10, anchor = CENTER)
slider()
#creating the close buton here.
closeimg = PhotoImage(file = "close.png")
closeimg_label = Button(window, bg = bright_background, image = closeimg, relief = FLAT, border = 0, activebackground = "yellow")
closeimg_label.pack(side = BOTTOM, padx = 5, pady = 10, anchor = CENTER)
#binding the buttons here.
closeimg_label.bind("<Button-1>", close_app)
window.mainloop()