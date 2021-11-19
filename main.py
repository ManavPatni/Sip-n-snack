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
main_title.place(x=0,y=10,width=1520, height=49)

main_frame = Frame(root,bd=1,relief=GROOVE,bg="white")
main_frame.place(x=0,y=65,width=1530,height=700)
#======================================#










# end of window
root.mainloop()
