from tkinter import *
from tkinter import filedialog
import os, subprocess, platform
import pathlib
from tkinter import messagebox

root = Tk()

root.title('Student Data Manager')
root.iconbitmap('C:/Users/Toshiba/Desktop/SDM.ico')



def Admin():

    top = Toplevel()
    top.geometry('600x100')
    top.title('Second Window Student Data Manager')
    top.iconbitmap('C:/Users/Toshiba/Desktop/SDM.ico')
    # input data box

    e = Entry(top, width=50)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



    # puts default text inside the text box
    # e.insert(0, 'Enter the name of a file')

    def Admin_Create_New_File():
        # creating a file
        f = e.get() + ".docx"
        path = pathlib.Path(f)
        a = path.exists()

        if a == True:
            response = messagebox.askyesno("Student Data Manager", 'File already exist. Do you want to replace it?')
            if (response == True):
                b = open(f, "w+")
                b.close()
                messagebox.showinfo("Student Data Manager", "New file created")
            else:
                messagebox.showinfo("Student Data Manager", 'Not CREATED')
        else:
            c=open(f, "w+")
            c.close()

        e.delete(0, END)

    def Admin_Open_File():
        top.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a file",
                                                   filetypes=(("docx files", "*.docx"), ("pdf files", "*.pdf"),("all files","*.*")))

        # Open document with default application in Python
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', top.filename))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(top.filename)
        else:                               # linux variants
            subprocess.call(('xdg-open', top.filename))

    # Defining buttons
    button_1AW = Button(top, text='Create New File', padx=50, pady=0, command=Admin_Create_New_File)
    button_2AW = Button(top, text='Open / Edit File', padx=50, pady=0, command=Admin_Open_File)

    # put buttons on the screen
    button_1AW.grid(row=0, column=3)
    button_2AW.grid(row=1, column=3)

def Guest():
    top = Toplevel()
    top.title('Second Window Student Data Manager')
    top.iconbitmap('C:/Users/Toshiba/Desktop/SDM.ico')
    def Guest_Open_File():
        top.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a file",
                                                  filetypes=(("text files", "*.txt"), ("pdf files", "*.pdf")))

        # Open document with default application in Python
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', top.filename))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(top.filename)
        else:                               # linux variants
            subprocess.call(('xdg-open', top.filename))

    button_1GW = Button(top, text="Open Files", command=Guest_Open_File).pack()





#status bar
#status1 = Label(root, text="Developer :- Roshan", bd=1, relief=SUNKEN, anchor=E)
#status2 = Label(root, text="Developed by Roshan", bd=1, relief=SUNKEN, anchor=W)
#status1.grid(row=5, column=3, sticky=E)
#status2.grid(row=5, columnspan=10, sticky=E + W)
# Create frame
# frame = LabelFrame(root, padx=50, pady=50)
# b = Button(frame, text="donasdf")
# b.pack()
# frame.pack(padx=200, pady=200)

button_1MW = Button(root, text="Admin",padx=50, pady=0, command=Admin)
button_1MW.grid(row=0, column=3)
button_2MW = Button(root, text="Guest",padx=50, pady=0, command=Guest)
button_2MW.grid(row=1, column=3)

root.geometry('200x100')
root.mainloop()
