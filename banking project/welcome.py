from tkinter import *
from PIL import Image,ImageTk
import loading
class welcome_class:
    def __init__(self):
        self.root=Tk()
        self.root.title('SG.. BANKS')
        self.root.geometry('700x600+350+100')
        self.root.config(background='gray85')
        self.root.resizable(False, False)
        
        #img=Image.open('d:/1.png')
        #img1=img.resize((100,100),Image.ANTIALIAS)
        #a=ImageTk.PhotoImage(img1)
        self.l1=Label(self.root,text='SG.. BANKS',background='gray85',foreground='gray20',font=('Times New Roman',56,'bold','underline'))#,image=a,compound='left')
        self.l1.pack(fill='x',anchor='w')
        i1=Image.open('d:\\01.jpg')
        i2=i1.resize((700,350),Image.ANTIALIAS)
        self.i1=ImageTk.PhotoImage(i2)
        Label(self.root,text='a',image=self.i1).pack()
        
        self.b1=Button(self.root,text='Click Here To Continue',font=(10),command=self.click,width=30,height=1,bg='gray30',fg='white')
        self.b1.pack(expand=True)
        
        self.root.mainloop()
    def click(self):
        self.root.destroy()
        o1=loading.loading_class()
if __name__ == "__main__":
    welcome_class()
        
        
