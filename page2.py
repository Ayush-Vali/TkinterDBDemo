from tkinter import *
from tkinter import messagebox
import pymysql
import tkinterproj
import page2


def table():
    con=pymysql.connect(user='root', password='abc', host='localhost', database='cus')
    cur=con.cursor()
   
    # cur.execute("insert into "+Customer.get()+"(item_name) values('"+var2.get()+"')")
    

    cur.execute("CREATE TABLE "+Customer.get()+"(item_name varchar,num int)")
                
    messagebox.showinfo("Record inserted")

    
    con.close()



def put(*arg):
    con=pymysql.connect(user='root', password='abc', host='localhost', database='cus')
    cur=con.cursor()
   
    # cur.execute("insert into "+Customer.get()+"(item_name) values('"+var2.get()+"')")
    cur.execute("insert into "+Customer.get()+"(item_name) values('"+var3.get()+"')")
    cur.execute("insert into "+Customer.get()+"(item_name) values('"+var4.get()+"')")
    cur.execute("insert into "+Customer.get()+"(item_name) values('"+var5.get()+"')")
    cur.execute("insert into "+Customer.get()+"(item_name) values('"+var6.get()+"')")
    

    messagebox.showinfo("Record inserted")

    con.commit()
    con.close()


#insert total no of items 
def initems(*arg):
    con=pymysql.connect(user='root', password='abc', host='localhost', database='cus')
    cur=con.cursor()

    cur.execute("insert into "+Customer.get()+"(num) values('"+n3.get()+"')")
    cur.execute("insert into "+Customer.get()+"(num) values('"+n4.get()+"')")
    cur.execute("insert into "+Customer.get()+"(num) values('"+n5.get()+"')")
    cur.execute("insert into "+Customer.get()+"(num) values('"+n6.get()+"')")
    

    messagebox.showinfo("Record inserted")
    con.commit()
    con.close()




#total items 
def totitems():
    con=pymysql.connect(user='root', password='abc', host='localhost', database='cus')
    cur=con.cursor()

    cur.execute("SELECT SUM(num) FROM "+Customer.get()+"")
    results=cur.fetchall()
    row=cur.fetchone()

    messagebox.showinfo("Info message",results)
    
    con.close()



w1 = Tk()
#customer
l1=Label(w1,text='Enter name again',bg='white',font=("Helvetica",20),height=3,width=50).pack(side= TOP)
Customer=Entry(w1,text='Enter name',width=30,fg='black',font=12).pack(pady=20 ) 
b=Button(w1,text='Insert',command=table).pack()

def prevPage():
    w1.destroy()
    import tkinterproj

var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()



C3 = Checkbutton (w1, text = "Maggi", variable = var3, onvalue="Maggi" ,offvalue = 0, height=5, width = 20,command=put).pack(anchor='w')
#  n3=Entry(w1, text=7000, variable= num3, onvalue= 1, offvalue = 0, height=5, width = 20,command=pnum).pack(anchor='e')
n3=Entry(w1,width=30,fg='black',font=12).pack(pady=20, side= LEFT ) 
b3=Button(w1,text='insert',command=initems).pack()

C4 = Checkbutton (w1, text = "Real Mayonnaise", variable = var4, onvalue= "Real Mayonnaise",offvalue = 0, height=5, width = 20,command=put).pack(anchor='w')
n4 =Entry(w1,width=30,fg='black',font=12).pack(pady=20, side= LEFT ) 
b4=Button(w1,text='insert',command=initems).pack()


C5 = Checkbutton (w1, text = "Bread", variable = var5, onvalue= "Bread",offvalue = 0, height=5, width = 20,command=put).pack(anchor='w')
n5 =Entry(w1,width=30,fg='black',font=12).pack(pady=20, side= LEFT ) 
b5=Button(w1,text='insert',command=initems).pack()


C6 = Checkbutton (w1, text = "Kissan Jam", variable = var6, onvalue= "Kissan Jam",offvalue = 0, height=5, width = 20,command=put).pack(anchor='w')
n6 =Entry(w1,width=30,fg='black',font=12).pack(pady=20, side= LEFT )
b6=Button(w1,text='insert',command=initems).pack()



#customers total list of items
Label(w1,text='Your total items are',bg='white',font=("Helvetica",20),height=4,width=100).pack(pady=10)


b3=Button(w1,text='total items',command=totitems).pack()
b3=Button(w1,text='prev page',command=prevPage).pack()


w1.mainloop()
