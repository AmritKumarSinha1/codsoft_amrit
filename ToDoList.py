#importing the modules
from tkinter import *
from tkinter import messagebox

#creating a window
ws=Tk()
ws.geometry('500x400+600+200')
ws.title('To Do List')
ws.config(bg='dark grey')

#creating the frames
f=Frame(ws)
f.pack(padx=10,pady=10)

#creating the listbox
l=Listbox(f,width=30,height=10,font=('algerian'),fg='black')
l.pack(side=LEFT,fil=BOTH)

task=[]
for item in task:
    l.insert(END,item)

#creating the scrollbar
sb1=Scrollbar(f)
sb1.pack(side= RIGHT,fill=BOTH)
l.config(yscrollcommand=sb1.set)
sb1.config(command=l.yview)

#creatng the entry
entry=Entry(ws,font=('Arial'))
entry.pack(pady=1)


#creating frames for button
bf=Frame(ws)
bf.pack(pady=15)

#defining the function
def newtask():
    task=entry.get()
    if task!="":
        l.insert(END,task)
    else:
        messagebox.showwarning("warning","you haven't entered any task")
    
def deltask():
    l.delete(ANCHOR)

#creating the buttons
addbutton=Button(bf,text='ADD TASK',font=('arial'),bg='teal',padx=20,pady=10,command=newtask)
addbutton.pack(fill=BOTH,side=LEFT)

delbutton=Button(bf,text='DELETE TASK',font=('arial'),bg='teal',padx=20,pady=10,command=deltask)
delbutton.pack(fill=BOTH,side=LEFT)

ws.mainloop()