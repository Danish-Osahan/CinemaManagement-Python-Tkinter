from cProfile import label
from dataclasses import InitVar
from email import message
from email.mime import image
from operator import imatmul
from platform import release
from re import L
from struct import pack
from sys import maxsize
from tkinter import *
from tkinter import messagebox
from tokenize import String
from turtle import bgcolor, dot, title, up, width
import tkinter.font as TkFont
from tkinter import ttk
from typing import List
from webbrowser import BackgroundBrowser
import cx_Oracle
from PIL import Image,ImageTk


class cust_info:
    def __init__(self,winearning):
        self.winearning=winearning
        self.winearning.title("Customer Info")
        self.winearning.geometry('1600x1204+0+0')

        self.login_image=ImageTk.PhotoImage(Image.open('4.jpg'))
        login_label=Label(self.winearning,image=self.login_image)
        login_label.place(x=0,y=0,relwidth=1,relheight=1)
        # Title Frame//////////////////////////////////////////////////////////////////
        title_frame=Frame(self.winearning)
        title_frame.pack()
        registration_text=Label(title_frame,text='Customer Info/...../Page',font=("rockwell",30,"bold"),bd=5,borderwidth=13,bg='#7d1515',relief=RAISED)
        registration_text.pack()

        quit_buttom=Button(self.winearning,text="QUIT AND GO BACK",bd=7,borderwidth=9,bg='#ad1a1a',width=22,font=("rockwell",14,"bold"),command=self.quit)
        quit_buttom.place(x=620,y=720)


       
        f2=Frame(self.winearning,bd=4,borderwidth=12,relief=RAISED,bg='#5e6269')
        f2.place(x=373,y=130,width=800,height=560)   
        scroll_x=Scrollbar(f2,orient=HORIZONTAL)
        scroll_y=Scrollbar(f2,orient=VERTICAL)

        self.Movie_Table=ttk.Treeview(f2,columns=("CUST_ID","USERNAME","SEATS","MOVIE_BOOKED"),yscrollcommand=scroll_y.set)

        # scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        # scroll_x.config(command=self.Movie_Table.xview)
        scroll_y.config(command=self.Movie_Table.yview)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("rockwell",13,"bold"),fieldbackground='#ad1a1a',background='#ad1a1a')
        style.configure("Treeview",background='#5e6269',fieldbackground='#5e6269',fieldforground="white",forground="white",font=("rockwell",12,"bold"))

        self.Movie_Table.heading("CUST_ID",text="CUST_ID")
        self.Movie_Table.heading("USERNAME",text="USERNAME")
        self.Movie_Table.heading("SEATS",text="SEATS")
        self.Movie_Table.heading("MOVIE_BOOKED",text="MOVIE_BOOKED")
        self.Movie_Table['show']="headings"
        self.Movie_Table.column("CUST_ID",width=80)
        self.Movie_Table.column("USERNAME",width=200)
        self.Movie_Table.column("SEATS",width=120)
        self.Movie_Table.column("MOVIE_BOOKED",width=100)
        self.Movie_Table.pack(fill=BOTH,expand=1)
        self.fetch_data()

    def fetch_data(self):
        con=cx_Oracle.connect("cinema/danish30")
        cur=con.cursor()
        cur.execute(" SELECT CUSTID,USERNAME,SEATS,MOVIE_BOOKED FROM CUSTOMER")
        rows = cur.fetchall()
        if (rows)!=0:
            self.Movie_Table.delete(*self.Movie_Table.get_children())
            for row in rows:
                self.Movie_Table.insert('',END,values=row)
            con.commit()
        con.close()    

    def quit(self):
        self.winearning.destroy()   













# root0=Toplevel()
# ob=cust_info(root0)
# root0.mainloop()

if __name__ =="main":    
    winearning=Tk()
    ob=cust_info(winearning)
    winearning.mainloop()

