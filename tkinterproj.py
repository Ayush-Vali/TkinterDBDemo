from tkinter import *
from tkinter import messagebox
import pymysql
import page2
import tkinterproj




def table():
    con=pymysql.connect(user='root', password='abc', host='localhost', database='cus')
    cur=con.cursor()
   
    # cur.execute("insert into "+Customer.get()+"(item_name) values('"+var2.get()+"')")
    

    cur.execute("CREATE TABLE +Customer.get()+(item_name varchar,num int)")
                
    messagebox.showinfo("Record inserted")

    
    con.close()


def put(*arg):
    con=pymysql.connect(user='root', password='abc', host='localhost', database='cus')
    cur=con.cursor()
   
    cur.execute("insert into "+Customer.get()+"(item_name) values('"+var1.get()+"')")
    cur.execute("insert into "+Customer.get()+"(item_name) values('"+var2.get()+"')")
    
    
    # cur.execute("select price from itemlist where itemname="+C1.get()+"")


    messagebox.showinfo("Record inserted")

    con.commit()
    con.close()


    

#insert total no of items 
def initems(*arg):
    con=pymysql.connect(user='root', password='abc', host='localhost', database='cus')
    cur=con.cursor()

    cur.execute("insert into "+Customer.get()+"(num) values('"+n1.get()+"')")
    cur.execute("insert into "+Customer.get()+"(num) values('"+n2.get()+"')")

    

    messagebox.showinfo("Record inserted")
    con.commit()
    con.close()


''' GUI  '''

w1=Tk()

def nextPage():
    w1.destroy()
    import page2



Label(w1,text='Super Market Bill generation',bg='black',font=("Helvetica",25),height=4,width=100,fg='pink').pack()


#customer
l1=Label(w1,text='Customer name',bg='white',font=("Helvetica",20),height=4,width=100).pack()
Customer=Entry(w1,text='Enter name',width=30,fg='black',font=12).pack(pady=20, side= TOP , anchor="w") 
b=Button(w1,text='Insert',command=table).pack()


#products
Label(w1,text='Select needed products and write how much needed',bg='white',font=("Bold",20),height=4,width=100).pack()
var1= IntVar()
var2 = IntVar()


C1 =Checkbutton (w1, text="Surfexel", variable= var1, onvalue= 'Surfexel', offvalue = 0, height=5, width = 20,command=put).pack(anchor='w')
n1=Entry(w1,width=30,fg='black',font=12).pack(pady=20, side= LEFT )


C2 = Checkbutton (w1, text = "Oreo", variable = var2, onvalue= 'Oreo',offvalue = 0, height=5, width = 20,command=put).pack(anchor='w')
n2=Entry(w1,width=30,fg='black',font=12).pack(pady=20, side= LEFT )
b2=Button(w1,text='insert',command=initems).pack()


Button(w1, text="Next Page", 
    font="Times",command=nextPage
    ).pack()




w1.mainloop()


#price total
# def put(*arg):
#     con=pymysql.connect(user='root', password='tiger', host='localhost', database='sya')
#     cur=con.cursor()
   
    
#     cur.execute("select price from "+l1.get()+" ")

#     messagebox.showinfo("Record inserted")

#     con.commit()
#     con.close()
