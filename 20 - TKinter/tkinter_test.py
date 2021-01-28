from tkinter import * # Import all so we don't have to qualify with tkinter.

# TKinter app uses two main features, the window and the widgets
window = Tk() # Start of a tkinter app

def km_to_miles():
    miles = 0.621371 * float(e1_value.get())
    t1.insert(END, miles)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=0)

# A widget's first argument needs to be the window it will be displayed in
b1 = Button(window, text='Convert', command=km_to_miles)
b1.grid(row=0, column=1)

t1 = Text(window, height = 1, width=20)
t1.grid(row=1, column=0)

window.mainloop() # end of a tkinter app