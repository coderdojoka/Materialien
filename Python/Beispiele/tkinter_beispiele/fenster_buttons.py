__author__ = 'Mark Weinreuter'

from tkinter import *
from tkinter.ttk import *

master = Tk()

frame = Frame(master)

separator = Frame(relief=GROOVE)
separator.pack(fill=X, padx=5, pady=5)

text1 = Label(master=master, text="Hallo Welt")  # , fg="red", bg="blue")
text1.pack()

listbox = Listbox(separator)
listbox.pack()


for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

listbox.insert(END, "a list entry")


e = Entry(master)
e.pack()

e.delete(0, END)
e.insert(0, "a default value")

button1 = Button(master=master, text="Drück mich!")
button1.pack(side=RIGHT)
button1["command"] = lambda: print(e.get())

button2 = Button(text="Hallo")
button2.pack()




top = Toplevel()
top.title("About this application...")

msg = Message(top, text="Hallo Welt")
msg.pack()

# create a toplevel menu
menubar = Menu(top)
menubar.add_command(label="Hello!", command=lambda: print("Hello"))
menubar.add_command(label="Quit!", command=top.deiconify)

# display the menu
top.config(menu=menubar)

v = IntVar()

Radiobutton(master, text="One", variable=v, value=1).pack(side="top")
Radiobutton(master, text="Two", variable=v, value=2).pack(side="left")

button = Button(top, text="Dismiss", command=top.destroy)
button.pack()

w = Spinbox(master, from_=0, to=10)
w.pack()

s = Style()
print(s.theme_names())
#s.theme_use("clam")

master.mainloop()
