#libraries 
from distutils import command
import imp
from random import choice
from tkinter import *
from tkinter import ttk
from tkinter import font
from xml.sax.handler import feature_external_ges
import data

limegreen = "#add160"


freshlist = []
#definitions
def login():
    total = 0
    
    def modeselected(modechoice):
        modechoice = trans_select.get()
        freshlist.append(modechoice)

        
        
       

    def adddestination(choice_des):
        choice_des = des_select.get()
        freshlist.append(choice_des)
        
    

    def addplace(choice_place):
        choice_place = stay_select.get()
        freshlist.append(choice_place)

    #for storing user details in database 
    
    tname = username.get()
    temail = useremail.get()
    tphone = userphone.get()
    data.fill_user(tname , temail , tphone)

    #clearing data 
    tname = ""
    tphone = ""
    temail = ""
    root.destroy()
    

    #move on to booking window
    bw = Tk()
    bw.geometry('700x700')
    bw.title('Book A Trip')
    bw.iconbitmap('icon.ico')

    des_select = StringVar()
    trans_select = StringVar()
    stay_select = StringVar()

   
     
    
    #-------------RECEIPT--------------
    def gen():
        print(freshlist)
        if freshlist[1] == 'AIR':
            data.fetch_airfare(freshlist[0])
           
        elif freshlist[1] == 'RAIL':
            return
            
        elif freshlist[1] == 'ROAD':
            return
           
   
    

    #structure
    f1 = Frame(bw , background="#add160" , height=200 , width=600) 
    f1.place(x=45 , y = 20)
    f2 = Frame(bw , background="#add160" , height=200 , width=600) 
    f2.place(x=45 , y = 250)
    f3 = Frame(bw , background="#add160" , height=200 , width=600) 
    f3.place(x=45 , y = 480)
    
    dest = Label(f1 , text="Destination" , font=("Calibri",21) , background= limegreen)
    dest.place(x=50 , y = 25)
    destsel = OptionMenu(f1 ,des_select, *destinations ,command = adddestination)
    destsel.place(x=50 , y =70,width=200)

    trans = Label(f2 , text="Transport" , font=("Calibri",21) , background= limegreen)
    trans.place(x=50 , y = 25)
    transsel = OptionMenu(f2 ,trans_select, *transport,command = modeselected )
    transsel.place(x=50 , y =70,width=200)
 
   

    stay = Label(f3 , text="Place of stay" , font=("Calibri",21) , background= limegreen)
    stay.place(x=50 , y = 25)
    staysel = OptionMenu(f3 , stay_select,*placeofstay , command= addplace)
    staysel.place(x=50 , y =70,width=200)

    genbutton = Button(f3 , text="GO////>" , font=("Calibri",21) , background= limegreen , command = gen)
    genbutton.place(x = 50 , y=110)


    
    
    
    #clear data
    

#login window
root = Tk()

#tk variables
username = StringVar()
useremail = StringVar()
userphone = StringVar()
details = ["1234"]
left = 170
box = 270

#basic structure
root.title("Book A Trip")
root.geometry('700x600')
root.iconbitmap('icon.ico')



#login window

mainf = Frame(root , background="#add160" , height=700 , width=700) 
mainf.pack()
mainc = Canvas(mainf  , width=400 , height=500 , background="grey")
mainc.grid(rowspan=15, columnspan=15, pady=40 ,padx=150)

logintext = Label(mainf,text="  USER " , font=("Calibri",30 ), background="gray").place(x=290 , y = 48)

nametext = Label(mainf , text="Name" , font=("Calibri",19) , background="gray").place(x=left , y=120)
namebox = Entry(mainf ,textvariable=username).place(x= box , y = 133 , width=220)

emailtext = Label(mainf , text="Email" , font=("Calibri",19) , background="gray").place(x=left, y=160)
emailbox = Entry(mainf ,textvariable=useremail).place(x= box, y = 173 , width=220)

phonetext = Label(mainf , text="Phone" , font=("Calibri",19) , background="gray").place(x=left, y=200)
phonebox = Entry(mainf,textvariable=userphone ).place(x= box, y = 213 , width=220)

loginbutton = Button(mainf , text="Login" , background="gray",command = login).place(x =295,y=300 , width=100)



# -------------------------------------- DATA ACCESS -----------------------------------------
#filling drop down with data
destinations= data.fetch_cities()
placeofstay = data.fetch_hotels()
transport = ["AIR" , "RAIL" , "ROAD"]






root.mainloop()


