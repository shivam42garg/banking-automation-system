from tkinter import *
import pymysql.cursors
from PIL import Image,ImageTk
from tkinter import messagebox
import datetime
import admin
from faulthandler import disable
class menu_class:
    def __init__(self,admid1):
        self.con=pymysql.connect(host='localhost',user='root',password='root',db='demo')
        self.cursor=self.con.cursor()
        ##############################################################################################  TKINTER WORK
        self.root=Tk()
        self.root.title('SG.. BANKS')
        self.root.geometry('700x600+350+100')
        self.root.config(background='whiteSmoke')
        self.root.option_add('*tearOff', False)
        self.root.resizable(False, False)
        self.admid=admid1
        
        
        self.fra=Frame(self.root,bg="whiteSmoke")
        self.fra.place(x=0,y=0,height=599,width=699)
        
        self.l1=Label(self.fra,text='Welcome Admin',background='whiteSmoke',foreground='gray90',font=('Times New Roman',56,'bold'))
        self.l1.place(x=90,y=10)
        
        self.l1=Label(self.fra,text='SG..BANKS',background='whiteSmoke',foreground='gray90',font=('Times New Roman',56,'bold','underline'))
        self.l1.place(x=-1,y=150)
        im=Image.open('d:\\4.jpg')
        im2=im.resize((700,300),Image.ANTIALIAS)
        im3=ImageTk.PhotoImage(im2)
        self.l1.config(image=im3,compound='center')
        
        txt1='Admin  :  '+str(self.admid)
        Label(self.fra,text=txt1,background='whiteSmoke',foreground='gray85',font=('Times New Roman',24,'bold')).place(x=300,y=550)
        
        self.root.bind('<Button-1>',self.showee1)
        
        self.mb=Menu(self.root)
        self.root.config(menu=self.mb)
        self.m1=Menu(self.mb)
        self.m2=Menu(self.mb)
        self.m3=Menu(self.mb)
        self.mb.add_cascade(menu=self.m1,label='Accounts')
        self.mb.add_cascade(menu=self.m2,label='Transactions')
        self.mb.add_cascade(menu=self.m3,label='Admin Module')
        self.mb.add_command(label='Help',command=self.help1)
        
        self.m1.add_command(label='Open New Account',command=self.openacc)
        self.m1.add_command(label='View All Accounts',command=self.viewacc)
        self.m1.add_command(label='Search Using Accno',command=self.search1)
        self.m1.add_command(label='Search Using Name',command=self.search2)
        self.m1.add_command(label='Modify Acc Details',command=self.modify)
        self.m1.add_command(label='Close account',command=self.delete)
        
        self.m2.add_command(label='Deposit',command=self.deposit)
        self.m2.add_command(label='Withdraw',command=self.withdraw)
        self.m2.add_command(label='Transfer',command=self.trans)
        self.m2.add_command(label='MiniStatement',command=self.minist)
        
        self.m3.add_command(label='Edit Profile',command=self.profile)
        self.m3.add_command(label='Edit Password',command=self.pwrd)
        self.m3.add_command(label='Edit Security Settings',command=self.sec)
        self.m3.add_command(label='Log out',command=self.lgout)
        
        self.root.mainloop()
        
 #############################################################################################################################
    def showee1(self,evt):
        self.fra.place_forget()
        self.fra.place(x=0,y=0,height=599,width=699)
 
 
 
 
 
 ##############################################################################################################################
 
        
 ###################################################################################    ACCOUNTS MENU 1   
    def openacc(self):
        self.f1=LabelFrame(self.root,text='open account',background='whiteSmoke')
        self.f1.place(x=1,y=1,height=599,width=699)
        Label(self.f1,text='Account No   :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=20)
        Label(self.f1,text='Name            :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=70)
        Label(self.f1,text='Address        :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=120)
        Label(self.f1,text='Gender          :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=170)
        Label(self.f1,text='Phone no       :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=220)
        Label(self.f1,text='Opening date :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=270)
        Label(self.f1,text='Balance         :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=320)
        
        self.e1=Entry(self.f1,width=25)
        self.e1.place(x=180,y=25)
        self.cursor.execute('select ifnull(max(accno),1000000000) from account')
        self.con.commit()
        row=self.cursor.fetchone()
        self.e1.config(state='normal')
        self.e1.insert(0,(int(row[0])+1))
        self.e1.config(state='disable')
        self.e2=Entry(self.f1,width=25)
        self.e2.place(x=180,y=75)
        self.e3=Entry(self.f1,width=25)
        self.e3.place(x=180,y=125)
        
        self.var=StringVar()
        self.var.set('Male')
        self.rb1=Radiobutton(self.f1,variable=self.var,text='Male',bg='whiteSmoke',value='Male')
        self.rb1.place(x=180,y=175)
        self.rb2=Radiobutton(self.f1,variable=self.var,text='Female',bg='whiteSmoke',value='Female')
        self.rb2.place(x=240,y=175)
       # self.e4=Entry(self.f1,width=25)
        #self.e4.place(x=180,y=175)
        self.e5=Entry(self.f1,width=25)
        self.e5.place(x=180,y=225)
        self.e6=Entry(self.f1,width=25)
        self.e6.place(x=180,y=275)
        self.e7=Entry(self.f1,width=25)
        self.e7.place(x=180,y=325)
        
        self.b1=Button(self.f1,text='Save',font=('Times New Roman',20),bg='whiteSmoke',command=self.r1)
        self.b1.place(x=180,y=370,width=100)
    
    def r1(self):
        if  self.e2.get()=='' or self.e3.get()==''  or self.e5.get()=='' or self.e6.get()=='' or self.e7.get()=='' :
            messagebox.showerror('error', 'values can`t be empty !')
        else:
            try:        
                if len(str(self.e5.get()))!=10:
                    messagebox.showerror('error','enter 10 digits value for phone field ! ')
                else:
                    bsd=int(self.e5.get())
                    jkjkj=int(self.e7.get())
                    self.e1.config(state='normal')
                    self.cursor.execute('insert into account values(%s,%s,%s,%s,%s,%s,%s)',(self.e1.get(),self.e2.get(),self.e3.get(),self.var.get(),self.e5.get(),self.e6.get(),self.e7.get()))
                    self.con.commit()
                    #self.e1.config(state='disable')
                    messagebox.showinfo('info', 'account opened !')
                    self.e1.delete(0,END)
                    self.e2.delete(0,END)
                    self.e3.delete(0,END)
                    #self.e4.delete(0,END)
                    self.e5.delete(0,END)
                    self.e6.delete(0,END)
                    self.e7.delete(0, END)
                    self.cursor.execute('select ifnull(max(accno),1000000000) from account')
                    self.con.commit()
                    row=self.cursor.fetchone()
                    self.e1.config(state='normal')
                    self.e1.insert(0,(int(row[0])+1))
                    self.e1.config(state='disable')
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value !')
        
    def viewacc(self):
        self.f2=LabelFrame(self.root,text='view accounts',background='whiteSmoke')
        self.f2.place(x=1,y=1,height=599,width=699)
        Label(self.f2,text='Account number : \n\nName :\n\nAddress :\n\nGender :\n\nPhone number :\n\nOpening date :\n\nBalance :',bg='whiteSmoke',font=('Times New Roman',20)).place(x=10,y=10)
        
        self.cursor.execute('select * from account')
        self.con.commit()
        row=self.cursor.fetchone()
        msg=''
        msg=msg+str(row[0]) +'\n\n'  +str(row[1])+ '\n\n'    +str(row[2]) + '\n\n'   +str(row[3]) +'\n\n'   +str(row[4]) +'\n\n'   +str(row[5]) + '\n\n'  + str(row[6])+'\n'
        Label(self.f2,text=msg,bg='whiteSmoke',fg='gray40',font=('Times New Roman',20)).place(x=250,y=10)
        
        Button(self.f2,text='Next',font=('Times New Roman',15),bg='whiteSmoke',command=self.nxt).place(x=250,y=500)
    
    
    def nxt(self):
        tp=(1,2)
        row=self.cursor.fetchone()
        if type(row)!=type(tp):
            messagebox.showinfo('info', 'No data left to show !')
        else:
            msg=''
            msg=msg+str(row[0]) +'\n\n'  +str(row[1])+ '\n\n'    +str(row[2]) + '\n\n'   +str(row[3]) +'\n\n'   +str(row[4]) +'\n\n'   +str(row[5]) + '\n\n'  + str(row[6])+'\n'
            Label(self.f2,text=msg,bg='whiteSmoke',fg='gray40',font=('Times New Roman',20)).place(x=250,y=10)
        
        
    def search1(self):
        self.f3=LabelFrame(self.root,text='search',background='whiteSmoke')
        self.f3.place(x=1,y=1,height=599,width=699)
        self.l2=Label(self.f3,text='Enter Accountno :',bg='whiteSmoke',font=('Times New Roman',24))
        self.l2.place(x=30,y=30)
        self.e8=Entry(self.f3,width=40)
        self.e8.place(x=300,y=42,height=25)
        
        self.fr=Frame(self.f3,bg='whiteSmoke')
        self.fr.place(x=1,y=200,height=390,width=690)
        Label(self.fr,text='Account number : \n\nName :\n\nAddress :\n\nGender :\n\nPhone number :\n\nOpening date :\n\nBalance :',bg='whiteSmoke',font=('Times New Roman',14)).place(x=50,y=10)
        self.fr.place_forget()
        
        Button(self.f3,text='Check',font=('Times New Roman',15),bg='whiteSmoke',command=self.chk).place(x=300,y=75)
    
    def chk(self):
        self.fr.place_forget()
        a=self.e8.get()
        if a=='':
            messagebox.showerror('error', 'entry can`t be empty !')
        else:
            try:
                alkj=int(self.e8.get())
                self.cursor.execute('select * from account where accno=(%s)',(a,))
                self.con.commit()
                if self.cursor.rowcount==0:
                    messagebox.showinfo('info', 'account does not exist')
                    self.e8.delete(0, END)
                else :
                    row=self.cursor.fetchone()
                    msg=''
                    msg=msg+str(row[0]) +'\n\n'  +str(row[1])+ '\n\n'    +str(row[2]) + '\n\n'   +str(row[3]) +'\n\n'   +str(row[4]) +'\n\n'   +str(row[5]) + '\n\n'  + str(row[6])+'\n'
                    Label(self.fr,text=msg,bg='whiteSmoke',fg='gray40',font=('Times New Roman',14)).place(x=220,y=10)
                    self.fr.place(x=1,y=200,height=390,width=690)
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value !')
    
    def search2(self):
        self.f4=LabelFrame(self.root,text='search',background='whiteSmoke')
        self.f4.place(x=1,y=1,height=599,width=699)
        Label(self.f4,text='Enter Customer Name :',bg='whiteSmoke',font=('Times New Roman',24)).place(x=30,y=30)
        self.e9=Entry(self.f4,width=40)
        self.e9.place(x=350,y=42,height=25)
        
        self.fr=Frame(self.f4,bg='whiteSmoke')
        self.fr.place(x=1,y=200,height=390,width=690)
        Label(self.fr,text='Account number : \n\nName :\n\nAddress :\n\nGender :\n\nPhone number :\n\nOpening date :\n\nBalance :',bg='whiteSmoke',font=('Times New Roman',14)).place(x=50,y=10)
        self.fr.place_forget()
        
        Button(self.f4,text='Check',font=('Times New Roman',15),bg='whiteSmoke',command=self.chk1).place(x=350,y=75)
        
        
        
    def chk1(self):
        self.fr.place_forget()
        a=self.e9.get()
        if a=='':
            messagebox.showerror('error', 'entry can`t be empty !')
        else:
            try:
                msg="select * from account where name like '{0}%'".format(a)
                self.cursor.execute(msg)
                self.con.commit()
                if self.cursor.rowcount==0:
                    messagebox.showinfo('info', 'account does not exist')
                    self.e9.delete(0, END)
                else:
                    row=self.cursor.fetchone()
                    msg=''
                    msg=msg+str(row[0]) +'\n\n'  +str(row[1])+ '\n\n'    +str(row[2]) + '\n\n'   +str(row[3]) +'\n\n'   +str(row[4]) +'\n\n'   +str(row[5]) + '\n\n'  + str(row[6])+'\n'
                    Label(self.fr,text=msg,bg='whiteSmoke',fg='gray40',font=('Times New Roman',14)).place(x=220,y=10)
                    self.fr.place(x=1,y=200,height=390,width=690)
                    Button(self.fr,text='Next',font=('Times New Roman',15),bg='whiteSmoke',command=self.nxxt).place(x=250,y=300)
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value !')
                
    def nxxt(self):
        tp=(1,2)
        row=self.cursor.fetchone()
        if type(row)!=type(tp):
            messagebox.showinfo('info', 'No data left to show !')
        else:
            msg=''
            msg=msg+str(row[0]) +'\n\n'  +str(row[1])+ '\n\n'    +str(row[2]) + '\n\n'   +str(row[3]) +'\n\n'   +str(row[4]) +'\n\n'   +str(row[5]) + '\n\n'  + str(row[6])+'\n'
            Label(self.fr,text=msg,bg='whiteSmoke',fg='gray40',font=('Times New Roman',14)).place(x=220,y=10)
            
    def modify(self):
        self.f6=LabelFrame(self.root,text='modify',background='whiteSmoke')
        self.f6.place(x=1,y=1,height=599,width=699)
        Label(self.f6,text='Enter Accountno :',bg='whiteSmoke',font=('Times New Roman',24)).place(x=30,y=30)
        
        self.e10=Entry(self.f6,width=40)
        self.e10.place(x=300,y=42,height=25)
        
        Button(self.f6,text='Check',font=('Times New Roman',15),bg='whiteSmoke',command=self.chk3).place(x=300,y=75)
        
    def chk3(self):
        a=self.e10.get()
        if a=='':
            messagebox.showerror('error','entry can`t be empty !')
        else:
            try:
                alkj=int(self.e10.get())
                self.cursor.execute('select * from account where accno=(%s)',(a,))
                if self.cursor.rowcount==0:
                    messagebox.showinfo('info', 'account does not exist')
                    self.e10.delete(0, END)
                else :
                    self.f6.place_forget()
                
                    self.f5=LabelFrame(self.root,text='modify account',background='whiteSmoke')
                    self.f5.place(x=1,y=1,height=599,width=699)
                    Label(self.f5,text='Account No   :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=20)
                    Label(self.f5,text='Name            :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=70)
                    Label(self.f5,text='Address        :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=120)
                    Label(self.f5,text='Gender          :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=170)
                    Label(self.f5,text='Phone no       :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=220)
                    #Label(self.f5,text='Opening date :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=270)
                   # Label(self.f5,text='Balance         :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=320)
                    
                    self.e1=Entry(self.f5,width=25)
                    self.e1.place(x=180,y=25)
                    self.e1.insert(0,self.e10.get())
                    self.e1.config(state='disable')
                    self.e2=Entry(self.f5,width=25)
                    self.e2.place(x=180,y=75)
                    self.e3=Entry(self.f5,width=25)
                    self.e3.place(x=180,y=125)
                    #self.e4=Entry(self.f5,width=25)
                    #self.e4.place(x=180,y=175)
                    self.var=StringVar()
                    self.rb1=Radiobutton(self.f5,variable=self.var,text='Male',bg='whiteSmoke',value='Male')
                    self.rb1.place(x=180,y=175)
                    self.rb2=Radiobutton(self.f5,variable=self.var,text='Female',bg='whiteSmoke',value='Female')
                    self.rb2.place(x=240,y=175)
                    
                    self.e5=Entry(self.f5,width=25)
                    self.e5.place(x=180,y=225)
                    
                    self.cursor.execute('select * from account where accno=(%s)',(self.e10.get()))
                    self.con.commit()
                    row=self.cursor.fetchone()
                    self.e2.insert(0,row[1])
                    self.e3.insert(0,row[2])
                    self.var.set(str(row[3]))
                    self.e5.insert(0,str(row[4]))
                    #self.e6=Entry(self.f5,width=25)
                    #self.e6.place(x=180,y=275)
                    #self.e7=Entry(self.f5,width=25)
                    #self.e7.place(x=180,y=325)
                    
                    Button(self.f5,text='Save',font=('Times New Roman',16),bg='whiteSmoke',command=self.r2).place(x=180,y=300,width=100)
                    
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value !')
            
    def r2(self):
        if self.e2.get()=='' or self.e3.get()=='' or self.e5.get()=='' or  self.e1.get()=='':
            messagebox.showerror('error', 'entries can`t be empty !')
        else:
            try:     
                alkj=int(self.e1.get())
                blkj=int(self.e5.get())
                if len(str(self.e5.get()))!=10:
                    messagebox.showerror('error','there should be 10 digits in phone number field')
                else:
                    self.cursor.execute('update account set name=(%s),address=(%s),gender=(%s),phno=(%s) where accno=(%s)',(self.e2.get(),self.e3.get(),self.var.get(),self.e5.get(),self.e1.get()))
                    self.con.commit()
                    messagebox.showinfo('info', 'account modified !')
                    self.e1.delete(0,END)
                    self.e2.delete(0,END)
                    self.e3.delete(0,END)
                    #self.e4.delete(0,END)
                    self.e5.delete(0,END)
            except ValueError as e:
                messagebox.showerror('error','enter appropriate values !')
        
    def delete(self):
        self.f6=LabelFrame(self.root,text='Close account',background='whiteSmoke')
        self.f6.place(x=1,y=1,height=599,width=699)
        Label(self.f6,text='Enter Accountno :',bg='whiteSmoke',font=('Times New Roman',24)).place(x=30,y=30)
        
        self.e10=Entry(self.f6,width=40)
        self.e10.place(x=300,y=42,height=25)
        
        self.fr=Frame(self.f6,bg='whiteSmoke')
        self.fr.place(x=1,y=200,height=390,width=690)
        Label(self.fr,text='Account number : \n\nName :\n\nAddress :\n\nGender :\n\nPhone number :\n\nOpening date :\n\nBalance :',bg='whiteSmoke',font=('Times New Roman',14)).place(x=50,y=10)
        self.fr.place_forget()
        
        Button(self.f6,text='Close',font=('Times New Roman',15),bg='whiteSmoke',command=self.del1).place(x=300,y=75)
            
    def del1(self):
        self.fr.place_forget()
        a=self.e10.get()
        if a=='':
            messagebox.showerror('error','entry can`t be empty !')
        else:
            try:
                alkj=int(self.e10.get())
                self.cursor.execute('select * from account where accno=(%s)',(a,))
                self.con.commit()
                if self.cursor.rowcount==0:
                    messagebox.showinfo('info', 'account does not exist')
                    self.e10.delete(0, END)
                else:
                    row=self.cursor.fetchone()
                    msg=''
                    msg=msg+str(row[0]) +'\n\n'  +str(row[1])+ '\n\n'    +str(row[2]) + '\n\n'   +str(row[3]) +'\n\n'   +str(row[4]) +'\n\n'   +str(row[5]) + '\n\n'  + str(row[6])+'\n'
                    Label(self.fr,text=msg,bg='whiteSmoke',fg='gray40',font=('Times New Roman',14)).place(x=220,y=10)
                    self.fr.place(x=1,y=200,height=390,width=690)
                    ab=messagebox.askyesno('confirm', 'Are u sure to close the account ?')
                    if ab==True:
                        self.cursor.execute('delete from transaction where transaccno=(%s)',(a,))
                        self.con.commit()
                        self.cursor.execute('delete from account where accno=(%s)',(a,))
                        self.con.commit()
                        messagebox.showinfo('info','Account closed')
                        self.e10.delete(0, END)
                        self.fr.place_forget()
                        
                    else:
                        self.e10.delete(0, END)
                        self.fr.place_forget()
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value !')
#####################################################################################################    ACCOUNT MENU DONE

######################################################################################################   TRANSACTION MENU

    def deposit(self):
        self.f1=LabelFrame(self.root,text='Deposit',background='whiteSmoke')
        self.f1.place(x=1,y=1,height=599,width=699)
        
        Label(self.f1,text='Enter Account No       :',font=('Times New Roman',18),bg='whiteSmoke').place(x=50,y=50)
        Label(self.f1,text='Enter Deposit Amount  :',font=('Times New Roman',18),bg='whiteSmoke').place(x=50,y=100)
        
        self.e1=Entry(self.f1,width=40)
        self.e1.place(x=300,y=55,height=25)
        self.e2=Entry(self.f1,width=40)
        self.e2.place(x=300,y=105,height=25)
        
        self.b1=Button(self.f1,text='Deposit',font=('Times New Roman',15),bg='whiteSmoke',command=self.dep)
        self.b1.place(x=300,y=160,width=100)
        
    def dep(self):
        a=self.e1.get()
        if a=='' or self.e2.get()=='':
            messagebox.showerror('error', 'entry fields can`t be empty !')
        else:
            try:   
                alkj=int(self.e1.get())
                blkj=int(self.e2.get())     
                self.cursor.execute('select * from account where accno=(%s)',(a,))
                if self.cursor.rowcount==0:
                    messagebox.showinfo('info','account does not exist !')
                else:
                    if int(self.e2.get())<1:
                        self.e2.delete(0, END)
                        messagebox.showerror('error','amount can`t ne negative !')
                    else:
                        now =datetime.datetime.now()
                        str=now.strftime("%Y-%m-%d %H:%M")
                        ls=str.split(' ')
                        self.cursor.execute('select ifnull(max(transid),101) from transaction')
                        self.con.commit()
                        abc=self.cursor.fetchone()
                        val=int(abc[0])+1
                        self.cursor.execute('update account set balance=balance+(%s) where accno=(%s)' ,(self.e2.get(),a))
                        self.con.commit()
                        self.cursor.execute('insert into transaction values(%s,%s,%s,%s,%s,%s)',(val,a,'deposit',self.e2.get(),ls[0],ls[1]))
                        self.con.commit()
                        messagebox.showinfo('sucess','Amount Deposited !')
                        self.e1.delete(0,END)
                        self.e2.delete(0,END)
            except ValueError as e:
                messagebox.showerror('error','enter appropriate values !')
            
    def withdraw(self):
        
        self.f1=LabelFrame(self.root,text='withdraw',background='whiteSmoke')
        self.f1.place(x=1,y=1,height=599,width=699)
                
        Label(self.f1,text='Enter Account No       :',font=('Times New Roman',18),bg='whiteSmoke').place(x=50,y=50)
        Label(self.f1,text='Enter Withdraw Amount:',font=('Times New Roman',18),bg='whiteSmoke').place(x=50,y=100)
                
        self.e1=Entry(self.f1,width=40)
        self.e1.place(x=310,y=55,height=25)
        self.e2=Entry(self.f1,width=40)
        self.e2.place(x=310,y=105,height=25)
                
        self.b1=Button(self.f1,text='Withdraw',font=('Times New Roman',15),bg='whiteSmoke',command=self.withd)
        self.b1.place(x=310,y=160,width=100)
            
        
    def withd(self):
        a=self.e1.get()
        if self.e1.get()=='' or self.e2.get()=='':
            messagebox.showerror('error', 'entry fields can`t be empty !')
        else:
            try:
                xa=int(self.e1.get())
                xa=int(self.e2.get())
                self.cursor.execute('select * from account where accno=(%s)',(a,))
                if self.cursor.rowcount==0:
                    messagebox.showinfo('info','account does not exist !')
                else:
                    if xa<1:
                        self.e2.delete(0, END)
                        messagebox.showerror('error','amount can`t be negative !')
                    else:
                        self.cursor.execute('select balance from account where accno=(%s)',(a,))
                        vaal=self.cursor.fetchone()
                        if int(self.e2.get())> int(vaal[0])-500:
                            messagebox.showerror('error', 'insufficient balance !')
                            self.e1.delete(0, END)
                            self.e2.delete(0, END)
                        else:
                            now =datetime.datetime.now()
                            str=now.strftime("%Y-%m-%d %H:%M")
                            ls=str.split(' ')
                            self.cursor.execute('select ifnull(max(transid),101) from transaction')
                            self.con.commit()
                            abc=self.cursor.fetchone()
                            val=int(abc[0])+1
                            self.cursor.execute('update account set balance=balance-(%s) where accno=(%s)',(self.e2.get(),self.e1.get()))
                            self.con.commit()
                            self.cursor.execute('insert into transaction values(%s,%s,%s,%s,%s,%s)',(val,a,'withdraw',self.e2.get(),ls[0],ls[1]))
                            self.con.commit()
                            messagebox.showinfo('sucess','Amount Withdrawn !')
                            self.e1.delete(0,END)
                            self.e2.delete(0,END)
            except ValueError as e:
                messagebox.showerror('error','enter appropriate values !')
                
    def trans(self):
        
        
        self.f1=LabelFrame(self.root,text='transfer',background='whiteSmoke')
        self.f1.place(x=1,y=1,height=599,width=699)
        
        Label(self.f1,text='Enter payee Account No     :',font=('Times New Roman',18),bg='whiteSmoke').place(x=20,y=50)
        Label(self.f1,text='Enter beneficiery Acc No  :',font=('Times New Roman',18),bg='whiteSmoke').place(x=20,y=100)
        Label(self.f1,text='Enter Transfer Amount       :',font=('Times New Roman',18),bg='whiteSmoke').place(x=20,y=150)
        
        self.e1=Entry(self.f1,width=40)
        self.e1.place(x=310,y=55,height=25)
        self.e2=Entry(self.f1,width=40)
        self.e2.place(x=310,y=105,height=25)
        self.e3=Entry(self.f1,width=40)
        self.e3.place(x=310,y=155,height=25)
        
        self.b1=Button(self.f1,text='Transfer',font=('Times New Roman',15),bg='whiteSmoke',command=self.tran)
        self.b1.place(x=310,y=200,width=100)
        
    def tran(self):
        
        a=self.e1.get()
        if a=='' or self.e2.get()=='' or self.e3.get()=='' :
            messagebox.showerror('error', 'entry fields can`t be empty !')
        else:
            try:        
                #a=self.e1.get()
                b=int(self.e2.get())
                c=int(self.e3.get())
                xy=int(self.e1.get())
                self.cursor.execute('select * from account where accno=(%s)',(a,))
                self.con.commit()
                if self.cursor.rowcount==0:
                    messagebox.showerror('error','invalid payee account !' )
                    self.e1.delete(0,END)
                else:
                    self.cursor.execute('select * from account where accno=(%s)',(b,))
                    self.con.commit()
                    if self.cursor.rowcount==0:
                        messagebox.showerror('error','invalid beneficiery account !' )
                        self.e2.delete(0,END)
                    else:
                        if c<1:
                            self.e3.delete(0, END)
                            messagebox.showerror('error','amount can`t be negative !')
                        else:
                            self.cursor.execute('select balance from account where accno=(%s)',(a,))
                            self.con.commit()
                            bal=self.cursor.fetchone()
                            if int(c)>int(bal[0])-500:
                                messagebox.showerror('error','insufficient balance in payee account !')
                            else:
                                now =datetime.datetime.now()
                                str=now.strftime("%Y-%m-%d %H:%M")
                                ls=str.split(' ')
                                self.cursor.execute('select ifnull(max(transid),101) from transaction')
                                self.con.commit()
                                abc=self.cursor.fetchone()
                                val=int(abc[0])+1
                                self.cursor.execute('update account set balance=balance-(%s) where accno=(%s)',(c,a))
                                self.con.commit()
                                self.cursor.execute('insert into transaction values(%s,%s,%s,%s,%s,%s)',(val,a,'withdraw',c,ls[0],ls[1]))
                                self.con.commit()
                                self.cursor.execute('select ifnull(max(transid),101) from transaction')
                                self.con.commit()
                                abc=self.cursor.fetchone()
                                val=int(abc[0])+1
                                self.cursor.execute('update account set balance=balance+(%s) where accno=(%s)',(c,b))
                                self.con.commit()
                                self.cursor.execute('insert into transaction values(%s,%s,%s,%s,%s,%s)',(val,b,'deposit',c,ls[0],ls[1]))
                                self.con.commit()
                                messagebox.showinfo('sucess','transfer completed !')
                                self.e1.delete(0,END)
                                self.e2.delete(0,END)
                                self.e3.delete(0,END)
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value !')
                
                    
    def minist(self):
        self.f2=LabelFrame(self.root,text='mini statements',background='whiteSmoke')
        self.f2.place(x=1,y=1,height=599,width=699)
        
        Label(self.f2,text='Enter Account No       :',font=('Times New Roman',20),bg='whiteSmoke').place(x=20,y=20)
        self.e1=Entry(self.f2,width=40)
        self.e1.place(x=300,y=28,height=25)
        self.b1=Button(self.f2,text='View',font=('Times New Roman',13),bg='whiteSmoke',command=self.view)
        self.b1.place(x=300,y=70,width=80)
        
        
    def view(self):
        a=int(self.e1.get())
        if a=='' :
            messagebox.showerror('error', 'entry fields can`t be empty !')
        else:
            try:
                aaa=int(self.e1.get())
                self.cursor.execute('select * from transaction where transaccno=(%s)',(a,))
                self.con.commit()
                if self.cursor.rowcount==0:
                    messagebox.showerror('error','No mini statements available for the entered account !' )
                    self.e1.delete(0,END)
                else:
                    self.t1=Text(self.f2)
                    self.t1.place(x=1,y=150,height=400,width=690)
                    msg='transaction id :'+'  '+'transaction accno :'+ '  '+'transaction type :'+'  '+'Amount :'+'  '+'date :'+'  '+'time :'+'\n'
                    for row in self.cursor: 
                        msg=msg+str(row[0])+'               '+str(row[1])+'             '+str(row[2])+'          '+str(row[3])+ '       '+str(row[4])+'    '+str(row[5])+'\n'
                    self.t1.insert('1.0',msg)
                    self.t1.config(state='disable')  
                    
            except ValueError as e:
                messagebox.showerror('error', 'enter appropriate values !')         
  #########################################################################################################################################
  
  
  ############################################################################################################    ADMIN MODULE
  
                
    def profile(self):
        self.f2=LabelFrame(self.root,text='Edit profile',background='whiteSmoke')
        self.f2.place(x=1,y=1,height=599,width=699)  
        
        txt1='Admin  :  '+str(self.admid)
        Label(self.f2,text=txt1,background='whiteSmoke',foreground='gray85',font=('Times New Roman',26,'bold')).place(x=10,y=30)
                  
        #Label(self.f2,text='Change id                  :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=20)
        Label(self.f2,text='Change Name            :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=120)
        Label(self.f2,text='Change Address        :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=220)
        Label(self.f2,text='Change Gender          :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=320)
        Label(self.f2,text='Change Phone no       :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=420)
        
        #self.e1=Entry(self.f2,width=40)
       # self.e1.place(x=210,y=25)
        self.e2=Entry(self.f2,width=40)
        self.e2.place(x=210,y=125)
        self.e3=Entry(self.f2,width=40)
        self.e3.place(x=210,y=225)
        #self.e4=Entry(self.f2,width=40)
        #self.e4.place(x=210,y=325)
        self.var=StringVar()
        self.var.set('Male')
        self.rb1=Radiobutton(self.f2,variable=self.var,text='Male',bg='whiteSmoke',value='Male')
        self.rb1.place(x=210,y=325)
        self.rb2=Radiobutton(self.f2,variable=self.var,text='Female',bg='whiteSmoke',value='Female')
        self.rb2.place(x=260,y=325)
        
        self.e5=Entry(self.f2,width=40)
        self.e5.place(x=210,y=425)
        
        
        self.cursor.execute('select * from admin where admid=(%s)',(self.admid,))
        self.con.commit()
        row=self.cursor.fetchone()
        self.e2.insert(0, row[2])
        self.e3.insert(0, row[6])
        self.var.set(str(row[5]))
        self.e5.insert(0, row[7])
        #Button(self.f2,text='Change',font=('Times New Roman',12),bg='whiteSmoke',command=self.a1).place(x=210,y=60)
        #Button(self.f2,text='Change',font=('Times New Roman',12),bg='whiteSmoke',command=self.a2).place(x=210,y=160)
       # Button(self.f2,text='Change',font=('Times New Roman',12),bg='whiteSmoke',command=self.a3).place(x=210,y=260)
      #  Button(self.f2,text='Change',font=('Times New Roman',12),bg='whiteSmoke',command=self.a4).place(x=210,y=360)
        Button(self.f2,text='Change',font=('Times New Roman',12),bg='whiteSmoke',command=self.a5).place(x=210,y=460)
        
    
    def a5(self):
        if self.e5.get()=='' or self.e2.get()=='' or self.e3.get()=='' :
            messagebox.showerror('error', 'please enter some value')
        else:
            try:
                alk=int(self.e5.get())
                if len(str(alk))!=10:
                    messagebox.showerror('error','digits in mobile number sgould be 10 !')
                else:
                    self.cursor.execute('update admin set name=(%s) where admid=(%s)',(self.e2.get(),self.admid))
                    self.con.commit()
                    self.cursor.execute('update admin set address=(%s) where admid=(%s)',(self.e3.get(),self.admid))
                    self.con.commit()
                    self.cursor.execute('update admin set phno=(%s) where admid=(%s)',(self.e5.get(),self.admid))       
                    self.con.commit()
                    self.cursor.execute('update admin set gender=(%s) where admid=(%s)',(self.var.get(),self.admid))
                    self.con.commit()
                    messagebox.showinfo('info', 'update sucessful !')
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value for phone number !')
                
    def pwrd(self):
        self.f2=LabelFrame(self.root,text='Edit password',background='whiteSmoke')
        self.f2.place(x=1,y=1,height=599,width=699)  
                  
        Label(self.f2,text='Enter old password    :',font=('Times New Roman',15),bg='whiteSmoke').place(x=50,y=50)
        self.e1=Entry(self.f2,width=40,show='*')
        self.e1.place(x=260,y=56)
        Button(self.f2,text='Confirm',font=('Times New Roman',12),bg='whiteSmoke',command=self.p1).place(x=260,y=100)
        
    def p1(self):
        if self.e1.get()=='':
            messagebox.showerror('error', 'please enter some value')
        else:
            try:
                self.cursor.execute('select * from admin where pwd=(%s)',(self.e1.get()))
                self.con.commit()
                if self.cursor.rowcount==0:
                    messagebox.showerror('error', 'wrong password entered')
                    self.e1.delete(0, END)
                else:
                    self.e1.config(state='disable')
                    Label(self.f2,text='Enter New password     :',font=('Times New Roman',15),bg='whiteSmoke').place(x=50,y=150)
                    Label(self.f2,text='Confirm New password   :',font=('Times New Roman',15),bg='whiteSmoke').place(x=40,y=200)
                    self.e2=Entry(self.f2,width=40,show='*')
                    self.e2.place(x=260,y=156)
                    self.e3=Entry(self.f2,width=40,show='*')
                    self.e3.place(x=260,y=206)
                    Button(self.f2,text='Change',font=('Times New Roman',12),bg='whiteSmoke',command=self.p2).place(x=260,y=250)
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value !')
        
    def p2(self):
        a=self.e2.get()
        b=self.e3.get()
        if self.e2.get()=='' or b=='':
            messagebox.showerror('error', 'please enter some value')
        else:
            try:
                if a!=b:
                    messagebox.showerror('error','password and confirm password does not match !')
                    self.e2.delete(0, END)
                    self.e3.delete(0,END)
                else:
                    self.cursor.execute('update admin set pwd=(%s) where admid=(%s)',(a,self.admid))
                    self.con.commit()
                    messagebox.showinfo('info','password changed !') 
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value !')
            
    def sec(self):
        self.f2=LabelFrame(self.root,text='Edit security settings',background='whiteSmoke')
        self.f2.place(x=1,y=1,height=599,width=699)  
                  
        Label(self.f2,text='previous security question :',font=('Times New Roman',15),bg='whiteSmoke').place(x=50,y=50)
        self.e1=Entry(self.f2,width=40)
        self.e1.place(x=300,y=56)
        self.cursor.execute('select secques from admin where admid=(%s)',(self.admid,))
        val=self.cursor.fetchone()
        self.e1.insert(0,val)
        self.e1.config(state='disable')
        Label(self.f2,text='Your answer   :',font=('Times New Roman',15),bg='whiteSmoke').place(x=150,y=100)
        self.e1=Entry(self.f2,width=40)
        self.e1.place(x=300,y=106)
        Button(self.f2,text='Confirm',font=('Times New Roman',12),bg='whiteSmoke',command=self.sec1).place(x=300,y=150)
           
    def sec1(self):
        a=self.e1.get()
        if self.e1.get()=='':
            messagebox.showerror('error', 'please enter some value')
        else:
            try:
                self.cursor.execute('select * from admin where admid=(%s) and secans=(%s)',(self.admid,a))
                if self.cursor.rowcount==0:
                    messagebox.showerror('error','wrong answer !')
                    self.e1.delete(0, END)
                else:
                    Label(self.f2,text='New security question :',font=('Times New Roman',15),bg='whiteSmoke').place(x=90,y=200)
                    self.e2=Entry(self.f2,width=40)
                    self.e2.place(x=300,y=206)
                    Label(self.f2,text='Your answer   :',font=('Times New Roman',15),bg='whiteSmoke').place(x=150,y=250)
                    self.e3=Entry(self.f2,width=40)
                    self.e3.place(x=300,y=256)
                    Button(self.f2,text='Confirm',font=('Times New Roman',12),bg='whiteSmoke',command=self.sec2).place(x=300,y=300)
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value !')
            
    def sec2(self):
        if self.e2.get()=='' or self.e3.get()=='':
            messagebox.showerror('error', 'please enter some value')
        else:
            try:
                self.cursor.execute('update admin set secques=(%s) , secans=(%s) where admid=(%s)',(self.e2.get(),self.e3.get(),self.admid))
                self.con.commit()
                messagebox.showinfo('info', 'values updated !')
            except ValueError as e:
                messagebox.showerror('error','enter appropriate value !')
        
    def lgout(self):
        self.root.destroy()
        admin.admin_class()
  ###################################################################################################       
        
        
   ##########################################################################################################     HELP     
        
    def help1(self):
        self.f=LabelFrame(self.root,text='Help')
        self.f.place(x=1,y=1,height=100,width=690)
        Label(self.f,text='This application is created by Shivam garg ! All rights reserved to shivam for its use and sale ! \n Interested buyers can contact 7837738088').place(x=10,y=10)
     
     
        
#menu_class('sg@gmail.com')