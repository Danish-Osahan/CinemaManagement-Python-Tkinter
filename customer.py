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

class cust:
    def __init__(self,wincustomer,u_name,u_id):

        self.wincustomer=wincustomer
        self.wincustomer.geometry('1600x1204+0+0')
        self.wincustomer.title("Customer Page")

        self.login_image=ImageTk.PhotoImage(Image.open('4.jpg'))
        login_label=Label(self.wincustomer,image=self.login_image)
        login_label.place(x=0,y=0,relwidth=1,relheight=1)

        
        # Variables to be used/////////////////////////////////////////////////////////////////////////
        global price
        # price=0
        self.user_id=u_id
        self.user_name=u_name
        self.postmovid_var=StringVar()
        self.seat_var=IntVar()
        self.type_var=StringVar()
        self.show_var=StringVar()
        self.price_var=IntVar()
        
        # QUIT BUTTON
        quit_button=Button(self.wincustomer,text='QUIT AND GO BACK',border=5,borderwidth=5,width=18,bg='#ad1a1a',font=("rockwell",15,"bold"),command=self.quit)
        quit_button.place(x=1080,y=750)
        

        # Movie info Frame///////////////////////////////////////////////////////////////////////////// 
        f1=Frame(self.wincustomer,bd=0,relief=RAISED,borderwidth=0,bg='#5e6269')
        f1.place(x=30,y=130,width=850,height=640)

        self.register_frame_image=ImageTk.PhotoImage(Image.open('3.jpg'))
        register_frame_label=Label(f1,image=self.register_frame_image)
        register_frame_label.place(x=0,y=0,relwidth=1,relheight=1)


        # Title////////////////////////////////////////////////////////////////////////////////////
        title_frame=Frame(self.wincustomer)
        title_frame.pack()
        registration_text=Label(title_frame,text='Ticket Booking/...../Page',font=("rockwell",30,"bold"),bd=5,borderwidth=13,bg='#7d1515',relief=RAISED)
        registration_text.pack()
        
        # f2=Frame(f1)
        # f2.place(x=250,y=190,width=270,height=370)

        # self.img=ImageTk.PhotoImage(Image.open("MOV1001.png"))
        # l=Label(f2,image=self.img)
        # l.pack(expand=True,fill=BOTH)

        id_label=Label(f1,text="SELECT THE MOVIE :-",bd=5,borderwidth=5,bg='#ad1a1a',relief=SUNKEN,font=("rockwell",12,"bold"))
        id_label.place(x=320,y=10)
        id_entry=Entry(f1,textvariable=self.postmovid_var,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        id_entry.place(x=560,y=10)

        enter_button=Button(f1,text="ENTER",bd=5,borderwidth=5,bg='#ad1a1a',font=("rockwell",12,"bold"),width=7,relief=RAISED,command=lambda: self.postview(f1))
        enter_button.place(x=740,y=10)

       
        #Tree view Frame////////////////////////////////////////////////////////////////////////////////
        
        f2=Frame(self.wincustomer,bd=4,borderwidth=12,relief=RIDGE,bg='#5e6269')
        f2.place(x=950,y=130,width=500,height=560)   
        scroll_x=Scrollbar(f2,orient=HORIZONTAL)
        scroll_y=Scrollbar(f2,orient=VERTICAL)

        self.Movie_Table=ttk.Treeview(f2,columns=("ID","NAME","R_DATE","SEATS","THEATRE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Movie_Table.xview)
        scroll_y.config(command=self.Movie_Table.yview)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("times new roman",13,"bold"),fieldbackground='#ad1a1a',background='#ad1a1a')
        style.configure("Treeview",background='#5e6269',fieldbackground='#5e6269',fieldforground="white",forground="white",font=("times new roman",12,"bold"))

        self.Movie_Table.heading("ID",text="ID")
        self.Movie_Table.heading("NAME",text="NAME")
        self.Movie_Table.heading("R_DATE",text="R_DATE")
        self.Movie_Table.heading("SEATS",text="SEATS")
        self.Movie_Table.heading("THEATRE",text="THEATRE")
        self.Movie_Table['show']="headings"
        self.Movie_Table.column("ID",width=80)
        self.Movie_Table.column("NAME",width=200)
        self.Movie_Table.column("R_DATE",width=120)
        self.Movie_Table.column("SEATS",width=80)
        self.Movie_Table.column("THEATRE",width=120)
        self.Movie_Table.bind("<ButtonRelease-1>",self.get_data)
        self.Movie_Table.pack(fill=BOTH,expand=1)
        self.fetch_data()




    def fetch_data(self):
        con=cx_Oracle.connect("cinema/danish30")
        cur=con.cursor()
        cur.execute(" select movie_id,movie_name,release_date,seats,theatre from movie_details")
        rows = cur.fetchall()
        if (rows)!=0:
            self.Movie_Table.delete(*self.Movie_Table.get_children())
            for row in rows:
                self.Movie_Table.insert('',END,values=row)
            con.commit()
        con.close()

    def get_data(self,event):
        cursor_row=self.Movie_Table.focus()
        contents=self.Movie_Table.item(cursor_row)
        row=contents['values']
        self.postmovid_var.set(row[0])

    def postview(self,f1):
        self.f1=f1
        try:
            M=self.postmovid_var.get()
            con=cx_Oracle.connect("cinema/danish30")
            cur=con.cursor()
            
            cur.execute("select * from Movie_Details where MOVIE_ID LIKE '%s'"%M)
            rows = cur.fetchall()
            
            if len(rows)!=0:
                # print(rows)
                # for row in rows:
                #     print(row)
                self.showpost_func(rows,self.f1)
            else:
                messagebox.showerror("Error",f"Movie with MOVIE ID: '{M}' Not Found !!!",parent=self.wincustomer)
            con.commit()
            con.close()
        except:
            import sys
            print(sys.exc_info())

    def showpost_func(self,ls,f1):
        self.f1=f1
        movid=ls[0][0]
        movie_name=ls[0][1]

        if self.isposterexits(movid):

            self.postpic=ImageTk.PhotoImage(file=f"{movid}.png")
            post_lbl=Label(self.f1,image=self.postpic,bd=0)
            post_lbl.place(x=40,y=140)
            
            #post_lbl.destroy()
            #post_lbl=Label(self.winposter,image=self.postpic,bd=0)
            #post_lbl.place(x=250,y=180)
        else:
            self.postpic=ImageTk.PhotoImage(file="posternotavailable.png")
            post_lbl=Label(self.f1,image=self.postpic,bd=0)
            post_lbl.pack(expand=True,fill=BOTH)

        lblname=Label(self.f1,text="Movie Name :-",bg='#ad1a1a',font=("rockwell",12,"bold"),width=13,relief=RAISED,bd=7,borderwidth=7)
        lblname.place(x=385,y=80)  

        txt_name=Label(self.f1,text=ls[0][1],bg='#ad1a1a',font=("times new roman",13,"bold"),width=25,relief=SUNKEN,bd=7,borderwidth=7,fg='white',anchor="w")
        txt_name.place(x=577,y=78)

        lbltype=Label(self.f1,text="Movie Type :-",bg='#ad1a1a',font=("rockwell",12,"bold"),width=13,relief=RAISED,bd=7,borderwidth=7)
        lbltype.place(x=385,y=135)

        txt_type=Label(self.f1,text=ls[0][2],bg='#ad1a1a',font=("times new roman",13,"bold"),width=25,relief=SUNKEN,bd=7,borderwidth=7,fg='white',anchor="w")
        txt_type.place(x=577,y=133)
        
        lblactor=Label(self.f1,text="ACTOR :-",bg='#ad1a1a',font=("rockwell",12,"bold"),width=13,relief=RAISED,bd=7,borderwidth=7)
        lblactor.place(x=385,y=185)

        txt_actor=Label(self.f1,text=ls[0][4],bg='#ad1a1a',font=("times new roman",13,"bold"),width=25,relief=SUNKEN,bd=7,borderwidth=7,fg='white',anchor="w")
        txt_actor.place(x=577,y=184)

        lblactoress=Label(self.f1,text="ACTRESS :-",bg='#ad1a1a',font=("rockwell",12,"bold"),width=13,relief=RAISED,bd=7,borderwidth=7)
        lblactoress.place(x=385,y=235)

        txt_actoress=Label(self.f1,text=ls[0][5],bg='#ad1a1a',font=("times new roman",13,"bold"),width=25,relief=SUNKEN,bd=7,borderwidth=7,fg='white',anchor="w")
        txt_actoress.place(x=577,y=233)

        lbldirector=Label(self.f1,text="DIRECTOR :-",bg='#ad1a1a',font=("rockwell",12,"bold"),width=13,relief=RAISED,bd=7,borderwidth=7)
        lbldirector.place(x=385,y=285)

        txt_director=Label(self.f1,text=ls[0][6],bg='#ad1a1a',font=("times new roman",13,"bold"),width=25,relief=SUNKEN,bd=7,borderwidth=7,fg='white',anchor="w")
        txt_director.place(x=577,y=282)

        seats_label=Label(self.f1,text=" TICKETS :-",bd=5,borderwidth=5,bg='#ad1a1a',font=("rockwell",12,"bold"),width=13,relief=RAISED)
        seats_label.place(x=385,y=340)
        seats_label_entry=Entry(self.f1,textvariable=self.seat_var,bg='#ad1a1a',font=("times new roman",13,"bold"),width=20,relief=SUNKEN,bd=7,borderwidth=7,fg='white')
        seats_label_entry.place(x=577,y=338)

        type_label=Label(self.f1,text=" SEAT TYPE :-",bd=5,borderwidth=5,bg='#ad1a1a',font=("rockwell",12,"bold"),width=13,relief=RAISED)
        type_label.place(x=385,y=395)
        # type_label_entry=Entry(self.f1,textvariable=self.type_var,bg='#ad1a1a',font=("times new roman",13,"bold"),width=20,relief=SUNKEN,bd=7,borderwidth=7,fg='white')
        # type_label_entry.place(x=577,y=390)

        type_label_entry=ttk.Combobox(self.f1,textvariable=self.type_var,width=20,font=("times new roman",13,"bold"))
        type_label_entry['values']=('Premium','Normal' )
        # type_label_entry.current(1)
        type_label_entry.place(x=577,y=395)


        show_label=Label(self.f1,text=" SHOW :-",bd=5,borderwidth=5,bg='#ad1a1a',font=("rockwell",12,"bold"),width=13,relief=RAISED)
        show_label.place(x=385,y=450)

        # show_label_entry=Entry(self.f1,textvariable=self.show_var,bg='#ad1a1a',font=("times new roman",13,"bold"),width=20,relief=SUNKEN,bd=7,borderwidth=7,fg='white')
        # show_label_entry.place(x=577,y=444)

        show_label_entry=ttk.Combobox(self.f1,textvariable=self.show_var,width=20,font=("times new roman",13,"bold"))
        show_label_entry['values']=('Morning','Evening','Night')
        show_label_entry.place(x=577,y=450)


        price_label=Button(self.f1,text=" Price :-",bd=5,borderwidth=5,bg='#ad1a1a',font=("rockwell",12,"bold"),width=13,relief=RAISED,command=self.price)
        price_label.place(x=385,y=505)
        price_label_entry=Entry(self.f1,text=self.price_var,bg='#ad1a1a',font=("times new roman",13,"bold"),width=20,relief=SUNKEN,bd=7,borderwidth=7,fg='white')
        price_label_entry.place(x=577,y=505)


        
        BOOK_button=Button(self.f1,text="BOOK NOW",bd=5,borderwidth=5,bg='#ad1a1a',font=("rockwell",12,"bold"),relief=RAISED,width=15,command=lambda:self.booking(movie_name,self.user_id))
        BOOK_button.place(x=565,y=568)


        

        # lblname=Label(self.self.f1,bg='#ad1a1a',font=("magneto",12,"bold"),width=7,relief=RAISED)
        # lblname.place(x=440,y=40)   



    # Price logic for tickets
    def price(self):
        if self.seat_var.get()==0 or self.show_var.get()=="" or self.type_var.get()=="":
            messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.wincustomer)
        else:
            
            seat=self.seat_var.get()
            type=self.type_var.get()
            show=self.show_var.get()
            
            if type=='Normal' and show=='Morning':
                price=250*seat
                self.price_var.set(price)
               
            elif type=='Premium' and show=='Morning':
                price=300*seat
                self.price_var.set(price)

            elif type=='Normal' and show=='Evening':

                price=300*seat
                self.price_var.set(price)      
            
            elif type=='Premium' and show=='Evening':

                price=350*seat
                self.price_var.set(price)
                
            elif type=='Normal' and show=='Night':

                price=350*seat
                self.price_var.set(price) 
            
            elif type=='Premium' and show=='Night':

                price=400*seat
                self.price_var.set(price)
                    

            


    def booking(self,m_name,u_id):
        if self.seat_var.get()=="" or self.type_var.get()=="" or self.show_var.get()=="":
            messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.wincustomer)

        else:
            M=self.postmovid_var.get()
            user_id=u_id
            
            self.movie_name=m_name
            seat=self.seat_var.get()
            type=self.type_var.get()
            show=self.show_var.get()
            
            con=cx_Oracle.connect("cinema/danish30")
            cur=con.cursor()
            cur.execute("select seats from movie_details where movie_id=:id",id=M)
            row=cur.fetchall()
            if(seat>row[0][0]):
                messagebox.showinfo("UNAVIALABLE",'NOT ENOUGH SEATS')
            else:
                
                if type=='Normal' and show=='Morning':
                    price=250*seat
                    cur.execute("update customer set seats= seats+:s ,movie_booked=:m where custid= :id",id=user_id,s=seat,m=self.movie_name)
                    cur.execute("UPDATE movie_earning SET total_earning= total_earning+ :p ,seats_booked=seats_booked+ :st where  movie_id= :id",p=price,st=seat,id=M)
                    seat=row[0][0]-seat
                    cur.execute("update movie_details set seats=:st where movie_id=:m",st=seat,m=M)
                    con.commit()
                    messagebox.showinfo("SUCCESS","BOOKED SUCCESSFULLY")
                    self.fetch_data()
                    con.close()
                elif type=='Premium' and show=='Morning':
                    price=300*seat  
                    cur.execute("update customer set seats=:s ,movie_booked=:m where custid= :id",id=user_id,s=seat,m=self.movie_name)
                    cur.execute("UPDATE movie_earning SET total_earning= total_earning+ :p ,seats_booked=seats_booked+ :st where  movie_id= :id",p=price,st=seat,id=M)
                    seat=row[0][0]-seat
                    cur.execute("update movie_details set seats=:st where movie_id=:m",st=seat,m=M)
                   
                    con.commit()     
                    messagebox.showinfo("SUCCESS","BOOKED SUCCESSFULLY")                                   
                    self.fetch_data()
                    con.close()
                elif type=='Normal' and show=='Evening':
                    price=300*seat
                    cur.execute("update customer set seats=:s ,movie_booked=:m where custid= :id",id=user_id,s=seat,m=self.movie_name)
                    cur.execute("UPDATE movie_earning SET total_earning= total_earning+ :p ,seats_booked=seats_booked+ :st where  movie_id= :id",p=price,st=seat,id=M)
                    seat=row[0][0]-seat
                    cur.execute("update movie_details set seats=:st where movie_id=:m",st=seat,m=M)
                   
                    con.commit()     
                    messagebox.showinfo("SUCCESS","BOOKED SUCCESSFULLY")                                   
                    self.fetch_data()
                    con.close()
                elif type=='Premium' and show=='Evening':
                    price=350*seat
                    cur.execute("update customer set seats=:s ,movie_booked=:m where custid= :id",id=user_id,s=seat,m=self.movie_name)
                    cur.execute("UPDATE movie_earning SET total_earning= total_earning+ :p ,seats_booked=seats_booked+ :st where  movie_id= :id",p=price,st=seat,id=M)
                    seat=row[0][0]-seat
                    cur.execute("update movie_details set seats=:st where movie_id=:m",st=seat,m=M)
                   
                    con.commit()   
                    messagebox.showinfo("SUCCESS","BOOKED SUCCESSFULLY")                                     
                    self.fetch_data()
                    con.close()
                elif type=='Normal' and show=='Night':
                    price=350*seat
                    cur.execute("update customer set seats=:s ,movie_booked=:m where custid= :id",id=user_id,s=seat,m=self.movie_name)
                    cur.execute("UPDATE movie_earning SET total_earning= total_earning+ :p ,seats_booked=seats_booked+ :st where  movie_id= :id",p=price,st=seat,id=M)
                    seat=row[0][0]-seat
                    cur.execute("update movie_details set seats=:st where movie_id=:m",st=seat,m=M)
                   
                    con.commit()   
                    messagebox.showinfo("SUCCESS","BOOKED SUCCESSFULLY")                                     
                    self.fetch_data()
                    con.close()
                elif type=='Premium' and show=='Night':
                    price=400*seat
                    cur.execute("update customer set seats=:s ,movie_booked=:m where custid= :id",id=user_id,s=seat,m=self.movie_name)
                    cur.execute("UPDATE movie_earning SET total_earning= total_earning+ :p ,seats_booked=seats_booked+ :st where  movie_id= :id",p=price,st=seat,id=M)
                    seat=row[0][0]-seat
                    cur.execute("update movie_details set seats=:st where movie_id=:m",st=seat,m=M)
                    con.commit()    
                    messagebox.showinfo("SUCCESS","BOOKED SUCCESSFULLY")                                    
                    self.fetch_data()
                    con.close()
            
    def isposterexits(self,mid):
        import os
        mid=mid+".png"
        #print(mid)
        return (os.path.exists(mid))


    def quit(self):
        self.wincustomer.destroy()
        













# root0=Toplevel()
# ob=cust(root0)
# root0.mainloop()

# if __name__ =="main":    
#     wincustomer=Tk()
#     ob=cust(wincustomer)
#     wincustomer.mainloop()




# root0=Toplevel()
# ob=cust(root0)
# root0.mainloop()

