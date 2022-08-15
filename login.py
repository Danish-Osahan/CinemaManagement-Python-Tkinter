# Creating a login page

from cProfile import label
from email import message
from email.mime import image
from re import U
from struct import pack
from sys import maxsize
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor, dot, title, width
import tkinter.font as TkFont
import cx_Oracle
from PIL import Image,ImageTk

# Register Button function 
def register():
    from Register_form import Register
    root2=Toplevel() 
    ob2=Register(root2)
    user_name.delete(0,END)
    user_password.delete(0,END)
    root2.mainloop()



# It will Take you to the manager page 
def manager():
    from manager_choice import man_choice
    root0=Toplevel()
    ob1=man_choice(root0)
    user_name.delete(0,END)
    user_password.delete(0,END)
    root0.mainloop()

# It will take you to the registration Page
def registaration():
    from Register_form import Register
    root1=Toplevel()
    ob2=Register(root1)
    # user_name.delete(0,END)
    # user_password.delete(0,END)
    root1.mainloop()
    # Register(root0)
 

# It will take you to the customer page    
def customer_page(u_name,u_id):
    user_id=u_id
    user_name=u_name
    from customer import cust
    root2=Toplevel()
    ob3=cust(root2,user_name,user_id)
    user_password.delete(0,END)
    root2.mainloop()



# oracle connection
# def connect():
#     con=cx_Oracle.connect('cinema/danish30')
#     print(con.version)
#     cursor=con.cursor()
#     return cursor


# Cancel function
def cancel():
    check=messagebox.askquestion("Permsission",'Do you Really Want to Exit')
    if(check=='yes'):
        root.destroy()



# Login function 
def login():
    u_name=user_name.get()
    u_pass=user_password.get()
    flag=-1
    
    # checking if fields are empty or not 
    if u_name=="" and u_pass=="":
        messagebox.showwarning('Login Error','Username And Password Required')

    # checking if MANAGER has acess the system
    elif u_name=='manager' and u_pass=="man123":
        
        print('manager has acessed the system')
        manager()
        
        
    # Creting or checking a customer 
    elif u_name!="" and u_pass!="":
        # con=cx_Oracle.connect('cinema/danish30')
        # print(con.version)
        # cursor=con.cursor()
        # cursor.execute('select * from password')
        # l=cursor.fetchall()
        # user_cursor=connect()
        con=cx_Oracle.connect('cinema/danish30')
        print(con.version)
        user_cursor=con.cursor()
        user_cursor.execute('select * from password')
        l=user_cursor.fetchall()
        user_id=0
        # user_id=l[2]
        # print(user_id)
        for i in l:
        #checking the USERNAME in the database 
            if(u_name==i[0]) and(u_pass==i[1]):
                user_id=i[2]
                print(user_id)
                flag=1
                break
        if(flag==1):
            customer_page(u_name,user_id)
            
        #  if username is not in the database then go to registration page
        else:
            user_check=messagebox.showerror('User Error','USER NOT FOUND')
            a=messagebox.askquestion('REGISTER','WANT TO REGISTER')
            if(a=='yes'):
                # Going to Registration page
                registaration()
                
                
                
                
            
        


root=Tk()
root.geometry('1600x1204+0+0')
root.title("LOGIN PAGE")
# root.minsize(1255,944)
# root.maxsize(1255,944)
# root.resizable(0,0)
# "magneto",30,"bold"

font=TkFont.Font(family="Bold",weight="bold")
# title_font=TkFont.Font(family="Comic Sans MS",weight="bold")
title_font=("Arial Greek",30,"bold","italic")





login_image=ImageTk.PhotoImage(Image.open('1.jpg'))
login_label=Label(root,image=login_image).place(x=0,y=0,relwidth=1,relheight=1)

# CANVAS PORTION
# login_canvas=Canvas(root,width=200,height=200)
# login_icon=PhotoImage(file="b.png")
# login_canvas.create_image((130,150),image=login_icon)
# login_canvas.pack()


login_frame=Frame(root,bd=10,borderwidth=7,relief=RAISED)
login_frame.place(x=510,y=340,width=520)
login_frame_img=ImageTk.PhotoImage(Image.open('Blur.jpg'))
login_frame_label=Label(login_frame,image=login_frame_img)
login_frame_label.place(anchor='center')

# Title frame
title_frame=Frame(root)
title_frame.pack()
title_text=Label(title_frame,text='Welcome To AGC Cinema',font=("rockwell",30,"bold"),bd=5,borderwidth=13,bg='#7d1515',relief=RAISED)
title_text.pack()

# Username and Passwords inputs
username=Label(login_frame,text='USERNAME :-',relief=RAISED,font=("rockwell",14,"bold"),bg='#6f747d',bd=4,width=14)
password=Label(login_frame,text='PASSWORD :-',relief=RAISED,font=("rockwell",14,"bold"),bg='#6f747d',bd=4,width=14)

user_name=Entry(login_frame,border=5,width=40,borderwidth=4,bg='#7d1515',relief=RIDGE,fg='white',font=("times new roman",9,"bold"))
user_password=Entry(login_frame,border=5,width=40,show='*',bg='#7d1515',relief=RIDGE,fg='white',font=("times new roman",9,"bold"))

username.grid(row=0,column=0,padx=21,pady=10)
password.grid(row=1,column=0)
user_name.grid(row=0,column=1,padx=20)
user_password.grid(row=1,column=1,padx=10)

# creating LOGIN button
login_button=Button(login_frame,text='Login',border=5,borderwidth=5,width=10,bg='#5e6269',font=("rockwell",14,"bold"),command=login)
login_button.grid(row=2,column=1,pady=10)

# Creating Cancel Button
cancel_button=Button(login_frame,text='Cancel',border=5,borderwidth=5,width=10,bg='#ad1a1a',font=("rockwell",14,"bold"),command=cancel)
cancel_button.grid(row=3,column=1)

# register label
register_button=Button(login_frame,text="Register Now",font=("rockwell",14,"bold"),bg='#ad1a1a',border=5,borderwidth=5,command=registaration)
register_button.grid(row=3,column=0)




root.mainloop()


