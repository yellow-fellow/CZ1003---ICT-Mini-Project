# ----------------------------------- Imports ----------------------------------------------
from time import * #gives you a current time in str
from tkinter import ttk #combobox for calendar hour and minute
from stall_functions import * #import our user-defined functions
from tkcalendar import * #import calendar #External python module used : tkCalendar
import datetime #get current date and time in datetime format
import calendar #Convert string to date e.g '11' to Nov
#This program is best run on Mac OS for better GUI experience
# ------------------------------- Defining Key Functions ----------------------------------- #Shaohang
main_window = tk.Tk() #create window
global user_input_time #make variable global
user_input_time = datetime.datetime.today().time() #assign current time to variable (eg: 18:36:07.317845)

#--------------------------------File paths of pictures------------------------------------------ #Shaohang & Jovan
fries = PhotoImage(file = os.path.join(get_directory_path(), "french_fries.gif"))
sandwich = PhotoImage(file = os.path.join(get_directory_path(), "sandwich.gif"))
oldman = PhotoImage(file = os.path.join(get_directory_path(), "oldman.gif"))
fish = PhotoImage(file = os.path.join(get_directory_path(), "fish.gif"))
pizza = PhotoImage(file = os.path.join(get_directory_path(),"pizza.gif"))
menu_pig = PhotoImage(file = os.path.join(get_directory_path(), "menu.gif"))
clock_pic = PhotoImage(file = os.path.join(get_directory_path(), "clock.gif"))
dino = PhotoImage(file = os.path.join(get_directory_path(), "dino.gif"))
rabbit = PhotoImage(file = os.path.join(get_directory_path(), "rabbit.gif"))

# ---------------------------------------  Time  -------------------------------------------
def tick(): #Shaohang & Eugene
    time_string = time.strftime("%H:%M:%S") #assign current time to variables (eg: 18:36:46)
    clock.config(text=time_string) #updates the current time dynamically on the label, 'clock' 
    clock.after(200, tick) #delay for 200ms before calling the function, tick() again

#Label stating the current date (eg: 12-Nov-2019)
Label(main_window, text=f"{datetime.datetime.now():%d-%b-%Y}", fg='white', bg="#7babed", font=("helvetica", 40, "bold")).grid(row=1,column=4,sticky = EW)

#Label for 'clock'
clock = Label(main_window, font=("helvetica", 40, "bold"), bg="#7babed", fg="white")
clock.grid(row=2, column=4, sticky = EW)

tick() #call the function, tick()

# ------------------------------ List of Stalls (Page 2) ------------------------------------
def list_of_stalls(): #All
    #make variables global
    global ljs_button, pizzahut_button, return_button
    #Label stating headers
    Label(font=('aria', 50, 'bold'), text="Canteen Stalls", fg="black", bd=20, bg='#7babed', anchor='center').grid(row=0,column=4,sticky=NSEW)    #Buttons
    #Button for McDonald's
    mac_button = Button(main_window, text="              McDonald's",fg='black',bg='#fcebbf',image = fries, compound = 'left',command=lambda:stall_functions("McDonald's"), height=65, width=20)
    mac_button.grid(row=3,column=4,sticky=EW)
    #Button for Subway
    subway_button = Button(main_window, text='        Subway',fg='black',bg='#fcebbf',image = sandwich, compound = 'left', height=65, command=lambda:stall_functions("Subway"), width=20)
    subway_button.grid(row=4,column=4,sticky=EW)
    #Button for KFC
    kfc_button = Button(main_window, text='           KFC',fg='black',bg='#fcebbf',image = oldman, compound = 'left', height=65, command=lambda:stall_functions("KFC"), width=20)
    kfc_button.grid(row=5,column=4,sticky=EW)
    #Button for Long John Silver
    ljs_button = Button(main_window, text='       Long John Silver',fg='black',bg='#fcebbf',image = fish, compound = 'left', height=65, command=lambda:stall_functions("Long John Silver"), width=20)
    ljs_button.grid(row=6,column=4,sticky=EW)
    #Button for Pizza Hut
    pizzahut_button = Button(main_window, text='        Pizza Hut',fg='black',bg='#fcebbf',image = pizza, compound = 'left', height=65, command=lambda:stall_functions("Pizza Hut"), width=20)
    pizzahut_button.grid(row=7,column=4,sticky=EW)
    #Button for back
    return_button = Button(main_window, text='Back',fg = '#e091a4', bg = '#f6c2d8', height=4, command=refresh, width=20)
    return_button.grid(row=8,column=4,sticky=EW)
# ----------------------------- Stall Information (Page 3) ----------------------------------
def stall_functions(stall_name): #All

    pizzahut_button.grid_forget() #remove grids
    return_button.grid_forget() #remove grids
    #Label stating header of window
    Label(main_window, font=('aria', 50, 'bold'),text= stall_name +  " Information ",fg = 'black',bg = '#7babed',anchor='center').grid(row=0,column=4,sticky=NSEW)
    #Button for Menu
    menu_button = Button(main_window,image = dino, compound = 'right',command=(lambda: get_menu(stall_name,user_input_time)), text='Menu',fg='black',bg='#fcebbf',height=4, width=20).grid(row=3,column=4,sticky=NSEW)
    #Button for Operating Hours
    operating_hours_button = Button(main_window, image = clock_pic, compound = 'right',command=lambda:show_operating_hours(stall_name), text='Operating Hours',fg='black',bg='#fcebbf',height=4, width=20).grid(row=4,column=4,sticky=NSEW)
    #Button for Estimated Waiting Time
    estimated_wait_time_button = Button(main_window, image = rabbit, compound = 'right',command=estimated_wait_time,text='Estimated Waiting Time',fg='black',bg='#fcebbf',height =4, width=20).grid(row=5,column=4,sticky=NSEW)
    #Button for return
    return_to_stall_button = Button(main_window, text='Back',fg = '#e091a4', command=list_of_stalls, height =4, width=20).grid(row=6,column=4,sticky=NSEW)

# -------------------------- User Defined Date & Time (Page 2) ----------------------------------

#open a window for user to set date & time
def set_date_and_time(): #Shaohang & Jovan
    global select_a_date
    #Create a window and give the window a title
    select_a_date = Tk()
    select_a_date.title("Select Date & Time")
    #set background colour for the window
    select_a_date.configure(background="#7babed")
    #set window's geometry
    select_a_date.geometry('350x300')
    #top user from resizing the window
    stop_resizing(select_a_date)

    #Label the title as "Date & Time"
    Label(select_a_date, text="Key in Date & Time", fg="black", bg="#7babed", font="Helvetica 15 bold").place(relx=0, rely=0)

    global dropdown_list_hour
    #create an empty list for hour_list
    hour_list = []
    #range of hour-hand is from 0 - 23.
    for hour_hand in range(0, 24):
        #if hour_hand is a single digit, add '0' to the front of that digit. (now all hour_hands got 2 digits)
        if hour_hand < 10:
            hour_hand = '0' + str(hour_hand)
        #add the 2 digits hour_hand into hour_list
        hour_list.append(str(hour_hand))
    #create a dropdown list for hour-hand
    dropdown_list_hour = ttk.Combobox(select_a_date, values=hour_list, width=5)
    dropdown_list_hour.place(relx=0.05, rely=0.15)

    global dropdown_list_minute
    #create an empty list for minute-hand
    minute_list = []
    #range of minute-hand is from 0 to 59
    for minute in range(0,60):
        #if minute-hand is a single digit, add '0' to the front of that digit. (now all minute-hands got 2 digits)
        if minute < 10:
            minute = '0' + str(minute)
        #add the 2 digits minute-hand into minute_list
        minute_list.append(str(minute))
    dropdown_list_minute = ttk.Combobox(select_a_date, values=minute_list, width=5)
    dropdown_list_minute.place(relx=0.31, rely=0.15)

    Label(select_a_date, text="Hours          :       Minutes",bg="#7babed", font="helvetica 10 bold").place(relx=0.0875, rely=0.08)
    Label(select_a_date, text = ":",fg="black", bg="#7babed").place(relx=0.26,rely = 0.15)

    #obtain current year, month and day
    year_now = int(strftime('%Y'))  
    month_now = int(strftime('%m'))
    day_now = int(strftime('%d'))

    global calendar_select
    # captures the current date to display on tkinter calendar
    calendar_select = Calendar(select_a_date, font="Arial 14", cursor="hand2",bordercolor='white', year=year_now, month=month_now, day=day_now,selectmode='day', foreground = 'black',background ='white',weekendforeground ='black',othermonthweforeground = '#ced6e3',othermonthforeground='#ced6e3', selectforeground = '#7babed')
    calendar_select.place(relx=0.5, rely=0.6, anchor="center")

    #button to enter date and time
    Button(select_a_date, text="Enter",bg = '#fcebbf', height=2, width=10, command=get_date_and_time).place(relx=0.8, rely=0.19, anchor='center')

#obtain the user's input for date & time
def get_date_and_time(): #Jovan
    try:
        # gets values of day, ..., from combobox in date_selection function (user's input)
        time_hour_str = dropdown_list_hour.get()
        assert 0 <= int(time_hour_str) <= 23 #Ensure user input is within this range #hour
        time_minute_str = dropdown_list_minute.get()
        assert 0 <= int(time_minute_str) <= 59 #Ensure user input is within this range #minutes
        cal_date = str(calendar_select.selection_get()) #Obtain input of date as a str e.g.2019-11-27

        time = time_hour_str + ":" + time_minute_str  # obtain the time from the string (HH:MM)

        #show updated date & time in main_window based on user's input
        Label(main_window,text = cal_date[8:10] +'-'+ calendar.month_abbr[int(cal_date[5:7])]  +'-'+ cal_date[0:4],font=("helvetica", 40, "bold"),bg='#7babed', fg='white').grid(row=1,column=4,sticky=EW)
        Label(main_window, text=('       '+str(time)+":00"+'       '), font=("helvetica", 40, "bold"), bg ='#7babed',fg="white").grid(row=2,column=4,sticky=EW)
        
        select_a_date.destroy() #close select_a_date window
        global user_input_time

        user_input_time = datetime.time(int(time[:2]),int(time[3:])) #update user_input_time
        list_of_stalls() #call list_of_stalls() function

    except AssertionError:
        # create a window
        error = tk.Tk()
        # title of window
        error.title('ERROR!')
        # stop user from resizing the window
        stop_resizing(error)
        # Label stating the error message
        Label(error, text="Hours must be an integer from 0 to 23 and Minutes must be an integer from 0 to 59!").grid()
        # Button to close error window
        Button(error, text='Ok', command=lambda: error.destroy()).grid(row=3)

    except ValueError: #when got ValueError, run this
        #create a window
        error = tk.Tk()
        #title of window
        error.title('ERROR!')
        #stop user from resizing the window
        stop_resizing(error)
        #Label stating the error message
        Label(error, text='You have not keyed in an integer for Hours and Minutes!').grid()
        Label(error, text ="Hours must be an integer from 0 to 23 and Minutes must be an integer from 0 to 59!").grid()
        #Button to close error window
        Button(error, text = 'Ok',command = lambda:error.destroy()).grid(row=3)
    except: #when there are other errors, run this
        #create a window
        error = tk.Tk()
        #title of window
        error.title('ERROR!')
        #stop user from resizing the window
        stop_resizing(error)
        #Label stating the error message
        Label(error, text='You have not keyed in an integer for Hours and Minutes!').grid()
        Label(error, text ="Hours must be an integer from 0 to 23 and Minutes must be an integer from 0 to 59!").grid()
        #Button to close error window
        Button(error, text = 'Ok',command = lambda:error.destroy()).grid(row=3)

# -------------------------- Title & Welcome Message of Main Window (Page 1) -----------------
#Shaohang
#title of window
main_window.title('NTU Real-Time Canteen Information')
#Label stating the header of window
Label(font=('aria', 50, 'bold'),image=menu_pig,compound='right', text="NTU Real-Time Canteen App", fg="black", bd=20,bg='#7babed', anchor='center').grid(row=0,column=4,sticky = EW)
#Button to select "Use Current Date & Time"
current_time_button = Button(main_window, text="View Canteen Stalls based on Current Date & Time",fg = 'black',bg = '#fcebbf', command=lambda:list_of_stalls(), height=4, width=20).grid(row=3,column=4,sticky=EW)
#Button to select "Input Date & Time"
input_date_time_button = Button(main_window, text="View Canteen Stalls based on your Input Date & Time",fg = 'black',bg = '#fcebbf', command=lambda:set_date_and_time(), height=4, width=20).grid(row=4,column=4,sticky=EW)
#Button to exit program
quit_button = Button(main_window, text="Exit",fg = '#e091a4', bg = '#f6c2d8', command=lambda:quit(), height=4, width=20).grid(row=5,column=4,sticky=EW)
#stop user from resizing the window
stop_resizing(main_window)
#mainloop runs until the main window is destroyed. Without this, the application will not run.
main_window.mainloop()

