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
    bright_sublabel = bright_mainheading
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
#creating the function here.
def get_covid_data(country_id):
    covid = Covid()
    covid_data = covid.get_status_by_country_id(country_id)
    key_list = list()
    value_list = list()
    for data in covid_data.keys():
        key_list.append(data)
    for data in covid_data.values():
        value_list.append(data)
    return key_list, value_list
def Process_start():
    # creating the close function here to close the window.
    def close_app(event):
        global close_app
        verify = messagebox.askyesno("EXIT CoronaMeter", "Are You Sure To EXIT ?")
        print(verify)
        if verify == True:
            messagebox.showinfo("GoodBye User", "Thanks For Using :)")
            window.destroy()
            os.system("%s %s" % (py, "Track_Data_2.py"))
        elif verify == False:
            pass
        else:
            pass
    country_value = countryvar.get()
    if str(country_value).isdigit() == True:
        try:
            keys, values = get_covid_data(country_value)
        except IndexError as unknown_country:
            print(unknown_country)
            messagebox.showerror("No Country Found", "Please Enter Valid Country ID\nAccording To The Country List")
        # scraping the headings of the data here
        country_ID = keys[0]
        country_name = keys[1]
        confirmed_cases = keys[2]
        active_cases = keys[3]
        death_cases = keys[4]
        recovered_cases = keys[5]
        latitude = keys[6]
        longitude = keys[7]
        last_update = keys[8]
        #scraping the headings data value here
        country_ID_value = values[0]
        country_name_value = values[1]
        confirmed_cases_value = values[2]
        active_cases_value = values[3]
        death_cases_value = values[4]
        recovered_cases_value = values[5]
        latitude_value = values[6]
        longitude_value = values[7]
        last_update_value = values[8]
        data_list = [country_ID, country_name, confirmed_cases, active_cases, death_cases, recovered_cases, latitude, longitude, last_update]
        datavalue_list = [country_ID_value, country_name_value, confirmed_cases_value, active_cases_value, death_cases_value, recovered_cases_value, latitude_value, longitude_value, last_update_value]
        #printing the data here.
        for i in range(len(data_list)):
            print(data_list[i], '=', datavalue_list[i])
        #creating the result or output screen window here.
        output_window = Toplevel(window)
        output_window.title("Covid-19 Realtime Data Tracking Result")
        output_window.attributes("-fullscreen", True)
        output_window.iconbitmap("iconfile.ico")
        window.attributes("-fullscreen", True)
        output_window.configure(bg = bright_background)
        #creating the mainframe here.
        mainframe = Frame(output_window, bg = bright_background, border = 0, relief = FLAT)
        mainframe.pack(side = TOP, padx = 5, pady = 5)
        #creating the objects for the images here.
        country_ID_image = PhotoImage(file = "identification.png")
        country_name_image = PhotoImage(file = "flag.png")
        confirmed_cases_image = PhotoImage(file = "confirmed.png")
        active_cases_image = PhotoImage(file = "active.png")
        death_cases_image = PhotoImage(file = "death.png")
        recovered_cases_image = PhotoImage(file = "recovered.png")
        latitude_image = PhotoImage(file = "latitude.png")
        longitude_image = PhotoImage(file = "zone.png")
        last_update_image = PhotoImage(file = "close.png")
        #creating the image labels here.
        country_ID_label = Label(mainframe, bg = bright_background, fg = bright_background, image = country_ID_image, border = 0, relief = FLAT)
        country_name_label = Label(mainframe, bg = bright_background, fg = bright_background, image = country_name_image, border = 0, relief = FLAT)
        confirmed_cases_label = Label(mainframe, bg = bright_background, fg = bright_background, image = confirmed_cases_image, border = 0, relief = FLAT)
        active_cases_label = Label(mainframe, bg = bright_background, fg = bright_background, image = active_cases_image, border = 0, relief = FLAT)
        death_cases_label = Label(mainframe, bg = bright_background, fg = bright_background, image = death_cases_image, border = 0, relief = FLAT)
        recovered_cases_label = Label(mainframe, bg = bright_background, fg = bright_background, image = recovered_cases_image, border = 0, relief = FLAT)
        latitude_label = Label(mainframe, bg = bright_background, fg = bright_background, image = latitude_image, border = 0, relief = FLAT)
        longitude_label = Label(mainframe, bg = bright_background, fg = bright_background, image = longitude_image, border = 0, relief = FLAT)
        last_update_label = Button(output_window, bg = bright_background, fg = bright_background, image = last_update_image, border = 0, relief = FLAT, command = close_app)
        #creating the text here.
        country_ID_text = "Country ID\n"+str(country_ID_value)
        country_name_text = "Country Name\n"+str(country_name_value)
        confirmed_cases_text = "Confirmed Cases\n"+str(confirmed_cases_value)
        active_cases_text = "Active Cases\n"+str(active_cases_value)
        recovered_cases_text = "Recovered Cases\n"+str(recovered_cases_value)
        death_cases_text = "Death Cases\n"+str(death_cases_value)
        latitude_text = "Latitude\n"+str(latitude_value)
        longitude_text = "Longitude\n"+str(longitude_value)
        last_update_text = "Back To HomePage"
        #creating the text labels here.
        country_ID_tlabel = Label(mainframe, bg = bright_background, fg = bright_sublabel, font = "Times 30 bold italic", text = country_ID_text)
        country_name_tlabel = Label(mainframe, bg = bright_background, fg = bright_sublabel, font = "Times 30 bold italic", text = country_name_text)
        confirmed_cases_tlabel = Label(mainframe, bg = bright_background, fg = bright_sublabel, font = "Times 30 bold italic", text = confirmed_cases_text)
        active_cases_tlabel = Label(mainframe, bg = bright_background, fg = bright_sublabel, font = "Times 30 bold italic", text = active_cases_text)
        recovered_cases_tlabel = Label(mainframe, bg = bright_background, fg = bright_sublabel, font = "Times 30 bold italic", text = recovered_cases_text)
        death_cases_tlabel = Label(mainframe, bg = bright_background, fg = bright_sublabel, font = "Times 30 bold italic", text = death_cases_text)
        latitude_tlabel = Label(mainframe, bg = bright_background, fg = bright_sublabel, font = "Times 30 bold italic", text = latitude_text)
        longitude_tlabel = Label(mainframe, bg = bright_background, fg = bright_sublabel, font = "Times 30 bold italic", text = longitude_text)
        last_update_tlabel = Label(output_window, bg = bright_background, fg = bright_sublabel, font = "Times 30 bold italic", text = last_update_text)
        #packing the whole entire system here.
        country_ID_label.grid(row = 0, column = 0, sticky = "w", padx = 50, pady = 5)
        country_name_label.grid(row = 0, column = 2, sticky = "w", padx = 50, pady = 5)
        confirmed_cases_label.grid(row = 1, column = 0, sticky = "w", padx = 50, pady = 5)
        active_cases_label.grid(row = 1, column = 2, sticky = "w", padx = 50, pady = 5)
        recovered_cases_label.grid(row =2 , column = 0, sticky = "w", padx = 50, pady = 5)
        death_cases_label.grid(row = 2, column = 2, sticky = "w", padx = 50, pady = 5)
        latitude_label.grid(row = 3, column = 0, sticky = "w", padx = 50, pady = 5)
        longitude_label.grid(row = 3, column = 2, sticky = "w", padx = 50, pady = 5)
        ###################################################################################
        country_ID_tlabel.grid(row=0, column=1, sticky="w", padx=0, pady=5)
        country_name_tlabel.grid(row=0, column=3, sticky="w", padx=0, pady=5)
        confirmed_cases_tlabel.grid(row=1, column=1, sticky="w", padx=0, pady=5)
        active_cases_tlabel.grid(row=1, column=3, sticky="w", padx=0, pady=5)
        recovered_cases_tlabel.grid(row=2, column=1, sticky="w", padx=0, pady=5)
        death_cases_tlabel.grid(row=2, column=3, sticky="w", padx=0, pady=5)
        latitude_tlabel.grid(row=3, column=1, sticky="w", padx=0, pady=5)
        longitude_tlabel.grid(row=3, column=3, sticky="w", padx=0, pady=5)
        last_update_label.pack(side = BOTTOM, padx = 5, pady = 5, anchor = CENTER)
        last_update_tlabel.pack(side = BOTTOM, padx = 5, pady = 5, anchor = CENTER)
        # binding the buttons here
        last_update_label.bind("<Button-1>", close_app)
        output_window.mainloop()
    else:
        messagebox.showerror("Invalid Country ID", "Please Use DIGITS For The Country ID !")
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
#creating the window here.
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
label_text3 = "Get All Covid-19 Data By Country ID"
label_text4 = "Enter The Country ID Below"
label_text5 = "Get Data"
label_text6 = "Close App"
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
#creating the main functionality here.
robotimg = PhotoImage(file = "chatbot.png")
closeimg = PhotoImage(file = "close.png")
countryimg = PhotoImage(file = "worldwide.png")
nextimg = PhotoImage(file = "next.png")
roboframe = Frame(window, bg = bright_background, border = 0, borderwidth = 0, relief = FLAT)
robotimg_label = Label(roboframe, bg = bright_background, image = robotimg, relief = FLAT, border = 0)
closeimg_label = Button(window, bg = bright_background, image = closeimg, relief = FLAT, border = 0, activebackground = "yellow")
countryimg_label = Label(window, bg = bright_background, image = countryimg, relief = FLAT, border = 0)
robo_label = Label(roboframe, bg = bright_background, fg = bright_sublabels, font = "Times 30 bold italic", text = label_text3)
nextimg_label = Button(window, bg = bright_background, image = nextimg, border = 0, borderwidth = 0, relief = FLAT, activebackground = "yellow", command = Process_start)
#packing the entire system here.
countryimg_label.pack(side = TOP, anchor = CENTER, padx = 0, pady = 3)
roboframe.pack(side = TOP, anchor = CENTER, padx = 0, pady = 3)
robotimg_label.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = 'w')
robo_label.grid(row = 0, column = 1, padx = 5, pady = 0, sticky = 'w')
closeimg_label.pack(side = BOTTOM, padx = 5, pady = 10, anchor = CENTER)
#creating the entry widget.
entry_label = Label(window, bg = bright_background, fg = bright_sublabel, font = "Times 45 bold italic", text = label_text4)
entry_label.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
countryvar = StringVar()
country_entry = Entry(window, bg = "#dff9fb", fg = 'darkblue', font = "Arial 30 bold", width = 20, textvariable = countryvar)
country_entry.focus()
country_entry.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
nextimg_label.pack(side = TOP, padx = 5,pady = 10, anchor = CENTER)
#binding the buttons here.
closeimg_label.bind("<Button-1>", close_app)
window.mainloop()