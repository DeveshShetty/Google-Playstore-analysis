
import matplotlib
import matplotlib.pyplot as py
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Label
import pandas as pd
import numpy as np
import xlsxwriter
import seaborn as sns
from collections import OrderedDict
#Creating the data frame to read the excel file 1(app list)

df = pd.read_csv('appdata1.csv')
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
# df['Price'] = df['Price'].astype(float)


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
review=pd.read_csv('appdata2.csv') #reading data

#print(review.head())
#print(review.isnull())
print(review.isnull().sum())
Data=review[review['Translated_Review'].notna()] #ELIMINATING NULL VALUES
#print(Data.isnull())
print(Data.isnull().sum())

#Tkinter Widgets Font
Label_font=("Arial Narrow",18,"bold")
Label1_font=("Calibri",15,"bold")
Button_font=("Calibri",13,'bold')
Button1_font=("Calibri",15,'bold')

# This function is used for adjusting window size and making the necessary configuration on start of window
def createWindow(window):
    window.geometry('1336x768')
    window.resizable(True,True)
    window.configure(background="#458B00")



# This function is used for Recalling home  window size 
def backtohome():
    global home
    backtohome=Tk()
    backtohome.title("HOMEPAGE")
    
    createWindow(backtohome)
    
    l = Label(backtohome,text="GOOGLE PLAYSTORE APP LAUNCH STUDY",width="500",height="2",font=Label_font,fg='white',bg='#458B00').pack()
              
    l1 = Label(backtohome,text="Percentage download in each category",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=90)
    b1= Button(backtohome, text="1",bg="#7FFF00", width="5", height="1", font=Button_font,fg='white',command=fig1).place(x=25,y=90)
               
    l2 = Label(backtohome,text="Number of Downloads",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=140)
    b2= Button(backtohome, text="2",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig2).place(x=25,y=140)
               
    l3 = Label(backtohome,text="Most,Least,Average Category",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=190)
    b3= Button(backtohome, text=" 3",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig3).place(x=25,y=190)
               
    l4 = Label(backtohome,text="Highest maximum average ratings",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=240)
    b4= Button(backtohome, text="4",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig4).place(x=25,y=240)
    
    l5 = Label(backtohome,text="Download category wise over period",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=290)
    b5= Button(backtohome, text="5",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig5).place(x=25,y=290)
               
    l6 =Label(backtohome,text="Downloads over period of three years",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=340)
    b6= Button(backtohome, text="6",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig6).place(x=25,y=340)
               
    l7 =Label(backtohome,text="Android version is not an issue",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=390)
    b7= Button(backtohome,text="7",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig7).place(x=25,y=390)
               
    l8 =Label(backtohome,text="Most likely to be downloaded",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=440)
    b8= Button(backtohome, text="8",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig8).place(x=25,y=440)
               
    l9 =Label(backtohome,text="Co-relation of downloads & ratings",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=490)
    b9= Button(backtohome, text="9",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig9).place(x=25,y=490)
               
    l10 =Label(backtohome,text="Qualifies as teen versus mature 17+.",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=90)
    b10= Button(backtohome, text="10",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig10).place(x=650,y=90)
 
    l11 =Label(backtohome,text="Year has generated highest no of install for each app",width="60",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=140)
    b11= Button(backtohome, text="11",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig11).place(x=650,y=140)
                
    l12 =Label(backtohome,text="Generate most positive & negative sentiments",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=190)
    b12= Button(backtohome, text="12",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig12).place(x=650,y=190)
                
    l13 =Label(backtohome,text="Relation between Sentiment-polarity & subjectivity ",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=240)
    b13= Button(backtohome, text="13",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig13).place(x=650,y=240)
                
    l14 =Label(backtohome,text="Reviews categorized as positive,negative & neutral",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=290)
    b14= Button(backtohome, text="14",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig14).place(x=650,y=290)
                
    l15 =Label(backtohome,text="Advisable to launch app like 10 Best foods for you?",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=340)
    b15= Button(backtohome, text="15",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig15).place(x=650,y=340)
                
    l16 =Label(backtohome,text="Indicator to aver. downloads generated entire year?",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=390)
    b16= Button(backtohome, text="16",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig16).place(x=650,y=390)
                
    l17 =Label(backtohome,text="Size of App influence number of installs",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=440)
    b17= Button(backtohome, text="17",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig17).place(x=650,y=440)
                
    l18 =Label(backtohome,text="Interface to add new data to both datasets",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=490)
    b18= Button(backtohome, text="18",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig19).place(x=650,y=490)
                
          
    backtohome.mainloop()  

#Question 1  
def fig1():
    
    fig1=Tk()
    fig1.title("QUESTION 1")
    createWindow(fig1)
    Label(fig1,width="100",height="2",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig1, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
    
    f=Figure(figsize=(12,8),dpi=80)
    a=f.add_subplot(111)   
    a.pie(df['Category'].value_counts().values,autopct= '%1.1f%%',pctdistance=1.1)
    a.legend(df['Category'].value_counts().index,loc ='center left',bbox_to_anchor=(1.04, 0.5),ncol = 1)
    
    canvas=FigureCanvasTkAgg(f,fig1)
    canvas.get_tk_widget().place(x=5,y=58)
    canvas.draw()

    fig1.mainloop()

#Question 2
def fig2():
    
    fig2=Tk()
    fig2.title("QUESTION 2")
    createWindow(fig2)
    Label(fig2,width="100",height="7",font=("Calibri",13,"bold"),fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig2, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
    
    cut_bins = df.Installs.unique()
    #print(cut_bins)
    req_cut_bins=[10000,50000,150000 ,500000,5000000,50000000,10000000000]
    InstallCout=pd.cut(df['Installs'],req_cut_bins,labels=['10k-50k','50k-150k','150k-500k','500k-5000k','5000k-50000k','50000k +'])
    
    figure1 = py.Figure(figsize=(7,8), dpi=75)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, fig2)
    bar1.get_tk_widget().place(x =400,y=10)
    InstallCout.value_counts(sort = False).plot(kind='bar', legend=False, ax=ax1)
    ax1.set_title('No of Apps Vs. No of Downloads')
    fig2.mainloop()

#Question 3
def fig3():
    
    fig3=Tk()
    fig3.title("QUESTION 3")
    createWindow(fig3)
    Label(fig3,width="100",height="3",font=("Calibri",13,"bold"),fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig3, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
    
    figure3 = Figure(figsize=(11, 9), dpi=65)
    ax3 = figure3.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure3, fig3)
    bar2.get_tk_widget().place(x = 450, y =15)
    
    #THIS MAKES A SERIES OF PANDAS (OBJECT THAT CONTAINS CATEGORIES AND MEAN INSTALL OF EACH CATEGORY)
    df.groupby('Category')['Installs'].mean().plot(kind = 'bar' ,legend = False , ax = ax3)
    bar2.draw()
    fig3.mainloop()
    
#Question 4
def fig4():
    
    fig4=Tk()
    fig4.title("QUESTION 4")
    createWindow(fig4)
    Label(fig4,width="110",height="3",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig4, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
    f=Figure(figsize=(11,9),dpi=65)
    ax=f.add_subplot(111) 
    a = df.groupby('Category')['Rating'].mean()
    x_axis = list(a.to_dict().keys())
    y_axis = list(a.to_dict().values())
    ax.scatter(x_axis,y_axis)
    ax.set_xticklabels(x_axis,rotation = 90 ,ha ='center')
    canvas=FigureCanvasTkAgg(f,fig4)
    canvas.get_tk_widget().place(x=5,y=78)
    canvas.draw()
    fig4.mainloop()
    
def year_2010():
    df['Year'] = df['Last Updated'].str[-4:]
    Category_Years = df.groupby(by=['Year', 'Category'])
    # Category_Years.describe()
    YearCat = Category_Years.Installs.mean()
    YearCat['2010'].plot.bar()
    fig_size = py.rcParams["figure.figsize"]
    #print ("Current size: ",fig_size)
    fig_size[0] = 10
    fig_size[1] = 8
    py.title("2010")
    py.rcParams["figure.figsize"] = fig_size
    py.show()
    

def year_2018():
    df['Year'] = df['Last Updated'].str[-4:]
    Category_Years = df.groupby(by=['Year', 'Category'])
    # Category_Years.describe()
    YearCat = Category_Years.Installs.mean()
    YearCat['2018'].plot.bar()
    fig_size = py.rcParams["figure.figsize"]
    #print ("Current size: ",fig_size)
    fig_size[0] = 10
    fig_size[1] = 8
    py.title("2018")
    py.rcParams["figure.figsize"] = fig_size
    matplotlib.pyplot.subplots_adjust(left=0.06, bottom=0.28, right=0.97, top=0.93, wspace=0.20, hspace=0.20)
    py.show()
    
#This function is used for Button
def getTrendDict(TrendDict,Category):
    years = []
    install = []
    for category , installs in TrendDict.items():
        if list(category)[0] == Category:
            years.append(list(category)[1])
            install.append(installs)
    return years,install

def new_plot(TrendDict,Category):
    years,install = getTrendDict(TrendDict,Category)
    py.xticks(ticks = years , labels = years)
    py.plot(years,install)
    py.show()     
    fig5.mainloop()

    
#Question 5
def fig5():
    
    fig5=Tk()
    fig5.title("QUESTION 5")
    createWindow(fig5)
    Label(fig5,width="110",height="3",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b =  Button(fig5, text="HOME PAGE", bg="#7FFF00", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    
    #Now starting with the drop down list
    OPTIONS = df['Category'].unique()
    variable = StringVar(fig5)
    variable.set('CATEGORY')
    w = OptionMenu(fig5,variable,*OPTIONS)
    w.place(x=250,y=220)
    w.configure(bg="#7FFF00",fg='white',height="1",font=Button1_font)
    b = Button(fig5 , text = 'SHOW',bg="#7FFF00", width="10", height="1", font=Button1_font, fg='white',command = lambda:new_plot(TrendDict,variable.get()))
    b.place(x=550, y = 220)
    

    

#this will return the category and corresponding number of installs
def get_parameters(a_dict,year):
    category = []
    install = []
    for years,installs in a_dict.items():
        if list(years)[0] == year:
            category.append(list(years)[1])
            install.append(installs)
    return category,install

def figure6(a_dict,variable):
    year = int(variable)
    category,install = get_parameters(a_dict,year)
    #print(category)
    #print(install)
    py.title(year)
    index = np.arange(len(category))
    py.xticks(index, category, fontsize=7, rotation=90)
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
    b1= Button(fig6, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
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
    

#Question 7
def fig7():
    android_df = df.copy()
    
    fig7=Tk()
    fig7.title("QUESTION 7")
    createWindow(fig7)
    Label(fig7,width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig7, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
    android_df = android_df[android_df['Android Ver'] == 'Varies with device']
    android_df.sort_values('Year',inplace = True)
    k = []
    for i in range(2018 - 2012 + 1):
        k.append(android_df[android_df.Year == (2012 + i)]['Installs'].sum())
    for i in range(2018 - 2012):
        print('{} to {} Download percent change : {}'.format((2012 + i), (2012 + i + 1),(((k[i + 1] - k[i]) / (k[i])) * 100)))
    Label(fig7,text="2012 to 2013 Download percent change : 2951.0\n2013 to 2014 Download percent change : 403.1137332022288\n2014 to 2015 Download percent change : 81.86387622149837\n2015 to 2016 Download percent change : 1806.729112102136\n2016 to 2017 Download percent change : 41.47751974465249\n2017 to 2018 Download percent change : 12104.35411777218",width="100", height="8", font=Label1_font, fg='black', bg='white').place(x=200, y=200)
    fig7.mainloop()
    
#Question 8
def fig8():
    
    fig8=Tk()
    fig8.title("QUESTION 8")
    createWindow(fig8)
    Label(fig8,width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig8, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
    # Now starting with the drop down list
    OPTIONS = ['SPORTS','ENTERTAINMENT','SOCIAL','NEWS_AND_MAGAZINES','EVENTS','TRAVEL_AND_LOCAL','GAME']
    variable = StringVar(fig8)
    variable.set('CATEGORY')
    w = OptionMenu(fig8, variable, *OPTIONS)
    w.place(x=250, y=220)
    w.configure(bg="#7FFF00", fg='white', height="1", font=Button1_font)
    b = Button(fig8 , text = 'SHOW',bg="#7FFF00", width="10", height="1", font=Button1_font, fg='white',command = lambda:new_plot(TrendDict,variable.get()))
    b.place(x=550, y=220)          
    fig8.mainloop()

#Question 9  
def fig9():
    
    fig9=Tk()
    fig9.title("QUESTION 9")
    createWindow(fig9)
    Label(fig9,width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig9, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
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

#Question 10
def fig10():
    
    fig10=Tk()
    fig10.title("QUESTION 10")
    createWindow(fig10)
    Label(fig10,width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig10, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
               
    fig10.mainloop()
    
#Question 11
def fig11():
    
    fig11=Tk()
    fig11.title("QUESTION 11")
    createWindow(fig11)
    Label(fig11,width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig11, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
               
    fig11.mainloop()
    
#Question 12
def fig12():
    fig12=Tk()
    fig12.title("QUESTION 12")
    createWindow(fig12)
    Label(fig12,width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig12, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
    
    polarity_sum = data.groupby('App')['Sentiment_Polarity'].sum().sort_values()
    print("Positive Rated :\n",polarity_sum.nlargest(1))
    print("Negative Rated :\n",polarity_sum.nsmallest(1))
    apps = list(data.App.unique())
    ratios = list()
    for app in apps:
       find = data.loc[data.App == app]
       pos_rat = find.loc[data.Sentiment == 'Positive']['Sentiment_Polarity'].sum()/len(find)
       neg_rat = find.loc[data.Sentiment == 'Negative']['Sentiment_Polarity'].sum()/len(find) * -1
       if abs(pos_rat-neg_rat) < 0.005:
        ratios.append((app,pos_rat,neg_rat))
    print('Apps with similar ratio for positive and Negative Sentiments are :')
    print(ratios)

    Label(fig12,text="App having Most Positive Sentiment : 10 Best Foods for You : 91.322167 \n \n App having Most Negative Sentiment : Be A Legend: Soccer : -9.726559 ",
          width="100", height="8", font=Label1_font, fg='black', bg='white').place(x=200, y=200)    

               
    fig12.mainloop()

    
#Question 13
def fig13():
    fig13=Tk()
    fig13.title("QUESTION 13")
    createWindow(fig13)
    Label(fig13,text="",width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig13, text="HOME PAGE",bg="#e79700", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
    Label(fig13,text="THE SENTIMENTS CATAGORY WISE COUNT:  Positive   : 23998\nNegative    : 8271\nNeutral    :  5163 ",
          width="100", height="8", font=Label1_font, fg='black', bg='white').place(x=200, y=200)           
    print("THE SENTIMENTS CATAGORY WISE COUNT: ",review['Sentiment'].value_counts())
    
    
    
    Data.Sentiment[Data.Sentiment =='Positive'] = 0
    Data.Sentiment[Data.Sentiment =='Neutral'] = 1
    Data.Sentiment[Data.Sentiment =='Negative'] = 2
    Data.head()
    
    Data.dtypes
    Data['Sentiment'] = Data['Sentiment'].astype('int')

    f=Figure(figsize=(12,8),dpi=80)
    a=f.add_subplot(111) 
    a=sns.scatterplot(Data['Sentiment_Polarity'],Data['Sentiment_Subjectivity'],hue=Data['Sentiment'], edgecolor='pink',palette="plasma_r")
    a.xlabel('Sentiment Polarity')
    a.ylabel('Sentiment Subjectivity')
    a.title("Sentiment Analysis")
    canvas=FigureCanvasTkAgg(f,fig13)
    canvas.get_tk_widget().place(x=5,y=58)
    canvas.draw()           
    
    fig13.mainloop()
#Question 14
def fig14():
    
    fig14=Tk()
    fig14.title("QUESTION 14")
    createWindow(fig14)
    Label(fig14,width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig14, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
               
    fig14.mainloop()
    
#Question 15

    
    
def fig15():
    
    fig15=Tk()
    fig15.title("QUESTION 15")
    createWindow(fig15)
    Label(fig15,width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig15, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
    
    kk = data.loc[(data.App == '10 Best Foods for You') & (data.Sentiment == 'Positive')]
    print(len(kk))
    print(kk['Sentiment_Polarity'].sum())
    
    Label(fig15,text="The Total number of positive Sentiments recieved by the App are 162 \n\n and Total Sentiment Polarity is 95.37216720779222 \n So it is Advisable to Launch the app like '10 BEST FOODS FOR YOU'",
          width="100",height="8",font=Label1_font,fg='black',bg='white').place(x=200,y=200)
               
    fig15.mainloop()

#Question 16
def fig16():

    fig16=Tk()
    fig16.title("QUESTION 16")
    createWindow(fig16)
    Label(fig16,width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig16, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
               
    fig16.mainloop()
    
#Question 17
def fig17():
    
    fig17=Tk()
    fig17.title("QUESTION 17")
    createWindow(fig17)
    Label(fig17,width="120",height="5",font=Label1_font,fg='white',bg='#458B00').place(x=0,y=0)
    b1= Button(fig17, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
               
    fig17.mainloop()
    


#Question 18 
    
def fig19():
    global fig19
    #screen19 = Toplevel(backtohome)
    b1=Button(fig19,command=startingScreen(tk.Tk())).pack()
    
data=pd.read_csv('appdata1.csv')

data=data.replace(np.NaN,0)
data.drop(index=[10472],inplace=True)
sample=pd.read_csv('appdata2.csv')

def saveing(x,y,z,p):
    global data
    value=[]  
    if z=='appdata1.csv':
        date1=p[0].get()
        month=p[1].get()
        year=p[2].get()
        date=month+' '+date1+','+' '+year
        dd=data.columns.tolist()
    elif z=='appdata2.csv':
        dd=sample.columns.tolist()
     
    for i in x:
        value.append(i.get())
    


    if z=='appdata1.csv':

        
        value.insert(10,date)
        print(value)
        value[5]=str(value[5])+'+'
        value[7]='$'+str(value[7])
        print(value)
        print(dd)
        dp=pd.DataFrame([value],columns=dd)
        dat=data.append(dp)
        
        
    elif z=='appdata2.csv':

        dp=pd.DataFrame([value],columns=dd)
        dat=sample.append(dp)


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
    ap=sample['App'].unique()
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
     
def adjustWindow(window):
    global screen
    ws=screen.winfo_screenwidth()
    hs=screen.winfo_screenheight()
    window.geometry('1366x768')
    window.resizable(True,True)
    window.configure(background='#458B00')

def startingScreen(root):
    global screen,df,data
    dates=[]
    month=['January', 'February', 'March', 'April','May','June','July','August','September', 'October', 'November','December']
    years=[]
    for i in range(1,32):
        dates.append(i)
    for i in range(2010,2020):
        years.append(i)

    root.destroy()
    
    screen = tk.Tk()
    adjustWindow(screen)
    screen.title("Insights of Google App's")
    
    tk.Label(screen,text="",bg="white").pack()
    tk.Label(screen,text="INSERT VALUES",width=1000,height=1,font=("Helvetica",15,'bold'),fg='white',bg='#458B00', borderwidth=2, relief="groove").pack()
    
    insertition_frame_1 = tk.Frame(screen,bg='#7FFF00',width = 500,height = 640,bd=4,relief=RIDGE)
    insertition_frame_1.place(x=100,y=80)
    
    tk.Label(insertition_frame_1,text="INSERT INTO GOOGLE PLAY STORE DATA SET",font=("Calibri",13,'italic'),fg='#458B00',bg='#7FFF00').place(x=90,y=0)
    
    header=data.columns.tolist()
    category= list(OrderedDict.fromkeys(data['Category']))
    content=list(OrderedDict.fromkeys(data['Content Rating']))
    genre=list(OrderedDict.fromkeys(data['Genres']))
    header2=sample.columns.tolist()
    screen.title('Data Modifying')
    txt=[]
    datecombo=[]
    for i in range(1,14):
        tk.Label(insertition_frame_1,text=header[i-1],width=11,font=("Calibri",11,'italic'),fg='#458B00',bg='#7FFF00').place(x=50,y=40*i)
        
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

    btn_save=tk.Button(insertition_frame_1,text='Save',state="disabled",bd=12,width=10,bg="#458B00",command=lambda:saveing(txt,btn_save,'DATA SET-2.csv',datecombo))    
    btn_validate=tk.Button(insertition_frame_1,text='Validate',bd=12,width=10,bg="#458B00",command=lambda:validate(txt,btn_save,datecombo))
    btn_validate.place(x=100,y=580)
    btn_save.place(x=250,y=580)   

    insertition_frame_2 = tk.Frame(screen,bg='#7FFF00',width = 500,height = 640,bd=4,relief=RIDGE)
    insertition_frame_2.place(x=700,y=80)
    
    tk.Label(insertition_frame_2,text="INSERT INTO REVIEW DATASET",font=("Calibri",13,'italic'),fg='#458B00',bg='#7FFF00').place(x=130,y=0)
    txt2=[]
    for i in range(1,6):
        tk.Label(insertition_frame_2,text=header2[i-1],width=17,font=("Calibri",11,'italic'),fg='#458B00',bg='#7FFF00').place(x=50,y=40*i)
        
    for i in range(1,6):
            if i!=3:
                txtfield=tk.Entry(insertition_frame_2,bd=10,insertwidth=4,bg="white")
                txt2.append(txtfield)
                txtfield.place(x=250,y=40*i)
            elif i==3:
                combo=ttk.Combobox(insertition_frame_2,values=['Positive','Negative','Neutral'],state="readonly")
                txt2.append(combo)
                combo.place(x=250,y=40*i)

    btn_save1=tk.Button(insertition_frame_2,text='Save',state="disabled",bd=12,width=10,bg="#458B00",command=lambda:saveing(txt2,btn_save1,'DATA SET-1.csv',''))    
    btn_validate1=tk.Button(insertition_frame_2,text='Validate',bd=12,width=10,bg="#458B00",command=lambda:validate2(txt2,btn_save1))
    btn_validate1.place(x=100,y=580)
    btn_save1.place(x=250,y=580)
    
    tk.Button(screen, text="HOME PAGE",bg="#7FFF00", width="10", height="1", font=Button1_font,fg='white',command=backtohome).place(x=0,y=0) 
    screen.mainloop()
         
  
#MainScreen (Questions Screen)  
def home():
    global home
    home=Tk()
    home.title("HOMEPAGE")
    
    createWindow(home)
    
    l = Label(home,text="GOOGLE PLAYSTORE APP LAUNCH STUDY",width="500",height="2",font=Label_font,fg='white',bg='#458B00').pack()
              
    l1 = Label(home,text="Percentage download in each category",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=90)
    b1= Button(home, text="1",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig1).place(x=25,y=90)
               
    l2 = Label(home,text="Number of Downloads",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=140)
    b2= Button(home, text=" 2",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig2).place(x=25,y=140)
               
    l3 = Label(home,text="Most,Least,Average Category",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=190)
    b3= Button(home, text="3",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig3).place(x=25,y=190)
               
    l4 = Label(home,text="Highest maximum average ratings",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=240)
    b4= Button(home, text="4",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig4).place(x=25,y=240)
    
    l5 = Label(home,text="Download category wise over period",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=290)
    b5= Button(home, text="5",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig5).place(x=25,y=290)
               
    l6 =Label(home,text="Downloads over period of three years",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=340)
    b6= Button(home, text="6",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig6).place(x=25,y=340)
               
    l7 =Label(home,text="Android version is not an issue",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=390)
    b7= Button(home, text="7",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig7).place(x=25,y=390)
               
    l8 =Label(home,text="Most likely to be downloaded",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=440)
    b8= Button(home, text="8",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig8).place(x=25,y=440)
               
    l9 =Label(home,text="Co-relation of downloads & ratings",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=25,y=490)
    b9= Button(home, text="9",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig9).place(x=25,y=490)
               
    l10 =Label(home,text="Qualifies as teen versus mature 17+",width="40",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=90)
    b10= Button(home, text="10",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig10).place(x=650,y=90)
               
    l11 =Label(home,text= "  Year has generated highest no of install for each app",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=140)
    b11= Button(home, text="11",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig11).place(x=650,y=140)
                
    l12 =Label(home,text="Generate most positive & negative sentiments",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=190)
    b12= Button(home, text="12",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig12).place(x=650,y=190)
                
    l13 =Label(home,text="Relation between Sentiment-polarity & subjectivity ",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=240)
    b13= Button(home, text="13",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig13).place(x=650,y=240)
                
    l14 =Label(home,text="Reviews categorized as positive,negative & neutral",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=290)
    b14= Button(home, text="14",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig14).place(x=650,y=290)
                
    l15 =Label(home,text="Advisable to launch app like 10 Best foods for you?",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=340)
    b15= Button(home, text="15",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig15).place(x=650,y=340)
                
    l16 =Label(home,text="Indicator to aver. downloads generated entire year?",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=390)
    b16= Button(home, text="16",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig16).place(x=650,y=390)
                
    l17 =Label(home,text="Size of App influence number of installs",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=440)
    b17= Button(home, text="17",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig17).place(x=650,y=440)
                
    l18 =Label(home,text="Interface to add new data to both datasets",width="50",height="1",font=Label_font,fg='white',bg='#458B00').place(x=650,y=490)
    b18= Button(home, text="18",bg="#7FFF00", width="5", height="1", font=("Open Sans",13,'bold'),fg='white',command=fig19).place(x=650,y=490)
                

    
    home.mainloop()
    
#Calling main function 
home()
