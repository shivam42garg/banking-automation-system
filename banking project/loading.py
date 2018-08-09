from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image,ImageTk
from threading import Thread
import time
import admin
class loading_class:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('700x600+350+100')
        self.root.config(bg='gray85')
        self.root.resizable(False, False)
        
        img=Image.open('d:/2.jpg')
        img1=img.resize((100,100),Image.ANTIALIAS)
        a=ImageTk.PhotoImage(img1)
        self.l1=Label(self.root,text='SG.. BANKS',bg='gray85',foreground='gray20',font=('Times New Roman',54,'bold','underline'),image=a,compound='left')
        
        img=Image.open('d:/4.jpg')
        img1=img.resize((700,300),Image.ANTIALIAS)
        b=ImageTk.PhotoImage(img1)
        self.l2=Label(self.root,text='Your Application Is Now Loading',bg='gray85',foreground='gray40',font=('italic',20,'bold'),image=b,compound='center')
        
        self.l1.place(x=110,y=10)
        self.l2.place(x=0,y=150)
        
        self.l3=Label(self.root,text='loading 1%',bg='gray85',foreground='gray40',font=('italic',15,'bold'))
        self.l3.place(x=100,y=480)
        
        self.v1=IntVar()
        self.v1.set(1)
        self.p1=Progressbar(self.root,mode='determinate',orient='horizontal',length=500,variable=self.v1)
        self.p1.place(x=100,y=520)
        self.t1=Thread(target=self.run,name='progressbar',args=(101,))
        self.t1.start()
        self.root.after(500, self.target)
        self.root.mainloop()
        
        
    def run(self,a):
        for i in range(a):
            self.v1.set(i)
            self.l3.config(text='loading {0}%'.format(i))
            time.sleep(0.05) 
        
    def target(self):
        if int(self.v1.get())==100:
            self.root.destroy() 
            a1=admin.admin_class()
        else:
            self.root.after(500,self.target)
        
#loading_class()
