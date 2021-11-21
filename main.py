# importing some usefull libares

from tkinter import *
from tkinter import ttk
from tkinter import Image
from tkinter.font import BOLD


class Bill_App:
    def __init__(self,root):
        self.root=root
        root.title("Sip 'N' Snack")
        # window title
        root.configure(bg="white")
        # geometry
        root.geometry('1520x790+0+0')
        root.resizable(False, False)

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
        main_title.place(x=0,y=10,width=1530, height=49)
        #======================================#

        #==============main frame==============#
        main_frame = Frame(self.root,bd=2,relief=GROOVE,bg="white")
        main_frame.place(x=10,y=100,width=1500,height=670)
        #======================================#

        #===============other infomation=======#
        o_info = LabelFrame(main_frame,text="Other Info", font=("times new roman",12,"bold"),bg="white", fg="red")
        o_info.place(x=10,y=5,width=350,height=140)

        #bill no.
        self.bill = Label(o_info,text="Bill No.", font=("arial",12,"bold"),bg="white")
        self.bill.grid(row=0,column=0,stick=W,padx=5,pady=2)
        #bill entry
        self.bill_ent = ttk.Entry(o_info, font=("arial",10),width=24)
        self.bill_ent.grid(row=0,column=1)

        #date
        self.dat_e = Label(o_info,text="Date", font=("arial",12,"bold"),bg="white")
        self.dat_e.grid(row=1,column=0,stick=W,padx=5,pady=2)
        #date entry
        self.dat_e_ent = ttk.Entry(o_info, font=("arial",10),width=24)
        self.dat_e_ent.grid(row=1,column=1)

        #time
        self.tim_e = Label(o_info,text="Time", font=("arial",12,"bold"),bg="white")
        self.tim_e.grid(row=2,column=0,stick=W,padx=5,pady=2)
        #time entry
        self.tim_e_ent = ttk.Entry(o_info, font=("arial",10),width=24)
        self.tim_e_ent.grid(row=2,column=1)
        #======================================#

        #=============Item information======#
        i_info = LabelFrame(main_frame,text="Item Info", font=("times new roman",12,"bold"),bg="white", fg="red")
        i_info.place(x=370,y=5,width=600,height=140)

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
        self.san_com = ttk.Combobox(i_info, font=("arial",10),width=24,state="readonly")
        self.san_com.grid(row=1,column=1)

        #drinks category
        self.d_cat = Label(i_info,text="Drinks", font=("arial",12,"bold"),bg="white")
        self.d_cat.grid(row=2,column=0,stick=W,padx=5,pady=2)
        #snacks category combobox
        self.dri_com = ttk.Combobox(i_info, font=("arial",10),width=24,state="readonly")
        self.dri_com.grid(row=2,column=1)

        #price
        self.p_cat = Label(i_info,text="Price", font=("arial",12,"bold"),bg="white")
        self.p_cat.grid(row=0,column=2,stick=W,padx=5,pady=2)
        #price combobox
        self.pri_com = ttk.Combobox(i_info, font=("arial",10),width=22)
        self.pri_com.grid(row=0,column=3)

        #quantity
        self.q_cat = Label(i_info,text="Quantity", font=("arial",12,"bold"),bg="white")
        self.q_cat.grid(row=1,column=2,stick=W,padx=5,pady=2)
        #quantity
        self.qua_com = ttk.Entry(i_info, font=("arial",10),width=24)
        self.qua_com.grid(row=1,column=3)
        #===================================#

        #============Bill search============#
        rc = Frame(main_frame,bd=2,bg="white" )
        rc.place(x=1020, y=15,width=455,height=40)
        
        #search label
        self.se = Label(rc,text="Search Bill", font=("arial",12,"bold"),bg="red",fg="white")
        self.se.grid(row=0,column=0,stick=W,padx=1)
        #search entry
        self.sea_com = ttk.Entry(rc, font=("arial",10,"bold"),width=24)
        self.sea_com.grid(row=0,column=1,stick=W,padx=2,pady=2)
        #search botton
        self.btn_s = Button(rc,text="Search", font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btn_s.grid(row=0,column=3)
        #===================================#

        #===============Bill area=========#
        rl = LabelFrame(main_frame,text="Bill Area", font=("times new roman",12,"bold"),bg="white", fg="red")
        rl.place(x=1000, y=45,width=480,height=490)

        #textarea and scroll bar for bill area
        self.scroll_y = Scrollbar(rl,orient=VERTICAL)
        self.textarea = Text(rl,yscrollcommand=self.scroll_y.set,bg="white",fg="blue", font=("times new roman",12,"bold"))
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        #===================================#

        #==========Billing Counter==========#
        bc = LabelFrame(main_frame,text="Billing Counter", font=("times new roman",12,"bold"),bg="white", fg="red")
        bc.place(x=0, y=540,width=1496,height=125)

        #Total
        self.t_cat = Label(bc,text="Total", font=("arial",12,"bold"),bg="white")
        self.t_cat.grid(row=0,column=0,stick=W,padx=5,pady=2)
        #toatl entry
        self.tol_com = ttk.Entry(bc, font=("arial",10),width=24)
        self.tol_com.grid(row=0,column=1)

        #Grand Total
        self.gt = Label(bc,text="Grand Total", font=("arial",12,"bold"),bg="white")
        self.gt.grid(row=1,column=0,stick=W,padx=5,pady=2)
        #Grand total entry
        self.gat = ttk.Entry(bc, font=("arial",10),width=24)
        self.gat.grid(row=1,column=1)
        #===================================#

        #===============Button==============#
        bt=Frame(bc,bd=2,bg="white")
        bt.place(x=320,y=0)

        #cart
        self.btn_ca = Button(bt,text="Add To Cart", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
        self.btn_ca.grid(row=0,column=0)

        #generate bill
        self.btn_ge = Button(bt,text="Generate Bill", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
        self.btn_ge.grid(row=0,column=1)

        #save bill
        self.btn_sa = Button(bt,text="Save Bill", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
        self.btn_sa.grid(row=0,column=3)

        #print
        self.btn_pr = Button(bt,text="Print", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
        self.btn_pr.grid(row=0,column=4)

        #clear
        self.btn_cl = Button(bt,text="Clear", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
        self.btn_cl.grid(row=0,column=5)

        #exit
        self.btn_e = Button(bt,text="Exit", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
        self.btn_e.grid(row=0,column=6)
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

    
        #=====================================#




# end of window
if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
