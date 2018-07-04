from tkinter import *
top=Tk()
mb=Menubutton(top,text="menu")
mb.grid()
mb.menu=Menu(mb,tearoff=0)
mb['menu']=mb.menu
cVar=IntVar()
aVar=IntVar()
mb.menu.add_checkbutton(label='contact',variable=cVar)
mb.menu.add_checkbutton(label='About',variable=aVar)
mb.pack()
top.mainloop()


from  tkinter import *
root=Tk()
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='new')
filemenu.add_command(label='opennnnnnnn')
filemenu.add_separator()
filemenu.add_command(label='exit',command=root.quit)
helpmenu=Menu(menu)
menu.add_cascade(label='help',menu=helpmenu)
helpmenu.add_command(label='about')
mainloop()

from tkinter import *
main=Tk()
ourmessage='this is our message'
messagevar=Message(main,text=ourmessage)
messagevar.config(bg='lightgreen')
messagevar.pack()
main.mainloop()



from tkinter import *
root=Tk()
v=IntVar
Label(root,text="choose a lang.").pack()
Radiobutton(root,text="python",variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="per1",variable=v,value=2).pack(anchor=W)
mainloop()

from tkinter import *
root=Tk()
w=Scale(root,from_=0,to =42)
w.pack()
w=Scale(root,from_=0,to =200,orient=HORIZONTAL)
w.pack()
mainloop()

from tkinter import  *
root=Tk()
root.title('ruby')
top=Toplevel()
top.title("python")
top.mainloop()

from  tkinter import *
m1=PanedWindow()
m1.pack(fill=BOTH,expand=1)
left=Entry(m1,bd=5)
m1.add(left)
m2=PanedWindow(m1,orient=VERTICAL)
m1.add(m2)
top=Scale(m2,orient=HORIZONTAL)
m2.add(top)
mainloop()

from tkinter import messagebox
from  tkinter import  *
root=Tk()
root.title('moiht')
def show():
    messagebox.showinfo("title","desc")
b1=Button(root,text='fff',command=show)
b1.pack()
mainloop()