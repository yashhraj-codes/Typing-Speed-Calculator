from tkinter import *
import random
from tkinter import messagebox

# GLOBAL VARIABLES #
userID = 0
score = 0
timeleft = 60
count = 0
miss = 0
wpm = 0
words_slide = ''
word_concad = ''
tech_words = []
science_words = []
literature_words = []
sports_words = []
topic_window = Tk()

# MAIN FUNCTIONS #
def topic():
    topic_window.title("CHOOSE A TOPIC")
    topic_window.geometry("{}x{}+0+0".format(topic_window.winfo_screenwidth(), topic_window.winfo_screenheight()))

# Creating an opening label (fixing the undefined label issue)
opening_label = Label(topic_window, text="Welcome to the SPEED TYPING APP", font=('arial', 40, 'italic bold'), fg="navy")
opening_label.pack()

# CREATING VARIOUS TOPIC BUTTONS #
# TECH SUB-FUNCTION #
def tech():
    global tech_words
    fh = open(r"C:\Users\Akash leol\Desktop\proj\actual thing\tech.txt")
    reader = fh.readlines()
    tech_words = reader
    typing_page(tech_words)
    type_window.bind('<Return>', lambda event: start_game(event, tech_words))

tech_button = Button(topic_window, text="TECH", width=92, height=23, fg="green", bg="navy", highlightbackground="#000000", command=tech)
tech_button.grid(row=0, column=0)

# SCIENCE SUB-FUNCTION #
def science():
    global science_words
    fh = open(r'C:\Users\Akash leol\Desktop\proj\actual thing\science.txt')
    reader = fh.readlines()
    science_words = reader
    typing_page(science_words)
    type_window.bind('<Return>', lambda event: start_game(event, science_words))

science_button = Button(topic_window, text="SCIENCE", width=92, height=23, fg="blue", bg="black", highlightbackground="#000000", command=science)
science_button.grid(row=0, column=1)

# LITERATURE SUB-FUNCTION #
def lit():
    global literature_words
    fh = open(r'C:\Users\Akash leol\Desktop\proj\actual thing\literature.txt')
    reader = fh.readlines()
    literature_words = reader
    typing_page(literature_words)
    type_window.bind('<Return>', lambda event: start_game(event, literature_words))

lit_button = Button(topic_window, text="LITERATURE", width=92, height=23, fg="red", bg="orange", highlightbackground="#000000", command=lit)
lit_button.grid(row=1, column=0)

# SPORTS SUB-FUNCTION #
def sports():
    global sports_words
    fh = open(r"C:\Users\Akash leol\Desktop\proj\actual thing\sports.txt")
    reader = fh.readlines()
    sports_words = reader
    typing_page(sports_words)
    type_window.bind('<Return>', lambda event: start_game(event, sports_words))

sport_button = Button(topic_window, text="SPORTS", width=92, height=23, fg="orange", bg="green", highlightbackground="#000000", command=sports)
sport_button.grid(row=1, column=1)

# Typing Page Function
def typing_page(input_words):
    global type_window
    type_window = Tk()
    type_window.title("THIS IS A SPEED TEST!")
    type_window.geometry("{0}x{1}+0+0".format(type_window.winfo_screenwidth(), type_window.winfo_screenheight()))
    type_window.configure(bg='SkyBlue4')
    random.shuffle(input_words)

    global word_display
    word_display = Label(type_window, text=input_words[0], font=('arial', 50, 'italic bold'), bg="SkyBlue4", fg="yellow")
    word_display.place(x=525, y=250)

    score_heading = Label(type_window, text='Words Correct : ', font=('arial', 35, 'italic bold'), bg="SkyBlue4", fg="PaleTurquoise")
    score_heading.place(x=10, y=100)

    global score_display
    score_display = Label(type_window, text=score, font=('arial', 35, 'italic bold'), bg="SkyBlue4", fg="PaleTurquoise")
    score_display.place(x=80, y=180)

    # WPM
    wpm_heading = Label(type_window, text="Your WPM :", font=('arial', 25, 'italic bold'), bg="SkyBlue4", fg="PaleTurquoise")
    wpm_heading.place(x=100, y=450)

    global wpm_count
    wpm_count = Label(type_window, text=wpm, font=('arial', 25, 'italic bold'), bg="SkyBlue4", fg="PaleTurquoise")
    wpm_count.place(x=100, y=500)

    timer = Label(type_window, text='Time Left', font=('arial', 35, 'italic bold'), bg="SkyBlue4", fg="PaleTurquoise")
    timer.place(x=900, y=100)

    global time_count
    time_count = Label(type_window, text=timeleft, font=('arial', 35, 'italic bold'), bg="SkyBlue4", fg="PaleTurquoise")
    time_count.place(x=980, y=180)

    global instructions
    instructions = Label(type_window, text='Type Word And Hit Enter Button', font=('arial', 30, 'italic bold'), bg="SkyBlue4", fg="PaleTurquoise")
    instructions.place(x=420, y=450)

    global word_entry
    word_entry = Entry(type_window, font=('arial', 35, 'italic bold'), bd=10, justify='center')
    word_entry.place(x=450, y=350)
    word_entry.focus_set()

    exit_button = Button(type_window, text="EXIT", command=type_window.quit)
    exit_button.pack()

# TIME COUNT FUNCTION
def time():
    global timeleft, score, miss, wpm
    if timeleft >= 11:
        pass
    else:
        time_count.configure(fg='red')

    if timeleft > 0:
        timeleft -= 1
        time_count.configure(text=timeleft)
        time_count.after(1000, time)
    else:
        instructions.configure(text='WPM = {}'.format(wpm))
        rr = messagebox.askretrycancel('Notification', 'To Play Again Hit Retry')
        if rr:
            score = 0
            timeleft = 60
            miss = 0
            wpm = 0
            time_count.configure(text=timeleft)
            word_display.configure(text=tech_words[0])
            score_display.configure(text=score)
            wpm_count.configure(text=wpm)

# GAME FUNCTION
def start_game(event, words):
    global score, miss, wpm, word_concad
    if timeleft == 60:
        time()
    instructions.configure(text='')
    for i in range(len(word_entry.get())):
        for j in range(len(word_display['text'])):
            if word_entry.get()[i] == word_display['text'][j]:
                word_concad += word_entry.get()[i]
                wpm = ((len(word_concad) / 5) / 1)
                score_display.configure(text=score)
                wpm_count.configure(text=wpm)
            if word_entry.get() == word_display['text']:
                score += 1
            else:
                miss += 1

    random.shuffle(words)
    word_display.configure(text=words[0])
    word_entry.delete(0, END)

# SLIDING WORD FUNCTION
def sliding_words():
    global count, words_slide
    text = 'Welcome to SPEED TYPING APP'
    if count >= len(text):
        count = 0
        words_slide = ''
    words_slide += text[count]
    count += 1
    opening_label.configure(text=words_slide)  # Referring to the opening label
    topic_window.after(100, sliding_words)

# Initializing the UserID
def user():
    global userID
    userID = random.randrange(0, 999999999)

# Start the application
sliding_words()
topic_window.mainloop()
user()
