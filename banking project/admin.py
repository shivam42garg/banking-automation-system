from tkinter import *
from PIL import Image,ImageTk
import pymysql.cursors
from tkinter import messagebox
import forgot_pass
import menu

class admin_class:
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
        
        self.l1=Label(self.root,text='Welcome Admin..',background='gray85',foreground='gray20',font=('Times New Roman',40,'bold','underline'))
        self.l1.place(x=150,y=10)
        
        self.l2=Label(self.root,text='Admin Id :',background='gray85',foreground='gray40',font=('Times New Roman',25,'bold'))
        self.l2.place(x=150,y=150)
        self.e2=Entry(self.root,width=40)
        self.e2.place(x=350,y=160,height=28)
        
        self.l3=Label(self.root,text='Password :',background='gray85',foreground='gray40',font=('Times New Roman',25,'bold'))
        self.l3.place(x=150,y=220)
        self.e3=Entry(self.root,width=40,show='*')
        self.e3.place(x=350,y=230,height=28)
        
        self.b1=Button(self.root,text='Log In',command=self.login,background='gray85',foreground='black',font=('Times New Roman',12),width=10)
        self.b1.place(x=350,y=280)
        
        self.b2=Button(self.root,text='Forget Password',command=self.forget1,background='gray85',foreground='black',font=('Times New Roman',14),width=17)
        self.b2.place(x=350,y=340)
        
        self.root.mainloop()
        ####################################################################################################################
        
        
    def login(self):
        xy=self.e2.get()
        yx=self.e3.get()
        if xy=='' or yx=='':
            messagebox.showerror('error', 'entry fields can`t be empty')
            self.clear()
        else:
            self.cursor.execute('select * from admin where admid=(%s) and pwd=(%s)',(xy,yx))
            self.con.commit()
            if self.cursor.rowcount==0:
                messagebox.showerror('error','invalid id or password !' )
                self.clear()
            else:
                self.root.destroy()
                menu.menu_class(xy)
                
    def forget1(self):
        self.root.destroy()
        obj = forgot_pass.forget_class()
    def clear(self):
        self.e2.delete(0, END)
        self.e3.delete(0,END)



        
