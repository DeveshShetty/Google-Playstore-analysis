from tkinter import *
import tkinter.messagebox as tsmg
root=Tk()
root.title("The gui for scale")
root.geometry("600x600")
def myfn():
    print(var)
    tsmg.showinfo("Alert",f"Thank You for order of { var.get() } we have placed your order")
var=StringVar()
var.set("Radio")
Label(root,text="Please select your favourate Snack",font="opensans 19 bold").pack(anchor="w")
rad=Radiobutton(root,text="dosa",variable=var,value="dosa").pack(anchor="w")
rad=Radiobutton(root,text="idly",variable=var,value="idly").pack(anchor="w")
rad=Radiobutton(root,text="wada",variable=var,value="wada").pack(anchor="w")
rad=Radiobutton(root,text="upma",variable=var,value="upma").pack(anchor="w")
Button(root,text="submit",bg="red",fg="white",command=myfn).pack(anchor="w")
root.mainloop()