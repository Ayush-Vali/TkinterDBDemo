from tkinter import *

from tkinter import messagebox

import pymysql

def put(*args):# used to pass a variable number of arguments to a function
    con=pymysql.connect(user='root', password='abc', host='localhost', database='db')
    cur=con.cursor()
    cur.execute("insert into student(roll_no,name) values('"+rollnoEntry.get()+"', '"+nameEntry.get()+"')")
    messagebox.showinfo("Record inserted")
    con.commit()
    con.close()

def get():
    con=pymysql.connect(user='root', password='abc', host='localhost', database='db')
    cur=con.cursor()
    cur.execute("select * from student")
    results=cur.fetchall()
    row=cur.fetchone()
    messagebox.showinfo("infomsg",results)
    con.close()








root=Tk()

root.title("insert data")

rollnoEntry=Entry(root,width=7)

nameEntry=Entry(root,width=7)

rollnoEntry.grid(row=1,column=1)

nameEntry.grid(row=2,column=1)

Label(root,text='rollno').grid(row=1,column=0) 

Label(root,text='name').grid(row=2,column=0)

Button(root,text='Insert',command=put).grid(row=3,column=0)

Button(root,text='Display',command=get).grid(row=3,column=1)

root.mainloop()
