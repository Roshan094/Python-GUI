from tkinter import *
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pathlib
from tkinter import messagebox
from tkinter import filedialog
import os, subprocess, platform


class SeaOfDataManagerApp:

    def __init__(self, window):
        self.window = window
        self.window.title('Student Data Manager')
        self.window.iconbitmap(default="SDM.ico")

        Label(text=" ").grid(row=0, column=1)
        Label(text="Welcome ").grid(row=1,column=2)

        self.Admin = Admin
        self.Guest = Guest

        ttk.Button(text="Admin", command=Admin).grid(row=2,column=5, padx=50, pady=10)
        ttk.Button(text="Guest", command=Guest).grid(row=3,column=5, padx=50, pady=10)



class Admin:

    def __init__(self):
        window.destroy()
        self.new_login_window =  ThemedTk(theme='radiance')
        app = Login(self.new_login_window)
        self.new_login_window.mainloop()

class Login:

    user = 'admin'
    passw = 'admin'

    def __init__(self,root):

        self.root = root
        self.root.title('LOGIN SCREEN')

        Label(text=' Username ', font='Times 15').grid(row=1, column=1, pady=20)
        self.username = Entry()
        self.username.grid(row=1, column=2, columnspan=20, pady=10, padx=50)

        Label(text=' Password ', font='Times 15').grid(row=2, column=1, pady=10)
        self.password = Entry(show='*')
        self.password.grid(row=2, column=2, columnspan=20, pady=10, padx=50)

        ttk.Button(text='  LOGIN  ', command=lambda :self.login_user(root)).grid(row=3, column=2)

    def login_user(self, root):

        '''Check username and password entered are correct'''
        if self.username.get() == self.user and self.password.get() == self.passw:
            # Destroy current window
            root.destroy()

            # Open new window
            new_window = ThemedTk(theme='radiance')
            application = School_Portal(new_window)
            new_window.mainloop()

        else:

            '''Prompt user that either id or password is wrong'''
            self.message = Label(text='Username or Password incorrect. Try again!', fg='Red')
            self.message.grid(row=6, column=2)
            Button()

class School_Portal:

    def __init__(self, new_window):

        self.new_window = new_window
        self.e = Entry(new_window, width=50)
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        print(self.e)

        # Defining buttons
        ttk.Button(new_window, text='Create New File', command=lambda: self.Create_New_File(self.e)).grid(row=0, column=3)
        ttk.Button(new_window, text='Open / Edit File', command=lambda: self.Admin_Open_File()).grid(row=1, column=3)

    def Create_New_File(self, e):

        self.e = e
        e.get() + ".docx"
        self.path = pathlib.Path(self.e)
        self.a = self.path.exists()
        if self.a == True:
            self.response = messagebox.askyesno("Student Data Manager", 'File already exist. Do you want to replace it?')
            if (self.response == True):
                self.b = open(self.e, "w+")
                self.b.close()
                messagebox.showinfo("Student Data Manager", "New file created")
            else:
                pass
                messagebox.showinfo("Student Data Manager", 'Not CREATED')
        else:
            self.c = open(self.e, "w+")
            self.c.close()

        # delete what's already in the box
        e.delete(0, END)

    def Admin_Open_File(self):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a file",
                                                  filetypes=(("docx files", "*.docx"), ("pdf files", "*.pdf")))

        # Open document with default application in Python
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', self.filename))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(self.filename)
        else:  # linux variants
            subprocess.call(('xdg-open', self.filename))



class Guest:

    def __init__(self):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a file", filetypes=(("text files", "*.txt"), ("pdf files", "*.pdf")))
        # Open document with default application in Python
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', self.filename))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(self.filename)
        else:  # linux variants
            subprocess.call(('xdg-open', self.filename))



window = ThemedTk(theme='radiance')
#window.geometry('425x225')
app = SeaOfDataManagerApp(window)
window.mainloop()