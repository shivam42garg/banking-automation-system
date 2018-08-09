from tkinter import *
from PIL import Image,ImageTk
import pymysql.cursors
from tkinter import messagebox
import admin
class forget_class:
    def __init__(self):
        self.con=pymysql.connect(host='localhost',user='root',password='root',db='demo')
        self.cursor=self.con.cursor()
        ##############################################################################################  TKINTER WORK
        self.root=Tk()
        self.root.title('SG.. BANKS')
        self.root.geometry('700x600+350+100')
        self.root.config(background='gray85')
        self.root.resizable(False, False)
        
        img=Image.open('d:/1.png')
        img1=img.resize((100,100),Image.ANTIALIAS)
        a=ImageTk.PhotoImage(img1)
        
        
        self.f1=Frame(self.root,bg='gray85')
        self.f1.place(x=1,y=1,height=599,width=699)
        self.l1=Label(self.f1,text='Forgot Password ..',background='gray85',foreground='gray20',font=('Times New Roman',40,'bold','underline'))
        self.l1.place(x=150,y=10)
        self.l2=Label(self.f1,text='      Enter Id :',background='gray85',foreground='gray40',font=('Times New Roman',20,'bold'))
        self.l2.place(x=150,y=100)
        self.e2=Entry(self.f1,width=40)
        self.e2.place(x=350,y=108,height=23)
        self.b1=Button(self.f1,text='Validate Id',command=self.validate,background='gray85',foreground='black',font=('Times New Roman',10),width=8)
        self.b1.place(x=350,y=140)
        
        self.f2=Frame(self.f1,bg='gray85')
        self.f2.place(x=1,y=170,height=449,width=699)
        self.l3=Label(self.f2,text='Your Security Question :',background='gray85',foreground='gray40',font=('Times New Roman',15,'bold'))
        self.l3.place(x=100,y=10)
        self.e3=Entry(self.f2,width=40)
        self.e3.place(x=350,y=15,height=20)
        self.l4=Label(self.f2,text='   Your Security Answer :',background='gray85',foreground='gray40',font=('Times New Roman',15,'bold'))
        self.l4.place(x=100,y=50)
        self.e4=Entry(self.f2,width=40)
        self.e4.place(x=350,y=55,height=20)
        self.b2=Button(self.f2,text='Check',background='gray85',foreground='black',font=('Times New Roman',10),width=10,command=self.check)
        self.b2.place(x=350,y=90)
        self.f2.place_forget()
        
        self.f3=Frame(self.f2,bg='gray85')
        self.f3.place(x=1,y=150,height=310,width=699)
        self.l5=Label(self.f3,text='     New Password :',background='gray85',foreground='gray40',font=('Times New Roman',15,'bold'))
        self.l5.place(x=150,y=10)
        self.e5=Entry(self.f3,width=40,show='*')
        self.e5.place(x=350,y=13,height=22)
        self.l6=Label(self.f3,text='Confirm Password :',background='gray85',foreground='gray40',font=('Times New Roman',15,'bold'))
        self.l6.place(x=150,y=60)
        self.e6=Entry(self.f3,width=40,show='*')
        self.e6.place(x=350,y=64,height=22)
        self.b3=Button(self.f3,text='Set Password',background='gray85',foreground='black',font=('Times New Roman',12),width=15,command=self.set)
        self.b3.place(x=350,y=100)
        self.f3.place_forget()
        
        self.root.mainloop()
        ####################################################################################################################
        
    def validate(self):
        id=self.e2.get()
        if id=='':
            messagebox.showerror('error','please enter value in id field !')
        else :
            self.cursor.execute('select * from admin where admid=(%s)',(id,))
            self.con.commit()
            if self.cursor.rowcount==0:
                messagebox.showwarning('warning','invalid id entered')
                self.e2.delete(0,END)
            else:
                self.f2.place(x=1,y=170,height=449,width=699)
                messagebox.showinfo('info','answer your security question !')
                self.cursor.execute('select secques from admin where admid=(%s)',(id,))
                self.con.commit()
                row=self.cursor.fetchone()
                self.e3.config(state='normal')
                self.e3.delete(0,END)
                self.e3.insert(0,row)
                self.e3.config(state='disable')
    
    def check(self):
        chk=self.e4.get()
        if chk=='':
            messagebox.showerror('error','please enter your response !')
        else:
            self.cursor.execute('select pwd from admin where secans=(%s) and admid=(%s)',(chk,self.e2.get()))
            self.con.commit()
            if self.cursor.rowcount==0:
                messagebox.showwarning('warning','invalid answer !')
                self.e4.delete(0,END)
            else:
                self.f3.place(x=1,y=150,height=310,width=699)
                self.e4.config(state='disable')
                messagebox.showinfo('update','Enter New Password !')
                
    def set(self):
        pas=self.e5.get()
        conpas=self.e6.get()
        if pas=='' or conpas=='':
            messagebox.showerror('error',' enter both the fields !')
        else:
            if pas!=conpas:
                messagebox.showerror('error','password and confirm password should be same , try again !')
                self.e5.delete(0,END)
                self.e6.delete(0,END)
            else:
                self.cursor.execute('update admin set pwd=(%s)',(pas,))
                self.con.commit()
                messagebox.showinfo('info','password sucessfully changed !\n please login again !')
                self.root.destroy()
                admin.admin_class() 
     
    def clear(self):
        self.e2.delete(0, END)
        self.e3.delete(0,END)

        
#forget()
