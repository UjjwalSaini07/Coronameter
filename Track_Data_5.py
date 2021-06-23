from covid import *
from covid import Covid
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import matplotlib.pyplot as plt
import random
import sys
py = sys.executable
# init the values for the color codes.
bright_background = "#ffeaa7"
bright_mainheading = "#273c75"
bright_subheading = "#e74c3c"
bright_sublabels = "black"
bright_sublabel = "darkblue"
bright_label1 = 'white'
bright_label2 = 'lightgreen'
#file-handling here.
themefile = open('savedtheme.txt')
readvalue = themefile.read()
if readvalue == "DarkThemeTRUE" or readvalue == "DarkTheme":
    # storing the color code for dark theme here.
    bright_background = "#30336b"
    bright_mainheading = "yellow"
    bright_subheading = "cyan"
    bright_sublabel = 'black'
    bright_sublabels = 'black'
    bright_label1 = 'white'
    bright_label2 = 'lightgreen'
elif readvalue == "BrightThemeTRUE" or readvalue == "BrightTheme":
    #storing the color code for bright theme here.
    bright_background = "#ffeaa7"
    bright_mainheading = "#273c75"
    bright_subheading = "#e74c3c"
    bright_sublabels = "black"
    bright_sublabel = "darkblue"
    bright_label1 = 'black'
    bright_label2 = 'darkblue'
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
covid = Covid()
#creating the function here.
def pie_chart(actual_values, value_label):
    plt.pie(actual_values, labels = value_label, textprops = {'fontsize':15}, autopct = '%0.0f%%', shadow = False)
    plt.legend()
    plt.axis("equal")
    plt.show()
def bar_graph(country_list, valuelist, colour, edgecolour, linestyle, label, graphtype, width = 0.2, align = 'edge'):
    plt.bar(country_list, valuelist, color = colour, edgecolor = edgecolour, linestyle = linestyle, label = label)
    plt.title(graphtype, fontsize = 20)
    plt.xlabel("Name Of Countries", fontsize = 15)
    plt.ylabel(f"Number Of {graphtype} For Each Country", fontsize = 15)
    plt.legend()
    plt.show()
def show_graph():
    id_string = countryvar.get()
    graph_type = graph_type_var.get()
    graph_data = graph_data_var.get()
    ids = id_string.split(',')
    main_ids = list()
    for id in ids:
        try:
            int_id = int(id)
            main_ids.append(int_id)
        except Exception as error:
            print(error)
            messagebox.showwarning("Warning", "Please Enter The Contry-ID\nIn Numbers Only !")
    datalist = list()
    for i in main_ids:
        data = covid.get_status_by_country_id(i)
        datalist.append(data)
    print(datalist)
    value_list = list()
    countrylist = list()
    if graph_data == "Recovered Cases" and graph_type == "Bar Graph":
        for i in datalist:
            rdata = i.get('recovered')
            cdata = i.get("country")
            value_list.append(rdata)
            countrylist.append(cdata)
        try:
            bar_graph(countrylist, value_list, 'lightgreen', edgecolour = 'red', linestyle = '--', label = graph_data, graphtype = graph_data)
        except Exception as internet_error:
            print(internet_error)
            messagebox.showerror("Unstable Network Detected !", "Please Make Sure That You Are Connected To The Internet")
    elif graph_data == "Active Cases" and graph_type == "Bar Graph":
        for i in datalist:
            rdata = i.get('active')
            cdata = i.get("country")
            value_list.append(rdata)
            countrylist.append(cdata)
        bar_graph(countrylist, value_list, 'red', edgecolour = 'lightgreen', linestyle = '--', label = graph_data, graphtype = graph_data)
    elif graph_data == "Death Cases" and graph_type == "Bar Graph":
        for i in datalist:
            rdata = i.get('deaths')
            cdata = i.get("country")
            value_list.append(rdata)
            countrylist.append(cdata)
        bar_graph(countrylist, value_list, 'yellow', edgecolour = 'red', linestyle = '--', label = graph_data, graphtype = graph_data)
    elif graph_data == "Confirmed Cases" and graph_type == "Bar Graph":
        for i in datalist:
            rdata = i.get('confirmed')
            cdata = i.get("country")
            value_list.append(rdata)
            countrylist.append(cdata)
        bar_graph(countrylist, value_list, 'red', edgecolour = 'yellow', linestyle = '--', label = graph_data, graphtype = graph_data)
#conditions for the pie chart.
    elif graph_data == "Confirmed Cases" and graph_type == "Pie Chart":
        for i in datalist:
            rdata = i.get('confirmed')
            cdata = i.get("country")
            value_list.append(rdata)
            countrylist.append(cdata)
        pie_chart(value_list, countrylist)
    elif graph_data == "Active Cases" and graph_type == "Pie Chart":
        for i in datalist:
            rdata = i.get('active')
            cdata = i.get("country")
            value_list.append(rdata)
            countrylist.append(cdata)
        pie_chart(value_list, countrylist)
    elif graph_data == "Recovered Cases" and graph_type == "Pie Chart":
        for i in datalist:
            rdata = i.get('recovered')
            cdata = i.get("country")
            value_list.append(rdata)
            countrylist.append(cdata)
        pie_chart(value_list, countrylist)
    elif graph_data == "Death Cases" and graph_type == "Pie Chart":
        for i in datalist:
            rdata = i.get('deaths')
            cdata = i.get("country")
            value_list.append(rdata)
            countrylist.append(cdata)
        pie_chart(value_list, countrylist)
    else:
        pass
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
window.title("Visualize Covid-19 RealTime Data With Graphs")
window.iconbitmap('iconfile.ico')
window.attributes("-fullscreen", True)
window.configure(bg = bright_background)
#creating the frame here.
window_frame1 = Frame(window, bg = bright_background, border = 0, borderwidth = 0, relief = FLAT)
window_frame1.pack(side = TOP, anchor = CENTER, padx = 300, pady = 0, fill = X)
#creating the labels text here.
label_text1 = "CoronaMeter"
label_text2 = "The Most Accurate Covid-19 Realtime Data Tracker"
label_text3 = "Visualize The Covid-19 Data With Graphs"
label_text4 = "Select The Graph Type"
label_text5 = "Enter Country ID's With ',' Separation Below"
label_text6 = "Close App"
label_text7 = "Select The Graph Data"
#creating the images here.
closeimg = PhotoImage(file = "close.png")
nextimg = PhotoImage(file = "next.png")
#creating the text label here.
heading_label = Label(window_frame1, bg = bright_background, fg = bright_mainheading, font = "Jokerman 80 bold", text = label_text1)
subhead_label = Label(window, bg = bright_background, fg = bright_subheading, font = "Times 60 bold italic", text = label_text2)
closeimg_label = Button(window, bg = bright_background, image = closeimg, relief = FLAT, border = 0, activebackground = "yellow")
label_1 = Label(window, text = label_text3, bg = bright_background, fg = bright_label1, font = "Times 30 bold italic underline")
label_2 = Label(window, text = label_text5, bg = bright_background, fg = bright_label2, font = "Times 30 bold")
countryvar = StringVar()
entry_box = Entry(window, bg = "white", fg = bright_sublabels, font = "Consolas 25 bold", textvariable = countryvar)
entry_box.focus()
label_3 = Label(window, text = label_text7, bg = bright_background, fg = bright_label2, font = "Times 30 bold")
graph_data_opts = ["Confirmed Cases", "Recovered Cases", "Active Cases", "Death Cases"]
graph_data_var = StringVar()
graph_data_var.set(graph_data_opts[0])
graph_data_menu = OptionMenu(window, graph_data_var, *graph_data_opts)
label_4 = Label(window, text = label_text4, bg = bright_background, fg = bright_label2, font = "Times 30 bold")
graph_type_opts = ["Bar Graph", "Pie Chart"]
graph_type_var = StringVar()
graph_type_var.set(graph_type_opts[0])
graph_type_menu = OptionMenu(window, graph_type_var, *graph_type_opts)
next_button = Button(window, image = nextimg, borderwidth = 0, bd = 0, relief = FLAT, command = show_graph, bg = bright_background, fg = bright_background)
#packing the system here.
heading_label.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
subhead_label.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
closeimg_label.pack(side = BOTTOM, padx = 5, pady = 0, anchor = CENTER)
closeimg_label.bind("<Button-1>", close_app)
label_1.pack(side = TOP, padx = 3, pady = 3, anchor = CENTER)
label_2.pack(side = TOP, padx = 3, pady = 3, anchor = CENTER)
entry_box.pack(side = TOP, padx = 5, pady = 0, anchor = CENTER)
label_3.pack(side = TOP, padx = 3, pady = 3, anchor = CENTER)
graph_data_menu.pack(side = TOP, padx = 3, pady = 3, anchor = CENTER)
graph_data_menu.config(font = "Times 25 bold italic", bg = "yellow", fg = bright_sublabel)
label_4.pack(side = TOP, padx = 3, pady = 3, anchor = CENTER)
graph_type_menu.pack(side = TOP, padx = 3, pady = 3, anchor = CENTER)
graph_type_menu.config(font = "Times 25 bold italic", bg = "yellow", fg = bright_sublabel)
next_button.pack(side = TOP,padx = 3, pady = 5, anchor = CENTER)
window.mainloop()
