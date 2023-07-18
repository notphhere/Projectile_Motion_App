import tkinter as tk
from tkinter import messagebox
from math import *
from tkinter import ttk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

# ----- CREATING GUI ---------------------------------------------------------------------------------------------------
gui = tk.Tk()
gui.title('Projectile Motion App')
# ----- GETTING SCREEN WIDTH AND HEIGHT AND MAKING GEOMETRY -----
app_width = 1125
app_height = 650
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
appx = (screen_width / 2) - (app_width / 2)
appy = (screen_height / 2) - (app_height / 2)
gui.geometry(f'{app_width}x{app_height}+{int(appx) - 110}+{int(appy) - 60}')
gui.resizable(False, False)


def first_page():
    plt.close()
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('first_page.png')
    resized_bgi = bgi.resize((app_width, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.pack()

    intro_button = tk.Button(gui, text='Introduction', height=1, width=19, font=('Grandview', 17), cursor='hand2',
                             command=intro1)
    intro_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    theory_button = tk.Button(gui, text='Theory', height=1, width=19, font=('Grandview', 17), cursor='hand2',
                              command=theory_1)
    theory_button.place(relx=0.5, rely=0.52, anchor=tk.CENTER)
    simulation_button = tk.Button(gui, text='Simulation', height=1, width=19, font=('Grandview', 17), cursor='hand2',
                                  command=simulation_page)
    simulation_button.place(relx=0.5, rely=0.64, anchor=tk.CENTER)
    quiz_button = tk.Button(gui, text='Quiz room', height=1, width=19, font=('Grandview', 17), cursor='hand2',
                            command=quiz_instruction)
    quiz_button.place(relx=0.5, rely=0.76, anchor=tk.CENTER)
    quit_button = tk.Button(gui, text='Exit', height=1, width=19, font=('Grandview', 17), cursor='hand2',
                            command=gui.destroy)
    quit_button.place(relx=0.5, rely=0.88, anchor=tk.CENTER)


def intro1():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('intro1.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), state='disabled', cursor='no')
    back_button.place(relx=0.1, rely=0.875)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.875)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro2)
    next_button.place(relx=0.745, rely=0.875)


def intro2():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('intro2.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro1)
    back_button.place(relx=0.1, rely=0.875)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.875)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro3)
    next_button.place(relx=0.745, rely=0.875)


def intro3():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('intro3.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro2)
    back_button.place(relx=0.1, rely=0.875)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.875)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro4)
    next_button.place(relx=0.745, rely=0.875)


def intro4():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('intro4.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro3)
    back_button.place(relx=0.1, rely=0.875)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.875)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro5)
    next_button.place(relx=0.745, rely=0.875)


def intro5():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('intro5.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro4)
    back_button.place(relx=0.1, rely=0.875)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.875)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro6)
    next_button.place(relx=0.745, rely=0.875)


def intro6():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('intro6.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro5)
    back_button.place(relx=0.1, rely=0.875)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.875)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro7)
    next_button.place(relx=0.745, rely=0.875)


def intro7():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('intro7.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro6)
    back_button.place(relx=0.1, rely=0.875)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.875)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro8)
    next_button.place(relx=0.745, rely=0.875)


def intro8():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('intro8.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro7)
    back_button.place(relx=0.1, rely=0.875)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.875)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro9)
    next_button.place(relx=0.745, rely=0.875)


def intro9():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('intro9.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro8)
    back_button.place(relx=0.1, rely=0.875)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.875)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro10)
    next_button.place(relx=0.745, rely=0.875)


def intro10():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('intro10.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=intro9)
    back_button.place(relx=0.1, rely=0.875)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.875)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), state='disabled', cursor='no')
    next_button.place(relx=0.745, rely=0.875)


def theory_1():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('theory_1.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), state='disabled', cursor='no')
    back_button.place(relx=0.1, rely=0.85)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.85)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_2)
    next_button.place(relx=0.745, rely=0.85)


def theory_2():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('theory_2.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_1)
    back_button.place(relx=0.1, rely=0.85)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.85)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_3)
    next_button.place(relx=0.745, rely=0.85)


def theory_3():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('theory_3.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_2)
    back_button.place(relx=0.1, rely=0.85)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.85)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_4)
    next_button.place(relx=0.745, rely=0.85)


def theory_4():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('theory_4.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_3)
    back_button.place(relx=0.1, rely=0.85)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.85)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_5)
    next_button.place(relx=0.745, rely=0.85)


def theory_5():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('theory_5.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_4)
    back_button.place(relx=0.1, rely=0.85)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.85)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_6)
    next_button.place(relx=0.745, rely=0.85)


def theory_6():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('theory_6.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_5)
    back_button.place(relx=0.1, rely=0.85)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.85)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_7)
    next_button.place(relx=0.745, rely=0.85)


def theory_7():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('theory_7.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_6)
    back_button.place(relx=0.1, rely=0.85)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.85)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_8)
    next_button.place(relx=0.745, rely=0.85)


def theory_8():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('theory_8.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_7)
    back_button.place(relx=0.1, rely=0.85)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.85)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_9)
    next_button.place(relx=0.745, rely=0.85)


def theory_9():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('theory_9.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    back_button = tk.Button(gui, text='Back', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=theory_8)
    back_button.place(relx=0.1, rely=0.85)
    home_button = tk.Button(gui, text='Homepage', height=2, width=15, font=('Helvetica', 15), cursor='hand2',
                            command=first_page)
    home_button.place(relx=0.4225, rely=0.85)
    next_button = tk.Button(gui, text='Next', height=2, width=15, font=('Helvetica', 15), state='disabled', cursor='no')
    next_button.place(relx=0.745, rely=0.85)


def quiz_instruction():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('quiz_rules1.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    start_image = Image.open('start_test.png')
    resized_start = start_image.resize((225, 90), Image.ANTIALIAS)
    new_start_image = ImageTk.PhotoImage(resized_start)
    start_button = tk.Button(gui, image=new_start_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                             command=quiz_one, activebackground='white')
    start_button.image = new_start_image
    start_button.place(relx=0.4, rely=0.65)

    home_image = Image.open('home_button.png')
    resized_home = home_image.resize((70, 70), Image.ANTIALIAS)
    new_home_image = ImageTk.PhotoImage(resized_home)
    home_button = tk.Button(gui, image=new_home_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                            command=first_page, activebackground='white')
    home_button.image = new_home_image
    home_button.place(relx=0.007, rely=0.01)


def quiz_one():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('q1new.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    def selection():
        selected = var.get()
        if selected == 1 or selected == 3 or selected == 4:
            messagebox.showerror(title="Wrong answer", message="Sorry, you got the wrong answer. Please try again.")
        elif selected == 2:
            submit_button.config(state='disabled')
            submit_button.config(cursor='no')
            next_button.config(state='normal')
            next_button.config(cursor='hand2')
            r1.config(state='disabled', cursor='no')
            r2.config(state='disabled', cursor='no')
            r3.config(state='disabled', cursor='no')
            r4.config(state='disabled', cursor='no')
            messagebox.showinfo(title="Correct answer", message="Congrats! You got it right. Please proceed to the "
                                                                "next question.")
        else:
            messagebox.showwarning(title="Invalid input", message="Please choose an answer.")

    var = tk.IntVar()
    r1 = tk.Radiobutton(gui, text="   Hitting a person with your palm", variable=var, value=1,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r1.place(relx=0.19, rely=0.4)
    r2 = tk.Radiobutton(gui, text="   Throwing a basketball into the hoop", variable=var, value=2,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r2.place(relx=0.19, rely=0.5)
    r3 = tk.Radiobutton(gui, text="   Opening a projector", variable=var, value=3,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r3.place(relx=0.19, rely=0.6)
    r4 = tk.Radiobutton(gui, text="   A butterfly flying from one place to another", variable=var, value=4,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r4.place(relx=0.19, rely=0.7)

    submit_image = Image.open('check.png')
    resized_submit = submit_image.resize((200, 70), Image.ANTIALIAS)
    new_submit_image = ImageTk.PhotoImage(resized_submit)
    submit_button = tk.Button(gui, image=new_submit_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                              command=selection, activebackground='white')
    submit_button.image = new_submit_image
    submit_button.place(relx=0.78, rely=0.05)
    prev_image = Image.open('prev_image.png')
    resized_prev = prev_image.resize((200, 75), Image.ANTIALIAS)
    new_prev_image = ImageTk.PhotoImage(resized_prev)
    prev_button = tk.Button(gui, image=new_prev_image, borderwidth=0, bg='white', relief='flat', state='disabled',
                            cursor='no', activebackground='white')
    prev_button.image = new_prev_image
    prev_button.place(relx=0.012, rely=0.818)
    next_image = Image.open('next_button.png')
    resized_next = next_image.resize((210, 80), Image.ANTIALIAS)
    new_next_image = ImageTk.PhotoImage(resized_next)
    next_button = tk.Button(gui, image=new_next_image, borderwidth=0, bg='white', relief='flat', cursor='no',
                            state='disabled', command=quiz_two, activebackground='white')
    next_button.image = new_next_image
    next_button.place(relx=0.8, rely=0.815)


def quiz_two():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('q2new.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    def selection():
        selected = var.get()
        if selected == 2 or selected == 3 or selected == 4:
            messagebox.showerror(title="Wrong answer", message="Sorry, you got the wrong answer. Please try again.")
        elif selected == 1:
            submit_button.config(state='disabled')
            submit_button.config(cursor='no')
            next_button.config(state='normal')
            next_button.config(cursor='hand2')
            r1.config(state='disabled', cursor='no')
            r2.config(state='disabled', cursor='no')
            r3.config(state='disabled', cursor='no')
            r4.config(state='disabled', cursor='no')
            messagebox.showinfo(title="Correct answer", message="Congrats! You got it right. Please proceed to the "
                                                                "next question.")
        else:
            messagebox.showwarning(title="Invalid input", message="Please choose an answer.")

    var = tk.IntVar()
    r1 = tk.Radiobutton(gui, text="   Trajectory", variable=var, value=1,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r1.place(relx=0.19, rely=0.4)
    r2 = tk.Radiobutton(gui, text="   Range", variable=var, value=2,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r2.place(relx=0.19, rely=0.5)
    r3 = tk.Radiobutton(gui, text="   Amplitude", variable=var, value=3,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r3.place(relx=0.19, rely=0.6)
    r4 = tk.Radiobutton(gui, text="   None of the above", variable=var, value=4,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r4.place(relx=0.19, rely=0.7)

    submit_image = Image.open('check.png')
    resized_submit = submit_image.resize((200, 70), Image.ANTIALIAS)
    new_submit_image = ImageTk.PhotoImage(resized_submit)
    submit_button = tk.Button(gui, image=new_submit_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                              command=selection, activebackground='white')
    submit_button.image = new_submit_image
    submit_button.place(relx=0.78, rely=0.05)
    prev_image = Image.open('prev_image.png')
    resized_prev = prev_image.resize((200, 75), Image.ANTIALIAS)
    new_prev_image = ImageTk.PhotoImage(resized_prev)
    prev_button = tk.Button(gui, image=new_prev_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                            activebackground='white', command=quiz_one)
    prev_button.image = new_prev_image
    prev_button.place(relx=0.012, rely=0.818)
    next_image = Image.open('next_button.png')
    resized_next = next_image.resize((210, 80), Image.ANTIALIAS)
    new_next_image = ImageTk.PhotoImage(resized_next)
    next_button = tk.Button(gui, image=new_next_image, borderwidth=0, bg='white', relief='flat', cursor='no',
                            state='disabled', command=quiz_three, activebackground='white')
    next_button.image = new_next_image
    next_button.place(relx=0.8, rely=0.815)


def quiz_three():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('q3new.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    def selection():
        selected = var.get()
        if selected == 1 or selected == 2 or selected == 4:
            messagebox.showerror(title="Wrong answer", message="Sorry, you got the wrong answer. Please try again.")
        elif selected == 3:
            submit_button.config(state='disabled')
            submit_button.config(cursor='no')
            next_button.config(state='normal')
            next_button.config(cursor='hand2')
            r1.config(state='disabled', cursor='no')
            r2.config(state='disabled', cursor='no')
            r3.config(state='disabled', cursor='no')
            r4.config(state='disabled', cursor='no')
            messagebox.showinfo(title="Correct answer", message="Congrats! You got it right. Please proceed to the "
                                                                "next question.")
        else:
            messagebox.showwarning(title="Invalid input", message="Please choose an answer.")

    var = tk.IntVar()
    r1 = tk.Radiobutton(gui, text="   100 m/s", variable=var, value=1,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r1.place(relx=0.19, rely=0.4)
    r2 = tk.Radiobutton(gui, text="   Max velocity", variable=var, value=2,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r2.place(relx=0.19, rely=0.5)
    r3 = tk.Radiobutton(gui, text="   0 m/s", variable=var, value=3,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r3.place(relx=0.19, rely=0.6)
    r4 = tk.Radiobutton(gui, text="   None of the above", variable=var, value=4,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r4.place(relx=0.19, rely=0.7)

    submit_image = Image.open('check.png')
    resized_submit = submit_image.resize((200, 70), Image.ANTIALIAS)
    new_submit_image = ImageTk.PhotoImage(resized_submit)
    submit_button = tk.Button(gui, image=new_submit_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                              command=selection, activebackground='white')
    submit_button.image = new_submit_image
    submit_button.place(relx=0.78, rely=0.05)
    prev_image = Image.open('prev_image.png')
    resized_prev = prev_image.resize((200, 75), Image.ANTIALIAS)
    new_prev_image = ImageTk.PhotoImage(resized_prev)
    prev_button = tk.Button(gui, image=new_prev_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                            activebackground='white', command=quiz_two)
    prev_button.image = new_prev_image
    prev_button.place(relx=0.012, rely=0.818)
    next_image = Image.open('next_button.png')
    resized_next = next_image.resize((210, 80), Image.ANTIALIAS)
    new_next_image = ImageTk.PhotoImage(resized_next)
    next_button = tk.Button(gui, image=new_next_image, borderwidth=0, bg='white', relief='flat', cursor='no',
                            state='disabled', command=quiz_four, activebackground='white')
    next_button.image = new_next_image
    next_button.place(relx=0.8, rely=0.815)


def quiz_four():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('q4new.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    def selection():
        selected = var.get()
        if selected == 1 or selected == 2 or selected == 4:
            messagebox.showerror(title="Wrong answer", message="Sorry, you got the wrong answer. Please try again.")
        elif selected == 3:
            submit_button.config(state='disabled')
            submit_button.config(cursor='no')
            next_button.config(state='normal')
            next_button.config(cursor='hand2')
            r1.config(state='disabled', cursor='no')
            r2.config(state='disabled', cursor='no')
            r3.config(state='disabled', cursor='no')
            r4.config(state='disabled', cursor='no')
            messagebox.showinfo(title="Correct answer", message="Congrats! You got it right. Please proceed to the "
                                                                "next question.")
        else:
            messagebox.showwarning(title="Invalid input", message="Please choose an answer.")

    var = tk.IntVar()
    r1 = tk.Radiobutton(gui, text="   Both cannonball will not stop moving", variable=var, value=1,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r1.place(relx=0.19, rely=0.4)
    r2 = tk.Radiobutton(gui, text="   The 45° cannonball", variable=var, value=2,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r2.place(relx=0.19, rely=0.5)
    r3 = tk.Radiobutton(gui, text="   The 60° cannonball", variable=var, value=3,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r3.place(relx=0.19, rely=0.6)
    r4 = tk.Radiobutton(gui, text="   The maximum height of both will be the same", variable=var, value=4,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r4.place(relx=0.19, rely=0.7)

    submit_image = Image.open('check.png')
    resized_submit = submit_image.resize((200, 70), Image.ANTIALIAS)
    new_submit_image = ImageTk.PhotoImage(resized_submit)
    submit_button = tk.Button(gui, image=new_submit_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                              command=selection, activebackground='white')
    submit_button.image = new_submit_image
    submit_button.place(relx=0.78, rely=0.05)
    prev_image = Image.open('prev_image.png')
    resized_prev = prev_image.resize((200, 75), Image.ANTIALIAS)
    new_prev_image = ImageTk.PhotoImage(resized_prev)
    prev_button = tk.Button(gui, image=new_prev_image, borderwidth=0, bg='white', relief='flat',
                            cursor='hand2', activebackground='white', command=quiz_three)
    prev_button.image = new_prev_image
    prev_button.place(relx=0.012, rely=0.818)
    next_image = Image.open('next_button.png')
    resized_next = next_image.resize((210, 80), Image.ANTIALIAS)
    new_next_image = ImageTk.PhotoImage(resized_next)
    next_button = tk.Button(gui, image=new_next_image, borderwidth=0, bg='white', relief='flat', cursor='no',
                            state='disabled', command=quiz_five, activebackground='white')
    next_button.image = new_next_image
    next_button.place(relx=0.8, rely=0.815)


def quiz_five():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('q5new.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    def selection():
        selected = var.get()
        if selected == 1 or selected == 2 or selected == 4:
            messagebox.showerror(title="Wrong answer", message="Sorry, you got the wrong answer. Please try again.")
        elif selected == 3:
            submit_button.config(state='disabled')
            submit_button.config(cursor='no')
            next_button.config(state='normal')
            next_button.config(cursor='hand2')
            r1.config(state='disabled', cursor='no')
            r2.config(state='disabled', cursor='no')
            r3.config(state='disabled', cursor='no')
            r4.config(state='disabled', cursor='no')
            messagebox.showinfo(title="Correct answer", message="Congrats! You got it right. Please proceed to the "
                                                                "next question.")
        else:
            messagebox.showwarning(title="Invalid input", message="Please choose an answer.")

    var = tk.IntVar()
    r1 = tk.Radiobutton(gui, text="   Depends on its acceleration in the x-direction", variable=var, value=1,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r1.place(relx=0.19, rely=0.4)
    r2 = tk.Radiobutton(gui, text="   Keep changing", variable=var, value=2,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r2.place(relx=0.19, rely=0.5)
    r3 = tk.Radiobutton(gui, text="   Kept constant", variable=var, value=3,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r3.place(relx=0.19, rely=0.6)
    r4 = tk.Radiobutton(gui, text="   A projectile has no horizontal velocity", variable=var, value=4,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r4.place(relx=0.19, rely=0.7)

    submit_image = Image.open('check.png')
    resized_submit = submit_image.resize((200, 70), Image.ANTIALIAS)
    new_submit_image = ImageTk.PhotoImage(resized_submit)
    submit_button = tk.Button(gui, image=new_submit_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                              command=selection, activebackground='white')
    submit_button.image = new_submit_image
    submit_button.place(relx=0.78, rely=0.05)
    prev_image = Image.open('prev_image.png')
    resized_prev = prev_image.resize((200, 75), Image.ANTIALIAS)
    new_prev_image = ImageTk.PhotoImage(resized_prev)
    prev_button = tk.Button(gui, image=new_prev_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                            activebackground='white', command=quiz_four)
    prev_button.image = new_prev_image
    prev_button.place(relx=0.012, rely=0.818)
    next_image = Image.open('next_button.png')
    resized_next = next_image.resize((210, 80), Image.ANTIALIAS)
    new_next_image = ImageTk.PhotoImage(resized_next)
    next_button = tk.Button(gui, image=new_next_image, borderwidth=0, bg='white', relief='flat', cursor='no',
                            state='disabled', command=quiz_six, activebackground='white')
    next_button.image = new_next_image
    next_button.place(relx=0.8, rely=0.815)


def quiz_six():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('q6new.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    def selection():
        selected = var.get()
        if selected == 2 or selected == 3 or selected == 4:
            messagebox.showerror(title="Wrong answer", message="Sorry, you got the wrong answer. Please try again.")
        elif selected == 1:
            submit_button.config(state='disabled')
            submit_button.config(cursor='no')
            next_button.config(state='normal')
            next_button.config(cursor='hand2')
            r1.config(state='disabled', cursor='no')
            r2.config(state='disabled', cursor='no')
            r3.config(state='disabled', cursor='no')
            r4.config(state='disabled', cursor='no')
            messagebox.showinfo(title="Correct answer", message="Congrats! You got it right. Please proceed to the "
                                                                "next question.")
        else:
            messagebox.showwarning(title="Invalid input", message="Please choose an answer.")

    var = tk.IntVar()
    r1 = tk.Radiobutton(gui, text="   3.64 m", variable=var, value=1,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r1.place(relx=0.19, rely=0.4)
    r2 = tk.Radiobutton(gui, text="   4.55 m", variable=var, value=2,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r2.place(relx=0.19, rely=0.5)
    r3 = tk.Radiobutton(gui, text="   10.52 m", variable=var, value=3,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r3.place(relx=0.19, rely=0.6)
    r4 = tk.Radiobutton(gui, text="   11.23 m", variable=var, value=4,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r4.place(relx=0.19, rely=0.7)

    submit_image = Image.open('check.png')
    resized_submit = submit_image.resize((200, 70), Image.ANTIALIAS)
    new_submit_image = ImageTk.PhotoImage(resized_submit)
    submit_button = tk.Button(gui, image=new_submit_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                              command=selection, activebackground='white')
    submit_button.image = new_submit_image
    submit_button.place(relx=0.78, rely=0.05)
    prev_image = Image.open('prev_image.png')
    resized_prev = prev_image.resize((200, 75), Image.ANTIALIAS)
    new_prev_image = ImageTk.PhotoImage(resized_prev)
    prev_button = tk.Button(gui, image=new_prev_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                            activebackground='white', command=quiz_five)
    prev_button.image = new_prev_image
    prev_button.place(relx=0.012, rely=0.818)
    next_image = Image.open('next_button.png')
    resized_next = next_image.resize((210, 80), Image.ANTIALIAS)
    new_next_image = ImageTk.PhotoImage(resized_next)
    next_button = tk.Button(gui, image=new_next_image, borderwidth=0, bg='white', relief='flat', cursor='no',
                            state='disabled', command=quiz_seven, activebackground='white')
    next_button.image = new_next_image
    next_button.place(relx=0.8, rely=0.815)


def quiz_seven():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('q7new.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    def selection():
        selected = var.get()
        if selected == 1 or selected == 3 or selected == 4:
            messagebox.showerror(title="Wrong answer", message="Sorry, you got the wrong answer. Please try again.")
        elif selected == 2:
            submit_button.config(state='disabled')
            submit_button.config(cursor='no')
            next_button.config(state='normal')
            next_button.config(cursor='hand2')
            r1.config(state='disabled', cursor='no')
            r2.config(state='disabled', cursor='no')
            r3.config(state='disabled', cursor='no')
            r4.config(state='disabled', cursor='no')
            messagebox.showinfo(title="Correct answer", message="Congrats! You got it right. Please proceed to the "
                                                                "next question.")
        else:
            messagebox.showwarning(title="Invalid input", message="Please choose an answer.")

    var = tk.IntVar()
    r1 = tk.Radiobutton(gui, text="   0.68 s", variable=var, value=1,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r1.place(relx=0.19, rely=0.4)
    r2 = tk.Radiobutton(gui, text="   1.16 s", variable=var, value=2,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r2.place(relx=0.19, rely=0.5)
    r3 = tk.Radiobutton(gui, text="   2.54 s", variable=var, value=3,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r3.place(relx=0.19, rely=0.6)
    r4 = tk.Radiobutton(gui, text="   3.97 s", variable=var, value=4,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r4.place(relx=0.19, rely=0.7)

    submit_image = Image.open('check.png')
    resized_submit = submit_image.resize((200, 70), Image.ANTIALIAS)
    new_submit_image = ImageTk.PhotoImage(resized_submit)
    submit_button = tk.Button(gui, image=new_submit_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                              command=selection, activebackground='white')
    submit_button.image = new_submit_image
    submit_button.place(relx=0.78, rely=0.05)
    prev_image = Image.open('prev_image.png')
    resized_prev = prev_image.resize((200, 75), Image.ANTIALIAS)
    new_prev_image = ImageTk.PhotoImage(resized_prev)
    prev_button = tk.Button(gui, image=new_prev_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                            activebackground='white', command=quiz_six)
    prev_button.image = new_prev_image
    prev_button.place(relx=0.012, rely=0.818)
    next_image = Image.open('next_button.png')
    resized_next = next_image.resize((210, 80), Image.ANTIALIAS)
    new_next_image = ImageTk.PhotoImage(resized_next)
    next_button = tk.Button(gui, image=new_next_image, borderwidth=0, bg='white', relief='flat', cursor='no',
                            state='disabled', command=quiz_eight, activebackground='white')
    next_button.image = new_next_image
    next_button.place(relx=0.8, rely=0.815)


def quiz_eight():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('q8new.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    def selection():
        selected = var.get()
        if selected == 1 or selected == 2 or selected == 3:
            messagebox.showerror(title="Wrong answer", message="Sorry, you got the wrong answer. Please try again.")
        elif selected == 4:
            submit_button.config(state='disabled')
            submit_button.config(cursor='no')
            next_button.config(state='normal')
            next_button.config(cursor='hand2')
            r1.config(state='disabled', cursor='no')
            r2.config(state='disabled', cursor='no')
            r3.config(state='disabled', cursor='no')
            r4.config(state='disabled', cursor='no')
            messagebox.showinfo(title="Correct answer", message="Congrats! You got it right. Please proceed to the "
                                                                "next question.")
        else:
            messagebox.showwarning(title="Invalid input", message="Please choose an answer.")

    var = tk.IntVar()
    r1 = tk.Radiobutton(gui, text="   20.6m/s < v² < 22.3/s", variable=var, value=1,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r1.place(relx=0.19, rely=0.4)
    r2 = tk.Radiobutton(gui, text="   10.2m/s < v² < 15.2m/s", variable=var, value=2,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r2.place(relx=0.19, rely=0.5)
    r3 = tk.Radiobutton(gui, text="   16.4m/s < v² < 17.6m/s", variable=var, value=3,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r3.place(relx=0.19, rely=0.6)
    r4 = tk.Radiobutton(gui, text="   18.4m/s < v² < 21.2m/s", variable=var, value=4,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r4.place(relx=0.19, rely=0.7)

    submit_image = Image.open('check.png')
    resized_submit = submit_image.resize((200, 70), Image.ANTIALIAS)
    new_submit_image = ImageTk.PhotoImage(resized_submit)
    submit_button = tk.Button(gui, image=new_submit_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                              command=selection, activebackground='white')
    submit_button.image = new_submit_image
    submit_button.place(relx=0.78, rely=0.05)
    prev_image = Image.open('prev_image.png')
    resized_prev = prev_image.resize((200, 75), Image.ANTIALIAS)
    new_prev_image = ImageTk.PhotoImage(resized_prev)
    prev_button = tk.Button(gui, image=new_prev_image, borderwidth=0, bg='white', relief='flat',
                            cursor='hand2', activebackground='white', command=quiz_seven)
    prev_button.image = new_prev_image
    prev_button.place(relx=0.012, rely=0.818)
    next_image = Image.open('next_button.png')
    resized_next = next_image.resize((210, 80), Image.ANTIALIAS)
    new_next_image = ImageTk.PhotoImage(resized_next)
    next_button = tk.Button(gui, image=new_next_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                            command=quiz_nine, activebackground='white')
    next_button.image = new_next_image
    next_button.place(relx=0.8, rely=0.815)


def quiz_nine():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('q9new.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    def selection():
        selected = var.get()
        if selected == 2 or selected == 1 or selected == 3:
            messagebox.showerror(title="Wrong answer", message="Sorry, you got the wrong answer. Please try again.")
        elif selected == 4:
            submit_button.config(state='disabled')
            submit_button.config(cursor='no')
            next_button.config(state='normal')
            next_button.config(cursor='hand2')
            r1.config(state='disabled', cursor='no')
            r2.config(state='disabled', cursor='no')
            r3.config(state='disabled', cursor='no')
            r4.config(state='disabled', cursor='no')
            messagebox.showinfo(title="Correct answer",
                                message="Congrats! You got it right. Please proceed to the "
                                        "next question.")
        else:
            messagebox.showwarning(title="Invalid input", message="Please choose an answer.")

    var = tk.IntVar()
    r1 = tk.Radiobutton(gui, text="   10.65 m/s", variable=var, value=1,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r1.place(relx=0.19, rely=0.4)
    r2 = tk.Radiobutton(gui, text="   16.5 m/s", variable=var, value=2,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r2.place(relx=0.19, rely=0.5)
    r3 = tk.Radiobutton(gui, text="   17.2 m/s", variable=var, value=3,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r3.place(relx=0.19, rely=0.6)
    r4 = tk.Radiobutton(gui, text="   18.3 m/s", variable=var, value=4, font=('Grandview', 17),
                        bg='white', cursor='hand2', activebackground='white')
    r4.place(relx=0.19, rely=0.7)

    submit_image = Image.open('check.png')
    resized_submit = submit_image.resize((200, 70), Image.ANTIALIAS)
    new_submit_image = ImageTk.PhotoImage(resized_submit)
    submit_button = tk.Button(gui, image=new_submit_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                              command=selection, activebackground='white')
    submit_button.image = new_submit_image
    submit_button.place(relx=0.78, rely=0.05)
    prev_image = Image.open('prev_image.png')
    resized_prev = prev_image.resize((200, 75), Image.ANTIALIAS)
    new_prev_image = ImageTk.PhotoImage(resized_prev)
    prev_button = tk.Button(gui, image=new_prev_image, borderwidth=0, bg='white', relief='flat',
                            cursor='hand2', activebackground='white', command=quiz_eight)
    prev_button.image = new_prev_image
    prev_button.place(relx=0.012, rely=0.818)
    next_image = Image.open('next_button.png')
    resized_next = next_image.resize((210, 80), Image.ANTIALIAS)
    new_next_image = ImageTk.PhotoImage(resized_next)
    next_button = tk.Button(gui, image=new_next_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                            command=quiz_ten, activebackground='white')
    next_button.image = new_next_image
    next_button.place(relx=0.8, rely=0.815)


def quiz_ten():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('q10new.png')
    resized_bgi = bgi.resize((1140, app_height))
    bgi = ImageTk.PhotoImage(resized_bgi)
    bgi_label = tk.Label(image=bgi)
    bgi_label.image = bgi
    bgi_label.place(relx=-0.015, rely=0)

    def selection():
        selected = var.get()
        if selected == 2 or selected == 3 or selected == 1:
            messagebox.showerror(title="Wrong answer", message="Sorry, you got the wrong answer. Please try again.")
        elif selected == 4:
            submit_button.config(state='disabled')
            submit_button.config(cursor='no')
            next_button.config(state='normal')
            next_button.config(cursor='hand2')
            r1.config(state='disabled', cursor='no')
            r2.config(state='disabled', cursor='no')
            r3.config(state='disabled', cursor='no')
            r4.config(state='disabled', cursor='no')
            messagebox.showinfo(title="Correct answer",
                                message="Congrats! You got it right. This is the end of the quiz."
                                        " Hope you've enjoyed it. 😁")
        else:
            messagebox.showwarning(title="Invalid input", message="Please choose an answer.")

    var = tk.IntVar()
    r1 = tk.Radiobutton(gui, text="   A projectile's v_x changes with gravity while v_y remains constant", variable=var,
                        value=1,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r1.place(relx=0.19, rely=0.4)
    r2 = tk.Radiobutton(gui, text="   Both v_x and v_y are constants", variable=var, value=2,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r2.place(relx=0.19, rely=0.5)
    r3 = tk.Radiobutton(gui, text="   A projectile has no acceleration in all directions", variable=var, value=3,
                        font=('Grandview', 17), bg='white', cursor='hand2', activebackground='white')
    r3.place(relx=0.19, rely=0.6)
    r4 = tk.Radiobutton(gui, text="   It has vertical acceleration and constant horizontal velocity",
                        variable=var, value=4, font=('Grandview', 17),
                        bg='white', cursor='hand2', activebackground='white')
    r4.place(relx=0.19, rely=0.7)

    submit_image = Image.open('check.png')
    resized_submit = submit_image.resize((200, 70), Image.ANTIALIAS)
    new_submit_image = ImageTk.PhotoImage(resized_submit)
    submit_button = tk.Button(gui, image=new_submit_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                              command=selection, activebackground='white')
    submit_button.image = new_submit_image
    submit_button.place(relx=0.78, rely=0.05)
    prev_image = Image.open('prev_image.png')
    resized_prev = prev_image.resize((200, 75), Image.ANTIALIAS)
    new_prev_image = ImageTk.PhotoImage(resized_prev)
    prev_button = tk.Button(gui, image=new_prev_image, borderwidth=0, bg='white', relief='flat', cursor='hand2',
                            activebackground='white', command=quiz_nine)
    prev_button.image = new_prev_image
    prev_button.place(relx=0.012, rely=0.818)
    next_image = Image.open('next_button.png')
    resized_next = next_image.resize((210, 80), Image.ANTIALIAS)
    new_next_image = ImageTk.PhotoImage(resized_next)
    next_button = tk.Button(gui, image=new_next_image, borderwidth=0, bg='white', relief='flat', cursor='no',
                            state='disabled', command=q_last, activebackground='white')
    next_button.image = new_next_image
    next_button.place(relx=0.8, rely=0.815)


def q_last():
    for widgets in gui.winfo_children():
        widgets.destroy()
    bgi = Image.open('last_page_quiz.png')
    resized_bgi = bgi.resize((1140, 625))
    bgi = ImageTk.PhotoImage(resized_bgi)
    click_button = tk.Button(gui, image=bgi, borderwidth=0, cursor='star', command=first_page, activebackground='white')
    click_button.image = bgi
    click_button.pack(side=tk.TOP)
    label = ttk.Label(gui, text='Click the image to return to homepage')
    label.pack(side=tk.BOTTOM, anchor=tk.CENTER)


def simulation_page():
    plt.close()
    for widgets in gui.winfo_children():
        widgets.destroy()

    def calculated():
        if planet_menu.cget("text") != "Planet":
            planet_name = planet_menu.cget("text")
            if planet_name == "Mercury":
                g = 3.7
            elif planet_name == "Venus":
                g = 8.87
            elif planet_name == "Earth":
                g = 9.81
            elif planet_name == "Moon":
                g = 1.62
            elif planet_name == "Mars":
                g = 3.721
            elif planet_name == "Jupiter":
                g = 24.79
            elif planet_name == "Saturn":
                g = 10.44
            elif planet_name == "Uranus":
                g = 8.87
            elif planet_name == "Neptune":
                g = 11.15
            else:
                g = 0.62

            u_ = float(u_entry.get())
            theta = float(angle_entry.get())
            ini_h = float(i_h_entry.get())
            u_x = u_ * cos(theta * pi / 180)
            u_y = u_ * sin(theta * pi / 180)

            def calculate_time():
                time_output.config(state='normal')
                time_output.delete(0, "end")
                time_output.config(state='disabled')
                t = (u_y + sqrt((u_y ** 2) + 2 * g * ini_h)) / g
                t_rounded = round(t, 2)
                time_output.config(state='normal')
                time_output.insert(0, str(t_rounded) + " s")
                time_output.config(state='disabled')

            def calculate_distance_travelled():
                displacement_output.config(state='normal')
                displacement_output.delete(0, "end")
                displacement_output.config(state='disabled')
                distance = u_x * ((u_y + sqrt((u_y ** 2) + 2 * g * ini_h)) / g)
                distance_rounded = round(distance, 2)
                displacement_output.config(state='normal')
                displacement_output.insert(0, str(distance_rounded) + " m")
                displacement_output.config(state='disabled')

            def calculate_max_height():
                max_height_output.config(state='normal')
                max_height_output.delete(0, "end")
                max_height_output.config(state='disabled')
                m_height = ini_h + ((u_y ** 2) / (2 * g))
                m_height_rounded = round(m_height, 2)
                max_height_output.config(state='normal')
                max_height_output.insert(0, str(m_height_rounded) + " m")
                max_height_output.config(state='disabled')

            def calculate_ux():
                u_x_output.config(state='normal')
                u_x_output.delete(0, "end")
                u_x_output.config(state='disabled')
                u_x_rounded = round(u_x, 2)
                u_x_output.config(state='normal')
                u_x_output.insert(0, str(u_x_rounded) + " m/s")
                u_x_output.config(state='disabled')

            def calculate_uy():
                u_y_output.config(state='normal')
                u_y_output.delete(0, "end")
                u_y_output.config(state='disabled')
                u_y_rounded = round(u_y, 2)
                u_y_output.config(state='normal')
                u_y_output.insert(0, str(u_y_rounded) + " m/s")
                u_y_output.config(state='disabled')

            def calculate_g():
                g_output.config(state='normal')
                g_output.delete(0, "end")
                g_output.config(state='disabled')
                g_output.config(state='normal')
                g_output.insert(0, str(g) + " m/s\N{SUPERSCRIPT TWO}")
                g_output.config(state='disabled')

            def calculate_energy():
                max_energy_entry.config(state='normal')
                max_energy_entry.delete(0, "end")
                max_energy_entry.config(state='disabled')
                max_energy = m * g * (ini_h + ((u_y ** 2) / (2 * g)))
                max_energy_rounded = round(max_energy, 2)
                max_energy_entry.config(state='normal')
                max_energy_entry.insert(0, str(max_energy_rounded) + " J")
                max_energy_entry.config(state='disabled')

            if mass_entry.get() > 0:
                m = float(mass_entry.get())
                calculate_time()
                calculate_distance_travelled()
                calculate_max_height()
                calculate_ux()
                calculate_uy()
                calculate_g()
                calculate_energy()
            else:
                messagebox.showwarning(title="Invalid input", message="Mass must be a positive value.")
        else:
            messagebox.showwarning(title="No planet detected", message="Please choose a planet before continuing.")

    def instant_to_zero():
        distance_instant_entry.config(state='normal')
        distance_instant_entry.delete(0, "end")
        distance_instant_entry.config(state='disabled')
        height_instant_entry.config(state='normal')
        height_instant_entry.delete(0, "end")
        height_instant_entry.config(state='disabled')
        velocity_instant_entry.config(state='normal')
        velocity_instant_entry.delete(0, "end")
        velocity_instant_entry.config(state='disabled')
        pe_instant_entry.config(state='normal')
        pe_instant_entry.delete(0, "end")
        pe_instant_entry.config(state='disabled')
        ke_instant_entry.config(state='normal')
        ke_instant_entry.delete(0, "end")
        ke_instant_entry.config(state='disabled')
        velocity_instant_entry.config(state='normal')
        velocity_instant_entry.delete(0, "end")
        velocity_instant_entry.config(state='disabled')
        distance_instant_entry.config(state='normal')
        distance_instant_entry.insert(0, " —")
        distance_instant_entry.config(state='disabled')
        height_instant_entry.config(state='normal')
        height_instant_entry.insert(0, " —")
        height_instant_entry.config(state='disabled')
        velocity_instant_entry.config(state='normal')
        velocity_instant_entry.insert(0, " —")
        velocity_instant_entry.config(state='disabled')
        pe_instant_entry.config(state='normal')
        pe_instant_entry.insert(0, " —")
        pe_instant_entry.config(state='disabled')
        ke_instant_entry.config(state='normal')
        ke_instant_entry.insert(0, " —")
        ke_instant_entry.config(state='disabled')

    def instant_to_max():
        planet_name = planet_menu.cget("text")
        if planet_name == "Mercury":
            g = 3.7
        elif planet_name == "Venus":
            g = 8.87
        elif planet_name == "Earth":
            g = 9.807
        elif planet_name == "Moon":
            g = 1.62
        elif planet_name == "Mars":
            g = 3.721
        elif planet_name == "Jupiter":
            g = 24.79
        elif planet_name == "Saturn":
            g = 10.44
        elif planet_name == "Uranus":
            g = 8.87
        elif planet_name == "Neptune":
            g = 11.15
        else:
            g = 0.62

        u_ = float(u_entry.get())
        theta = float(angle_entry.get())
        ini_h = float(i_h_entry.get())
        u_x = u_ * cos(theta * pi / 180)
        u_y = u_ * sin(theta * pi / 180)

        def calculate_distance_travelled():
            distance_instant_entry.config(state='normal')
            distance_instant_entry.delete(0, "end")
            distance_instant_entry.config(state='disabled')
            distance = u_x * ((u_y + sqrt((u_y ** 2) + 2 * g * ini_h)) / g)
            distance_rounded = round(distance, 2)
            distance_instant_entry.config(state='normal')
            distance_instant_entry.insert(0, str(distance_rounded) + " m")
            distance_instant_entry.config(state='disabled')

        def zero_height():
            height_instant_entry.config(state='normal')
            height_instant_entry.delete(0, "end")
            height_instant_entry.config(state='disabled')
            final_height = 0
            height_instant_entry.config(state='normal')
            height_instant_entry.insert(0, str(final_height) + " m")
            height_instant_entry.config(state='disabled')

        def zero_velocity():
            velocity_instant_entry.config(state='normal')
            velocity_instant_entry.delete(0, "end")
            velocity_instant_entry.config(state='disabled')
            final_velocity = 0
            velocity_instant_entry.config(state='normal')
            velocity_instant_entry.insert(0, str(final_velocity) + " m/s")
            velocity_instant_entry.config(state='disabled')

        def calculate_zero_energy():
            pe_instant_entry.config(state='normal')
            pe_instant_entry.delete(0, "end")
            pe_instant_entry.config(state='disabled')
            zero_energy = 0
            pe_instant_entry.config(state='normal')
            pe_instant_entry.insert(0, str(zero_energy) + " J")
            pe_instant_entry.config(state='disabled')

        def calculate_final_energy():
            ke_instant_entry.config(state='normal')
            ke_instant_entry.delete(0, "end")
            ke_instant_entry.config(state='disabled')
            final_energy = 0
            ke_instant_entry.config(state='normal')
            ke_instant_entry.insert(0, str(final_energy) + " J")
            ke_instant_entry.config(state='disabled')

        calculate_distance_travelled()
        zero_height()
        zero_velocity()
        calculate_final_energy()
        calculate_zero_energy()

    def instant():
        if planet_menu.cget("text") != "Planet":
            planet_name = planet_menu.cget("text")
            if planet_name == "Mercury":
                g = 3.7
            elif planet_name == "Venus":
                g = 8.87
            elif planet_name == "Earth":
                g = 9.807
            elif planet_name == "Moon":
                g = 1.62
            elif planet_name == "Mars":
                g = 3.721
            elif planet_name == "Jupiter":
                g = 24.79
            elif planet_name == "Saturn":
                g = 10.44
            elif planet_name == "Uranus":
                g = 8.87
            elif planet_name == "Neptune":
                g = 11.15
            else:
                g = 0.62

            def is_float(value):
                try:
                    float(value)
                    return True
                except ValueError:
                    return False

            def instant_distance():
                distance_instant_entry.config(state='normal')
                distance_instant_entry.delete(0, "end")
                distance_instant_entry.config(state='disabled')
                s_x = u_x * t_instant
                s_x_rounded = round(s_x, 2)
                distance_instant_entry.config(state='normal')
                distance_instant_entry.insert(0, str(s_x_rounded) + " m")
                distance_instant_entry.config(state='disabled')

            def instant_height():
                height_instant_entry.config(state='normal')
                height_instant_entry.delete(0, "end")
                height_instant_entry.config(state='disabled')
                s_y = ini_h + u_y * t_instant - (1 / 2) * g * t_instant ** 2
                s_y_rounded = round(s_y, 2)
                height_instant_entry.config(state='normal')
                height_instant_entry.insert(0, str(s_y_rounded) + " m")
                height_instant_entry.config(state='disabled')

            def instant_velocity():
                velocity_instant_entry.config(state='normal')
                velocity_instant_entry.delete(0, "end")
                velocity_instant_entry.config(state='disabled')
                v_y = u_y - g * t_instant
                instant_v = sqrt((v_y ** 2) + (u_x ** 2))
                instant_v_rounded = round(instant_v, 2)
                velocity_instant_entry.config(state='normal')
                velocity_instant_entry.insert(0, str(instant_v_rounded) + " m/s")
                velocity_instant_entry.config(state='disabled')

            def instant_pe():
                pe_instant_entry.config(state='normal')
                pe_instant_entry.delete(0, "end")
                s_y = ini_h + u_y * t_instant - (1 / 2) * g * t_instant ** 2
                instant_potential = m * g * s_y
                instant_potential_rounded = round(instant_potential, 2)
                pe_instant_entry.config(state='normal')
                pe_instant_entry.insert(0, str(instant_potential_rounded) + " J")
                pe_instant_entry.config(state='disabled')

            def instant_ke():
                ke_instant_entry.config(state='normal')
                ke_instant_entry.delete(0, "end")
                ke_instant_entry.config(state='disabled')
                ke_instant = (1 / 2) * m * (u_y - g * t_instant) ** 2
                ke_instant_rounded = round(ke_instant, 2)
                ke_instant_entry.config(state='normal')
                ke_instant_entry.insert(0, str(ke_instant_rounded) + " J")
                ke_instant_entry.config(state='disabled')

            if i_h_entry.get() or u_entry.get() != 0:
                u_ = float(u_entry.get())
                theta = float(angle_entry.get())
                ini_h = float(i_h_entry.get())
                u_x = u_ * cos(theta * pi / 180)
                u_y = u_ * sin(theta * pi / 180)
                if mass_entry.get() != 0:
                    m = mass_entry.get()
                    if time_instant_entry.get() != "":
                        if is_float(time_instant_entry.get()):
                            t_instant = float(time_instant_entry.get())
                            full_t = (u_y + sqrt((u_y ** 2) + 2 * g * ini_h)) / g
                            if 0 <= t_instant <= full_t:
                                instant_velocity()
                                instant_height()
                                instant_distance()
                                instant_pe()
                                instant_ke()
                            elif t_instant < 0:
                                instant_to_zero()
                                messagebox.showwarning(title='Invalid input', message='Time must be a positive'
                                                                                      ' value.')
                            else:
                                instant_to_max()
                                messagebox.showinfo(title='Info',
                                                    message='At this time, the object is already on the ground.')
                        else:
                            instant_to_zero()
                            messagebox.showwarning(title='Invalid input', message='Please only input numbers for time.')
                    else:
                        instant_to_zero()
                        messagebox.showwarning(title='No input detected', message='Please input values for time.')
                else:
                    instant_to_zero()
                    messagebox.showwarning(title="Invalid input", message="Mass must be a positive value.")
            else:
                u_ = float(u_entry.get())
                theta = float(angle_entry.get())
                ini_h = float(i_h_entry.get())
                u_x = u_ * cos(theta * pi / 180)
                u_y = u_ * sin(theta * pi / 180)
                if mass_entry.get() != 0:
                    m = mass_entry.get()
                    if time_instant_entry.get() != "":
                        if is_float(time_instant_entry.get()):
                            t_instant = float(time_instant_entry.get())
                            full_t = (u_y + sqrt((u_y ** 2) + 2 * g * ini_h)) / g
                            if 0 <= t_instant <= full_t:
                                instant_velocity()
                                instant_height()
                                instant_distance()
                                instant_pe()
                                instant_ke()
                                messagebox.showinfo(title="Info",
                                                    message="Please input values more than 0 for either initial "
                                                            "velocity or "
                                                            "initial height to have at least one instantaneous "
                                                            "output.")
                            elif t_instant < 0:
                                instant_to_zero()
                                messagebox.showwarning(title='Invalid input', message='Time must be a positive'
                                                                                      ' value.')
                            else:
                                instant_to_max()
                                messagebox.showinfo(title='Info',
                                                    message='At this time, the object is already on the ground.')
                                messagebox.showinfo(title="Info",
                                                    message="Please input values more than 0 for either initial "
                                                            "velocity or "
                                                            "initial height to have at least one instantaneous "
                                                            "output.")
                        else:
                            instant_to_zero()
                            messagebox.showwarning(title='Invalid input',
                                                   message='Please only input numbers for time.')
                    else:
                        instant_to_zero()
                        messagebox.showwarning(title='No input detected', message='Please input values for time.')
                else:
                    instant_to_zero()
                    messagebox.showwarning(title="Invalid input", message="Mass must be a positive value.")
        else:
            messagebox.showwarning(title="No planet detected", message="Please choose a planet before continuing.")

    def graphing():
        plt.close()
        if graph_menu.cget("text") != '       Graph':
            graph_name = graph_menu.cget("text")
            if planet_menu.cget("text") != "Planet":
                if mass_entry.get() != 0:
                    planet_name = planet_menu.cget("text")
                    if planet_name == "Mercury":
                        g = 3.7
                    elif planet_name == "Venus":
                        g = 8.87
                    elif planet_name == "Earth":
                        g = 9.807
                    elif planet_name == "Moon":
                        g = 1.62
                    elif planet_name == "Mars":
                        g = 3.721
                    elif planet_name == "Jupiter":
                        g = 24.79
                    elif planet_name == "Saturn":
                        g = 10.44
                    elif planet_name == "Uranus":
                        g = 8.87
                    elif planet_name == "Neptune":
                        g = 11.15
                    else:
                        g = 0.62

                    def height_displacement_graphed():
                        t = 0
                        dt = 0.001
                        u_ = float(u_entry.get())
                        theta = float(angle_entry.get())
                        ini_h = float(i_h_entry.get())
                        u_x_graph = u_ * cos(theta * pi / 180)
                        u_y_graph = u_ * sin(theta * pi / 180)
                        x_location = [0]
                        y_location = [ini_h]
                        while True:
                            x_loc = u_x_graph * t
                            y_loc = ini_h + u_y_graph * t - 1 / 2 * g * t ** 2
                            if y_loc < 0:
                                break
                            x_location.append(x_loc)
                            y_location.append(y_loc)
                            t += dt
                        plt.plot(x_location, y_location)
                        plt.xlabel('Displacement (m)')
                        plt.ylabel('Height (m)')
                        plt.title('Height-Displacement graph')
                        plt.show()

                    def displacement_time_graphed():
                        t = 0
                        dt = 0.001
                        u_ = float(u_entry.get())
                        ini_h = float(i_h_entry.get())
                        theta = float(angle_entry.get())
                        u_x_graph = u_ * cos(theta * pi / 180)
                        u_y_graph = u_ * sin(theta * pi / 180)
                        x_location = [0]
                        y_location = [0]
                        full_time = (u_y_graph + sqrt((u_y_graph ** 2) + 2 * g * ini_h)) / g
                        while True:
                            x_loc = t
                            y_loc = u_x_graph * t
                            if x_loc > full_time:
                                break
                            x_location.append(x_loc)
                            y_location.append(y_loc)
                            t += dt
                        plt.plot(x_location, y_location)
                        plt.xlabel('Time (s)')
                        plt.ylabel('Displacement (m)')
                        plt.title('Displacement-Time graph')
                        plt.show()

                    def height_time_graphed():
                        t = 0
                        dt = 0.001
                        u_ = float(u_entry.get())
                        theta = float(angle_entry.get())
                        ini_h = float(i_h_entry.get())
                        u_y_graph = u_ * sin(theta * pi / 180)
                        x_location = [0]
                        y_location = [ini_h]
                        while True:
                            x_loc = t
                            y_loc = ini_h + u_y_graph * t - 1 / 2 * g * t ** 2
                            if y_loc < 0:
                                break
                            x_location.append(x_loc)
                            y_location.append(y_loc)
                            t += dt
                        plt.plot(x_location, y_location)
                        plt.xlabel('Time (s)')
                        plt.ylabel('Height (m)')
                        plt.title('Height-Time graph')
                        plt.show()

                    def velocity_vx_time_graphed():
                        t = 0
                        dt = 0.001
                        u_ = float(u_entry.get())
                        ini_h = float(i_h_entry.get())
                        theta = float(angle_entry.get())
                        u_x_graph = u_ * cos(theta * pi / 180)
                        u_y_graph = u_ * sin(theta * pi / 180)
                        x_location = [0]
                        y_location = [u_x_graph]
                        full_time = (u_y_graph + sqrt((u_y_graph ** 2) + 2 * g * ini_h)) / g
                        while True:
                            x_loc = t
                            y_loc = u_x_graph
                            if x_loc > full_time:
                                break
                            x_location.append(x_loc)
                            y_location.append(y_loc)
                            t += dt
                        plt.plot(x_location, y_location)
                        plt.xlabel('Time (s)')
                        plt.ylabel('Velocity, $v_x$ ($ms^{-1}$)')
                        plt.title('Velocity, $v_x$-Time graph')
                        plt.show()

                    def velocity_vy_time_graphed():
                        t = 0
                        dt = 0.001
                        u_ = float(u_entry.get())
                        ini_h = float(i_h_entry.get())
                        theta = float(angle_entry.get())
                        u_y_graph = u_ * sin(theta * pi / 180)
                        x_location = [0]
                        y_location = [u_y_graph]
                        full_time = (u_y_graph + sqrt((u_y_graph ** 2) + 2 * g * ini_h)) / g
                        while True:
                            x_loc = t
                            y_loc = u_y_graph - g * t
                            if x_loc > full_time:
                                break
                            x_location.append(x_loc)
                            y_location.append(y_loc)
                            t += dt
                        plt.plot(x_location, y_location)
                        plt.xlabel('Time (s)')
                        plt.ylabel('Velocity, $v_y$ ($ms^{-1}$)')
                        plt.title('Velocity, $v_y$-Time graph')
                        plt.show()

                    def acceleration_ax_time_graphed():
                        t = 0
                        dt = 0.001
                        u_ = float(u_entry.get())
                        ini_h = float(i_h_entry.get())
                        theta = float(angle_entry.get())
                        u_y_graph = u_ * sin(theta * pi / 180)
                        x_location = [0]
                        y_location = [0]
                        full_time = (u_y_graph + sqrt((u_y_graph ** 2) + 2 * g * ini_h)) / g
                        while True:
                            x_loc = t
                            y_loc = 0
                            if x_loc > full_time:
                                break
                            x_location.append(x_loc)
                            y_location.append(y_loc)
                            t += dt
                        plt.plot(x_location, y_location)
                        plt.xlabel('Time (s)')
                        plt.ylabel('Acceleration, $a_x$ ($ms^{-2}$)')
                        plt.title('Acceleration, $a_x$-Time graph')
                        plt.show()

                    def acceleration_ay_time_graphed():
                        t = 0
                        dt = 0.001
                        u_ = float(u_entry.get())
                        ini_h = float(i_h_entry.get())
                        theta = float(angle_entry.get())
                        u_y_graph = u_ * sin(theta * pi / 180)
                        x_location = [0]
                        y_location = [g]
                        full_time = (u_y_graph + sqrt((u_y_graph ** 2) + 2 * g * ini_h)) / g
                        while True:
                            x_loc = t
                            y_loc = g
                            if x_loc > full_time:
                                break
                            x_location.append(x_loc)
                            y_location.append(y_loc)
                            t += dt
                        plt.plot(x_location, y_location)
                        plt.xlabel('Time (s)')
                        plt.ylabel('Acceleration, $a_y$ ($ms^{-2}$)')
                        plt.title('Acceleration, $a_y$-Time graph')
                        plt.show()

                    if graph_name == "Height-Displacement":
                        height_displacement_graphed()
                    elif graph_name == "Displacement-Time":
                        displacement_time_graphed()
                    elif graph_name == "Height-Time":
                        height_time_graphed()
                    elif graph_name == "Velocity, v_x-Time":
                        velocity_vx_time_graphed()
                    elif graph_name == "Velocity, v_y-Time":
                        velocity_vy_time_graphed()
                    elif graph_name == "Acceleration, a_x-Time":
                        acceleration_ax_time_graphed()
                    elif graph_name == "Acceleration, a_y-Time":
                        acceleration_ay_time_graphed()
                else:
                    messagebox.showwarning(title="Invalid input", message="Mass must be a positive value.")
            else:
                messagebox.showwarning(title="No planet detected",
                                       message="Please choose a planet before continuing.")
        else:
            messagebox.showwarning(title="No graph detected", message="Please choose a graph before continuing")

    img = (Image.open("mercury.png"))
    resized_mercury = img.resize((900, 370), Image.ANTIALIAS)
    mercury_bgi = ImageTk.PhotoImage(resized_mercury)

    img = (Image.open("venus.png"))
    resized_venus = img.resize((900, 370), Image.ANTIALIAS)
    venus_bgi = ImageTk.PhotoImage(resized_venus)

    img = (Image.open("earth.png"))
    resized_earth = img.resize((900, 370), Image.ANTIALIAS)
    earth_bgi = ImageTk.PhotoImage(resized_earth)

    img = (Image.open("moon.png"))
    resized_moon = img.resize((900, 370), Image.ANTIALIAS)
    moon_bgi = ImageTk.PhotoImage(resized_moon)

    img = (Image.open("mars.png"))
    resized_mars = img.resize((900, 370), Image.ANTIALIAS)
    mars_bgi = ImageTk.PhotoImage(resized_mars)

    img = (Image.open("jupiter.png"))
    resized_jupiter = img.resize((900, 370), Image.ANTIALIAS)
    jupiter_bgi = ImageTk.PhotoImage(resized_jupiter)

    img = (Image.open("saturn.png"))
    resized_saturn = img.resize((900, 370), Image.ANTIALIAS)
    saturn_bgi = ImageTk.PhotoImage(resized_saturn)

    img = (Image.open("uranus.png"))
    resized_uranus = img.resize((900, 370), Image.ANTIALIAS)
    uranus_bgi = ImageTk.PhotoImage(resized_uranus)

    img = (Image.open("neptune.png"))
    resized_neptune = img.resize((900, 370), Image.ANTIALIAS)
    neptune_bgi = ImageTk.PhotoImage(resized_neptune)

    img = (Image.open("pluto.png"))
    resized_pluto = img.resize((900, 370), Image.ANTIALIAS)
    pluto_bgi = ImageTk.PhotoImage(resized_pluto)

    def create_mercury_bg2():
        animation_canvas.create_image(0, 0, image=mercury_bgi, anchor="nw")

    def create_venus_bg2():
        animation_canvas.create_image(0, 0, image=venus_bgi, anchor="nw")

    def create_earth_bg2():
        animation_canvas.create_image(0, 0, image=earth_bgi, anchor="nw")

    def create_moon_bg2():
        animation_canvas.create_image(0, 0, image=moon_bgi, anchor="nw")

    def create_mars_bg2():
        animation_canvas.create_image(0, 0, image=mars_bgi, anchor="nw")

    def create_jupiter_bg2():
        animation_canvas.create_image(0, 0, image=jupiter_bgi, anchor="nw")

    def create_saturn_bg2():
        animation_canvas.create_image(0, 0, image=saturn_bgi, anchor="nw")

    def create_uranus_bg2():
        animation_canvas.create_image(0, 0, image=uranus_bgi, anchor="nw")

    def create_neptune_bg2():
        animation_canvas.create_image(0, 0, image=neptune_bgi, anchor="nw")

    def create_pluto_bg2():
        animation_canvas.create_image(0, 0, image=pluto_bgi, anchor="nw")

    def bg_image2():
        if planet_menu.cget("text") != "Planet":
            planet_name = planet_menu.cget("text")
            if planet_name == "Mercury":
                create_mercury_bg2()
            elif planet_name == "Venus":
                create_venus_bg2()
            elif planet_name == "Earth":
                create_earth_bg2()
            elif planet_name == "Moon":
                create_moon_bg2()
            elif planet_name == "Mars":
                create_mars_bg2()
            elif planet_name == "Jupiter":
                create_jupiter_bg2()
            elif planet_name == "Saturn":
                create_saturn_bg2()
            elif planet_name == "Uranus":
                create_uranus_bg2()
            elif planet_name == "Neptune":
                create_neptune_bg2()
            else:
                create_pluto_bg2()

    def create_mercury_bg1():
        animation_canvas.create_image(0, 0, image=mercury_bgi, anchor="nw")
        trail()

    def create_venus_bg1():
        animation_canvas.create_image(0, 0, image=venus_bgi, anchor="nw")
        trail()

    def create_earth_bg1():
        animation_canvas.create_image(0, 0, image=earth_bgi, anchor="nw")
        trail()

    def create_moon_bg1():
        animation_canvas.create_image(0, 0, image=moon_bgi, anchor="nw")
        trail()

    def create_mars_bg1():
        animation_canvas.create_image(0, 0, image=mars_bgi, anchor="nw")
        trail()

    def create_jupiter_bg1():
        animation_canvas.create_image(0, 0, image=jupiter_bgi, anchor="nw")
        trail()

    def create_saturn_bg1():
        animation_canvas.create_image(0, 0, image=saturn_bgi, anchor="nw")
        trail()

    def create_uranus_bg1():
        animation_canvas.create_image(0, 0, image=uranus_bgi, anchor="nw")
        trail()

    def create_neptune_bg1():
        animation_canvas.create_image(0, 0, image=neptune_bgi, anchor="nw")
        trail()

    def create_pluto_bg1():
        animation_canvas.create_image(0, 0, image=pluto_bgi, anchor="nw")
        trail()

    def bg_image1():
        if planet_menu.cget("text") != "Planet":
            planet_name = planet_menu.cget("text")
            if planet_name == "Mercury":
                create_mercury_bg1()
            elif planet_name == "Venus":
                create_venus_bg1()
            elif planet_name == "Earth":
                create_earth_bg1()
            elif planet_name == "Moon":
                create_moon_bg1()
            elif planet_name == "Mars":
                create_mars_bg1()
            elif planet_name == "Jupiter":
                create_jupiter_bg1()
            elif planet_name == "Saturn":
                create_saturn_bg1()
            elif planet_name == "Uranus":
                create_uranus_bg1()
            elif planet_name == "Neptune":
                create_neptune_bg1()
            else:
                create_pluto_bg1()

    def create_mercury_bg():
        animation_canvas.create_image(0, 0, image=mercury_bgi, anchor="nw")
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()

    def create_venus_bg():
        animation_canvas.create_image(0, 0, image=venus_bgi, anchor="nw")
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()

    def create_earth_bg():
        animation_canvas.create_image(0, 0, image=earth_bgi, anchor="nw")
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()

    def create_moon_bg():
        animation_canvas.create_image(0, 0, image=moon_bgi, anchor="nw")
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()

    def create_mars_bg():
        animation_canvas.create_image(0, 0, image=mars_bgi, anchor="nw")
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()

    def create_jupiter_bg():
        animation_canvas.create_image(0, 0, image=jupiter_bgi, anchor="nw")
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()

    def create_saturn_bg():
        animation_canvas.create_image(0, 0, image=saturn_bgi, anchor="nw")
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()

    def create_uranus_bg():
        animation_canvas.create_image(0, 0, image=uranus_bgi, anchor="nw")
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()

    def create_neptune_bg():
        animation_canvas.create_image(0, 0, image=neptune_bgi, anchor="nw")
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()

    def create_pluto_bg():
        animation_canvas.create_image(0, 0, image=pluto_bgi, anchor="nw")
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()

    def bg_image():
        if planet_menu.cget("text") != "Planet":
            planet_name = planet_menu.cget("text")
            if planet_name == "Mercury":
                create_mercury_bg()
            elif planet_name == "Venus":
                create_venus_bg()
            elif planet_name == "Earth":
                create_earth_bg()
            elif planet_name == "Moon":
                create_moon_bg()
            elif planet_name == "Mars":
                create_mars_bg()
            elif planet_name == "Jupiter":
                create_jupiter_bg()
            elif planet_name == "Saturn":
                create_saturn_bg()
            elif planet_name == "Uranus":
                create_uranus_bg()
            elif planet_name == "Neptune":
                create_neptune_bg()
            else:
                create_pluto_bg()

    def changing_height1():
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.delete(tk.ALL)
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()
        bg_image()

    def changing_height(_):
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.delete(tk.ALL)
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()
        bg_image()

    def changing_initial1():
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.delete(tk.ALL)
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()
        bg_image()

    def changing_initial(_):
        ini_h_animation = float(i_h_entry.get())
        x_movement = 0
        y_movement = 370 - ini_h_animation
        animation_canvas.delete(tk.ALL)
        animation_canvas.create_oval(x_movement, y_movement - b_height, x_movement + b_width, y_movement,
                                     fill='white')
        trail()
        bg_image()

    def trail():
        ini_h = float(i_h_entry.get())
        u_ = float(u_entry.get())
        theta = float(angle_entry.get())
        u_y = u_ * sin(theta * pi / 180)
        u_x = u_ * cos(theta * pi / 180)
        if planet_menu.cget("text") != "Planet":
            planet_name = planet_menu.cget("text")
            if planet_name == "Mercury":
                g = 3.7
            elif planet_name == "Venus":
                g = 8.87
            elif planet_name == "Earth":
                g = 9.807
            elif planet_name == "Moon":
                g = 1.62
            elif planet_name == "Mars":
                g = 3.721
            elif planet_name == "Jupiter":
                g = 24.79
            elif planet_name == "Saturn":
                g = 10.44
            elif planet_name == "Uranus":
                g = 8.87
            elif planet_name == "Neptune":
                g = 11.15
            else:
                g = 0.62

            t = 0
            dt = 0.1
            cords_list = []
            for time in range(1000):
                x_loc = u_x * t + b_width / 2
                y_loc = 370 - ((b_width / 2) + ini_h + u_y * t - 1 / 2 * g * t ** 2)
                if y_loc > 370:
                    break
                cords_list.append(x_loc)
                cords_list.append(y_loc)
                t += dt
            cords_tuple = tuple(cords_list)
            animation_canvas.create_line(cords_tuple, smooth=True, dash=(5, 1), fill='white')
        else:
            pass

    def animation():
        if planet_menu.cget("text") != "Planet":
            if mass_entry.get() > 0:
                planet_name = planet_menu.cget("text")
                if planet_name == "Mercury":
                    g = 3.7
                elif planet_name == "Venus":
                    g = 8.87
                elif planet_name == "Earth":
                    g = 9.807
                elif planet_name == "Moon":
                    g = 1.62
                elif planet_name == "Mars":
                    g = 3.721
                elif planet_name == "Jupiter":
                    g = 24.79
                elif planet_name == "Saturn":
                    g = 10.44
                elif planet_name == "Uranus":
                    g = 8.87
                elif planet_name == "Neptune":
                    g = 11.15
                else:
                    g = 0.62
                t = 0
                dt = 0.01
                u_ = float(u_entry.get())
                theta = float(angle_entry.get())
                ini_h = float(i_h_entry.get())
                u_x = u_ * cos(theta * pi / 180)
                u_y = u_ * sin(theta * pi / 180)
                while True:
                    try:
                        u_entry.config(state='disabled', cursor='no')
                        i_h_entry.config(state='disabled', cursor='no')
                        angle_entry.config(state='disabled', cursor='no')
                        mass_entry.config(state='disabled', cursor='no')
                        animate_button.config(state='disabled', cursor='no')
                        planet_menu.config(state='disabled', cursor='no')
                        animation_canvas.delete(tk.ALL)
                        bg_image1()
                        trail()
                        x_loc = u_x * t
                        y_loc = 370 - (b_width + ini_h + u_y * t - 1 / 2 * g * t ** 2)
                        animation_canvas.create_oval(x_loc, y_loc, x_loc + b_width, y_loc + b_height, fill='white')
                        t += dt
                        animation_canvas.update()
                        if y_loc + b_height > 370:
                            u_entry.config(state='normal', cursor='hand2')
                            i_h_entry.config(state='normal', cursor='hand2')
                            angle_entry.config(state='normal', cursor='hand2')
                            mass_entry.config(state='normal', cursor='hand2')
                            animate_button.config(state='normal', cursor='hand2')
                            planet_menu.config(state='normal', cursor='hand2')
                            messagebox.showinfo(title='Done!', message='The ball has reached the ground.')
                            animation_canvas.delete(tk.ALL)
                            bg_image2()
                            changing_height1()
                            changing_initial1()
                            break
                    except:
                        break
            else:
                messagebox.showwarning(title="Invalid input", message="Mass must be a positive value.")
        else:
            messagebox.showwarning(title="No planet detected",
                                   message="Please choose a planet before continuing.")

    # ----- INPUT FRAME (FRAME 1) --------------------------------------------------------------------------------------
    frame_1 = ttk.LabelFrame(gui, relief='groove', text='Inputs')
    frame_1.place(relx=0.015, rely=0.6225)
    # ----- INPUT LABELS FOR FRAME 1-----
    u_label = tk.Label(frame_1, text='Initial Velocity (m/s)')
    u_label.grid(row=0, column=0, pady=5, padx=5)
    angle_label = tk.Label(frame_1, text='Angle of Projection (\N{DEGREE SIGN})')
    angle_label.grid(row=2, column=0, pady=5, padx=5)
    i_h_label = tk.Label(frame_1, text='Initial height (m)')
    i_h_label.grid(row=2, column=1, pady=5, padx=5)
    mass_label = tk.Label(frame_1, text='Mass (kg)')
    mass_label.grid(row=0, column=1, pady=5, padx=5)
    # ----- PLANET MENU OPTION -----
    empty_label_1 = tk.Label(frame_1, text='                               ')
    empty_label_1.grid(row=0, column=2, pady=5, padx=5)
    planet_op = ['Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    planet_var = tk.StringVar()
    planet_var.set('Planet')
    planet_menu = tk.OptionMenu(frame_1, planet_var, *planet_op, command=changing_initial)
    planet_menu.config(width='7')
    planet_menu.config(cursor='hand2')
    planet_menu.grid(row=0, column=2, pady=5, padx=5)
    # ----- BUTTONS FOR FRAME 1 -----
    calculate_button = tk.Button(frame_1, text='Calculate', width=10, cursor='hand2', command=calculated)
    calculate_button.grid(row=1, column=2, pady=5, padx=5)
    empty_label_2 = tk.Label(frame_1, text='                            ')
    empty_label_2.grid(row=4, column=1, pady=5)
    # -----INPUT FOR FRAME 1-----
    u_entry = tk.Scale(frame_1, from_=0, to=100, cursor='hand2', orient='horizontal', command=changing_initial)
    u_entry.grid(row=1, column=0, pady=5, padx=5)
    angle_entry = tk.Scale(frame_1, from_=0, to=90, cursor='hand2', orient='horizontal', command=changing_initial)
    angle_entry.grid(row=3, column=0, pady=5, padx=5)
    i_h_entry = tk.Scale(frame_1, from_=0, to=100, cursor='hand2', orient='horizontal', command=changing_height)
    i_h_entry.grid(row=3, column=1, pady=5, padx=5)
    mass_entry = tk.Scale(frame_1, from_=0, to=50, cursor='hand2', orient='horizontal')
    mass_entry.grid(row=1, column=1, pady=5, padx=5)

    # ----- OUTPUT FRAME (FRAME 2) -------------------------------------------------------------------------------------
    frame_2 = ttk.LabelFrame(gui, relief='groove', text='Outputs')
    frame_2.place(relx=0.83, rely=0.015)
    # ----- OUTPUT LABELS FOR FRAME 2-----
    time_label = tk.Label(frame_2, text='Time Taken')
    time_label.grid(row=0, column=0, pady=5, padx=5)
    displacement_label = tk.Label(frame_2, text='Displacement')
    displacement_label.grid(row=2, column=0, pady=5, padx=5)
    max_height_label = tk.Label(frame_2, text='Maximum Height')
    max_height_label.grid(row=4, column=0, pady=5, padx=5)
    u_x_label = tk.Label(frame_2, text='Initial Velocity (Horizontal)')
    u_x_label.grid(row=6, column=0, pady=5, padx=5)
    u_y_label = tk.Label(frame_2, text='Initial Velocity (Vertical)')
    u_y_label.grid(row=8, column=0, pady=5, padx=5)
    g_label = tk.Label(frame_2, text='Gravitational Acceleration')
    g_label.grid(row=10, column=0, pady=5, padx=5)
    max_energy_label = tk.Label(frame_2, text='Total Energy')
    max_energy_label.grid(row=12, column=0, pady=5, padx=5)
    # ----- OUTPUT BOXES FOR FRAME 2 -----
    time_output = ttk.Entry(frame_2, state='disabled', cursor='no', width=22)
    time_output.grid(row=1, column=0, pady=5, padx=5)
    displacement_output = ttk.Entry(frame_2, state='disabled', cursor='no', width=22)
    displacement_output.grid(row=3, column=0, pady=5, padx=5)
    max_height_output = ttk.Entry(frame_2, state='disabled', cursor='no', width=22)
    max_height_output.grid(row=5, column=0, pady=5, padx=5)
    u_x_output = ttk.Entry(frame_2, state='disabled', cursor='no', width=22)
    u_x_output.grid(row=7, column=0, pady=5, padx=5)
    u_y_output = ttk.Entry(frame_2, state='disabled', cursor='no', width=22)
    u_y_output.grid(row=9, column=0, pady=5, padx=5)
    g_output = ttk.Entry(frame_2, state='disabled', cursor='no', width=22)
    g_output.grid(row=11, column=0, pady=5, padx=5)
    max_energy_entry = ttk.Entry(frame_2, state='disabled', cursor='no', width=22)
    max_energy_entry.grid(row=13, column=0, pady=5, padx=5)
    empty_label_2 = ttk.Label(frame_2, text='                                                   ')
    empty_label_2.grid(row=14, column=0, pady=5, padx=5)

    # ----- INSTANTANEOUS INPUT AND OUTPUTS FRAME (FRAME 3) ------------------------------------------------------------
    frame_3 = ttk.LabelFrame(gui, relief='groove', text='Instantaneous')
    frame_3.place(relx=0.34, rely=0.6225)
    # ----- INSTANTANEOUS INPUT AND OUTPUT LABEL FOR FRAME 3 -----
    time_instant_label = tk.Label(frame_3, text='Time (s)')
    time_instant_label.grid(row=0, column=0, pady=5, padx=5)
    time_instant_entry = ttk.Entry(frame_3, cursor='xterm')
    time_instant_entry.grid(row=1, column=0, pady=5, padx=5)
    velocity_instant_label = tk.Label(frame_3, text='Velocity')
    velocity_instant_label.grid(row=2, column=0, pady=5, padx=5)
    velocity_instant_entry = ttk.Entry(frame_3, state='disabled', cursor='no')
    velocity_instant_entry.grid(row=3, column=0, pady=5, padx=5)
    distance_instant_label = tk.Label(frame_3, text='Displacement')
    distance_instant_label.grid(row=4, column=0, pady=5, padx=5)
    distance_instant_entry = ttk.Entry(frame_3, state='disabled', cursor='no')
    distance_instant_entry.grid(row=5, column=0, pady=5, padx=5)
    height_instant_label = tk.Label(frame_3, text='Height')
    height_instant_label.grid(row=0, column=1, pady=5, padx=5)
    height_instant_entry = ttk.Entry(frame_3, state='disabled', cursor='no')
    height_instant_entry.grid(row=1, column=1, pady=5, padx=5)
    pe_instant_label = tk.Label(frame_3, text='Gravitational\nPotential Energy')
    pe_instant_label.grid(row=2, column=1, pady=5, padx=5)
    pe_instant_entry = ttk.Entry(frame_3, state='disabled', cursor='no')
    pe_instant_entry.grid(row=3, column=1, pady=5, padx=5)
    ke_instant_label = tk.Label(frame_3, text='Kinetic Energy')
    ke_instant_label.grid(row=4, column=1, pady=5, padx=5)
    ke_instant_entry = ttk.Entry(frame_3, state='disabled', cursor='no')
    ke_instant_entry.grid(row=5, column=1, pady=5, padx=5)
    # ----- BUTTONS FOR FRAME 3 -----
    find_button = tk.Button(frame_3, text='Find', width=10, cursor='hand2', command=instant)
    find_button.grid(row=0, column=3, pady=5, padx=5)

    # ----- OTHER BUTTONS FRAME (FRAME 5) ------------------------------------------------------------------------------
    frame_5 = ttk.LabelFrame(gui, relief='groove', text='Graph and Animations')
    frame_5.place(relx=0.67, rely=0.622)
    # ----- GRAPH MENU OPTION -----
    graph_op = ['Height-Displacement', 'Displacement-Time', 'Height-Time', 'Velocity, v_x-Time', 'Velocity, v_y-Time',
                'Acceleration, a_x-Time', 'Acceleration, a_y-Time']
    graph_var = tk.StringVar()
    graph_var.set('       Graph')
    graph_menu = tk.OptionMenu(frame_5, graph_var, *graph_op)
    graph_menu.config(width='19')
    graph_menu.config(cursor='hand2')
    graph_menu.grid(row=0, column=0, pady=7, padx=5)
    graph_button = tk.Button(frame_5, text='Display Graph', width='21', cursor='hand2', command=graphing)
    graph_button.grid(row=1, column=0, pady=7, padx=0)
    # ----- BUTTONS FOR ANIMATION FRAME ----
    empty_label_1 = tk.Label(frame_5, text='            ')
    empty_label_1.grid(row=4, column=0, pady=11, padx=5)
    animate_button = tk.Button(frame_5, text='Show animation', width=21, cursor='hand2', command=animation)
    animate_button.grid(row=2, column=0, pady=7, padx=5)
    empty_label_1 = tk.Label(frame_5, text='            ')
    empty_label_1.grid(row=3, column=0, pady=9, padx=5)

    # ----- BUTTONS FOR RESET AND BACK TO HOME PAGE -----
    home_image = Image.open('homepage_button.png')
    resized_home = home_image.resize((50, 48), Image.ANTIALIAS)
    new_home_image = ImageTk.PhotoImage(resized_home)
    home_button = tk.Button(image=new_home_image, borderwidth=0, bg='#F0F0F0', relief='flat', cursor='hand2',
                            command=first_page)
    home_button.image = new_home_image
    home_button.place(relx=0.935, rely=0.89)
    reset_image = Image.open('reset_button.png')
    resized_reset = reset_image.resize((52, 50), Image.ANTIALIAS)
    new_reset_image = ImageTk.PhotoImage(resized_reset)
    reset_button = tk.Button(image=new_reset_image, borderwidth=0, bg='#F0F0F0', relief='flat', cursor='exchange',
                             command=simulation_page)
    reset_button.image = new_reset_image
    reset_button.place(relx=0.84, rely=0.89)

    # ----- ANIMATION FRAME (FRAME 4) ----------------------------------------------------------------------------------
    frame_4 = ttk.LabelFrame(gui, relief='groove', text='Animation')
    frame_4.place(relx=0.015, rely=0.015)
    animation_canvas = tk.Canvas(frame_4, width=900, height=370, cursor='crosshair', )
    animation_canvas.pack(expand=True, fill="both")
    b_height = 36
    b_width = 36
    x = 0
    y = 370
    animation_canvas.create_oval(x, y - b_height, x + b_width, y, fill='white')


first_page()
gui.mainloop()
