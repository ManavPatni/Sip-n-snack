# importing some usefull libares

from tkinter import *
from tkinter import ttk
from tkinter import Image
from tkinter.font import BOLD
import random,os
from tkinter import messagebox
import tempfile
import webbrowser


class Bill_App:
    def __init__(self,root):
        self.root=root
        root.title("Sip 'N' Snack")
        # window title
        root.configure(bg="white")
        
        # geometry
        root.geometry('1320x650+0+0')
        root.resizable(False, False)

        def callback(url):
           webbrowser.open_new(url)

        #========Variables====================#
        self.bill_no=StringVar()       #bill no.
        #random no. for bill generater
        z = random.randint(100,99999)
        self.bill_no.set(z)

        self.date=StringVar()          #date
        self.time=StringVar()          #time
        self.search_bill=StringVar()   #search bill
        self.product=StringVar()       #item
        self.product2=StringVar()      #item2
        self.rate=IntVar()             #rate
        self.prices=IntVar()           #price
        self.qty=IntVar()              #quantity
        self.total=StringVar()         #total
        #=====================================#

        #==============Combobox List==========#
        #main category list
        self.m_category = ["Select Option","Snacks","Drinks"]
        #snacks list
        self.s_snack = ["Select Snack","Nachos","Sandwhich","Bhel"]
        #price for snacks
        #p_snack = [70,50,40]
        self.price_nachos = 70
        self.price_sandwhich = 50
        self.price_bhel = 40

        #drinks list
        self.s_drink = ["Select Drink","Coffee"]
        #price for drinks
        #p_drink = [70]
        self.price_coffee = 70

        #=====================================#

        #=================title================#
        main_title = Label(self.root, text="Sip 'N' Snack", font=("times new roman",30,"bold"),bg="white", fg="red")
        main_title.place(x=0,y=10,width=1330, height=39)
        #======================================#

        #==============main frame==============#
        main_frame = Frame(self.root,bd=2,relief=GROOVE,bg="white")
        main_frame.place(x=10,y=100,width=1300,height=525)
        #======================================#

        #===============other infomation=======#
        o_info = LabelFrame(main_frame,text="Other Info", font=("times new roman",12,"bold"),bg="white", fg="red")
        o_info.place(x=10,y=5,width=350,height=140)

        #bill no.
        self.bill = Label(o_info,text="Bill no.", font=("arial",12,"bold"),bg="white")
        self.bill.grid(row=0,column=0,stick=W,padx=5,pady=2)
        #bill no entry
        self.b_ent = ttk.Entry(o_info, font=("arial",10),textvariable=self.bill_no,width=24)
        self.b_ent.grid(row=0,column=1)


        #date
        self.dat_e = Label(o_info,text="Date", font=("arial",12,"bold"),bg="white")
        self.dat_e.grid(row=1,column=0,stick=W,padx=5,pady=2)
        #date entry
        self.dat_e_ent = ttk.Entry(o_info, font=("arial",10),textvariable=self.date,width=24)
        self.dat_e_ent.grid(row=1,column=1)

        #time
        self.tim_e = Label(o_info,text="Time", font=("arial",12,"bold"),bg="white")
        self.tim_e.grid(row=2,column=0,stick=W,padx=5,pady=2)
        #time entry
        self.tim_e_ent = ttk.Entry(o_info, font=("arial",10),textvariable=self.time,width=24)
        self.tim_e_ent.grid(row=2,column=1)
        #======================================#

        #=============Item information======#
        i_info = LabelFrame(main_frame,text="Item Info", font=("times new roman",12,"bold"),bg="white", fg="red")
        i_info.place(x=10,y=150,width=600,height=140)

        #main category
        self.m_cat = Label(i_info,text="Select Category", font=("arial",12,"bold"),bg="white")
        self.m_cat.grid(row=0,column=0,stick=W,padx=5,pady=2)
        #main category combobox
        self.cat_com = ttk.Combobox(i_info, font=("arial",10),value=self.m_category,width=24,state="readonly")
        self.cat_com.current(0)
        self.cat_com.grid(row=0,column=1)
        self.cat_com.bind("<<ComboboxSelected>>",self.Category)
        


        #snacks category
        self.s_cat = Label(i_info,text="Snacks", font=("arial",12,"bold"),bg="white")
        self.s_cat.grid(row=1,column=0,stick=W,padx=5,pady=2)
        #snacks category combobox
        self.san_com = ttk.Combobox(i_info, font=("arial",10),textvariable=self.product,width=24,state="readonly")
        self.san_com.grid(row=1,column=1)
        self.san_com.bind("<<ComboboxSelected>>",self.price)

        #drinks category
        self.d_cat = Label(i_info,text="Drinks", font=("arial",12,"bold"),bg="white")
        self.d_cat.grid(row=2,column=0,stick=W,padx=5,pady=2)
        #drinks category combobox
        self.dri_com = ttk.Combobox(i_info, font=("arial",10),textvariable=self.product2,width=24,state="readonly")
        self.dri_com.grid(row=2,column=1)
        self.dri_com.bind("<<ComboboxSelected>>",self.price)
        

        #rate
        self.r_cat = Label(i_info,text="Rate", font=("arial",12,"bold"),bg="white")
        self.r_cat.grid(row=0,column=2,stick=W,padx=5,pady=2)
        #rate combobox
        self.rat_com = ttk.Combobox(i_info, font=("arial",10),textvariable=self.rate,width=22)
        self.rat_com.grid(row=0,column=3)

        #Amount
        self.a_cat = Label(i_info,text="Amount", font=("arial",12,"bold"),bg="white")
        self.a_cat.grid(row=1,column=2,stick=W,padx=5,pady=2)
        #amount combobox
        self.pri_com = ttk.Combobox(i_info, font=("arial",10),textvariable=self.prices,width=22)
        self.pri_com.grid(row=1,column=3)

        #quantity
        self.q_cat = Label(i_info,text="Quantity", font=("arial",12,"bold"),bg="white")
        self.q_cat.grid(row=2,column=2,stick=W,padx=5,pady=2)
        #quantity
        self.qua_com = ttk.Entry(i_info, font=("arial",10),textvariable=self.qty,width=24)
        self.qua_com.grid(row=2,column=3)
        #===================================#

        #============Bill search============#
        rc = Frame(main_frame,bd=2,bg="white" )
        rc.place(x=800, y=15,width=455,height=40)
        
        #search label
        self.se = Label(rc,text="Search Bill", font=("arial",12,"bold"),bg="red",fg="white")
        self.se.grid(row=0,column=0,stick=W,padx=1)
        #search entry
        self.sea_com = ttk.Entry(rc, font=("arial",10,"bold"),textvariable=self.search_bill,width=24)
        self.sea_com.grid(row=0,column=1,stick=W,padx=2,pady=2)
        #search botton
        self.btn_s = Button(rc,text="Search",command=self.find_bill, font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btn_s.grid(row=0,column=3)
        #===================================#

        #===============Bill area=========#
        rl = LabelFrame(main_frame,text="Bill Area", font=("times new roman",12,"bold"),bg="white", fg="red")
        rl.place(x=800, y=45,width=480,height=470)

        #textarea and scroll bar for bill area
        self.scroll_y = Scrollbar(rl,orient=VERTICAL)
        self.textarea = Text(rl,yscrollcommand=self.scroll_y.set,bg="white",fg="blue", font=("times new roman",12,"bold"))
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        #===================================#

        #==========Billing Counter==========#
        bc = LabelFrame(main_frame,text="Billing Counter", font=("times new roman",12,"bold"),bg="white", fg="red")
        bc.place(x=10, y=294,width=600,height=125)

        #Total
        self.t_cat = Label(bc,text="Total", font=("arial",12,"bold"),bg="white")
        self.t_cat.grid(row=0,column=0,stick=W,padx=5,pady=2)
        #toatl entry
        self.tol_com = ttk.Entry(bc, font=("arial",10),textvariable=self.total,width=24)
        self.tol_com.grid(row=0,column=1)

        '''#Grand Total
        self.gt = Label(bc,text="Grand Total", font=("arial",12,"bold"),bg="white")
        self.gt.grid(row=1,column=0,stick=W,padx=5,pady=2)
        #Grand total entry
        self.gat = ttk.Entry(bc, font=("arial",10),width=24)
        self.gat.grid(row=1,column=1)'''
        #===================================#

        #===============Button==============#
        bt=Frame(main_frame,bd=2,bg="white")
        bt.place(x=620,y=0,width=175,height=500)

        #cart
        self.btn_ca = Button(bt,text="Add To Cart",command=self.AddItem, font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=12,cursor="hand2")
        self.btn_ca.grid(row=0,column=0)

        #generate bill
        self.btn_ge = Button(bt,text="Generate Bill",command=self.gen_bill, font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=12,cursor="hand2")
        self.btn_ge.grid(row=1,column=0,pady=5)

        #save bill
        self.btn_sa = Button(bt,text="Save Bill",command=self.save_bill, font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=12,cursor="hand2")
        self.btn_sa.grid(row=2,column=0,pady=5)

        #print
        self.btn_pr = Button(bt,text="Print",command=self.iprint, font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=12,cursor="hand2")
        self.btn_pr.grid(row=3,column=0,pady=5)

        #add new
        self.btn_cl = Button(bt,text="Add New",command=self.add_new, font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=12,cursor="hand2")
        self.btn_cl.grid(row=4,column=0,pady=5)

        #exit
        self.btn_e = Button(bt,text="Exit", font=("arial",15,"bold"),command=self.root.destroy,bg="orangered",fg="white",height=2,width=12,cursor="hand2")
        self.btn_e.grid(row=5,column=0,pady=5)

        #show it on bill area
        self.welcome()
        #===================================#
        self.l=list()

        #============Tab frame============#
        tf = Frame(self.root,bg="white")
        tf.place(x=10,y=625,width=1300,height=25)

        self.tabControl = ttk.Notebook(main_frame)

        
        #add item to category botton
        btn_ad = ttk.Button(tf,text="Add Items",cursor="hand2",command=self.add)
        btn_ad.grid(row=0,column=0)

        #about btn
        btn_abo = ttk.Button(tf,text="About",cursor="hand2",command=self.about_us)
        btn_abo.grid(row=0,column=1)
        
        #created my label hyperlink
        com_txt = Label(tf,text="This Software is created by FireFrame  /  A Deh Infotech Company", cursor="hand2",bg="white")
        com_txt.place(x=500)
        
        # Bind the label with the URL to open in a new tab
        com_txt.bind("<Button-1>", lambda e: callback('https://fireframe.godaddysites.com/'))
        
        #verision lable
        ver_txt = Label(tf,text="Version:",bg="white")
        ver_txt.place(x=1200)

        #verision number label
        ver_no = Label(tf,text="1.1.10",bg="white")
        ver_no.place(x=1250)
        #===================================#

        #===========Def funtion===============#
        #def for depending combobox
         #for snacks
    def Category(self,event=""):
         if self.cat_com.get() == "Snacks":
            self.san_com.config(value=self.s_snack)
            self.san_com.current(0)
        #for drinks
         if self.cat_com.get() == "Drinks":
            self.dri_com.config(value=self.s_drink)
            self.dri_com.current(0)   

        #def function for price
    def price(self,event=""):
        #price for snacks
        #price for nachos
        if self.san_com.get() == "Nachos":
            self.pri_com.config(value=self.price_nachos)
            self.pri_com.current(0)
            self.rat_com.config(value=self.price_nachos)
            self.rat_com.current(0)
            self.qty.set(1)
        
        #price for sandwhich
        if self.san_com.get() == "Sandwhich":
            self.pri_com.config(value=self.price_sandwhich)
            self.pri_com.current(0)
            self.rat_com.config(value=self.price_sandwhich)
            self.rat_com.current(0)
            self.qty.set(1)

        #price for bhel
        if self.san_com.get() == "Bhel":
            self.pri_com.config(value=self.price_bhel)
            self.pri_com.current(0)
            self.rat_com.config(value=self.price_bhel)
            self.rat_com.current(0)
            self.qty.set(1)

        #price for drinks
        #price for coffee
        if self.dri_com.get() == "Coffee":
            self.pri_com.config(value=self.price_coffee)
            self.pri_com.current(0)
            self.rat_com.config(value=self.price_coffee)
            self.rat_com.current(0)
            self.qty.set(1)
            
    #bill area def function
    def welcome(self):
        self.textarea.delete(1.0,END)
        #company name
        self.textarea.insert(END,"\t\t\t Sip 'N' Snack")
        #bill no.
        self.textarea.insert(END,f"\n Bill no.: {self.bill_no.get()}")
        #date
        self.textarea.insert(END,f"\n Date: {self.date.get()}")
        #time
        self.textarea.insert(END,f"\n Time: {self.time.get()}")

        #formating
        self.textarea.insert(END,"\n==================================================")
        self.textarea.insert(END,"\nItems\t\tQty\t\tRate\t\tAmount")
        self.textarea.insert(END,"\n==================================================\n")

        #self.textarea.insert(END,f"\n Total: {self.total.get()}")
        
    #add to cart def function    
    def AddItem(self):
        
        self.n=int(self.pri_com.get())
        self.m=int(self.qua_com.get())* self.n
        self.l.append(self.m)
        if self.san_com.get()=="" and self.dri_com.get()=="":
            pass
        else:
            self.textarea.insert(END,f"{self.san_com.get()}{self.dri_com.get()}\t\t{self.qua_com.get()}\t\t{self.rat_com.get()}\t\t{self.m}\n")
            self.total.set(str('Rs.%.2f'%(sum(self.l))))
            self.san_com.set("")
            self.dri_com.set("")
            
    
    #grenerating bill def function
    def gen_bill(self):
        if self.san_com.get()=="" and self.dri_com.get()=="":
            text=self.textarea.get(8.0,(8.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n==================================================")
            self.textarea.insert(END,f"\nTotal:\t\t\t\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n==================================================")
        else:
            text=self.textarea.get(8.0,(8.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n==================================================")
            self.textarea.insert(END,f"\nTotal:\t\t\t\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n==================================================")
    
    #save def function
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you this Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('data/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            messagebox.showinfo("Bill saved",f"Bill no.: {self.bill_no.get()} saved successfully!")
            f1.close()

    #print def function
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    #search bill def function
    def find_bill(self):
        found="no"
        for i in os.listdir("data/"):
            if i.split('.')[0]==self.search_bill.get():
                f2=open(f'data/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f2:
                    self.textarea.insert(END,d)
                f2.close()
                found="yes"
            if found=="no":
                messagebox.showerror("Error","Invaild bill number")
    
    #add new def function
    def add_new(self):
        self.textarea.delete(8.0,END)
        #random no. for bill generater
        z = random.randint(100,99999)
        self.bill_no.set(str(z))
        self.date.set("")         #date
        self.time.set("")         #time
        self.search_bill.set("")  #search bill
        self.product.set("")      #item
        self.product2.set("")     #item2
        self.rate.set("")         #rate
        self.prices.set("")       #price
        self.qty.set("")          #quantity
        self.total.set("")        #total

    #hyperlink def function
    def open_url(self,url):
       webbrowser.open_new_tab(url)

    #about def function
    def about_us(self):
        messagebox.showinfo("About Sip 'N' Snack",'''Software Name: Sip 'N' Snack\n Version: 1.1.10\n\n
                              \n This Softwere is made by FireFrame, A Deh Infotech company.CEO/Owner of FireFrame Manav Patni has created this software.Manav Patni Student of SGI Junior College 11 A Commerce (2021-22). To create any kind of app for windows/mac/android/iphone contact Manav Patni or mail E-mail id:- help.fireframe.@gmail.com or visit our website. Website: https://fireframe.godaddysites.com/''')

    #about def function
    def add(self):
        messagebox.showwarning("Coming Soon","We are currently working on it. This function will be coming soon")
        #=====================================#




# end of window
if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
