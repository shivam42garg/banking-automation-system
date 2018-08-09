


    def deposit(self):
        self.f1=LabelFrame(self.root,text='Deposit',background='whiteSmoke')
        self.f1.place(x=1,y=1,height=599,width=699//2)
        
        Label(self.f1,text='Enter Account No       :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=20)
        Label(self.f1,text='Enter Deposit Amount   :',font=('Times New Roman',15),bg='whiteSmoke').place(x=20,y=70)
        
        self.e1=Entry(self.f1,width=25)
        self.e1.place(x=180,y=25)
        self.e2=Entry(self.f1,width=25)
        self.e2.place(x=180,y=75)
        
        self.b1=Button(self.f1,text='Deposit',font=('Times New Roman',15),bg='whiteSmoke',command=self.dep)
        self.b1.place(x=180,y=100,width=100)
        
    def dep(self):
        a=self.e1.get()
        self.cursor.execute('select * from account where accno=(%s)',(a,))
        if self.cursor.rowcount==0:
            messagebox.showinfo('info','account does not exist !')
        else:
            now =datetime.datetime.now()
            str=now.strftime("%Y-%m-%d %H:%M")
            ls=str.split(' ')
            self.cursor.execute('select ifnull(max(transid,101)) from transaction')
            self.con.commit()
            val=int(self.cursor.fetchone())+1
            self.cursor.execute('update account set balance=balance+(%s)',(a,))
            self.con.commit()
            self.cursor.execute('insert into transaction values(%s,%s,%s,%s,%s,%s)',(val,a,'deposit',self.e2.get(),ls[0],ls[1]))
            self.con.commit()
            messagebox.showinfo('sucess','Amount Deposited !')
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            