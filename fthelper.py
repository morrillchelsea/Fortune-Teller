'''Team 3: Fortune Teller Application
Created By: Constance Sturm, Michelle Cook, Chelsea Nieves,
Valerie Rudich, and Hoi Lam Wong
University of Maryland Global Campus
CMSC 495-7382: Capstone in Computer Science
Professor David Castillo
December 12, 2023

Helper module for fortune_teller.py
'''
#Wildcard import tkinter (wildcard-import)
from tkinter import *
from loghandler import db_logger
import secrets

LOVE_FORTUNE_PATH = 'texts/love_fortune.txt'
CAREER_FORTUNE_PATH = 'texts/career_fortune.txt'
GENERAL_FORTUNE_PATH = 'texts/general_fortune.txt'
HEALTH_FORTUNE_PATH = 'texts/health_fortune.txt'

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    win.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def center_widget(widget, row, column, rowspan=1, columnspan=1):
    widget.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew")

def crystal_ball_ascii_art(win):
    '''Function to add a label with crystal ball ascii art to window win'''
    def pad_to_center(l: list, w: int) -> str:
        '''Helper Method for Manual centering ascii art'''
        padding = ' ' * (w // 2)  # a 1 char line would need at most w/2 spaces in front
        parts = [padding[0: (w - len(p)) // 2 + 1] + p for p in l]
        return '\n'.join(parts)

    crystal_ball_raw = r'''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠾⠛⠋⠉⠉⠉⠉⢙⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⣷⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣾⢇⣤⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠁⢹⣇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⣤⡙⠻⢿⣿⣿⣿⣿⣿⣋⣠⣤⡶⠟⢁⣤⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣷⣤⣈⣉⠉⠛⠛⠉⣉⣠⣤⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣾⣦⣀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢋⣠⣴⣷⠀⠀⠀⠀
    ⠀⠀⠀⠀⢿⣿⣿⣿⣷⣶⣤⣬⣭⣉⣉⣉⣩⣭⣥⣤⣶⣾⣿⣿⣿⡿⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        '''

    crystal_ball_text = pad_to_center(crystal_ball_raw.split('\n'), 60)
    Label(win, justify=LEFT, text=crystal_ball_text).pack()

def get_love_fortune():
    '''Method to parse txt file to output fortune to user
    :return: fortune'''
    try:
        fortune = []
        with open(LOVE_FORTUNE_PATH, 'r', encoding = 'utf-8') as file1:
            lines = file1.read().splitlines()
            for line in lines:
                fortune.append(line)
    except IOError as err:
        db_logger.error(err)
    return secrets.choice(fortune)

def get_career_fortune():
    '''Method to parse txt file to output fortune to user
    :return: fortune'''
    try:
        fortune = []
        with open(CAREER_FORTUNE_PATH, 'r', encoding = 'utf-8') as file1:
            lines = file1.read().splitlines()
            for line in lines:
                fortune.append(line)
    except IOError as err:
        db_logger.error(err)
    return secrets.choice(fortune)

def get_health_fortune():
    '''Method to parse txt file to output fortune to user
    :return: fortune'''
    try:
        fortune = []
        with open(HEALTH_FORTUNE_PATH, 'r', encoding = 'utf-8') as file1:
            lines = file1.read().splitlines()
            for line in lines:
                fortune.append(line)
    except IOError as err:
        db_logger.error(err)
    return secrets.choice(fortune)

def get_general_fortune():
    '''Method to parse txt file to output fortune to user
    :return: fortune'''
    try:
        fortune = []
        with open(GENERAL_FORTUNE_PATH, 'r', encoding = 'utf-8') as file1:
            lines = file1.read().splitlines()
            for line in lines:
                fortune.append(line)
    except IOError as err:
        print('Unable to find file general_fortune.txt')
        db_logger.error(err)
    return secrets.choice(fortune)

def get_random_fortune():
    '''Method to parse txt file to output fortune to user
    :return: fortune'''
    fortune = []
    try:
        # Open multiple text files
        with (
            open(LOVE_FORTUNE_PATH, 'r', encoding = 'utf-8') as file_love,
            open(GENERAL_FORTUNE_PATH, 'r', encoding = 'utf-8') as file_general,
            open(HEALTH_FORTUNE_PATH, 'r' , encoding = 'utf-8') as file_health,
            open(CAREER_FORTUNE_PATH, 'r', encoding = 'utf-8') as file_career
        ):
            # Read text files and split by line
            lines_love = file_love.read().splitlines()
            lines_general = file_general.read().splitlines()
            lines_health = file_health.read().splitlines()
            lines_career = file_career.read().splitlines()

            # Append lines to fortune
            for line in lines_love:
                fortune.append(line)
            for line in lines_general:
                fortune.append(line)
            for line in lines_health:
                fortune.append(line)
            for line in lines_career:
                fortune.append(line)
    except IOError as err:
        db_logger.error(err)
    return secrets.choice(fortune)
