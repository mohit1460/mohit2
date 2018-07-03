#question1

import tkinter as tk
from tkinter import *
def destroy():
    m.destroy()
m=tk.Tk()
m.title("mohit")
var=StringVar()
label=Label(m,textvariable=var)
var.set("hello world")
button=tk.Button(m,text='exit',width=25,command=destroy)
label.pack()
button.pack()
m.mainloop()

#question2

m=tk.Tk()
m.title("mohit")
def mohit():
    var=StringVar()
    label=Label(m,textvariable=var)
    var.set("my name is mohit")
    label.pack()
button=tk.Button(m,text='display',width=35,command=mohit)
button.pack()
m.mainloop()

#question3

from tkinter import *
import tkinter as tk
s=tk.Tk()
s.title("sharma")
def mo():
    s.destroy()
button1=tk.Button(s,text='exit',width=25,command=mo)
button1.pack()
def moh():
    var1 = StringVar()
    label1 = Label(s, textvariable=var1)
    var1.set("my name is mohit sharma")
    label1.pack()
    label2.destroy()
button2=tk.Button(s,text='name',command=moh)
button2.pack()
var2 = StringVar()
label2 = Label(s, textvariable=var2)
var2.set("my name is mohit")
label2.pack()
s.mainloop()

#question4

from tkinter import *
import tkinter
import tkinter as tk
z=tk.Tk()
z.title("mohit sharma")
l1=Label(z,text='name')
l1.grid(row=0)
e1=Entry(z)
e1.grid(row=0,column=3)
def mohitsh():
    e=e1.get()
    print(e)
    z.destroy()
b1=Button(z,text='enter',width=25,command=mohitsh)
b1.grid(row=4,column=4)

mainloop()


