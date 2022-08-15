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

class man_choice:
    def __init__(self,winmanager):
        self.winmanager=winmanager
        self.winmanager.title('MANAGER CHOICE PAGE')
        self.winmanager.geometry('1600x1204+0+0')

        self.login_image=ImageTk.PhotoImage(Image.open('1.jpg'))
        login_label=Label(self.winmanager,image=self.login_image)
        login_label.place(x=0,y=0,relwidth=1,relheight=1)

        title_frame=Frame(self.winmanager)
        title_frame.pack()
        registration_text=Label(title_frame,text='What Would You Like To Do',font=("rockwell",30,"bold"),bd=5,borderwidth=13,bg='#7d1515',relief=RAISED)
        registration_text.pack()


        login_frame=Frame(self.winmanager,bd=10,borderwidth=7,relief=RAISED)
        login_frame.place(x=510,y=340,width=520,height=180)
        self.login_frame_img=ImageTk.PhotoImage(Image.open('Blur.jpg'))
        login_frame_label=Label(login_frame,image=self.login_frame_img)
        login_frame_label.place(anchor='center')

        movies_page=Button(login_frame,text='MANAGE MOVIES',border=5,borderwidth=5,width=15,bg='#ad1a1a',font=("rockwell",15,"bold"),command=self.movies)
        movies_page.grid(row=0,column=0,pady=15,padx=10)

        movies_earning_page=Button(login_frame,text='MOVIES EARNING',border=5,borderwidth=5,width=15,bg='#ad1a1a',font=("rockwell",15,"bold"),command=self.earning)
        movies_earning_page.grid(row=0,column=1,pady=10,padx=15)

        customer_info_page=Button(login_frame,text='CUSTOMER INFO',border=5,borderwidth=5,width=15,bg='#ad1a1a',font=("rockwell",15,"bold"),command=self.custinfo)
        customer_info_page.grid(row=1,column=0,pady=25,padx=22)

        quit=Button(login_frame,text='QUIT',border=5,borderwidth=5,width=15,bg='#ad1a1a',font=("rockwell",15,"bold"),command=self.quit)
        quit.grid(row=1,column=1,pady=22,padx=23)

    def movies(self):
        from manager_page import manage
        root0=Toplevel()
        ob1=manage(root0)
        root0.mainloop()

    def custinfo(self):
        from customer_info import cust_info
        root0=Toplevel()
        ob1=cust_info(root0)
        root0.mainloop()

    def earning(self):
        from movie_earning import m_earning
        root0=Toplevel()
        ob1=m_earning(root0)
        root0.mainloop()

    def quit(self):
        self.winmanager.destroy()



# root0=Toplevel()
# ob=man_choice(root0)
# root0.mainloop()

if __name__ =="main":    
    winearning=Tk()
    ob=man_choice(winearning)
    winearning.mainloop()        
