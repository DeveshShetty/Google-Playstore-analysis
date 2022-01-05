from tkinter import *
from tkcalendar import *
import tkinter.messagebox as tsmg
root=Tk()
def cal_fn():
    def cal_val():
        tsmg.showinfo("Alert",f"Your Date Is {cal.get_date()}")
        print(cal.get_date())

    top=Toplevel(root)
    cal=Calendar(top , font="Arial 10 ", selectmode="day", year=2019 , month=7 , day=26)
    cal.pack(fill="both",expand=True)
    bt3=Button(top,text="Get Me",command=cal_val).pack()
    
# TODO: THis Does Not Works Properly#####################################################################
def dat_fn():
    top=Toplevel(root)
    
    def dat_val():
        tsmg.showinfo("Alert",f"Your selected Date Is {ent2.get()}")
    ent2=StringVar()
    Label(top,text="Select Date").pack(padx=22,pady=22)
    ent=DateEntry(top,widt=15,bg="blue",fg="red",borderwidth=3,variable=ent2).pack(padx=22,pady=22)
    bt4=Button(top,text="Get Date",command=dat_val).pack()
############################################################################################################    
bt=Button(root,text="Calender",command=cal_fn).pack()
bt2=Button(root,text="DateEntry",command=dat_fn).pack()
root.mainloop()
