# pyPokerPro
# Lightweight python app with exercises to improve Poker skills
# GUI created with Tkinter
from tkinter import *

CURRENT_VERSION = "v0.1.0"
BACKGROUND_COLOR = '#35654d'


def tk_main_menu():
    root = Tk()

    # Variables for dynamically setting window size
    screen_max_width = root.winfo_screenwidth()  # get max screen width
    screen_max_height = root.winfo_screenheight()  # get max screen height
    window_width = int(screen_max_width * 0.5)  # set window width to 50% of screen width
    window_height = int(screen_max_height * 0.8)  # set window height to 80% of screen height
    window_x_loc = int((screen_max_width - window_width) / 2)  # get window starting x location
    window_y_loc = int((screen_max_height - window_height) / 2)  # get window starting y location

    root.geometry('%dx%d+%d+%d' % (window_width, window_height, window_x_loc, window_y_loc))  # dynamically size window
    root.title("pyPokerPro " + CURRENT_VERSION)  # Window title/name w/ current version
    root['bg'] = BACKGROUND_COLOR  # Window background color

    label1 = Label(root,
        text="pyPokerPro",
        font=("Arial", 20),
        bd=1,
        fg='white',
        bg=BACKGROUND_COLOR)
    label1.pack()
    return root


if __name__ == '__main__':
    window = tk_main_menu()
    window.mainloop()