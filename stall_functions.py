#------------------------------------------------import-------------------------------------------
import datetime
import time
import tkinter as tk
from tkinter import *
import datetime
import json
import os

#---------------------------------------File Management--------------------------------------------

#get path of current directory only
def get_directory_path(): #Jovan
    return os.path.dirname(__file__)

#get menu.json's full filepath
def get_menu_filepath(): #Jovan
    return get_directory_path() + "/Menu.json"

#get Operating_Times's full filepath
def get_operating_times_filepath(): #Jovan
    return os.path.dirname(__file__) + "/Operating_Times.json"

#read json file's content
def read_jsonfile(filepath): #Jovan
    with open(filepath, 'r') as fp:
        return json.load(fp)

#get dictionary of the stalls' operating times, breakfast menu timing and regular menu timing #Jovi
def get_operating_times_dict(): #Jovan
    return read_jsonfile(get_operating_times_filepath())

#get dictionary of the stalls' breakfast menus and regular menus. #Jovi
def get_menu_dict(): #Jovan
    return read_jsonfile(get_menu_filepath())

#Assign Menu's dictionary and Operating Times' dictionary to variables
menu_dict = get_menu_dict()
operatingtimes_dict= get_operating_times_dict()

#---------------------------------Stop end-users from resizing the window----------------------------------------------------

def stop_resizing(window_name): #Jovan
    window_name.resizable(width=False, height=False)


#-----------------convert str to datetime object (eg str: "00:00" to datetime object)-----------------------------------------
def convert_str_to_datetime(str): #Shaohang & Eugene
    return datetime.datetime.strptime(str,'%H:%M').time()

#----------------------------------------------------Operating Hours-----------------------------------------------------------

#get stall_opening_time, stall_closing_time, stall_breakfast_opening and stall_breakfast_closing based on user's selected stall
def get_stall_hours(input_stall): #Eugene
    #get operating hours (in string format) from dictionary (eg: 07:00 - 23:59)
    get_stall_ot = operatingtimes_dict[input_stall]["Monday - Sunday"] 

    #get breakfast menu hours (in string format) from dictionary (eg: 07:00 - 23:59)
    get_stall_breakfast_time = operatingtimes_dict[input_stall]["Breakfast Menu"] 
    
    #make variables global
    global stall_opening_time, stall_closing_time
    global stall_breakfast_opening, stall_breakfast_closing
    
    stall_opening_time = get_stall_ot[:5] #get stall opening time (eg: 07:00)
    stall_closing_time = get_stall_ot[-5:] #get stall closing time (eg: 22:00)

    stall_breakfast_opening = get_stall_breakfast_time[:5] #get breakfast menu starting time (eg: 07:00)
    stall_breakfast_closing = get_stall_breakfast_time[-5:] #get breakfast menu ending time (eg: 11:00)

#open a new window to show operating hours based on user's selected stall
def show_operating_hours(input_stall): #Eugene
    #create new window
    operating_hours_window = Tk()
    #name the title of window
    operating_hours_window.title(input_stall + " Operating Hours")
    #stop end-users from resizing the window
    stop_resizing(operating_hours_window)
    #Label the header of the window
    Label(operating_hours_window, text = input_stall + " Operating Hours",font=('aria', 15, 'bold','underline'),fg = 'black').grid(row=0,column=0,sticky = EW)
    row_y = 0 #instantiates variable to 0
    for stalls in operatingtimes_dict.keys(): #iterates through all the keys in operating times dictionary. Keys = stall's names.
        if stalls == input_stall: # if stall in dictionary == user's input of stall,
            global timings #make a variable global
            timings = operatingtimes_dict.get(stalls) #assign user's selected stall's operating hours' dictionary to a variable
            for days , time in timings.items(): #iterates through key, values pairs in the selected stall's operating hours' dictionary, 3 keys in dict: 1)Monday-Sunday 2)Breakfast Menu 3)Regular Menu
                row_y += 1 #add 1 to row_y
                #show key, values pairs in window. 3 keys are 1)Monday-Sunday 2)Breakfast Menu 3)Regular Menu. Their keys are the respective timings.
                Label(operating_hours_window, text=days + ' : ' + time, wraplength=500,font=('aria', 15, 'italic'),fg = 'black',width=30).grid(row = row_y,column = 0,sticky = EW)
    #Button to close operating hours window
    Button(operating_hours_window, text='Back', command=lambda:operating_hours_window.destroy(),fg = '#e091a4', height = 2, width =30).grid(row=row_y + 1, column=0, sticky=EW, pady=4)

#----------------------------------------------------------Menu-----------------------------------------------------------------

#call either regular/breakfast/no menu based on user's input of selected stall and time
def get_menu(input_stall,input_time): #Eugene & Jovan
    #call the function get_stall_hours to obtain stall_opening_time, stall_closing_time, stall_breakfast_opening and stall_breakfast_closing
    get_stall_hours(input_stall)

    #convert string to datetime object for comparision of time later
    breakfast_start = convert_str_to_datetime(stall_breakfast_opening) #from get_stall_hours()
    breakfast_end = convert_str_to_datetime(stall_breakfast_closing)
    operating_start = convert_str_to_datetime(stall_opening_time)
    operating_end = convert_str_to_datetime(stall_closing_time)

    if operating_start <= input_time <= operating_end: #check if user's selected time is within the operating hours of selected stall
        if breakfast_start <= input_time <= breakfast_end: #check if user's selected time is within the breakfast hours of selected stall
            breakfast_menu(input_stall) #call breakfast_menu of selected stall
        else:
            regular_menu(input_stall) #call regular_menu of selected stall
    else:
        no_menu(input_stall) #call no_menu of selected stall

#open "no menu" window based on user's selected stall 
def no_menu(input_stall): #Eugene & Jovan
    #create window
    menu_window = Tk()
    #title of window
    menu_window.title("STALL CLOSED")
    #Label saying stall is closed at this hour
    Label(menu_window, text = input_stall + " is closed at this hour.", font=('aria', 15, 'bold'),fg = 'black',bg = '#7babed').grid(row=0,column=0)
    #Button to close windows
    Button(menu_window, text = "Back",command= lambda: menu_window.destroy(),fg = '#e091a4').grid(row = 1, column = 0,sticky=EW)
    #stop users from resizing the window
    stop_resizing(menu_window)

#open "breakfast menu" windows based on user's selected stall
def breakfast_menu(input_stall): #All
    #create a window
    menu_window = Tk()
    #title of window
    menu_window.title(input_stall + " Breakfast Menu")
    #prevents user from resizing the window
    stop_resizing(menu_window)
    #Label the window with stall's food and price
    for stalls in menu_dict.keys(): #iterates through the stalls in dictionary
        if stalls == input_stall: #if stall (key) in dictionary = user's input of stall
            menu = menu_dict.get(stalls) #assign the menu (values) of the stall (key) to a variable, menu
            for menu_type,choices in menu.items(): #iterates through the menu dictionary
                if menu_type == 'Breakfast Menu': #if the menu (key) = 'Breakfast Menu'
                    column_x = 0 #instantiates column_x to 0
                    for types, food in choices.items(): #iterates through the breakfast menu dictionary
                        row_y = 1 #instantiates row_y to 1
                        #Label stating the types of food in the menu (eg: Burgers, Wraps) as subheading
                        Label(menu_window, text=types, wraplength=500,borderwidth='1.5',font=('aria', 15, 'bold', 'underline'),fg = 'black').grid(row=row_y, column=column_x,sticky = EW)
                        for set, cost in food.items(): #iterates through the type of food's dictionary. It contains food's set names (keys) and costs (values).
                            row_y += 1 #add 1 to row_y
                            #Label stating the food set name (key) and cost(value) (Eg: "Egg McMuffin": "$4.50")
                            Label(menu_window, text=set + ' : ' + cost, wraplength=500,font=('aria', 10,'italic'),fg = 'black').grid(row=row_y, column=column_x)
                        column_x += 1 #add 1 to column_x for the next type of food
    #Label stating the header, "Breakfast Menu"
    Label(menu_window, text = input_stall + " Breakfast Menu",font=('aria', 15, 'bold','underline'),fg = 'black',anchor = 'center').grid(row=0,column=0,columnspan=column_x,sticky = EW)

#open "regular menu" window based on user's selected stall
def regular_menu(input_stall): #All
    #create a window
    menu_window = Tk()
    #title of window
    menu_window.title(input_stall + " Regular Menu")
    #stop end-users from resizing the window
    stop_resizing(menu_window) 
    for stalls in menu_dict.keys(): #iterates through the stalls in dictionary
        if stalls == input_stall: #if stall (key) in dictionary = user's input of stall
            menu = menu_dict.get(stalls) #assign the menu (values) of the stall (key) to a variable, menu
            for menu_type ,choices in menu.items(): #iterates through the menu dictionary
                if menu_type == 'Regular Menu': #if the menu (key) = 'Regular Menu'
                    column_x = 0 #instantiates column_x to 0
                    for types, food in choices.items():  #iterates through the Regular menu dictionary
                        row_y = 1 #instantiates row_y to 1
                        #Label stating the types of food in the menu (eg: Burgers, Wraps) as subheading
                        Label(menu_window, text=types, wraplength=500,borderwidth='1.5',font=('aria', 15, 'bold', 'underline'),fg = 'black').grid(row=row_y, column=column_x,sticky = EW)
                        for set, cost in food.items(): #iterates through the type of food's dictionary. It contains food's set names (keys) and costs (values).
                            row_y += 1 #add 1 to row_y
                            #Label stating the food set name (key) and cost(value) (Eg: "Egg McMuffin": "$4.50")
                            Label(menu_window, text=set + ' : ' + cost, wraplength=500,font=('aria', 10, 'italic'),fg = 'black').grid(row=row_y, column=column_x)
                        column_x += 1 #add 1 to column_x
    #Label stating the header, "Regular Menu"
    Label(menu_window, text = input_stall + " Regular Menu",font=('aria', 15, 'bold','underline'),fg = 'black',anchor = 'center').grid(row=0,column=0,columnspan=column_x,sticky = EW)

# ----------------------Calculation of Estimated Wait Time----------------------------

def estimated_wait_time(): #Shaohang
    #create a window
    estimated_wait_time_window = Tk()
    #title of window
    estimated_wait_time_window.title('Estimated Wait Time')
    #stop end-users from resizing the window
    stop_resizing(estimated_wait_time_window)
    #Label asking for user's input of no of pax in the queue
    Label(estimated_wait_time_window, text="Please input no. of pax in front of you:", font = 'Helvetica').grid(row=0)
    #Label stating that Estimated Wait Time is only valid during operating hours
    Label(estimated_wait_time_window, text="Disclaimer: Estimated Wait Time is only valid during operating hours.", font=('Helvetica',7)).grid(row=1)
    #create a entry box for user to input values
    entry = tk.Entry(estimated_wait_time_window)
    entry.grid(row = 0, column = 1)

    def show_entry_fields():
    #Error checking for input of number of people
        try:
            #convert user's input to integer
            no_of_people = int(entry.get())
            assert no_of_people >= 0
            #create a window
            frame_ewt = Tk()
            #title of window
            frame_ewt.title('Estimated Waiting Time')
            #stop end-users from resizing the window
            stop_resizing(frame_ewt)
            #Label stating the estimated waiting time
            Label(frame_ewt, text="Your estimated waiting time is " + str((no_of_people) * 3) + " minutes.", font = 'Helvetica',bg = '#5083c8',fg = 'white').grid(row=0)

        #ensure user input is a positive integer
        except AssertionError:
            # create a window
            frame_error = Tk()
            # title of window
            frame_error.title('ERROR')
            # stop end-users from resizing the window
            stop_resizing(frame_error)
            # Label stating the reason for error
            Label(frame_error, text='You have not keyed in a positive integer. Please try again!', font='Helvetica',fg='black').grid(row=0)
        except ValueError: #when there is ValueError, run this.
            #create a window
            frame_error = Tk()
            #title of window
            frame_error.title('ERROR')
            #stop end-users from resizing the window
            stop_resizing(frame_error)
            #Label stating the reason for error
            Label(frame_error, text='You have not keyed in a positive integer. Please try again!',font = 'Helvetica',fg ='black').grid(row=0)
        except: #if there are any other errors, run this.
            #create a window
            frame_error = Tk()
            #title of window
            frame_error.title('ERROR')
            #stop end-users from resizing the window
            stop_resizing(frame_error)
            #Label stating the reason for error
            Label(frame_error, text='You have not keyed in a positive integer. Please try again!',font = 'Helvetica',fg ='black').grid(row=0)

    #Button for calculation of Estimated Wait Time 
    Button(estimated_wait_time_window, text='Calculate', font = 'Helvetica', command=show_entry_fields).grid(row=1,column=1,sticky=tk.W,pady=4)
    #Button for closing estimated_wait_time_window
    Button(estimated_wait_time_window, text='Back',font = 'Helvetica', command=lambda:estimated_wait_time_window.destroy()).grid(row=1, column=1, sticky=tk.N, pady=4)

# --------------------------- Restart Program ----------------------------------------

def refresh(): #kyle
    python = sys.executable
    os.execl(python, python, *sys.argv)
