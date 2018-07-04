#question1

import tkinter as tk
from tkinter import *
m=tk.Tk()
m.title("info")
dict={'name':'mohit','mobile_number':919112665688}
scrollbar=Scrollbar(m)
scrollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(m,yscrollcommand= scrollbar.set)
for key in dict.__iter__():
        mylist.insert(END,key)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
def g():
    m.quit()
b=Button(m,text="enter",command=g)
b.pack()
m.mainloop()


#question2


def di():
    dict.update({"age":21})
    print(dict)
button1=Button(m,text='good',command=di)
button1.pack()
m.mainloop()
