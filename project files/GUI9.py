from tkinter import *
import tkinter.messagebox as tsmg
root=Tk()
root.title("The gui for scale")
root.geometry("600x600")
def myfn():
    tsmg.showinfo("Alert",f"Thank You for { mu.get() } rating")
Label(root,text="Ratings:Please rate us").pack()
mu=Scale(root,from_=0,to=10,orient=HORIZONTAL).pack()
print(mu)
Button(root,text="Final",bg="red",fg="white",command=myfn).pack()
root.mainloop()