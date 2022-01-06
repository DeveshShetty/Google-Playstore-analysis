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
import tkinter.messagebox as tsmg
import csv

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tsmg
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import re,pymysql
from tkinter import Image
from PIL import Image, ImageTk
import seaborn as sns
import cv2
import test
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

from sklearn.metrics import r2_score
import statsmodels.api as sm
from tkinter import ttk
from collections import OrderedDict
import numpy as np
import math
import collections
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import itertools
import cv2
from collections import OrderedDict
from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import ttk   
import tkinter as tk
import tkinter
#import tkMessageBox
import collections
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import itertools
import csv 
#code
global data
global no
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
 
df = pd.read_csv("appdata1.csv")
print(df.head())

#DATA WRANGLING (Cleaning )
df.drop(index = 10472 , inplace = True) #dropping Row 10472
df.drop(index = 9148,inplace=True)      #dropping Row 9148
#Cleaning the data of the Installs column
df['Installs'] = df['Installs'].str.strip('+')
df['Installs'] = df['Installs'].str.replace(',','')
df['Installs'] = df['Installs'].astype(int)
# CLEANING DATA FOR COLUMN 'Price'
df['Price'] = df['Price'].astype(str)
df['Price'] = df['Price'].apply(lambda x: x.replace('$', ''))
#df['Price'] = df['Price'].astype(float)
#DATA WRANGLING (Cleaning) for Column 'SIZE'
def change_size(size):
    if 'M' in size:
        x = size[:-1]
        x = float(x)*1000000
        return(x)
    elif 'k' == size[-1:]:
        x = size[:-1]
        x = float(x)*1000
        return(x)
    else:
        return None
df["Size"] = df["Size"].map(change_size)
#filling Size which had NA
df.Size.fillna(method = 'ffill', inplace = True)
#DATA WRANGLING (Cleaning) for Column 'REVIEWS'
df['Reviews'] = df['Reviews'].astype(str)
def get_reviews(reviews):
    if reviews.endswith('.0M'):
        reviews = reviews[:-3] + '000000'
        return int(reviews)
    else:
        return int(reviews)
df['Reviews'] = df['Reviews'].apply(get_reviews)
df['Reviews'] = df['Reviews'].astype(int)

# Converting the last Updated column in the form 01-02-2003
df['Last Updated'] = df['Last Updated'].astype('datetime64[ns]')
# Now we will be creating a column that will consist of only years
df['Year'] = pd.DatetimeIndex(df['Last Updated']).year
# Now we will create a pandas series object that will be grouped by year and category
CatYear = df.groupby(by=['Category', 'Year'])
# Now we will convert into dictionary
TrendDict = CatYear.Installs.mean().to_dict()

#For question 6 we will be creating a dictionary
Year_Category = df.groupby(by = ['Year','Category'])
Year_cat_installs = Year_Category.Installs.mean()
#dictionary created
a_dict = Year_cat_installs.to_dict()


#Connecting Dataset 2 (Reviews)
review=pd.read_csv("appdata2.csv") #reading data

#print(review.head())
#print(review.isnull())
print(review.isnull().sum())
Data=review[review['Translated_Review'].notna()] #ELIMINATING NULL VALUES
#print(Data.isnull())
print(Data.isnull().sum())


#Tkinter Widgets Font
Label_font=("Calibri",18,"bold")
Label1_font=("Calibri",15,"bold")
Button_font=("Calibri",13,'bold')
Button1_font=("Calibri",15,'bold')

def list_return(x,y,positive,negative,neutral,scroll1,scroll2,scroll3):
    
    """    
    positive.delete(0,'end')
    negative.delete(0,'end')
    neutral.delete(0,'end')
    """
    df2 = pd.read_csv("appdata2.csv")
    print(df2.head(5))
    for i in range(len(df2['Sentiment'])):
        if df2['App'][i][:10]+"..."==y.get():
                    if df2['Sentiment'][i]=='Positive':
                         positive.insert('end',df2['Translated_Review'][i])
                         print(df2['Translated_Review'][i])
                    elif df2['Sentiment'][i]=='Negative':
                         negative.insert('end',df2['Translated_Review'][i])
                    elif df2['Sentiment'][i]=='Neutral':
                         neutral.insert('end',df2['Translated_Review'][i]) 

    
    scroll1.pack(side='right', fill='y' )

    scroll2.pack(side='right', fill='y' )

    scroll3.pack( side='right', fill='y' )
    positive.pack( side = 'left', fill = 'both' )
    negative.pack( side = 'left', fill = 'both' )
    neutral.pack( side = 'left', fill = 'both' )
    scroll1.config( command = positive.yview )
    scroll2.config( command = negative.yview )
    scroll3.config( command = neutral.yview )
    
#Other stats

#Adjust Window
def adjustWindow(window):
 w = 1360
 h = 760
 #ws = screenn.winfo_screenwidth()
 ws = thugs.winfo_screenwidth()
 hs = thugs.winfo_screenheight()
# hs = screenn.winfo_screenheight() 
 x = (ws/2) - (w/2) 
 y = (hs/2) - (h/2)
 window.geometry('%dx%d+%d+%d' % (w, h, x, y)) 

 window.resizable(False, False) 
 window.configure(background='white') 
#Other stats
def screen9():
    df2 = pd.read_csv("appdata2.csv")
    Apps=list(OrderedDict.fromkeys(df2['App']))
    canvas=[]
    filtered=[]
    for i in df2["App"].unique():
        filtered.append(i[:10]+"...")


    screen_start=tk.Tk()
    screen_start.resizable(False,False) 
    screen_start.geometry('1280x720')

    for i in range(4):
        can=tk.Canvas(screen_start,width=320,height=720,bg='#EFEFFB')
        canvas.append(can)
        can.grid(row=0,column=i)
    
    combo=ttk.Combobox(canvas[0],values=filtered[:100],state="readonly")
    combo.place(x=80,y=200)
    
    for i in range(1,4):
        can=tk.Canvas(canvas[i],width=280,height=600,bg='#EFEFFB')
        canvas.append(can)
        can.place(x=20,y=110)
                
    #labels for interface
    l=tk.Label(canvas[0],text='Apps',bg='#EFEFFB')
    l.config(font=("Courier", 20))
    l.place(x=115,y=50)
    l=tk.Label(canvas[1],text='Positive',bg='#EFEFFB')
    l.config(font=("Courier", 20))
    l.place(x=100,y=50)
    l=tk.Label(canvas[2],text='Neutral',bg='#EFEFFB')
    l.config(font=("Courier", 20))
    l.place(x=100,y=50)
    l=tk.Label(canvas[3],text='Negative',bg='#EFEFFB')
    l.config(font=("Courier", 20))
    l.place(x=100,y=50)
        
    scroll1=tk.Scrollbar(canvas[4])
    scroll2=tk.Scrollbar(canvas[5])
    scroll3=tk.Scrollbar(canvas[6])
    positive=tk.Listbox(canvas[4],yscrollcommand = scroll1.set,height=35,width=45,bg='#F5A9BC')
    negative=tk.Listbox(canvas[6],yscrollcommand = scroll2.set,height=35,width=43,bg='#F7F8E0')
    neutral=tk.Listbox(canvas[5],yscrollcommand = scroll3.set,height=35,width=45,bg='#F8E0F1')
                       
    btn_submit=tk.Button(canvas[0],text='Select',height=5,width=15,bg='grey',command=lambda:list_return(canvas,combo,positive,negative,neutral,scroll1,scroll2,scroll3)).place(x=90,y=400)
    
def check(x):
    data=pd.read_csv("appdata1.csv")
    df=data.columns.tolist()
    print(df,x)
    dp=pd.DataFrame([x],columns=dd)
    dat=data.append(dp)
    dat.to_csv('appdata1.csv')
    
def cal_fn():
    def cal_val():
        tsmg.showinfo("Alert",f"Your Date Is {cal.get_date()}")
        print(cal.get_date())

    top=Toplevel(screen)
    cal=Calendar(top , font="Arial 10 ", selectmode="day", year=2019 , month=7 , day=26)
    cal.pack(fill="both",expand=True)
    bt3=Button(top,text="Get Me",command=cal_val).pack()
  
def new_data():
    global new_data
   # screen51 = Toplevel(screen)    
    Button(new_data,command=startingScreen(tk.Tk())).pack()
def saveing(x,y,z,p):
    global data
    value=[]  
    if z=='App-data.csv':
        
        date1=p[0].get()
        month=p[1].get()
        year=p[2].get()
        date=month+' '+date1+','+' '+year
        dd=data.columns.tolist()
    elif z=='user_reviews.csv':
        dd=data2.columns.tolist()
     
    for i in x:
        value.append(i.get())
    if z=='App-data.csv':     
        value.insert(10,date)
        print(value)
        value[5]=str(value[5])+'+'
        value[7]='$'+str(value[7])
        print(value)
        print(dd)
        dp=pd.DataFrame([value],columns=dd)
        dat=data.append(dp)   
    elif z=='user_reviews.csv':

        dp=pd.DataFrame([value],columns=dd)
        dat=data2.append(dp)


    tk.messagebox.showinfo('Success','Data Successfully Written')
    dat.to_csv(z,index=False)
    y.config(state='disabled')
    
def check1(x):

        for i in x:
            if i.get()=='':
                
                tk.messagebox.showwarning('Fields empty','Please provide all the fields')
                return True
        try:
            if(isinstance(float(x[3].get()), float) and isinstance(float(x[4].get()), float)):
                if(float(x[3].get())<=1 and float(x[3].get())>=-1):
                    return False
                    if(float(x[4].get())<=1 and float(x[4].get())>=-1):
                        return False
                    else:
                        tk.messagebox.showwarning('Wrong Value','Please provide value in range -1 to 1')
                        return True
                else:
                    tk.messagebox.showwarning('Wrong Value','Please provide value in range -1 to 1')
                    return True
        except:
            tk.messagebox.showwarning('Wrong Value','Please provide a float value in rating column')
            return True
def check(x,z):
    d=[]
    for i in x:    
        if i.get()=='':
            tk.messagebox.showwarning('Fields empty','Please provide all the fields')
            return True
    for i in z:
        if i.get()=='':
            tk.messagebox.showwarning('Fields empty','Please provide all the fields')
            return True

    try:
        if(isinstance(float(x[2].get()), float)):# code for checking the user entered a valid rating in the entry field
            if(float(x[2].get())<=5 and float(x[2].get())>=0):
                d.append(False)
            else:
                tk.messagebox.showerror('Out of range','Rating should be between 0 to 5 only')
                return True
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a float value in rating column')
        return True
    try:
        if(isinstance(int(x[3].get()), int)):
            d.append(False)
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a integer value in Reviews')
        return True
    try:
        
        if(isinstance(float(x[4].get()[:-1]), float)):
            if(x[4].get()[-1]=='k' or x[4].get()[-1]=='M'):
                d.append(False)
            else:
                tk.messagebox.showerror('Size',"Size should end with 'k' or 'M'")
                return True           
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a integer value followed in size column')
        return True
    try:
        if(isinstance(float(x[5].get()), float)):
            d.append(False)
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a integer value in Installs')
        return True
    try:
        if(isinstance(float(x[7].get()), float)):
            d.append(False)
    except:
        tk.messagebox.showwarning('Wrong Value','Please provide a float value in Price')
        return True

    
    if set(d)==False:
        return False
    
    
    
    
       
def validate2(x,y):
    App=x[0].get()
    d=0
    ap=data2['App'].unique()
    for i in ap:
        if i.strip()==App.strip():
            msg='App named '+App+' is already present'
            tk.messagebox.showerror("Error",msg)
            d=1
    if(check1(x)):
        d=1
    if d==0:
        y.config(state='normal')
    
    
           
def validate(x,y,z):
    App=x[0].get()
    d=0
    ap=data['App']
    for i in ap:
        if i.strip()==App.strip():
            msg='App named '+App+' is already present'
            tk.messagebox.showerror("Error",msg)
            d=1
            break
            
    if check(x,z):
        
        d=1
    
    if d==0:
        y.config(state='normal')
        
def adjustWindow2(window):
    global screen
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    window.geometry("%dx%s"%(1300,hs))
    window.resizable(False,False)
    window.configure(background='white')

def startingScreen(root):
    global screen,df,data
    dates=[]
    month=['January', 'February', 'March', 'April','May','June','July','August','September', 'October', 'November','December']
    years=[]
    for i in range(1,32):
        dates.append(i)
    for i in range(2010,2020):
        years.append(i)
        #bt=Button(screen,text="Calender",command=cal_fn).pack()
    root.destroy()
    
    screen = tk.Tk()
    adjustWindow2(screen)
    screen.title("Insights of Google App's")
    
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="ENTER DATA HERE",width=100,height=1,font=("Helvetica",15,'bold'),fg='#483D8B',bg='#FFF68F', borderwidth=2, relief="groove").pack()
    
    insertition_frame_1 = tk.Frame(screen,bg='#8DEEEE',width = 500,height = 640,bd=4,relief=RIDGE)
    insertition_frame_1.place(x=100,y=80)
    
    header=data.columns.tolist()
    category= list(OrderedDict.fromkeys(data['Category']))
    content=list(OrderedDict.fromkeys(data['Content Rating']))
    genre=list(OrderedDict.fromkeys(data['Genres']))
    header2=data.columns.tolist()
    screen.title('Data Modifying')
    txt=[]
    datecombo=[]
    for i in range(1,14):
        tk.Label(insertition_frame_1,text=header[i-1],width=11,font=("Calibri",11,'italic'),fg='white',bg='Black').place(x=50,y=40*i)
        
    for i in range(1,14):
        if i!=2 and i!=10 and i!=9 and i!=7 and i!=11 and i!=13:
            txtfield=tk.Entry(insertition_frame_1,bd=10,insertwidth=4,bg="white")
            txt.append(txtfield)
            txtfield.place(x=150,y=40*i)
        elif i==2:
            combo=ttk.Combobox(insertition_frame_1,values=category)
            txt.append(combo)
            combo.place(x=150,y=40*i)
        elif i==9:
            combo=ttk.Combobox(insertition_frame_1,values=content,state="readonly")
            txt.append(combo)
            combo.place(x=150,y=40*i)
        elif i==10:
            combo=ttk.Combobox(insertition_frame_1,values=genre,state="readonly")
            txt.append(combo)
            combo.place(x=150,y=40*i)
        elif i==7:
            combo=ttk.Combobox(insertition_frame_1,values=['Free','Paid'],state="readonly")
            txt.append(combo)
            combo.place(x=150,y=40*i)
        elif i==11:
            combo=ttk.Combobox(insertition_frame_1,values=dates,width=2,state="readonly")
            datecombo.append(combo)
            combo.place(x=150,y=40*i)
            
            combo=ttk.Combobox(insertition_frame_1,values=month,width=10,state="readonly")
            datecombo.append(combo)
            combo.place(x=190,y=40*i)
            
            combo=ttk.Combobox(insertition_frame_1,values=years,width=5,state="readonly")
            datecombo.append(combo)
            combo.place(x=278,y=40*i)
        elif i==13:
            combo=ttk.Combobox(insertition_frame_1,values=list(data['Android Ver'].unique()),state="readonly")
            txt.append(combo)
            combo.place(x=150,y=40*i)

    btn_save=tk.Button(insertition_frame_1,text='Save',state="disabled",bd=12,width=10,fg='#483D8B',bg="#FFF68F",command=lambda:saveing(txt,btn_save,'dataset-1.csv',datecombo))    
    btn_validate=tk.Button(insertition_frame_1,text='Validate',bd=12,width=10,fg='#483D8B',bg="#FFF68F",command=lambda:validate(txt,btn_save,datecombo))
    btn_validate.place(x=100,y=580)
    btn_save.place(x=250,y=580)   

    insertition_frame_2 = tk.Frame(screen,bg='#8DEEEE',width = 500,height = 640,bd=4,relief=RIDGE)
    insertition_frame_2.place(x=700,y=80)
    
    txt2=[]
    for i in range(1,6):
        tk.Label(insertition_frame_2,text=header2[i-1],width=17,font=("Calibri",11,'italic'),fg='#483D8B',bg='#8DEEEE').place(x=50,y=40*i)
        
    for i in range(1,6):
            if i!=3:
                txtfield=tk.Entry(insertition_frame_2,bd=10,insertwidth=4,bg="white")
                txt2.append(txtfield)
                txtfield.place(x=250,y=40*i)
            elif i==3:
                combo=ttk.Combobox(insertition_frame_2,values=['Positive','Negative','Neutral'],state="readonly")
                txt2.append(combo)
                combo.place(x=250,y=40*i)

    btn_save1=tk.Button(insertition_frame_2,text='Save',state="disabled",bd=12,width=10,fg='#483D8B',bg="#FFF68F",command=lambda:saveing(txt2,btn_save1,'dataset-2.csv',''))    
    btn_validate1=tk.Button(insertition_frame_2,text='Validate',bd=12,width=10,fg='#483D8B',bg="#FFF68F",command=lambda:validate2(txt2,btn_save1))
    btn_validate1.place(x=100,y=580)
    btn_save1.place(x=250,y=580)
    screen.mainloop()
 
def createWindow(window):
    window.geometry('1366x768')
    window.resizable(True,True)
    window.configure(background="white")
    
def quarter(x):
        if x !='0':
            x=x.split()
        if x[0]=='January' or x[0]=='February' or x[0]=='March':
            x[0]='January-March '+str(x[-1])
            return (x[0])
        elif x[0]=='April' or x[0]=='May' or x[0]=='June':
            x[0]='April-June '+str(x[-1])
            return (x[0])
        elif x[0]=='July' or x[0]=='August' or x[0]=='September':
            x[0]='July-September '+str(x[-1])
            return (x[0])
        elif x[0]=='October' or x[0]=='November' or x[0]=='December':
            x[0]='October-December '+str(x[-1])
            return (x[0])
    
def plotquestion11(df_app):
    sns.set(style="white")
    f, ax = plt.subplots(figsize=(16,16))
    sns.barplot(x='Installs',y='Last Updated',data=df_app,ci=None)
    plt.title("QUARTER OF YEAR WITH NUMBER OF INSTALLS")

    return f

def question11():
    df_app=pd.read_csv('appdata1.csv')
    df_app=df_app.dropna()
    df_app=df_app.drop_duplicates(subset='App')
    df_app['Installs']=df_app['Installs'].apply(lambda a:a.split('+')[0])   #Removes '+' from Installs
    se=df_app['Installs'].apply(lambda a:a.split(','))                      #Removes ',' from Installs 
    df_app['Installs']=se.apply(lambda a:add_list(a))                      #Convert str to int values 
    df_app['Price']=df_app['Price'].apply(lambda a:remove_curr(a))  #Removes '$' from Price
    df_app['Last Updated']=df_app['Last Updated'].apply(lambda a:quarter(a))
    root11 = tkinter.Tk()
    root11.wm_title("Embedding in Tk")
    label11 = tkinter.Label(root11, text="Matplotlib with Seaborn in Tkinter")
    label11.pack()
    fig11 = plotquestion11(df_app)
    canvas11 = FigureCanvasTkAgg(fig11, master=root11)  # A tk.DrawingArea.
    canvas11.draw()
    canvas11.get_tk_widget().pack()
    button11 = tkinter.Button(root11, text="Quit", command=root11.destroy)
    button11.pack()
    tkinter.mainloop()
 

def first():    
    no = data['Category'].value_counts()
    percent = (no/data['Category'].count())*100
    plt.figure(figsize=(8,8),facecolor='pink')
    percent.plot(kind='bar')
    plt.title('Downloads per Category in percent',color='red')
    plt.xlabel('Category',color='blue')
    plt.ylabel('Percentage',color='blue')
    plt.savefig('yes.png')

def second():
    temp=StringtoInt()
    #print(sum(temp))
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    
    for i in temp:
        if i>=10000 and i<50000:
            c1=c1+1
        elif i>=50000 and i<150000:
            c2=c2+1
        elif i>=150000 and i<500000:
            c3=c3+1
        elif i>=500000 and i<5000000:
            c4=c4+1
        elif i>=5000000:
            c5=c5+1
    
    c=[c1,c2,c3,c4,c5]
#c=Downloadrate(info)
    category=('10k-50k','50k-15k','15k-5lakh','5lakh-50lakh','more than 50lakh')
    plt.figure(figsize=(8,8),facecolor='pink')
    plt.bar(category,c,color='grey',edgecolor='yellow',linewidth=3)
    plt.title('Number of Apps with different dowload rate',color='red')
    plt.xlabel('Number of downloads',color='purple')
    plt.ylabel('Number of Apps',color='purple')
    plt.savefig('new.png')

def fig1():
    
    fig1=Tk()
    fig1.title("Q.1")
    createWindow(fig1)
    Label(fig1,text="What is the percentage download in each category on the playstore ? ",width="100",height="2",font=Label1_font,fg='white',bg='black').pack(fill=X)
    #Label(fig1,text="family as the  ",width="100",height="2",font=Label1_font,fg='Black',bg='white').place(x=1200,y=80)
    #b1= Button(fig1, text="BACK",bg="Black", width="10", height="1",fg='white',command=fig1.destroy).place(x=1200,y=800) 
    f=Figure(figsize=(12,8),dpi=85)
    a=f.add_subplot(111)   
    a.pie(df['Category'].value_counts().values,autopct= '%1.1f%%',pctdistance=1.1)
    a.legend(df['Category'].value_counts().index,loc ='center left',bbox_to_anchor=(1.04, 0.5),ncol = 1)
    canvas=FigureCanvasTkAgg(f,fig1)
    canvas.get_tk_widget().place(x=5,y=58)
    canvas.draw()
    fig1.mainloop()
    
def fig2():
    #fig2=Tk()
    fig2 = Toplevel(screen2)
    fig2.title("QUESTION 2")
    
    #TODO: There are about 3 question put the modules in click here
    
    #.title("Prediction Models & Other Stastics")
    adjustWindow(fig2) # configuring the window
    #screen6.geometry("1280x1280")
     #screen6.minsize(280,280)
    #createWindow(fig2)
    Label(fig2, text="Question 2", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg="Black").pack()
    #Label(fig2,text="How many apps have managed to get the following number of downloads \n a) Between 10,000 and 50,000 \n b) Between 50,000 and 150000 \n c) Between 150000 and 500000 \n d) Between 500000 and 5000000 \n e) More than 5000000",width="100",height="7",font=("Calibri",13,"bold"),fg='white',bg='#174873').place(x=0,y=0)
    #cut_bins = df.Installs.unique()
    #print(cut_bins)
    Label(fig2,text="""  Apps getting downloads between 10k to 50K 985     
          """,font=("Opensans",15,"bold"),fg='white',bg='Black').pack(padx=20,pady=20)
    Label(fig2,text="""  Apps getting downloads between 50k to 150K 1550   """,font=("Opensans",15,"bold"),fg='white',bg='Black').pack(padx=20,pady=20)
    Label(fig2,text="""  Apps getting downloads between 150k to 500K 0     """,font=("Opensans",15,"bold"),fg='white',bg='Black').pack(padx=20,pady=20)
    Label(fig2,text="""  Apps getting downloads between 500k to 5000K 1917 """,font=("Opensans",15,"bold"),fg='white',bg='Black').pack(padx=20,pady=20)
    Label(fig2,text="""  Apps getting downloads more than 5000K 3737       """,font=("Opensans",15,"bold"),fg='white',bg='Black').pack(padx=20,pady=20)
    #req_cut_bins=[10000,50000,150000 ,500000,5000000,50000000,10000000000]
    #InstallCout=pd.cut(df['Installs'],req_cut_bins,labels=['10k-50k','50k-150k','150k-500k','500k-5000k','5000k-50000k','50000k +'])
    #figure1 = py.Figure(figsize=(7,8), dpi=75)
    #ax1 = figure1.add_subplot(111)
    #bar1 = FigureCanvasTkAgg(figure1, fig2)
    #bar1.get_tk_widget().place(x =820,y=0)
    #InstallCout.value_counts(sort = False).plot(kind='bar', legend=False, ax=ax1)
    Button(fig2, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen2.destroy).place(x=1150,y=600)
    #b1= Button(fig2, text="BACK",bg="Black", width="10", height="1",fg='white',command=fig2.destroy ).place(x=1200,y=800) #ax1.set_title('No of Apps Vs. No of Downloads')
    #fig2.mainloop()
    
def fig5():
    fig5=Tk()
    fig5.title("QUESTION 5")
    createWindow(fig5)
    Label(fig5,text="Download Trend Category Wise",width="110",height="3",font=Label1_font,fg='white',bg='Black').pack(fill=X)
    #b =  Button(fig5, text="back", bg="black", width="10", height="1", font=Button1_font, fg='white',command=fig5.destroy).place(x=1200, y=800)
    #Now starting with the drop down list
    render=PhotoImage(file="t2.png")#ImageTK.
    img=Label(fig5,image=render)
    img.image=render
    img.place(x=0,y=200)
    OPTIONS = df['Category'].unique()
    variable = StringVar(fig5)
    variable.set('CATEGORY')
    w = OptionMenu(fig5,variable,*OPTIONS)
    w.place(x=250,y=220)
    w.configure(bg="Black",fg='white',height="1",font=Button1_font)
    b = Button(fig5 , text = 'SHOW',bg="Black", width="10", height="1", font=Button1_font, fg='white',command = lambda:new_plot(TrendDict,variable.get()))
    b.place(x=550, y = 220)
    Button(fig5, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=fig5.destroy).place(x=1200,y=600)
    fig5.mainloop()
    
def figure6(a_dict,variable):
    year = int(variable)
    category,install = get_parameters(a_dict,year)
    #print(category)
    #print(install)
    py.title(year)
    index = np.arange(len(category))
    py.xticks(index, category, fontsize=5, rotation=90)
    py.bar(category, install)
    py.show()
    
def year_2016(a_dict,year):
    category1 = []
    install1 = []
    fig2016 = Tk()
    fig2016.title('2016')
    createWindow(fig2016)
    Label(fig2016,text="Percentage increase and decrease in 2016",width="120", height="5", font=Label1_font, fg='white', bg='#458B00').place(x=0, y=0)
    for years,installs in a_dict.items():
        if list(years)[0] == year:
            category1.append(list(years)[1])
            install1.append(installs)
    #print(category1)
    #print(install1)
    #now creating an dictionary
    dict_2016 = dict(zip(category1,install1))
    maximum = max(dict_2016,key = dict_2016.get)
    print(maximum,dict_2016[maximum])
    minimum = min(dict_2016,key = dict_2016.get)
    print(minimum,dict_2016[minimum])
    Label(fig2016,text="MAXIMUM: VIDEO_PLAYERS -  12222178.57142857\nMINIMUM: WEATHER - 750.0",width="60", height="8", font=Label1_font, fg='black', bg='white').place(x=200, y=200)
    fig2016.mainloop()
def year_2017(a_dict,year):
    category1 = []
    install1 = []
    fig2017= Tk()
    fig2017.title('2017')
    createWindow(fig2017)
    Label(fig2017,text="Percentage increase and decrease in 2017",width="120", height="5", font=Label1_font, fg='white', bg='#458B00').place(x=0, y=0)
    for years,installs in a_dict.items():
        if list(years)[0] == year:
            category1.append(list(years)[1])
            install1.append(installs)
    #print(category1)
    #print(install1)
    #now creating an dictionary
    dict_2017 = dict(zip(category1,install1))
    maximum = max(dict_2017,key = dict_2017.get)
    print(maximum,dict_2017[maximum])
    minimum = min(dict_2017,key = dict_2017.get)
    print(minimum,dict_2017[minimum])
    Label(fig2017,text="MAXIMUM: GAME =7631323.026881721\nMINIMUM:MEDICAL=17026.93181818182",width="60", height="8", font=Label1_font, fg='black', bg='white').place(x=200, y=200)
    fig2017.mainloop()

def year_2018(a_dict,year):
    category2 = []
    install2 = []
    fig2018= Tk()
    fig2018.title('2018')
    createWindow(fig2018)
    Label(fig2018,text="Percentage increase and decrease in 2018 ",width="120", height="5", font=Label1_font, fg='white', bg='#458B00').place(x=0, y=0)
    for years,installs in a_dict.items():
        if list(years)[0] == year:
            category2.append(list(years)[1])
            install2.append(installs)
    #print(category1)
    #print(install1)
    #now creating an dictionary
    dict_2018 = dict(zip(category2,install2))
    maximum = max(dict_2018,key = dict_2018.get)
    print(maximum,dict_2018[maximum])
    minimum = min(dict_2018,key = dict_2018.get)
    print(minimum,dict_2018[minimum])
    Label(fig2018,text="MAXIMUM :COMMUNICATION =118791514.18248175\nMINIMUM:MEDICAL =164144.5357142857",width="60", height="8", font=Label1_font, fg='black', bg='white').place(x=200, y=200)
    fig2018.mainloop()    
#Question 6    
def fig6():
    fig6=Tk()
    fig6.title("QUESTION 6")
    createWindow(fig6)
    Label(fig6,text="For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads.\n What is the percentage increase or decrease that the apps have got over the period of three years ?",width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig6, text="back",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=fig6.destroy).place(x=1200,y=600) 
    OPTIONS = ['2016','2017','2018']
    variable = StringVar(fig6)
    variable.set('CATEGORY')
    w = OptionMenu(fig6, variable, *OPTIONS)
    w.place(x=250, y=220)
    w.configure(bg="#7FFF00", fg='white', height="1", font=Button1_font)
    b = Button(fig6, text='SHOW',bg="#7FFF00", width="10", height="1", font=Button1_font, fg='white', command = lambda:figure6(a_dict,variable.get()))
    b.place(x=550, y=220)
    b1 = Button(fig6,text='2016',bg="#7FFF00",width = '10',height = '1',font=Button1_font, fg='white',command = lambda:year_2016(a_dict,2016))
    b1.place(x=250,y=300)
    b1 = Button(fig6,text='2017',bg="#7FFF00",width = '10',height = '1',font=Button1_font, fg='white',command = lambda:year_2017(a_dict,2017))
    b1.place(x=250,y=400)
    b1 = Button(fig6,text='2018',bg="#7FFF00",width = '10',height = '1',font=Button1_font, fg='white',command = lambda:year_2018(a_dict,2018))
    b1.place(x=250,y=500)
    fig6.mainloop()
    
def fig8():
    
    fig8=Tk()
    fig8.title("QUESTION 8")
    createWindow(fig8)
    Label(fig8,text="Amongst sports, entertainment,social media,news,events,travel and games,\n Which is the category of app that is most likely to be downloaded in the coming years,\n kindly make a prediction and back it with suitable findings ?",width="120",height="5",font=Label1_font,fg='white',bg='#174873').place(x=0,y=0)
    b1= Button(fig8, text="BACK",bg="#e79700", width="10", height="1", font=Button1_font,fg='white',command=fig8.destroy).place(x=1200,y=600) 
    # Now starting with the drop down list
    OPTIONS = ['SPORTS','ENTERTAINMENT','SOCIAL','NEWS_AND_MAGAZINES','EVENTS','TRAVEL_AND_LOCAL','GAME']
    variable = StringVar(fig8)
    variable.set('CATEGORY')
    w = OptionMenu(fig8, variable, *OPTIONS)
    w.place(x=250, y=220)
    w.configure(bg="#e79700", fg='white', height="1", font=Button1_font)
    b = Button(fig8 , text = 'SHOW',bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command = lambda:new_plot(TrendDict,variable.get()))
    b.place(x=550, y=220)          
    fig8.mainloop()
    
def fig9():
    
    fig9=Tk()
    fig9.title("QUESTION 9")
    createWindow(fig9)
    Label(fig9,text="All those apps who have managed to get over 1,00,000 downloads,\n have they managed to get an average rating of 4.1 and above? \n An we conclude something in co-relation to the number of downloads and the ratings received ?",width="120",height="5",font=Label1_font,fg='white',bg='#174873').place(x=0,y=0)
    b1= Button(fig9, text="BACK",bg="#e79700", width="10", height="1", font=Button1_font,fg='white',command=fig9.destroy).place(x=1200,y=600) 
    figure9 = py.Figure(figsize = (7,8) , dpi = 75)
    ax9 = figure9.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure9, fig9)
    bar2.get_tk_widget().place(x=70, y=100)
    #Now we will switch to the Rating column
    #this will make the NaN values present in the rating column as zero
    df.loc[df['Rating'].isna(),'Rating'] = 0
    #This will create dataframe GoodApps that will consists the Apps whose Installs is greater than 1,00,000
    GoodApps = df[df['Installs'] >= 100000]
    #Creating a column Greater that will help in plotting
    GoodApps['Greater'] = GoodApps['Rating'].apply(lambda x: '>4.1' if x > 4.1 else '<4.1')
    #Now we will groupby with Greater
    GroupGoodApps = GoodApps.groupby(by = 'Greater')
    GroupGoodApps['Rating'].count().plot(kind = 'bar' , legend = False , ax = ax9)
    bar2.draw()           
    fig9.mainloop()
    
def add_list(x):
        sum=' '
        for i in range(0,len(x)):
            sum+=x[i]
        return int(sum)
def remove_curr(x):
        if x !='0':
            x=x.split('$')[1]
        return float(x)
    
def plotquestion16(df_app):
        sns.set(style="white")
        f, ax = plt.subplots(figsize=(22,19))
        sns.barplot(x='Installs',y='Last Updated',data=df_app,ci=None)
        plt.title('Month')
        return f 
def month(x):
        if x !='0':
            x=x.split()
        return str(x[0])  
    
def figure16():
    df_app=pd.read_csv('appdata1.csv')
    df_app=df_app.dropna()
    df_app.duplicated(subset='App').value_counts()
    df_app=df_app.drop_duplicates(subset='App')
    df_app['Installs']=df_app['Installs'].apply(lambda a:a.split('+')[0])   #Removes '+' from Installs
    se=df_app['Installs'].apply(lambda a:a.split(','))                      #Removes ',' from Installs 
    df_app['Installs']=se.apply(lambda a:add_list(a))                      #Convert str to int 
    df_app['Price']=df_app['Price'].apply(lambda a:remove_curr(a)) 
    df_app.drop(df_app[df_app['Installs'] < 250000].index, inplace = True)
    df_app['Last Updated']=df_app['Last Updated'].apply(lambda a:month(a))
    
    root16 = tkinter.Tk()
    root16.wm_title("Embedding in Tk")
    label16= tkinter.Label(root16, text="Matplotlib with Seaborn in Tkinter")
    label16.pack()
    fig16 = plotquestion16(df_app)
        
    canvas16 = FigureCanvasTkAgg(fig16, master=root16)  # A tk.DrawingArea.
    canvas16.draw()
    canvas16.get_tk_widget().pack()
    button16 = tkinter.Button(root16, text="Quit", command=root16.destroy)
    button16.pack()
    tkinter.mainloop()

    

    
def s2():
     f=cv2.imread('2.png')
     text=cv2.imshow('image',f)
def s3():
     f=cv2.imread('3.png')
     text=cv2.imshow('image',f)
     
def s4():
     f=cv2.imread('4.png')
     text=cv2.imshow('image',f)
     
def s5():
     f=cv2.imread('5.png')
     text=cv2.imshow('image',f)
     
def s6():
     f=cv2.imread('6.png')
     text=cv2.imshow('image',f)
     
def s7():
     #Label(text="7.Android",fg="White",bg="Black").pack()
     f=cv2.imread('7.png')
     text=cv2.imshow('image',f)
def s8():
     f=cv2.imread('8.png')
     text=cv2.imshow('image',f)
     
def s9():
     f=cv2.imread('9.png')
     text=cv2.imshow('image',f)
     
def s10():
     f=cv2.imread('10new.png')
     text=cv2.imshow('image',f)
     
def s11():
     f=cv2.imread('11new.png')
     text=cv2.imshow('image',f)
     
def s12():
     f=cv2.imread('12new.png')
     text=cv2.imshow('image',f)
     
def s13():
     f=cv2.imread('13.png')
     text=cv2.imshow('image',f)
     
def s14():
     f=cv2.imread('14.png')
     text=cv2.imshow('image',f)
     
def s15():
     f=cv2.imread('15new.png')
     text=cv2.imshow('image',f)
     
def s16():
     f=cv2.imread('16new.png')
     text=cv2.imshow('image',f)
def s17():
     f=cv2.imread('17new.png')
     text=cv2.imshow('image',f)     
def s20():
     f=cv2.imread('free.png')
     text=cv2.imshow('image',f)    
def s21():
     f=cv2.imread('21.png')
     text=cv2.imshow('image',f) 
    
 
 
 
 
###### 
def Osts():
 global screen6
 #TODO: There are about 3 question put the modules in click here
 screen6 = Toplevel(root)
 screen6.title("Prediction Models & Other Stastics")
 adjustWindow(screen6) # configuring the window
 #screen6.geometry("1280x1280")
 screen6.minsize(280,280)
 
 Label(screen6, text="Prediction Models & Other Stastics", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#9370DB').pack()
# Label(screen4, text="", bg='#174873', width='200', height='50').place(x=0, y=120)
 
 #Label(screen4, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#174873', anchor=W).pack()
 Label(screen6, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#7FFF00').pack(fill=X,pady=10)
 #Label(screen4, text="",width='200', height="3", bg='#174873').pack()
 
 Label(screen6, text='''8) Amongst sports, entertainment,social media,news,events,travel and games,which
 is the category of app that is most likely to be downloaded in the coming years,
 kindly make a prediction and back it with suitable findings. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen6, text="Click Here", bg="#9370DB", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=fig8).place(x=1150,y=165)#command=first_option
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 
 Label(screen6, text='''15) Is it advisable to launch an app like ’10 Best foods for you’? Do the users like these
apps? :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen6, text="Click Here", bg="#9370DB", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s15).place(x=1150,y=255)#, command=registerd1
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 
 Label(screen6, text='''17) Does the size of the App influence the number of installs that it gets ? if,yes the
 trend is positive or negative with the increase in the app size. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen6, text="Click Here", bg="#9370DB", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s17).place(x=1150,y=330)#, command=registerd1
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
#TODO : Implementation of extra feature free vs paid
 Label(screen6, text='''20) Comparison between Free Vs Paid Application on playstore and conclusion on this :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen6, text="Click Here", bg="#9370DB", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s20).place(x=1150,y=392)#, command=registerd1
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 Button(screen6, text="Back", bg="#7FFF00", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen6.destroy).place(x=1150,y=600)
 labelkw=Label(screen6,text="The Python Thugs : Prediction & Other",bg="#9370DB",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
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
 
 Label(screen5, text="Sentimentss", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg="#FF69B4").pack()
# Label(screen4, text="", bg='#174873', width='200', height='50').place(x=0, y=120)
 
 #Label(screen4, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#174873', anchor=W).pack()
 Label(screen5, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#7FFF00').pack(fill=X,pady=10)
 #Label(screen4, text="",width='200', height="3", bg='#174873').pack()
 
 Label(screen5, text='''12) Which of all the apps given have managed to generate the most positive and
negative sentiments.Also figure out the app which has generated approximately
the same ratio for positive and negative sentiments. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen5, text="Click Here",bg="#FF69B4", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s12).place(x=1150,y=165)#command=first_option
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 
 Label(screen5, text='''13) Study and find out the relation between the Sentiment-polarity and sentiment-
subjectivity of all the apps. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen5, text="Click Here",bg="#FF69B4", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s13).place(x=1150,y=250)#, command=registerd1
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 #TODO : Implementation of extra feature Graph
 #Label(screen5, text='''19) Graph on sentimental analysis (This is an additional feature) :''', font=("Open Sans", 17, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 #Button(screen5, text="Click Here", bg="#FF69B4", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white').place(x=1150,y=318)#, command=registerd1
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 Button(screen5, text="Back",bg='#7FFF00', width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen5.destroy).place(x=1150,y=600)
 labelkb=Label(screen5,text="The Python Thugs : Sentiments",bg="#FF69B4",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
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
 
 Label(screen4, text="Ratings & Reviews", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg="#FFD700").pack()
# Label(screen4, text="", bg='#174873', width='200', height='50').place(x=0, y=120)
 
 #Label(screen4, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#174873', anchor=W).pack()
 Label(screen4, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#7FFF00').pack(fill=X,pady=10)
 #Label(screen4, text="",width='200', height="3", bg='#174873').pack()
 
 Label(screen4, text='''4) Which category of apps have managed to get the highest maximum average ratings
 from the users. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen4, text="Click Here",bg="#FFD700", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command =s4).place(x=1150,y=155)#command=first_option
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 
 Label(screen4, text='''9) All those apps who habve managed to get over 1,00,000 downloads, have they
 managed to get an average rating of 4.1 and above? An we conclude something in
 co-relation to the number of downloads and the ratings received. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen4, text="Click Here",bg="#FFD700", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=fig9).place(x=1150,y=245)#, command=registerd1
 
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 
 Label(screen4, text='''14) Generate an interface where the client can see the reviews categorized as
 positive.negative and neutral ,once they have selected the app from a list of apps
 available for the study. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen4, text="Click Here",bg="#FFD700", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command =screen9).place(x=1150,y=340)#, command=registerd1
 #Label(screen4, text="",width='100', height="3", bg='#174873').pack()
 Button(screen4, text="Back",bg='#7FFF00', width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen4.destroy).place(x=1150,y=600)
 labelke=Label(screen4,text="The Python Thugs : Reviews & Ratings",bg="#FFD700",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
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
 Label(screen2, text="Download Percentage and count", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg='black').pack()
# Label(screen1, text="", bg='#174873', width='200', height='50').place(x=0, y=120)
 Label(screen2, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='black').pack(fill=X,pady=10)
 #Label(screen2, text="",width='200', height="3", bg='#174873').pack()
 Label(screen2, text='''1) What is the percentage download in each category on the playstore. :''', font=("Open Sans", 17, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen2, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=fig1).place(x=1150,y=145)#command=first_option
 
 #Label(screen2, text="",width='100', height="3", bg='#174873').pack()
 Label(screen2, text='''7) All those apps , whose android version is not an issue and can work with varying devices 
      ,what is the percentage increase or decrease in the downloads. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen2, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s7).place(x=1150,y=205)#command=registerd1
# Label(screen2, text="",width='100', height="3", bg='#174873').pack()
#TODO : Dont know was there in previous gui
 Label(screen2, text='''10.b) What is the ratio of downloads for the app that qualifies as teen versus mature17+.''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen2, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s21).place(x=1150,y=272)#, command=registerd1
 #Label(screen2, text="",width='100', height="3", bg='#174873').pack()
       
 Label(screen2, text='''16) Which month(s) of the year , is the best indicator to the avarage downloads that an
app will generate over the entire year?. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen2, text="Click Here", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s16).place(x=1150,y=335)
 Label(screen2, text='''2) How many apps have managed to get the following number of downloads
                            a) Between 10,000 and 50,000
                            b) Between 50,000 and 150000
                            c) Between 150000 and 500000
                            d) Between 500000 and 5000000
                            e) More than 5000000           :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen2, text="Click Here",bg="Grey", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=fig2).place(x=1150,y=450)#, command=registerd1
 Button(screen2, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen2.destroy).place(x=1150,y=600)

def downB():
    #TODO: Add command to button
 global screen3
 screen3 = Toplevel(screen1)
 screen3.title("Download Analysis")
 adjustWindow(screen3) # configuring the window
# screen3.geometry("1280x1280")
 #screen3.minsize(280,280)
 Label(screen3, text="Download Analysis", width='200', height="2", font=("Calibri", 22,'bold'), fg='white', bg='black').pack()
# Label(screen3, text="", bg='#174873', width='200', height='50').place(x=0, y=120)
 Label(screen3, text="To know:-", font=("Open Sans", 15, 'bold'), fg='white',bg='black').pack( fill=X,pady=10)
       #Label(screen3, text="To know:-", font=("Open Sans", 20, 'bold'), fg='white',bg='#174873', anchor=W).pack()
# Label(screen3, text="",width='200', height="3", bg='#174873').pack()
 Label(screen3, text='''3) Which category of apps have managed to get the most,least and an average of
 2,50,000 downloads atleast. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen3, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s3).place(x=1150,y=150)#, command=registerd1
 
 #Label(screen3, text="",width='100', height="3", bg='#174873').pack()
 Label(screen3, text='''5) What is the download trend category wise over the period for which the data is
 being made available. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen3, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=fig5).place(x=1150,y=220)#, command=registerd1
 
 #Label(screen3, text="",width='100', height="3", bg='#174873').pack()

 Label(screen3, text='''6) For the years 2016,2017,2018 what are the category of apps that have got the most
and the least downloads. What is the percentage increase or decrease that the
apps have got over the period of three years. : ''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen3, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=fig6).place(x=1150,y=310)#, command=registerd1
 
 #Label(screen3, text="",width='100', height="3", bg='#174873').pack()
     
 Label(screen3, text='''10.a) Across all the years ,which month has seen the maximum downloads fr each of the
 category. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 #Label(screen3, text="",width='100', height="3", bg='#174873').pack()
 Button(screen3, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s10).place(x=1150,y=395)#, command=registerd1

 Label(screen3, text='''11) Which quarter of which year has generated the highest number of install for each
 app used in the study?. :''', font=("Open Sans", 15, 'bold'), fg='black',bg='white', anchor=W).pack(fill=X,pady=10,padx=20)
 Button(screen3, text="Click Here", bg="black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=s11).place(x=1150,y=470)#, command=registerd1
 Button(screen3, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen3.destroy).place(x=1150,y=600)
#For Downloads
def down():
 global screen1
 screen1 = Toplevel(root)
 screen1.title("Downloads")
 #screen1.geometry("1200x1200")
 adjustWindow(screen1)
 #screen1.minsize(280,280) # configuring the window
 Label(screen1, text="Select download category", width='100', height="4", font=("Calibri", 28,'bold'), fg='white', bg="#00BFFF").pack()
 ##Label(screen1, text="", width='100', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#d9660a').pack()
 #Label(screen1, text="",width='500', height="2", bg='white').pack()

 #Label(screen1, text="",width='500', height="5", bg='black').pack()

 Button(screen1, text="Download Percentage", bg="black", width=30, height=2,font=("Open Sans",20, 'bold'), fg='white', command=downA).pack(pady=22)
 #Label(screen1, text="",width='200', height="5", bg='white').pack()
 Button(screen1, text="Download Analysis", bg="black", width=30, height=2,font=("Open Sans",20, 'bold'), fg='white',command=downB ).pack(pady=22)#command=registerd2
 #Label(screen1, text="",width='200', height="5", bg='white').pack(anchor='n')
 labelk=Label(screen1,text="The Python Thugs : Downloads",bg="#00BFFF",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
 labelk.pack(side=BOTTOM,anchor="sw",fill=X)
 Button(screen1, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen1.destroy).place(x=1150,y=600)






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
    #root=Tk()
#guilogic
    root=Toplevel(screenn)
    root.title("The PyThon Thugs")
    root.geometry("1200x1200")
    root.minsize(280,280)
    
    def hello():
        print("HellO Devesh How are YOuUU????")
    def name():
       k=input("Enter YOur Name")
       print(k)
    def myfunc():
        print("Hello")
    def Help():
        tsmg.showinfo("Alert","Please Contact at tpt2019@thugs.com and send your query we will soon contact you")
    
    
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
    render=PhotoImage(file="Capture3.png")#ImageTK.
    img=Label(root,image=render)
    img.image=render
    img.place(x=0,y=40)
    div=Frame(root,bg="#32CD32",borderwidth=7,relief=SUNKEN)
    div.pack(side=TOP,fill="x")
    
    
    
    label2=Label(root,text="Please Select Your Choice",fg="White",bg="#7FFF00",font="Opensans 19 bold")
    label2.pack(fill=X)
    #for spacing
    #labelb=Label(root,text="",fg="White",bg="white",height=16,font="Opensans 19 bold")
    #labelb.pack(fill=X)
    # For Downloads
    b0=Button(root,text="Downloads",fg="White",bg="#00BFFF",font="Opensans 12 bold",width=30,height=3,command=down)
    b0.place(x=200,y=200)
    # For Reviews and rating
    b1=Button(root,text="Reviews & Ratings",bg="#FFD700",fg="white",font="Opensans 12 bold",width=30,height=3,command=RanR)
    b1.place(x=525,y=200)
    # For Sentiments
    b2=Button(root,text="Sentiments",bg="#FF69B4",fg="white",font="Opensans 12 bold",width=30,height=3,command=Senti)
    b2.place(x=850,y=200)
    #TODO : This is for Extra Features which is to be implemented.
    b3=Button(root,text="Prediction Model & Other Stastics",bg="#9370DB",fg="white",font="Opensans 12 bold",width=30,height=3,command=Osts)
    b3.place(x=525,y=300)
    #TODO: Add New data attach your gui
    b4=Button(root,text="Add New Data",bg="#FF4500",fg="white",font="Opensans 12 bold",width=30,height=3,command=new_data)
    b4.place(x=525,y=400)
    label2=Label(root,text="The Python Thugs",bg="#32CD32",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
    label2.pack(side=BOTTOM,anchor="sw",fill=X)
    #for menu
    menu1=Menu(root)
    menu2=Menu(menu1,tearoff=0)
    menu2.add_command(label="Q.1",command=myfunc)
    menu2.add_command(label="Q.2",command=myfunc)
    menu2.add_command(label="Q.7",command=myfunc)
    menu2.add_command(label="Q.10.b",command=myfunc)
    menu2.add_command(label="Q.16",command=myfunc)
    menu2.add_separator()
    menu2.add_command(label="Q.3",command=myfunc)
    menu2.add_command(label="Q.5",command=myfunc)
    menu2.add_command(label="Q.6",command=myfunc)
    menu2.add_command(label="Q.10.a",command=myfunc)
    menu2.add_command(label="Q.11",command=myfunc)
    
    menu1.add_cascade(label="Downloads",menu=menu2)
    root.config(menu=menu1)
    menu3=Menu(menu1,tearoff=0)
    menu3.add_command(label="Q.4",command=myfunc)
    menu3.add_command(label="Q.9",command=myfunc)
   # menu3.add_command(label="Q.14",command=myfunc)
    #menu3.add_separator()
    #menu3.add_command(label="Save as",command=myfunc)
    #menu3.add_command(label="Exit",command=myfunc)
    menu1.add_cascade(label="Ratings&Review",menu=menu3)
    root.config(menu=menu1)
    menu4=Menu(menu1,tearoff=0)
    menu4.add_command(label="Q.12",command=myfunc)
    menu4.add_command(label="Q.13",command=myfunc)
    menu4.add_command(label="Q.14",command=myfunc)
    #menu4.add_command(label="Q.19",command=myfunc)
    #menu4.add_separator()
    #menu4.add_command(label="Save as",command=myfunc)
    #menu4.add_command(label="Exit",command=myfunc)
    menu1.add_cascade(label="Sentiments",menu=menu4)
    root.config(menu=menu1)
    
    menu6=Menu(menu1,tearoff=0)
    menu6.add_command(label="Q.8",command=rate)
    menu6.add_command(label="Q.15",command=rate)
    menu6.add_command(label="Q.17",command=rate)
    menu6.add_command(label="Q.20",command=rate)
    menu1.add_cascade(label="O & P",menu=menu6)
    root.config(menu=menu1)
    
    menu5=Menu(menu1,tearoff=0)
    menu5.add_command(label="Rate",command=rate)
    menu5.add_separator()
    menu5.add_command(label="Help",command=Help)
    menu1.add_cascade(label="Rate Us ",menu=menu5)
    root.config(menu=menu1)
    
    
   
    #photo1=PhotoImage(file="hello.png")
    #label3=Label(image=photo1)
    #label3.pack()
    #root.mainloop()
    #main_Window()

def register_form():
 global screen20, fullname, email, password, repassword, university, gender, tnc 

 fullname = StringVar()
 email = StringVar()
 password = StringVar()
 repassword = StringVar()
 university = StringVar()
 gender = IntVar()
 tnc = IntVar()
 screen20 = Toplevel(screenn)
 screen20.title("Registeration Page")
 adjustWindow(screen20) # configuring the window
 Label(screen20, text="T.P.T :Registration Form", width='50', height="2",font=("Open Sans", 21, 'bold'), fg='white', bg='#32CD32').pack(fill=X)
 render=PhotoImage(file="hand.png")#ImageTK.
 img=Label(screen20,image=render)
 img.image=render
 img.place(x=700,y=150)
 #Label(screen20, text="", bg='#174873', width='70', height='25').place(x=45, y=120)
 Label(screen20, text="Full Name:", font=("Open Sans", 11, 'bold'), fg='black',bg='white', anchor=W).place(x=150, y=160)
 Entry(screen20, textvar=fullname,borderwidth=7,relief=SUNKEN).place(x=300, y=160)
 
 Label(screen20, text="Email ID:", font=("Open Sans", 11, 'bold'), fg='black',bg='white', anchor=W).place(x=150, y=210)
 Entry(screen20, textvar=email,borderwidth=7,relief=SUNKEN).place(x=300, y=210)
 
 Label(screen20, text="Gender:", font=("Open Sans", 11, 'bold'), fg='black',bg='white',anchor=W).place(x=150, y=260)
 Radiobutton(screen20, text="Male", variable=gender, value=1,bg='White').place(x=300, y=260)
 Radiobutton(screen20, text="Female", variable=gender, value=2,bg='white').place(x=370, y=260)
 
 Label(screen20, text="Password:", font=("Open Sans", 11, 'bold'), fg='black',bg='white', anchor=W).place(x=150, y=300)
 Entry(screen20, textvar=password, show="*",borderwidth=7,relief=SUNKEN).place(x=300, y=300)
 
 Label(screen20, text="Re-Password:", font=("Open Sans", 11, 'bold'),fg='black',bg='white', anchor=W).place(x=150, y=360)
 Entry(screen20, textvar=repassword, show="*",borderwidth=7,relief=SUNKEN).place(x=300, y=360)
# entry_4.place(x=300, y=410)
 Checkbutton(screen20, text="I accept all terms and conditions", variable=tnc,bg='White', font=("Open Sans", 9, 'bold'), fg='brown').place(x=175, y=410)
 Button(screen20, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown',fg='white').place(x=170, y=470)#, command=register_user
 Button(screen20, text="Back", bg="Black", width=10, height=1,font=("Open Sans",13, 'bold'), fg='white',command=screen20.destroy).place(x=1150,y=600)



def first_screen():
    global screenn,username_verify,password_verify
    #screenn=Tk()
    screenn = Toplevel(thugs)
    username_verify=StringVar()
    password_verify=StringVar()
    screenn.title("The Login")
    adjustWindow(screenn)
    div=Frame(screenn,bg="#32CD32",borderwidth=7,relief=SUNKEN)
    div.pack(side=TOP,fill="x")
    label1=Label(div,text="The Playstore App Analysis",fg="White",bg="#32CD32",height=3,font="Opensans 19 bold")
    label1.pack()
    render=PhotoImage(file="brain.png")#ImageTK.
    img=Label(screenn,image=render)
    img.image=render
    img.place(x=190,y=100)
    #Label(screenn,text="Google Playstore App Launch Study",width="100",height="2",font=("Calibri",22,'bold'),fg='white',bg='#1B4F72').pack()
    Label(text="Please Enter Your UserName & Password", font=("Open Sans", 15, 'bold'),fg="black",bg='white').pack(pady=10,padx=10)
    #Label(screenn,text="",bg='#EBF5FB',width='1500',height='650').place(x=0,y=80)
    Label(screenn,text="USERNAME",font=("Calibri",22,'bold'),bg='white',fg='black').pack(padx=20,pady=20)
    Entry(screenn,textvar=username_verify,width=50,borderwidth=7,relief=SUNKEN).pack(padx=20,pady=10)
    #Label(screenn,text="",bg='#EBF5FB').pack()
    #Label(screenn,text="",bg='#EBF5FB').pack()
    #Label(screenn,text="",bg='#EBF5FB').pack()
    Label(screenn,text="PASSWORD",font=("Calibri",22,'bold'),bg='white',fg='black').pack(padx=20,pady=20)
    Entry(screenn,textvar=password_verify,show="*",width=50,borderwidth=7,relief=SUNKEN).pack(padx=20,pady=10)
    #Label(screenn,text="",bg='#EBF5FB').pack()
    #Label(screenn,text="",bg='#EBF5FB').pack()      
    #Label(screenn,text="",bg='#EBF5FB').pack()      
    Button(screenn,text="START",bg='#32CD32',fg='white',width=15,height=1,font=("Calibri",22,'bold'),command=main_Window).pack(padx=20,pady=10)
    Button(screenn, text="New User? Register Here", height="2", width="30", bg='#00BFFF',
    font=("Open Sans", 10, 'bold'), fg='white',command=register_form ).pack()
    label2=Label(text="The Python Thugs",bg="#32CD32",fg="White",font="Opensans 19 bold",padx=19,pady=19,borderwidth=3,relief="groove")
    label2.pack(side=BOTTOM,anchor="sw",fill=X) 
    
#    screenn.mainloop()
    
#first_screen()
def zeroth_screen():
    global thugs
    thugs=Tk()
    adjustWindow(thugs)
    div=Frame(thugs,bg="#32CD32",borderwidth=7,relief=SUNKEN)
    div.pack(side=TOP,fill="x")
    label1=Label(div,text="Install Please",fg="White",bg="#32CD32",height=2,font="Opensans 19 bold")
    label1.pack()
    render=PhotoImage(file="pyto.png")#ImageTK.
    img=Label(thugs,image=render)
    img.image=render
    img.place(x=100,y=85)
    Button(thugs, text="Install", height="5", bg='#32CD32',width=40,font=("Open Sans", 10, 'bold'),command=first_screen ).place(x=800,y=391)
    thugs.mainloop()
zeroth_screen()