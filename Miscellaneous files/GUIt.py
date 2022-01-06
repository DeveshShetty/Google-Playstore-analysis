from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tsmg
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
import collections
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import itertools
#Adjust Window
def adjustWindow(window):
 w = 1360
 h = 760
 ws = root.winfo_screenwidth()
 hs = root.winfo_screenheight() 
 x = (ws/2) - (w/2) 
 y = (hs/2) - (h/2)
 window.geometry('%dx%d+%d+%d' % (w, h, x, y)) 

 window.resizable(False, False) 
 window.configure(background='white') 
#Other stats
def Osts():
 global screen6
 #TODO: There are about 3 question put the modules in click here
 screen6 = Toplevel(root)
 screen6.title("Prediction Models & Other Stastics")
 adjustWindow(screen6) # configuring the window
 #screen6.geometry("1280x1280")
 screen6.minsize(280,280)
 
 Label(screen6, text="Prediction Models & Other Stastics", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#32CD32').pack()
# Label(screen4, text="", bg='#174873', width='200', height='50').place(x=0, y=120)
 
 #Label(screen4, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#174873', anchor=W).pack()
 Label(screen6, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#7FFF00').pack(fill=X,pady=10)
 #Label(screen4, text="",width='200', height="3", bg='#174873').pack()
 
 Label(screen6, text='''8) Amongst sports, entertainment,social media,news,events,travel and games,which
 is the category of app that is most likely to be downloaded in the coming years,
 kindly make a prediction and back it with suitable findings. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen6, text="Click Here", bg="#32CD32", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=165)#command=first_option
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 
 Label(screen6, text='''15) Is it advisable to launch an app like ’10 Best foods for you’? Do the users like these
apps? :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen6, text="Click Here", bg="#32CD32", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=255)#, command=registerd1
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 
 Label(screen6, text='''17) Does the size of the App influence the number of installs that it gets ? if,yes the
 trend is positive or negative with the increase in the app size. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen6, text="Click Here", bg="#32CD32", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=330)#, command=registerd1
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
#TODO : Implementation of extra feature free vs paid
 Label(screen6, text='''20) Comparison between Free Vs Paid Application on playstore and conclusion on this :''', font=("Open Sans", 17, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen6, text="Click Here", bg="#32CD32", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=392)#, command=registerd1
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 Button(screen6, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen6.destroy).place(x=1150,y=600)
 labelkw=Label(screen6,text="The Python Thugs : Prediction & Other",bg="#32CD32",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
 labelkw.pack(side=BOTTOM,anchor="sw",fill=X)     


# for sentiments
def Senti():
 global screen5
 #TODO: There are about 3 question put the modules in click here
 screen5 = Toplevel(root)
 screen5.title("Sentiments")
 adjustWindow(screen5) # configuring the window
 #screen5.geometry("1280x1280")
 #screen5.minsize(280,280)
 
 Label(screen5, text="Sentimentss", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#32CD32').pack()
# Label(screen4, text="", bg='#174873', width='200', height='50').place(x=0, y=120)
 
 #Label(screen4, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#174873', anchor=W).pack()
 Label(screen5, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#7FFF00').pack(fill=X,pady=10)
 #Label(screen4, text="",width='200', height="3", bg='#174873').pack()
 
 Label(screen5, text='''12) Which of all the apps given have managed to generate the most positive and
negative sentiments.Also figure out the app which has generated approximately
the same ratio for positive and negative sentiments. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen5, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=165)#command=first_option
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 
 Label(screen5, text='''13) Study and find out the relation between the Sentiment-polarity and sentiment-
subjectivity of all the apps. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen5, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=250)#, command=registerd1
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 #TODO : Implementation of extra feature Graph
 Label(screen5, text='''19) Graph on sentimental analysis (This is an additional feature) :''', font=("Open Sans", 17, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen5, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=318)#, command=registerd1
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 Button(screen5, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen5.destroy).place(x=1150,y=600)
 labelkb=Label(screen5,text="The Python Thugs : Sentiments",bg="#32CD32",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
 labelkb.pack(side=BOTTOM,anchor="sw",fill=X)
# now review and rating
def RanR():
 global screen4
 #TODO: There are about 3 question put the modules in click here
 screen4 = Toplevel(root)
 screen4.title("Rating and Review")
 adjustWindow(screen4) # configuring the window
 #screen4.geometry("1280x1280")
 #screen4.minsize(280,280)
 
 Label(screen4, text="Ratings & Reviews", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#32CD32').pack()
# Label(screen4, text="", bg='#174873', width='200', height='50').place(x=0, y=120)
 
 #Label(screen4, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#174873', anchor=W).pack()
 Label(screen4, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#7FFF00').pack(fill=X,pady=10)
 #Label(screen4, text="",width='200', height="3", bg='#174873').pack()
 
 Label(screen4, text='''4) Which category of apps have managed to get the highest maximum average ratings
 from the users. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen4, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=155)#command=first_option
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 
 Label(screen4, text='''9) All those apps who habve managed to get over 1,00,000 downloads, have they
 managed to get an average rating of 4.1 and above? An we conclude something in
 co-relation to the number of downloads and the ratings received. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen4, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=245)#, command=registerd1
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 
 Label(screen4, text='''14) Generate an interface where the client can see the reviews categorized as
 positive.negative and neutral ,once they have selected the app from a list of apps
 available for the study. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen4, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=340)#, command=registerd1
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 Button(screen4, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen4.destroy).place(x=1150,y=600)
 labelke=Label(screen4,text="The Python Thugs : Reviews & Ratings",bg="#32CD32",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
 labelke.pack(side=BOTTOM,anchor="sw",fill=X)     

#TODO :This Part Is For Downloads
def downA():
    #TODO: Add command to button
 global screen2
 screen2 = Toplevel(screen1)
 screen2.title("Download Percentage ")
 adjustWindow(screen2) # configuring the window
 #screen2.geometry("1280x1280")
 #screen2.minsize(280,280)
 Label(screen2, text="Download Percentage and count", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#32CD32').pack()
# Label(screen1, text="", bg='#174873', width='200', height='50').place(x=0, y=120)
 Label(screen2, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#7FFF00').pack(fill=X,pady=10)
 #Label(screen2, text="",width='200', height="3", bg='#174873').pack()
 Label(screen2, text='''1) What is the percentage download in each category on the playstore. :''', font=("Open Sans", 17, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen2, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=145)#command=first_option
 
 #Label(screen2, text="",width='100', height="3", bg='#174873').pack()
 Label(screen2, text='''7) All those apps , whose android version is not an issue and can work with varying
devices ,what is the percentage increase or decrease in the downloads. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen2, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=205)#command=registerd1
# Label(screen2, text="",width='100', height="3", bg='#174873').pack()
#TODO : Dont know was there in previous gui
 Label(screen2, text='''percentage increase or decrease of apps over the period of years.''', font=("Open Sans", 17, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen2, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=272)#, command=registerd1
 #Label(screen2, text="",width='100', height="3", bg='#174873').pack()
       
 Label(screen2, text='''16) Which month(s) of the year , is the best indicator to the avarage downloads that an
app will generate over the entire year?. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen2, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=335)#,
 Label(screen2, text='''2) How many apps have managed to get the following number of downloads
                            a) Between 10,000 and 50,000
                            b) Between 50,000 and 150000
                            c) Between 150000 and 500000
                            d) Between 500000 and 5000000
                            e) More than 5000000           :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen2, text="Click Here",bg="Grey", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=450)#, command=registerd1
 Button(screen2, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen2.destroy).place(x=1200,y=600)

def downB():
    #TODO: Add command to button
 global screen1
 screen3 = Toplevel(screen1)
 screen3.title("Download Analysis")
 adjustWindow(screen3) # configuring the window
# screen3.geometry("1280x1280")
 #screen3.minsize(280,280)
 Label(screen3, text="Download Analysis", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#32CD32').pack()
# Label(screen3, text="", bg='#174873', width='200', height='50').place(x=0, y=120)
 Label(screen3, text="To know:-", font=("Open Sans", 15, 'bold'), fg='white',bg='#7FFF00').pack( fill=X,pady=10)
       #Label(screen3, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#174873', anchor=W).pack()
# Label(screen3, text="",width='200', height="3", bg='#174873').pack()
 Label(screen3, text='''3) Which category of apps have managed to get the most,least and an average of
 2,50,000 downloads atleast. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen3, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=150)#, command=registerd1
 
 #Label(screen3, text="",width='100', height="3", bg='#174873').pack()
 Label(screen3, text='''5) What is the download trend category wise over the period for which the data is
 being made available. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen3, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=220)#, command=registerd1
 
 #Label(screen3, text="",width='100', height="3", bg='#174873').pack()

 Label(screen3, text='''6) For the years 2016,2017,2018 what are the category of apps that have got the most
and the least downloads. What is the percentage increase or decrease that the
apps have got over the period of three years. : ''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen3, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=310)#, command=registerd1
 
 #Label(screen3, text="",width='100', height="3", bg='#174873').pack()
     
 Label(screen3, text='''10) Across all the years ,which month has seen the maximum downloads fr each of the
category. What is the ratio of downloads for the app that qualifies as teen versus mature17+. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 #Label(screen3, text="",width='100', height="3", bg='#174873').pack()
 Button(screen3, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=395)#, command=registerd1

 Label(screen3, text='''11) Which quarter of which year has generated the highest number of install for each
app used in the study?. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen3, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=470)#, command=registerd1
 Button(screen3, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen3.destroy).place(x=1150,y=600)
#For Downloads
def down():
 global screen1
 screen1 = Toplevel(root)
 screen1.title("Downloads")
 #screen1.geometry("1200x1200")
 adjustWindow(screen1)
 #screen1.minsize(280,280) # configuring the window
 Label(screen1, text="Select download category", width='100', height="4", font=("Calibri", 28,'bold'), fg='white', bg='#32CD32').pack()
 ##Label(screen1, text="", width='100', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#d9660a').pack()
 #Label(screen1, text="",width='500', height="2", bg='white').pack()

 #Label(screen1, text="",width='500', height="5", bg='black').pack()

 Button(screen1, text="Download Percentage", bg="black", width=30, height=2,font=("Open Sans",20, 'bold'), fg='white', command=downA).pack(pady=22)
 #Label(screen1, text="",width='200', height="5", bg='white').pack()
 Button(screen1, text="Download Analysis", bg="black", width=30, height=2,font=("Open Sans",20, 'bold'), fg='white',command=downB ).pack(pady=22)#command=registerd2
 #Label(screen1, text="",width='200', height="5", bg='white').pack(anchor='n')
 labelk=Label(screen1,text="The Python Thugs : Downloads",bg="#32CD32",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
 labelk.pack(side=BOTTOM,anchor="sw",fill=X)
 Button(screen1, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen1.destroy).place(x=1200,y=600)
def rate():
#For Rating from 0 to 10
 global screen0
 screen0= Toplevel(root)
 screen0.title("Rate us")
 screen0.geometry("400x400")
 screen0.minsize(280,280)
 def rate1():
     tsmg.showinfo("Alert","Thank You for rating")
 Label(screen0,text="Ratings:Please rate us",bg="Black",fg="White",font="Opensans 19 bold",padx=19,pady=19).pack(fill=X)
 #m=IntVar()
 Scale(screen0,from_=0,to=10,orient=HORIZONTAL).pack()
 Button(screen0,text="Submit Your Rating",bg="Black",fg="white",width=30,command=rate1).pack()
def main_Window():
    global root    
root=Tk()
#guilogic

def hello():
    print("HellO Devesh How are YOuUU????")
def name():
   k=input("Enter YOur Name")
   print(k)
def myfunc():
    print("Hello")
def Help():
    tsmg.showinfo("Alert","Please Contact at tpt2019@thugs.com and send your query we will soon contact you")

root.title("The PyThon Thugs")
root.geometry("1200x1200")
root.minsize(280,280)
#adjustWindow(root)
#load=Image.open("Capture.png")
render=PhotoImage(file="Capture3.png")#ImageTK.
img=Label(root,image=render)
img.image=render
img.place(x=0,y=40)
div=Frame(root,bg="#32CD32",borderwidth=7,relief=SUNKEN)
div.pack(side=TOP,fill="x")
label1=Label(div,text="Welcome To Play Store Analysis",fg="White",bg="#32CD32",font="Opensans 19 bold")
label1.pack()
labelk=Label(root,text="",fg="White",bg="white",font="Opensans 19 bold")
labelk.pack(fill=X)



label2=Label(root,text="Please Select Your Choice",fg="White",bg="#7FFF00",font="Opensans 19 bold")
label2.pack(fill=X)
#for spacing
#labelb=Label(root,text="",fg="White",bg="white",height=16,font="Opensans 19 bold")
#labelb.pack(fill=X)
# For Downloads
b0=Button(root,text="Downloads",fg="White",bg="#00BFFF",font="Opensans 11 bold",width=30,height=3,command=down)
b0.place(x=200,y=200)
# For Reviews and rating
b1=Button(root,text="Reviews & Ratings",bg="#FFD700",fg="white",font="Opensans 11 bold",width=30,height=3,command=RanR)
b1.place(x=500,y=200)
# For Sentiments
b2=Button(root,text="Sentiments",bg="#FF69B4",fg="white",font="Opensans 11 bold",width=30,height=3,command=Senti)
b2.place(x=800,y=200)
#TODO : This is for Extra Features which is to be implemented.
b3=Button(root,text="Prediction Model & Other Stastics",bg="#9370DB",fg="white",font="Opensans 11 bold",width=30,height=3,command=Osts)
b3.place(x=500,y=300)
#TODO: Add New data attach your gui
b4=Button(root,text="Add New Data",bg="#FF4500",fg="white",font="Opensans 11 bold",width=30,height=3,command=name)
b4.place(x=500,y=400)
label2=Label(text="The Python Thugs",bg="#32CD32",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
label2.pack(side=BOTTOM,anchor="sw",fill=X)
#for menu
menu1=Menu(root)
menu2=Menu(menu1,tearoff=0)
menu2.add_command(label="Q.1",command=myfunc)
menu2.add_command(label="Q.2",command=myfunc)
menu2.add_command(label="Q.7",command=myfunc)
menu2.add_command(label="Q.16",command=myfunc)
menu2.add_separator()
menu2.add_command(label="Q.3",command=myfunc)
menu2.add_command(label="Q.5",command=myfunc)
menu2.add_command(label="Q.6",command=myfunc)
menu2.add_command(label="Q.11",command=myfunc)
menu1.add_cascade(label="Downloads",menu=menu2)
root.config(menu=menu1)
menu3=Menu(menu1,tearoff=0)
menu3.add_command(label="Q.4",command=myfunc)
menu3.add_command(label="Q.9",command=myfunc)
menu3.add_command(label="Q.14",command=myfunc)
#menu3.add_separator()
#menu3.add_command(label="Save as",command=myfunc)
#menu3.add_command(label="Exit",command=myfunc)
menu1.add_cascade(label="Ratings&Review",menu=menu3)
root.config(menu=menu1)
menu4=Menu(menu1,tearoff=0)
menu4.add_command(label="Q.12",command=myfunc)
menu4.add_command(label="Q.13",command=myfunc)
menu4.add_command(label="Q.19",command=myfunc)
#menu4.add_separator()
#menu4.add_command(label="Save as",command=myfunc)
#menu4.add_command(label="Exit",command=myfunc)
menu1.add_cascade(label="Sentiments",menu=menu4)
root.config(menu=menu1)
menu5=Menu(menu1,tearoff=0)
menu5.add_command(label="Rate",command=rate)
menu5.add_separator()
menu5.add_command(label="Help",command=Help)
menu1.add_cascade(label="Rate Us ",menu=menu5)
root.config(menu=menu1)


menu6=Menu(menu1,tearoff=0)
menu6.add_command(label="Q.8",command=rate)
menu6.add_command(label="Q.15",command=rate)
menu6.add_command(label="Q.17",command=rate)
menu6.add_command(label="Q.20",command=rate)
menu1.add_cascade(label="O & P",menu=menu6)
root.config(menu=menu1)
#photo1=PhotoImage(file="hello.png")
#label3=Label(image=photo1)
#label3.pack()


root.mainloop()
main_Window()