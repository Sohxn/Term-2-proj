#libraries 
from code import compile_command
from random import choice
from tkinter import *
from tkinter import ttk
from tkinter import font
import data

limegreen = "#add160"


freshlist = []
costlist = []
#definitions
def login():
    
    
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
    bw.title('Travel Plan')
    bw.iconbitmap('icon.ico')

    des_select = StringVar()
    trans_select = StringVar()
    stay_select = StringVar()
    

    
     
    
    #-------------RECEIPT--------------
    
    def gen():
        print(freshlist)
        airfare = 0
        railfare = 0
        roadfare = 0
        hotelexp = 0
        #transport
        if freshlist[1] == 'AIR':
            a = data.fetch_airfare(freshlist[0])
            airfare = a[0][0]
            
           
        elif freshlist[1] == 'RAIL':
            b = data.fetch_railfare(freshlist[0])
            railfare = b[0][0]
            
            
        elif freshlist[1] == 'ROAD':
            c = data.fetch_roadfare(freshlist[0])
            roadfare = c[0][0]
            
        #hotels
        d = data.fetch_hotelexp(freshlist[2])
        cost = d[0][0]

        #--------CALCULATION--------
        heads = headentry.get()
        tax = 69420
        headcount = int(heads)  
        fares = airfare + railfare + roadfare
        hotelexp = int(cost) 
        totalfare = fares * headcount
        sumtotal = hotelexp + totalfare 
        grandtotal = sumtotal + tax
        costlist.append(sumtotal)
        costlist.append(grandtotal)
        print("TOTAL: \n  ",sumtotal)

        #call the function to generate the receipt page
        receipt()

        
    def receipt():
        bw.destroy()
        rt = Tk()
        rt.geometry('500x600')
        rt.title('Receipt')
        rt.iconbitmap('icon.ico')


         
        tymsg = Label(text = "THANK YOU FOR USING OUR SERVICES",font=("Calibri",18))
        tymsg.place(x = 80 ,y=30)

        title = Label(text="-------------Receipt-------------",font=("Calibri",16) )
        title.place(x = 150, y = 100)
        title = Label(text="Amount:        ",font=("Calibri",16) )
        title.place(x = 110, y = 150)
        amount = Label(text= str(costlist[0]),font=("Calibri",16) )
        amount.place(x = 200 , y =150)
        title = Label(text="Taxes:        ",font=("Calibri",16) )
        title.place(x = 110, y = 190)
        amount = Label(text= "69420",font=("Calibri",16) )
        amount.place(x = 200 , y =190)
        lines = Label(text="--------------------")
        lines.place(x=200,y=220)
        line1 = Label(text="--------------------")
        line1.place(x=140,y=220)
        grand = Label(text="Grand total:        ",font=("Calibri",16) )
        grand.place(x = 110, y = 240)
        amount = Label(text= str(costlist[1]),font=("Calibri",16) )
        amount.place(x = 200 , y =240)
        
            
           
   
    

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

    genbutton = Button(f3 , text="Good To Go" , font=("Calibri",21) , background= limegreen , command = gen)
    genbutton.place(x = 50 , y=110)

    headtext = Label(f3 , text="No. of heads",font=("Calibri",18) ,  background=limegreen)
    headtext.place(x = 420 , y = 40)

    headentry = Entry(f3 ,background=limegreen , )
    headentry.place(x  = 420 , y = 80)


    
    
    
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



