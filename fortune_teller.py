'''Team 3: Fortune Teller Application
Created By: Constance Sturm, Michelle Cook, Chelsea Nieves,
Valerie Rudich, and Hoi Lam Wong
University of Maryland Global Campus
CMSC 495-7382: Capstone in Computer Science
Professor David Castillo
December 12, 2023

Main Module
'''
#Pylint
#Wildcard import tkinter (wildcard-import)
from tkinter import messagebox
#Pylint
#Wildcard import tkinter.ttk (wildcard-import)
from tkinter.ttk import *
import tkinter as tk
from databasehelper import sign_up, save_fortune_to_table, get_previous_fortunes, create_table
import sessionhandler
### Pylint WildCard Import
from fthelper import *

# create root window
root = Tk()

# Constance Sturm 11/26/2023, 12/5/23
def display_rules():
    ''' Create a window that displays the rules to the user'''
    # Initialize New Window
    rules_tk = Toplevel()
    rules_tk.geometry('650x415')
    rules_tk.title('Rules of the Fortune Teller')
    center_window(rules_tk, 650, 415)

    lbl = Label(rules_tk, text='How to Play the Fortune Teller Game\n', font='50')
    lbl.pack()
    # Chelsea Nieves: updated rules 12/10/23
    msg = Message(rules_tk, text='> From the "Main Menu", select "Play as Guest" or "Login!" \n '
                  '> If you do not already have an account, you may register by selecting '
                  '"Register" from the "Main Menu". \n'
                  '> Select "Play as Guest" or "Get a Fortune!" to arrive at the '
                  '"Fortune Menu". \n'
                  '> Select the desired category of your fortune and '
                  'it will magically appear! \n'
                  '> If you are logged in, you may save your fortune to view from the '
                  '"Past Fortunes" menu at anytime! \n')
    msg.pack()
    btn_rule_close = tk.Button(rules_tk, text='Close', bd='5', command=rules_tk.destroy)
    btn_rule_close.pack()

    rules_tk.mainloop()

# Valerie Rudich 12/4/2023
def user_menu():
    '''Display Main Menu and Welcome Message for Authenticated Users'''
    # Initialize New Window
    user_menu_tk = Toplevel()
    user_menu_tk.title('Fortune Teller')
    user_menu_tk.geometry('650x415')
    center_window(user_menu_tk, 650, 415)

    # add label and buttons to the window
    welcome_user_message = 'Welcome Back, ' + sessionhandler.user_session['username'] + ', to the Fortune Teller Game!'
    lbl1 = Label(user_menu_tk, text=welcome_user_message)
    lbl2 = Label(user_menu_tk, text='Reveal what your future holds!')
    lbl1.pack()
    lbl2.pack()

    # add crystal ball ascii art
    crystal_ball_ascii_art(user_menu_tk)

    btn_get_frtn = Button(user_menu_tk, text='Get a Fortune', command=lambda: fortune_menu())
    btn_past_frtn = Button(user_menu_tk, text='View Past Fortune',
                           command=lambda: past_fortunes_window())

    btn_get_frtn.pack()
    btn_past_frtn.pack()

    menu_bar(user_menu_tk)
    user_menu_tk.mainloop()

# Hoi Lam Wong 11/28/2023
def login_window():
    '''This function is used for returning users'''
    # Hoi Lam Wong 12/4/2023
    def user_login():
        uname = username_login_entry.get().lower().strip()
        password = password_login_entry.get().strip()
        
        sessionhandler.login(uname, password)

        if sessionhandler.is_authenticated():
            tk.messagebox.showinfo(title=None, message='Login Successful!')
            login_tk.destroy()
            root.withdraw()
            user_menu()
        else:
            tk.messagebox.showinfo(title=None, message='Authentication Failed!')
    # Initialize New Window
    login_tk = Toplevel(root)
    login_tk.title('User Login')
    center_window(login_tk, 650, 415)

    # create new frame to contain the labels and entry boxes
    login_form = Frame(login_tk, relief=SUNKEN, borderwidth=3)
    login_form.pack(side = 'top')

    username_login_label = Label(login_form, text='Username:')
    username_login_label.grid(row=1, column=0, pady=10)

    password_login_label = Label(login_form, text='Password:')
    password_login_label.grid(row=2, column=0, pady=10)

    username_login_entry = Entry(login_form)
    username_login_entry.grid(row=1, column=2, pady=10)

    password_login_entry = Entry(login_form, show='*')
    password_login_entry.grid(row=2, column=2, pady=10)

     # Create a frame for buttons
    frm_buttons = Frame(login_tk)
    frm_buttons.pack(side=BOTTOM, pady=10)

    btn_login_submit = Button(frm_buttons, text='Login', command=lambda: user_login())
    btn_login_submit.pack(side = 'right', padx=5)

    btn_login_close = Button(frm_buttons, text='Cancel', command=login_tk.destroy)
    btn_login_close.pack(side = 'right', padx=5)

    login_tk.mainloop()

# Constance 11/27/2023, 12/5/23
def registration_window():
    ''' This function is used to create a new window that holds registration form '''
    def user_register():
        '''Method for registration() for backend
        Note: This method is part of/inside of method registration()
        '''
        # Get value from text boxes
        uname = username_entry.get()
        fname = first_name_entry.get()
        lname = last_name_entry.get()
        email = email_entry.get()
        pass1 = password_entry.get()
        pass2 = password_confirm_entry.get()

        # 8Dec Nieves, Chelsea
        # if sign_up returns true
        if sign_up(uname, fname, lname, email, pass1, pass2):
            # Call method to create a new window that contains the confirmation/error message
            tk.messagebox.showinfo(title=None, message='Registration Successful! Please Log In')
            # Destroy the registration form if successfully signed up
            registration_tk.destroy()
    # Initialize New Window
    registration_tk = Toplevel(root)
    registration_tk.geometry('650x415')
    registration_tk.title('Registration')
    center_window(registration_tk, 650, 415)

    # Create new frame to contain the labels and entry boxes
    frm_form = Frame(registration_tk, relief=SUNKEN, borderwidth=3)
    frm_form.pack(side = 'top')

    first_name_label = Label(frm_form, text='First Name:')
    first_name_label.grid(row=0, column=0)
    last_name_label = Label(frm_form, text='Last Name:')
    last_name_label.grid(row=1, column=0)
    username_label = Label(frm_form, text='Username:')
    username_label.grid(row=2, column=0)
    email_label = Label(frm_form, text='Email:')
    email_label.grid(row=3, column=0)
    password_label = Label(frm_form, text='Password:')
    password_label.grid(row=4, column=0)
    password_confirm_label = Label(frm_form, text='Confirm Password:')
    password_confirm_label.grid(row=5, column=0)

    first_name_entry = Entry(frm_form)
    first_name_entry.grid(row=0, column=1)
    last_name_entry = Entry(frm_form)
    last_name_entry.grid(row=1, column=1)
    username_entry = Entry(frm_form)
    username_entry.grid(row=2, column=1)
    email_entry = Entry(frm_form)
    email_entry.grid(row=3, column=1)
    password_entry = Entry(frm_form, show='*')
    password_entry.grid(row=4, column=1)
    password_confirm_entry = Entry(frm_form, show='*')
    password_confirm_entry.grid(row=5, column=1)

    # Added 12/10/2023 Hoi Lam, for displaying password requirement in window
    password_must_be_label = Label(frm_form, text='Password must \ncontain at least :')
    password_must_be_label.grid(row=7, column=0)
    password_requirement_label = Label(frm_form, text='\n - 12 characters\n'
                                                       ' - 1 numerical character \n'
                                                       ' - 1 lowercase character  \n'
                                                       ' - 1 uppercase character \n'
                                                       ' - 1 special character \n')
    password_requirement_label.grid(row=7, column=1)

    # Create a frame for buttons
    frm_buttons = Frame(registration_tk)
    frm_buttons.pack(side=BOTTOM, pady=10)

    btn_submit = Button(frm_buttons, text='Submit', command=user_register)
    btn_submit.pack(side='right', padx=5)
    btn_close = Button(frm_buttons, text='Cancel', command=registration_tk.destroy)
    btn_close.pack(side='right', padx=5)

    # Call to create registration_tk... END of registration TK
    registration_tk.mainloop()

# Constance 11/27/2023, 12/5/23
def fortune_menu():
    '''This menu will give the user the option to choose a category'''
    # Initialize New Window
    fortune_menu_tk = Toplevel()
    fortune_menu_tk.geometry('650x415')
    fortune_menu_tk.title('Fortune Menu')
    center_window(fortune_menu_tk, 650, 415)

    lbl = Label(fortune_menu_tk, text='Please select a category!')
    lbl.pack()

    # Create a frame for buttons
    frm_buttons = Frame(fortune_menu_tk)
    frm_buttons.pack(pady=10)

    # delcare buttons
    btn_love = Button(frm_buttons, text='Love', command=lambda: display_fortune('Love'))
    btn_career = Button(frm_buttons, text='Career', command=lambda: display_fortune('Career'))
    btn_health = Button(frm_buttons, text='Health', command=lambda: display_fortune('Health'))
    btn_general = Button(frm_buttons, text='General',
                         command=lambda: display_fortune('General'))
    btn_random = Button(frm_buttons, text='Random', command=lambda: display_fortune('Random'))

    # pack buttons to frame
    btn_love.pack()
    btn_career.pack()
    btn_health.pack()
    btn_general.pack()
    btn_random.pack()

    fortune_menu_tk.mainloop()

# Hoi Lam Wong 11/28/2023
def display_fortune(category):
    ''' Method to create a new window to display user's fortune 
    based on the category they choose in fortune menu'''
    # Hoi Lam Wong 12/4/2023
    def save_fortune_confirm_window():
        if (res := tk.messagebox.askquestion('Save Fortune', 'Do you want to save your fortune?')) == 'yes' :
            if save_fortune_to_table(category, user_fortune):
                tk.messagebox.showinfo(title=None, message='Fortune saved successfully!')
            else :
                tk.messagebox.showerror(title=None, message='Something went wrong!\n'
                                        'Unable to save fortune.')
                fortune_tk.destroy()

    user_fortune = ''
    if category == 'Love':
        user_fortune = get_love_fortune()
    elif category == 'Career':
        user_fortune = get_career_fortune()
    elif category == 'General':
        user_fortune = get_general_fortune()
    elif category == 'Health':
        user_fortune = get_health_fortune()
    elif category == 'Random':
        user_fortune = get_random_fortune()

    # Initialize New Window
    fortune_tk = Toplevel(root)
    fortune_tk.title('Fortune Menu')
    fortune_tk.geometry('650x415')
    center_window(fortune_tk, 650, 415)
    
    # Create a frame for buttons
    frm_fortune = Frame(fortune_tk, relief=SUNKEN, borderwidth=3)
    frm_fortune.pack(pady=10)

    header = f'Your {category} Fortune'
    lbl = Label(frm_fortune, text=header)
    lbl.pack()

    fortune_message = Message(frm_fortune, text=user_fortune, width = 250)
    fortune_message.pack()

    btn_fortune_new = tk.Button(fortune_tk, text='New Fortune', bd='2', command=fortune_tk.destroy)
    btn_fortune_new.pack()
    # Valerie Rudich 12/5/2023
    # adds save option only if the user is signed in
    if sessionhandler.is_authenticated():
        btn_fortune_save = tk.Button(fortune_tk, text='Save', bd='2',
                                     command=lambda: [save_fortune_confirm_window()])
        btn_fortune_save.pack()

# Hoi Lam Wong 12/4/2023
def past_fortunes_window():
    ''' Method to create new window for displaying user's past fortunes '''
    # Get username if user is logged in
    if sessionhandler.is_authenticated():
        username = sessionhandler.user_session['username']
    else:
        username = 'GUEST: Not Logged In'

    # Initialize New Window
    previous_fortunes_tk = Toplevel(root)
    previous_fortunes_tk.title('Past Fortunes')
    previous_fortunes_tk.geometry('800x415')
    center_window(previous_fortunes_tk, 800, 415)

    # Create table
    columns, data = get_previous_fortunes(username)

    tree = Treeview(previous_fortunes_tk, columns = columns, show ='headings')
    for col in columns:
        tree.heading(col, text = col)
        if col == 'Fortune':
            tree.column(col, minwidth=0, width=300)
        else:
            tree.column(col, minwidth=0, width=100, stretch=NO)
    for row in data:
        tree.insert('', 'end', values=row)
    tree.pack(fill = 'x')

    # Button for Action
    btn_close = tk.Button(previous_fortunes_tk, text='Close', bd='5',
                          command=previous_fortunes_tk.destroy)
    btn_close.pack()
   
    previous_fortunes_tk.update_idletasks()
    previous_fortunes_tk.mainloop()

def signout_window(user_menu_tk):
    ''' method to handle user sign out confirmation '''
    if (res := tk.messagebox.askquestion(title='Sign Out', message='Confirm Sign Out?')) == 'yes':
        sessionhandler.logout()
        if not sessionhandler.is_authenticated():
            tk.messagebox.showinfo(title='Success', message='Successfully Signed Out!')
            user_menu_tk.destroy()
            root.deiconify() # main will not double print content in same window
            menu_bar(root)
        else:
            tk.messagebox.showerror(title='Error', message ='Sign out failed!')
    else:
        return

# Constance Sturm 12/6/23
# Edited and Completed by Valerie Rudich 12/8/23
def menu_bar(window):
    ''' method to define menu bar '''
    # add menu bar to allow user to view rules, fortune,or exit
    menubar = Menu(window)
    window.config(menu=menubar)

    # add Rules menu and commands
    rules = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Rules', menu=rules)
    rules.add_command(label='View Rules', command=lambda: display_rules())

    # add Exit and Sign Out menu and commands
    program_exit = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Exit', menu=program_exit)
    if sessionhandler.is_authenticated():
        program_exit.add_command(label='Sign Out', command=lambda: signout_window(window))
    program_exit.add_command(label='Exit Program', command=exit)

def main_menu():
    # root window and title dimensions
    root.title('Fortune Teller')
    # geometry of the box (width x height)
    root.geometry('650x415')
    # center window
    center_window(root, 650, 415)
    # to close program using 'x' in title bar
    root.protocol("WM_DELETE_WINDOW", lambda:exit())
    root.bind("<Destroy>", None, True)

    # add label to the root window
    lbl1 = Label(root, text='Welcome to the Fortune Teller Game!')
    lbl2 = Label(root, text='Reveal what your future holds!')
    lbl1.pack()
    lbl2.pack()

    # add crystal ball ascii art
    crystal_ball_ascii_art(root)

    # Changed Buttons to include more options
    btn_play = tk.Button(root, text='Play as Guest', bd='1', command=lambda: fortune_menu())
    btn_login = tk.Button(root, text='Login', bd='1', command=lambda: login_window())
    btn_register = tk.Button(root, text='Register', bd='1', command=lambda: registration_window())

    btn_play.pack()
    btn_login.pack()
    btn_register.pack()

    # display menu
    menu_bar(root)
    # call mainloop() to display window
    root.mainloop()

def main():
    '''Display Main Menu and Welcome Message for Unauthenticated Users'''
    # call method to create db tables
    create_table()

    main_menu()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
