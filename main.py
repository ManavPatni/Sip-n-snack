# importing some usefull libares

from tkinter import *
from tkinter import ttk
from tkinter import Image
from tkinter.font import BOLD

# creating window
root = Tk()
# window title
root.title("Sip 'N' Snack")
root.configure(bg="white")
# geometry
root.geometry('1520x790+0+0')
root.resizable(False, False)

#=================title================#
main_title = Label(root, text="Sip 'N' Snack", font=("times new roman",30,"bold"),bg="white", fg="red")
main_title.place(x=0,y=10,width=1530, height=49)
#======================================#

#==============main frame==============#
main_frame = Frame(root,bd=2,relief=GROOVE,bg="white")
main_frame.place(x=10,y=100,width=1500,height=670)
#======================================#

#===============other infomation=======#
o_info = LabelFrame(main_frame,text="Other Info", font=("times new roman",12,"bold"),bg="white", fg="red")
o_info.place(x=10,y=5,width=350,height=140)

#bill no.
bill = Label(o_info,text="Bill No.", font=("arial",12,"bold"),bg="white")
bill.grid(row=0,column=0,stick=W,padx=5,pady=2)
#bill entry
bill_ent = ttk.Entry(o_info, font=("arial",10,"bold"),width=24)
bill_ent.grid(row=0,column=1)

#date
dat_e = Label(o_info,text="Date", font=("arial",12,"bold"),bg="white")
dat_e.grid(row=1,column=0,stick=W,padx=5,pady=2)
#date entry
dat_e_ent = ttk.Entry(o_info, font=("arial",10,"bold"),width=24)
dat_e_ent.grid(row=1,column=1)

#time
tim_e = Label(o_info,text="Time", font=("arial",12,"bold"),bg="white")
tim_e.grid(row=2,column=0,stick=W,padx=5,pady=2)
#time entry
tim_e_ent = ttk.Entry(o_info, font=("arial",10,"bold"),width=24)
tim_e_ent.grid(row=2,column=1)
#======================================#

#=============Item information======#
i_info = LabelFrame(main_frame,text="Item Info", font=("times new roman",12,"bold"),bg="white", fg="red")
i_info.place(x=370,y=5,width=600,height=140)

#main category
m_cat = Label(i_info,text="Select Category", font=("arial",12,"bold"),bg="white")
m_cat.grid(row=0,column=0,stick=W,padx=5,pady=2)
#main category combobox
cat_com = ttk.Combobox(i_info, font=("arial",10,"bold"),width=24,state="readonly")
cat_com.grid(row=0,column=1)

#snacks category
s_cat = Label(i_info,text="Snacks", font=("arial",12,"bold"),bg="white")
s_cat.grid(row=1,column=0,stick=W,padx=5,pady=2)
#snacks category combobox
san_com = ttk.Combobox(i_info, font=("arial",10,"bold"),width=24,state="readonly")
san_com.grid(row=1,column=1)

#drinks category
d_cat = Label(i_info,text="Drinks", font=("arial",12,"bold"),bg="white")
d_cat.grid(row=2,column=0,stick=W,padx=5,pady=2)
#snacks category combobox
dri_com = ttk.Combobox(i_info, font=("arial",10,"bold"),width=24,state="readonly")
dri_com.grid(row=2,column=1)

#price
p_cat = Label(i_info,text="Price", font=("arial",12,"bold"),bg="white")
p_cat.grid(row=0,column=2,stick=W,padx=5,pady=2)
#price combobox
pri_com = ttk.Combobox(i_info, font=("arial",10,"bold"),width=22,state="readonly")
pri_com.grid(row=0,column=3)

#quantity
q_cat = Label(i_info,text="Quantity", font=("arial",12,"bold"),bg="white")
q_cat.grid(row=1,column=2,stick=W,padx=5,pady=2)
#quantity
qua_com = ttk.Entry(i_info, font=("arial",10,"bold"),width=24)
qua_com.grid(row=1,column=3)
#===================================#

#============Bill search============#
rc = Frame(main_frame,bd=2,bg="white" )
rc.place(x=1020, y=15,width=455,height=40)

#search label
se = Label(rc,text="Search Bill", font=("arial",12,"bold"),bg="red",fg="white")
se.grid(row=0,column=0,stick=W,padx=1)
#search entry
sea_com = ttk.Entry(rc, font=("arial",10,"bold"),width=24)
sea_com.grid(row=0,column=1,stick=W,padx=2,pady=2)
#search botton
btn_s = Button(rc,text="Search", font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
btn_s.grid(row=0,column=3)
#===================================#

#===============Bill area=========#
rl = LabelFrame(main_frame,text="Bill Area", font=("times new roman",12,"bold"),bg="white", fg="red")
rl.place(x=1000, y=45,width=480,height=490)

#textarea and scroll bar for bill area
scroll_y = Scrollbar(rl,orient=VERTICAL)
textarea = Text(rl,yscrollcommand=scroll_y.set,bg="white",fg="blue", font=("times new roman",12,"bold"))
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack(fill=BOTH,expand=1)
#===================================#

#==========Billing Counter==========#
bc = LabelFrame(main_frame,text="Billing Counter", font=("times new roman",12,"bold"),bg="white", fg="red")
bc.place(x=0, y=540,width=1496,height=125)

#Total
t_cat = Label(bc,text="Total", font=("arial",12,"bold"),bg="white")
t_cat.grid(row=0,column=0,stick=W,padx=5,pady=2)
#toatl entry
tol_com = ttk.Entry(bc, font=("arial",10,"bold"),width=24)
tol_com.grid(row=0,column=1)

#Grand Total
gt = Label(bc,text="Grand Total", font=("arial",12,"bold"),bg="white")
gt.grid(row=1,column=0,stick=W,padx=5,pady=2)
#Grand total entry
gat = ttk.Entry(bc, font=("arial",10,"bold"),width=24)
gat.grid(row=1,column=1)
#===================================#

#===============Button==============#
bt=Frame(bc,bd=2,bg="white")
bt.place(x=320,y=0)

#cart
btn_ca = Button(bt,text="Add To Cart", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
btn_ca.grid(row=0,column=0)

#generate bill
btn_ge = Button(bt,text="Generate Bill", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
btn_ge.grid(row=0,column=1)

#save bill
btn_sa = Button(bt,text="Save Bill", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
btn_sa.grid(row=0,column=3)

#print
btn_pr = Button(bt,text="Print", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
btn_pr.grid(row=0,column=4)

#clear
btn_cl = Button(bt,text="Clear", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
btn_cl.grid(row=0,column=5)

#exit
btn_e = Button(bt,text="Exit", font=("arial",15,"bold"),bg="orangered",fg="white",height=2,width=15,cursor="hand2")
btn_e.grid(row=0,column=6)
#===================================#




# end of window
root.mainloop()
