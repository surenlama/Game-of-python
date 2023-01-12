#yo example matrai ho primary key nai chaideaina yesto gare pugchamaile bujeko main select *from game where games=%s,[---]
from tkinter import *
import os
# from games import screen
import mysql.connector
import time
import pygame  
import smtplib
# server = smtplib.SMTP('smtp.gmail.com',587)
a="Confirmed"

# server.starttls()
# server.login('surenlama620@gmail.com','Nerus@12345')
# server.sendmail('surenlama620@gmail.com','surenlama620@gmail.com','mail send from app')
def delete4():
    global screen10
    screen10.destroy()  


def delete():
    global screen11
    screen11=Toplevel(root)
    screen11.title("delete")
    screen11.geometry("450x400")
    screen11.config(background="blue")
    
    global originalname2
    originalname2=StringVar()
    Label(screen11,text="").pack()
    Label(screen11,text="").pack()
    Label(screen11,text="Search First Name",fg="white",bg="blue").pack()
    original3=Entry(screen11,textvariable=originalname2,fg="black")
    original3.pack()
    Label(screen11,text="").pack()
    Button(screen11,text="Press",width=7,height=1,command=delote,bg="red").pack()


def delote():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    mycursor.execute("delete from game1 where first_name=%s",[originalname2.get()])
    mydb.commit()
    mydb.close() 
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    mycursor.execute("delete from game where username=%s",[originalname2.get()])
    mydb.commit()
    mydb.close() 
    global screen11
    screen11=Toplevel(root)
    screen11.title("delete")
    screen11.geometry("150x100")
    Label(screen11,text="Sucessfully Deleted").pack()
    Button(screen11,text="OK",command=delete5).pack()


def pleasefillup():
    global screen3
    screen3=Toplevel(root)
    screen3.title("fillup")
    screen3.geometry("150x100")
    Label(screen3,text="Please Fillup").pack()
    Button(screen3,text="OK",command=delete2).pack()    




def customer2():
    global pickuplocation
    pickuplocation0=pickuplocation.get()
    dropuplocation0=dropuplocation.get()
    pickuptime0=pickuptime.get()
    pickdate0=pickdate.get()
    username0=username.get()

    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    s="INSERT INTO customerphase1 (username,pickuplocation,dropuplocation,pickuptime,pickdate) VALUES(%s,%s,%s,%s,%s)"
    b1=[pickuplocation0,dropuplocation0,pickuptime0,pickdate0,username0]
    if b1[0] and b1[1] and b1[2] and b1[3] and b1[4]:
        mycursor.execute(s,b1)
        mydb.commit()
        mydb.close()   
        global screen022
        screen022=Toplevel(root)
        screen022.title("Created")
        screen022.geometry("150x100")
        Label(screen022,text="Sucessfully Added").pack()
        Button(screen022,text="OK",command=customer2).pack()
    else:
        pleasefillup()     

def customer2fronted():
    global screen6
    screen6=Toplevel(root)
    screen6.title("TaxiBooking App")
    screen6.geometry("750x450")
    screen6.configure(background="blue")
    global pickuplocation,dropuplocation,pickuptime,pickdate,username
    pickuplocation=StringVar()
    dropuplocation=StringVar()
    pickuptime=StringVar()
    pickdate=StringVar()
    username=StringVar()

    global nameentry,emailentry,phoneentry

    yourmenu=Menu(screen6)
    m1=Menu(yourmenu, tearoff=0)
    m1.add_command(label="Edit",command=update) 
    m1.add_command(label="delete",command=delete) 
    m1.add_command(label="Show",command=show) 
    screen6.config(menu=yourmenu)
    yourmenu.add_cascade(label="Account",menu=m1)

    m2=Menu(yourmenu, tearoff=0)
    m2.add_command(label="Melody",command=Melody) 
    m2.add_command(label="rocking",command=rocking) 
    m2.add_command(label="serious",command=serious) 
    m2.add_command(label="romantic",command=romantic) 
    m2.add_command(label="Nepali",command=nepali) 
   
    m2.add_command(label="Stop",command=stop) 
    screen6.config(menu=yourmenu)
    yourmenu.add_cascade(label="Music",menu=m2)
    
    m3=Menu(yourmenu, tearoff=0)
    m3.add_command(label="green",command=green1) 
    m3.add_command(label="blue",command=blue1) 
    m3.add_command(label="white",command=white1) 
    m3.add_command(label="red",command=red1) 
    m3.add_command(label="black",command=black1) 
    m3.add_command(label="yellow",command=yellow1)
    screen6.config(menu=yourmenu)
    yourmenu.add_cascade(label="Color",menu=m3)



    Label(screen6,text="").pack()


    Label(screen6,text="Enter UserName",fg="white",bg="blue").pack()
    pickupdate=Entry(screen6,textvariable=username,fg="black")
    pickupdate.pack()

    Label(screen6,text="Enter PickUp Location",fg="white",bg="blue").pack()
    pickuplocationentry=Entry(screen6,textvariable=pickuplocation,fg="black")
    pickuplocationentry.pack()


    Label(screen6,text="Enter DropUp Location",fg="white",bg="blue").pack()
    dropuplocationentry=Entry(screen6,textvariable=dropuplocation,fg="black")
    dropuplocationentry.pack()

    Label(screen6,text="Enter PickUp Time",fg="white",bg="blue").pack()
    pickuptime=Entry(screen6,textvariable=pickuptime,fg="black")
    pickuptime.pack()

    Label(screen6,text="Enter PickUp Date",fg="white",bg="blue").pack()
    pickupdate=Entry(screen6,textvariable=pickdate,fg="black")
    pickupdate.pack()

    Label(screen6,text="").pack()
    Button(screen6,text="Add",width=10,height=1,command=customephase1,bg="red").pack()



def customephase1():
    pickuplocation0=pickuplocation.get()
    dropuplocation0=dropuplocation.get()
    pickuptime0=pickuptime.get()
    pickdate0=pickdate.get()
    username0 = username.get()
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    s="INSERT INTO customerphase1 (username,pickuplocation,dropuplocation,pickuptime,pickdate,drivername,customername,vehiclenumber,estimatedfare) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    b1=[username0,pickuplocation0,dropuplocation0,pickuptime0,pickdate0,"","","",""]
    if b1[0] and b1[1] and b1[2] and b1[3] and b1[4]:
        mycursor.execute(s,b1)
        mydb.commit()
        mydb.close()   
        global screen022
        screen022=Toplevel(root)
        screen022.title("Created")
        screen022.geometry("150x100")
        Label(screen022,text="Sucessfully Added").pack()
        Button(screen022,text="OK").pack()
    else:
        pleasefillup() 


def update1():    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    mycursor.execute("select * from game1 where first_name=%s",[originalname.get()])
    result=mycursor.fetchall()
    for row in result:  
       Label(screen9,text="").pack()
       name3.set(row[2])
       email3.set(row[5])
       phone3.set(row[8])
       username3.set(row[1])
       password3.set(row[15])
    mydb.commit()    
    mydb.close()  

def update():
    global screen9
    screen9=Toplevel(root)
    screen9.title("Update")
    screen9.geometry("600x550")
    screen9.configure(background="blue")
    global name3,email3,phone3,username3,password3,originalname
    originalname=StringVar()
    name3=StringVar()
    email3=StringVar()
    phone3=StringVar()
    username3=StringVar()
    password3=StringVar()    
    global nameentry3,emailentry3,phoneentry3,usernameentry3,passwordentry3,original3
    Label(screen9,text="Please enter details below to Update",fg="white",bg="red",font=("comicsansms",8,"bold")).pack()
    Label(screen9,text="").pack()
    Label(screen9,text="").pack()
    Label(screen9,text="Search First Name",fg="white",bg="blue").pack()
    original3=Entry(screen9,textvariable=originalname,fg="black")
    original3.pack()
    Label(screen9,text="").pack()
    Button(screen9,text="Press",width=7,height=1,command=update1,bg="red").pack()

    Label(screen9,text="").pack()
    Label(screen9,text="").pack()
    Label(screen9,text="Name",fg="white",bg="blue").pack()
    nameentry3=Entry(screen9,textvariable=name3,fg="black")
    nameentry3.pack()
    Label(screen9,text="Email",fg="white",bg="blue").pack()
    emailentry3=Entry(screen9,textvariable=email3,fg="black")
    emailentry3.pack()
    Label(screen9,text="Phone",fg="white",bg="blue").pack()
    phoneentry3=Entry(screen9,textvariable=phone3,fg="black")
    phoneentry3.pack()
    Label(screen9,text="Username",fg="white",bg="blue").pack()
    usernameentry3=Entry(screen9,textvariable=username3,fg="black")
    usernameentry3.pack()
    Label(screen9,text="Password",fg="white",bg="blue").pack()
    passwordentry3=Entry(screen9,textvariable=password3,fg="black")
    passwordentry3.pack()
    Label(screen9,text="").pack()
    Button(screen9,text="Update",width=7,height=1,command=update_data,bg="red").pack()


def update_data():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    mycursor.execute("UPDATE  game1 SET first_name=%s,email=%s,phone_number=%s,username=%s,password=%s WHERE first_name=%s",[
        name3.get(),
        email3.get(),
        phone3.get(),
        username3.get(),
        password3.get(),
        original3.get()
    ])

    mydb.commit()
    mydb.close()
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    mycursor.execute("UPDATE game SET username=%s,password=%s WHERE id=%s",[
        username3.get(),
        password3.get(),
    ])
    mydb.commit()
    mydb.close()
    file=open(username3.get(),"w")
    file.write(username3.get()+"\n")
    file.write(password3.get()+"\n")
    file.write(password3.get())
    file.close()
    global screen10
    screen10=Toplevel(root)
    screen10.title("Update")
    screen10.geometry("150x100")
    Label(screen10,text="Sucessfully Updated").pack()
    Button(screen10,text="OK",command=delete4).pack()



def thankyou():
    b="Trip Confirmed"
    global screen10
    screen10=Toplevel(root)
    screen10.title("Update")
    screen10.geometry("150x100")
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    s="INSERT INTO trip (customername,tripstatus) VALUES(%s,%s)"
    b1=[d,b]
    mycursor.execute(s,b1)
    mydb.commit()
    mydb.close()
    Label(screen10,text="Confirmation was successfully drive is on the way?").pack()
    Button(screen10,text="OK",command=delete4).pack()

def customertripView():
    global d
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor() 
    mycursor.execute("select * from customerphase1 where username=%s",[username0.get()])
    result=mycursor.fetchall()
    print(result)
    for row in result:             
        Label(screen7,text="").pack()
        Label(screen7,text='User Name:'+row[0],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Drop Location:'+row[1],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='PickUp Location:'+row[2],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Pick Up Time:'+row[3],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Pick Up Date:'+row[4],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Driver Name:'+row[5],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Customer Name:'+row[6],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Vehicle Number:'+row[7],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Estimated Fair:'+row[8],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        d=row[6]
    Button(screen7,text="Confirm Booking",width=7,height=1,command=thankyou,bg="red").pack()
    mydb.commit()    
    mydb.close()



def customertripdetail():
    global screen7
    screen7=Toplevel(root)
    screen7.title("")
    screen7.geometry("450x400")
    screen7.config(background="blue")
    
    global username0
    username0=StringVar()
    Label(screen7,text="").pack()
    Label(screen7,text="").pack()
    Label(screen7,text="Type UserName To View Detail",fg="white",bg="blue").pack()
    original3=Entry(screen7,textvariable=username0,fg="black")
    original3.pack()
    Label(screen7,text="").pack()
    Button(screen7,text="Press",width=7,height=1,command=customertripView,bg="red").pack()

def show1():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor() 
    mycursor.execute("select * from game1 where first_name=%s",[originalname.get()])
    result=mycursor.fetchall()

    for row in result:             
        Label(screen7,text="").pack()
        Label(screen7,text='User Name:'+row[1],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='First Name:'+row[2],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Middle Name:'+row[3],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Last Name:'+row[4],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Email Address:'+row[5],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Phone Number:'+row[8],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
        Label(screen7,text='Address:'+row[9],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
  
    mydb.commit()    
    mydb.close()

def show():
    global screen7
    screen7=Toplevel(root)
    screen7.title("")
    screen7.geometry("450x400")
    screen7.config(background="blue")
    
    global originalname
    originalname=StringVar()
    Label(screen7,text="").pack()
    Label(screen7,text="").pack()
    Label(screen7,text="Search First Name",fg="white",bg="blue").pack()
    original3=Entry(screen7,textvariable=originalname,fg="black")
    original3.pack()
    Label(screen7,text="").pack()
    Button(screen7,text="Press",width=7,height=1,command=show1,bg="red").pack()


def update2():    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    mycursor.execute("select * from customerphase1 where username=%s",[originalnametrip.get()])
    result=mycursor.fetchall()
    for row in result:  
       Label(screen9,text="").pack()
       username3.set(row[4])
       pickuplocation3.set(row[0])
       dropuplocation3.set(row[1])
       pickuptime3.set(row[2])
       pickdate3.set(row[3])
       drivername3.set(row[5])
       vehiclenumber3.set(row[6])
       estimatedfare3.set(row[7])
    mydb.commit()    
    mydb.close()  

def updatetrip():
    global screen9
    screen9=Toplevel(root)
    screen9.title("Update trip")
    screen9.geometry("600x650")
    screen9.configure(background="blue")
    global pickuplocation3,dropuplocation3,pickuptime3,pickdate3,username3,originalnametrip,drivername3,vehiclenumber3,estimatedfare3
    pickuplocation3=StringVar()
    dropuplocation3=StringVar()
    pickuptime3=StringVar()
    pickdate3=StringVar()
    username3=StringVar()
    drivername3=StringVar()
    vehiclenumber3=StringVar()
    estimatedfare3=StringVar()
    originalnametrip=StringVar()

    global nameentry3,emailentry3,phoneentry3,usernameentry3,passwordentry3,original3
    Label(screen9,text="Please enter details below to Update",fg="white",bg="red",font=("comicsansms",8,"bold")).pack()
    Label(screen9,text="").pack()
    Label(screen9,text="").pack()
    Label(screen9,text="Enter UserName",fg="white",bg="blue").pack()
    original3=Entry(screen9,textvariable=originalnametrip,fg="black")
    original3.pack()
    Label(screen9,text="").pack()
    Button(screen9,text="Press",width=7,height=1,command=update2,bg="red").pack()

    Label(screen9,text="").pack()
    Label(screen9,text="").pack()
    Label(screen9,text="Username",fg="white",bg="blue").pack()
    nameentry3=Entry(screen9,textvariable=username3,fg="black")
    nameentry3.pack()

    Label(screen9,text="Assigned Driver Name",fg="white",bg="blue").pack()
    driver3=Entry(screen9,textvariable=drivername3,fg="black")
    print(driver3.get())
    print(drivername3.get())
    driver3.pack()

    Label(screen9,text="Vehicle Number",fg="white",bg="blue").pack()
    vehicle3=Entry(screen9,textvariable=vehiclenumber3,fg="black")
    vehicle3.pack()

    Label(screen9,text="Estimated Fare",fg="white",bg="blue").pack()
    estimate3=Entry(screen9,textvariable=estimatedfare3,fg="black")
    estimate3.pack()

    Label(screen9,text="Pick Up Location",fg="white",bg="blue").pack()
    nameentry3=Entry(screen9,textvariable=pickuplocation3,fg="black")
    nameentry3.pack()
    Label(screen9,text="Drop Up Location",fg="white",bg="blue").pack()
    emailentry3=Entry(screen9,textvariable=dropuplocation3,fg="black")
    emailentry3.pack()
    Label(screen9,text="Pick Up Time",fg="white",bg="blue").pack()
    phoneentry3=Entry(screen9,textvariable=pickuptime3,fg="black")
    phoneentry3.pack()
    Label(screen9,text="Pick Up Date",fg="white",bg="blue").pack()
    usernameentry3=Entry(screen9,textvariable=pickdate3,fg="black")
    usernameentry3.pack()
    Label(screen9,text="").pack()
    # Button(screen9,text="Update",width=7,height=1,command=update_datatrip,bg="red").pack()


def update_datatrip():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    mycursor.execute("UPDATE  customerphase1 SET username=%s,dropuplocation=%s,pickuplocation=%s,pickuptime=%s,pickdate=%s,drivername=%s,vehiclenumber=%s,estimatedfare=%s WHERE username=%s",[
        username3.get(),
        dropuplocation3.get(),
        pickuplocation3.get(),
        pickuptime3.get(),
        pickdate3.get(),
        original3.get(),
        drivername3.get(),
        vehiclenumber3.get(),
        estimatedfare3.get()
    ])
    mydb.commit()
    mydb.close()
    mycursor=mydb.cursor()
    # s="INSERT INTO customerphase1 (username,dropuplocation,pickuplocation,pickuptime,pickdate,drivername,vehiclenumber,estimatedfare) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    # b1=[username3.get(),dropuplocation3.get(),pickuplocation3.get(),pickuptime3.get(),pickdate3.get(),drivername3.get(),vehiclenumber3.get(),estimatedfare3.get()]
    # if b1[0] and b1[1] and b1[2] and b1[3] and b1[4] and b[5] and b[6] and b[7]:
    #     mycursor.execute(s,b1)
    #     mydb.commit()
    #     mydb.close()
    global screen10
    screen10=Toplevel(root)
    screen10.title("Update")
    screen10.geometry("150x100")
    Label(screen10,text="Sucessfully Updated").pack()
    Button(screen10,text="OK",command=delete4).pack()


def admindashboarddatabase():
    pickuplocation0=pickuplocation.get()
    dropuplocation0=dropuplocation.get()
    pickuptime0=pickuptime.get()
    pickdate0=pickdate.get()
    username0 = username.get()
    assgindriver0 = assgindriver.get()
    vehiclenumber0 = vehiclenumber.get()
    estimatefair0 = estimatefair.get()
    customername0 = customername.get()
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    s="INSERT INTO customerphase1 (username,pickuplocation,dropuplocation,pickuptime,pickdate,drivername,customername,vehiclenumber,estimatedfare) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    b1=[username0,pickuplocation0,dropuplocation0,pickuptime0,pickdate0,assgindriver0,customername0,vehiclenumber0,estimatefair0]
    if b1[0] and b1[1] and b1[2] and b1[3] and b1[4] and b1[5] and b1[6] and b1[7] and b1[8]:
        mycursor.execute(s,b1)
        mydb.commit()
        mydb.close()
        # if a is None:
        #     print('nonw')
        # else:
        #     print('jknk')    
        global screen022
        screen022=Toplevel(root)
        screen022.title("Created")
        screen022.geometry("150x100")
        Label(screen022,text="Sucessfully Added").pack()
    else:
        pleasefillup() 


def admindashboard():
    global screen6
    screen6=Toplevel(root)
    screen6.title("Trip details")
    screen6.geometry("750x650")
    screen6.configure(background="blue")
    global pickuplocation,dropuplocation,pickuptime,pickdate,username,assgindriver,customername,vehiclenumber,estimatefair
    pickuplocation=StringVar()
    dropuplocation=StringVar()
    pickuptime=StringVar()
    pickdate=StringVar()
    username=StringVar()
    assgindriver=StringVar()
    vehiclenumber=StringVar()
    estimatefair=StringVar()
    customername=StringVar()


    global nameentry,emailentry,phoneentry

    yourmenu=Menu(screen6)
    m1=Menu(yourmenu, tearoff=0)
    m1.add_command(label="Edit",command=updatetrip) 
    m1.add_command(label="Create Driver",command=Driver) 

    screen6.config(menu=yourmenu)
    yourmenu.add_cascade(label="View Trip ",menu=m1)

    m2=Menu(yourmenu, tearoff=0)
    m2.add_command(label="Melody",command=Melody) 
    m2.add_command(label="rocking",command=rocking) 
    m2.add_command(label="serious",command=serious) 
    m2.add_command(label="romantic",command=romantic) 
    m2.add_command(label="Nepali",command=nepali) 
   
    m2.add_command(label="Stop",command=stop) 
    screen6.config(menu=yourmenu)
    yourmenu.add_cascade(label="Music",menu=m2)
    
    m3=Menu(yourmenu, tearoff=0)
    m3.add_command(label="green",command=green1) 
    m3.add_command(label="blue",command=blue1) 
    m3.add_command(label="white",command=white1) 
    m3.add_command(label="red",command=red1) 
    m3.add_command(label="black",command=black1) 
    m3.add_command(label="yellow",command=yellow1)
    screen6.config(menu=yourmenu)
    yourmenu.add_cascade(label="Color",menu=m3)

    Label(screen6,text="").pack()

    Label(screen6,text="Enter UserName",fg="white",bg="blue").pack()
    pickuplocationentry=Entry(screen6,textvariable=username,fg="black")
    pickuplocationentry.pack()

    Label(screen6,text="Enter PickUp Location",fg="white",bg="blue").pack()
    pickuplocationentry=Entry(screen6,textvariable=pickuplocation,fg="black")
    pickuplocationentry.pack()

    Label(screen6,text="Enter DropUp Location",fg="white",bg="blue").pack()
    dropuplocationentry=Entry(screen6,textvariable=dropuplocation,fg="black")
    dropuplocationentry.pack()

    Label(screen6,text="Enter PickUp Time",fg="white",bg="blue").pack()
    pickuptime=Entry(screen6,textvariable=pickuptime,fg="black")
    pickuptime.pack()

    Label(screen6,text="Enter PickUp Date",fg="white",bg="blue").pack()
    pickupdate=Entry(screen6,textvariable=pickdate,fg="black")
    pickupdate.pack()

    Label(screen6,text="Assigned Driver",fg="white",bg="blue").pack()
    pickupdate=Entry(screen6,textvariable=assgindriver,fg="black")
    pickupdate.pack()

    Label(screen6,text="Assigned Customer Name",fg="white",bg="blue").pack()
    pickupdate=Entry(screen6,textvariable=customername,fg="black")
    pickupdate.pack()

    Label(screen6,text="Vehicle Number",fg="white",bg="blue").pack()
    pickupdate=Entry(screen6,textvariable=vehiclenumber,fg="black")
    pickupdate.pack()

    Label(screen6,text="Estimate Fair",fg="white",bg="blue").pack()
    pickupdate=Entry(screen6,textvariable=estimatefair,fg="black")
    pickupdate.pack()    
    


    Label(screen6,text="").pack()
    Button(screen6,text="Add",width=10,height=1,command=admindashboarddatabase,bg="red").pack()
           
def logregsetting():
    global screen6
    screen6=Toplevel(root)
    screen6.title("Playerdetails")
    screen6.geometry("750x450")
    screen6.configure(background="blue")
    global pickuplocation,dropuplocation,pickuptime,pickdate,username
    pickuplocation=StringVar()
    dropuplocation=StringVar()
    pickuptime=StringVar()
    pickdate=StringVar()
    username=StringVar()

    global nameentry,emailentry,phoneentry

    yourmenu=Menu(screen6)
    m1=Menu(yourmenu, tearoff=0)
    m1.add_command(label="Edit",command=update) 
    m1.add_command(label="delete",command=delete) 
    m1.add_command(label="Show",command=show) 

    screen6.config(menu=yourmenu)
    yourmenu.add_cascade(label="Account",menu=m1)

    m2=Menu(yourmenu, tearoff=0)
    m2.add_command(label="Melody",command=Melody) 
    m2.add_command(label="rocking",command=rocking) 
    m2.add_command(label="serious",command=serious) 
    m2.add_command(label="romantic",command=romantic) 
    m2.add_command(label="Nepali",command=nepali) 
   
    m2.add_command(label="Stop",command=stop) 
    screen6.config(menu=yourmenu)
    yourmenu.add_cascade(label="Music",menu=m2)
    
    m3=Menu(yourmenu, tearoff=0)
    m3.add_command(label="green",command=green1) 
    m3.add_command(label="blue",command=blue1) 
    m3.add_command(label="white",command=white1) 
    m3.add_command(label="red",command=red1) 
    m3.add_command(label="black",command=black1) 
    m3.add_command(label="yellow",command=yellow1)

    m4=Menu(yourmenu, tearoff=0)
    m4.add_command(label="View Trip Detail",command=customertripdetail) 
    screen6.config(menu=yourmenu)
    yourmenu.add_cascade(label="View Trip Detail",menu=m4)

    yourmenu.add_cascade(label="Color",menu=m3)

    Label(screen6,text="").pack()

    Label(screen6,text="Enter UserName",fg="white",bg="blue").pack()
    usernameentry=Entry(screen6,textvariable=username,fg="black")
    usernameentry.pack()

    Label(screen6,text="Enter PickUp Location",fg="white",bg="blue").pack()
    pickuplocationentry=Entry(screen6,textvariable=pickuplocation,fg="black")
    pickuplocationentry.pack()

    Label(screen6,text="Enter DropUp Location",fg="white",bg="blue").pack()
    dropuplocationentry=Entry(screen6,textvariable=dropuplocation,fg="black")
    dropuplocationentry.pack()

    Label(screen6,text="Enter PickUp Time",fg="white",bg="blue").pack()
    pickuptime=Entry(screen6,textvariable=pickuptime,fg="black")
    pickuptime.pack()

    Label(screen6,text="Enter PickUp Date",fg="white",bg="blue").pack()
    pickupdate=Entry(screen6,textvariable=pickdate,fg="black")
    pickupdate.pack()

    Label(screen6,text="").pack()
    Button(screen6,text="Add",width=10,height=1,command=customephase1,bg="red").pack()


def database():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    s="INSERT INTO game (username,password) VALUES(%s,%s)"
    b1=(usernameinfo,passwordinfo)
    mycursor.execute(s,b1)
    mydb.commit()
   
def regisdatabase():#userle input haneko username check gareko databasema
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    query="select * from game where username=%s"

    mycursor.execute(query,[usernameinfo])
    if (len(mycursor.fetchall())>0):
        return 1
    else:
        return 2 
    mydb.commit()    
    mydb.close()
    
def logdatabase():      
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    query="select * from game where username=%s and password=%s"
    mycursor.execute(query,(username2,password2))
    if (len(mycursor.fetchall())>0):
        return 1
    else:
        return 2
    mydb.commit()       
    mydb.close()



def registerverify():
    global usernameinfo,passwordinfo
    usernameinfo=username.get()
    passwordinfo=password.get()
    repasswordinfo=repassword.get()
    listoffiles= os.listdir()
    if usernameinfo=="" or passwordinfo=="" or repasswordinfo=="":
        empty()
    else:        
        if usernameinfo not in listoffiles and regisdatabase()==2:           
            if passwordinfo==repasswordinfo:
                file=open(usernameinfo,"w")
                file.write(usernameinfo+"\n")
                file.write(passwordinfo+"\n")
                file.write(repasswordinfo)
                file.close()
                usernameentry.delete(0,END)
                userpasswordentry.delete(0,END)
                userrepasswordentry.delete(0,END)
                sucessregister()
                database()
                add()
            else:
                passworddoesnotmatch()        
        else:
            Usernotexit()


def sucessregister():
    global screen3
    screen3=Toplevel(root)
    screen3.title("Sucess")
    screen3.geometry("150x100")
    Label(screen3,text="Sucessfully registered").pack()
    Button(screen3,text="OK",command=delete2).pack()
       
    
def empty():
    global screen3
    screen3=Toplevel(root)
    screen3.title("Empty")
    screen3.geometry("150x100")
    Label(screen3,text="PleaseFillUp").pack()
    Button(screen3,text="OK",command=delete2).pack()    


def passworddoesnotmatch():
    global screen3
    screen3=Toplevel(root)
    screen3.title("UserNotExit")
    screen3.geometry("150x100")
    Label(screen3,text="PasswordNotMatch").pack()
    Button(screen3,text="OK",command=delete2).pack()

def Usernotexit():
    global screen3
    screen3=Toplevel(root)
    screen3.title("UserNotExit")
    screen3.geometry("150x100")
    Label(screen3,text="UserAlreadyExits").pack()
    Button(screen3,text="OK",command=delete2).pack()

def delete2():
    global screen3
    screen3.destroy()




def delete5():
    global screen11
    screen11.destroy()        

def delete3():
    global screen8
    screen8.destroy()    

def register():
    global screen1
    screen1=Toplevel(root)
    screen1.title("Register")
    screen1.geometry("1000x750")
    screen1.configure(background="blue")
    global username,password,repassword,first_name,middle_name,last_name,email,dateof_birth,sex,phone_number,address,method_of_payment,\
        card_number,card_holdnumber,expiry_date,security_code
    username=StringVar()
    first_name=StringVar()
    middle_name=StringVar()
    last_name=StringVar()
    email=StringVar()
    dateof_birth=StringVar()
    sex=StringVar()
    phone_number=StringVar()
    address=StringVar()
    method_of_payment=StringVar()
    card_number=StringVar()
    card_holdnumber=StringVar()
    expiry_date=StringVar()
    security_code=StringVar()
    password=StringVar()
    repassword=StringVar()
    global usernameentry,userpasswordentry,userrepasswordentry

    Label(screen1,text="Please enter details below to register",fg="white",bg="red",font=("comicsansms",8,"bold")).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username",fg="white",bg="blue").pack()
    usernameentry=Entry(screen1,textvariable=username,fg="black")
    usernameentry.pack()

    Label(screen1,text="First Name",fg="white",bg="blue").pack()
    firstnameentry=Entry(screen1,textvariable=first_name,fg="black")
    firstnameentry.pack()

    Label(screen1,text="Middle Name",fg="white",bg="blue").pack()
    middlenameentry=Entry(screen1,textvariable=middle_name,fg="black")
    middlenameentry.pack()

    Label(screen1,text="Last Name",fg="white",bg="blue").pack()
    lastnameentry=Entry(screen1,textvariable=last_name,fg="black")
    lastnameentry.pack()

    Label(screen1,text="Email Address",fg="white",bg="blue").pack()
    emailentry=Entry(screen1,textvariable=email,fg="black")
    emailentry.pack()

    Label(screen1,text="Date of Birth",fg="white",bg="blue").pack()
    dateof_birthentry=Entry(screen1,textvariable=dateof_birth,fg="black")
    dateof_birthentry.pack()

    # Label(screen1,text="Sex",fg="white",bg="blue").pack()
    # sexentry=Entry(screen1,textvariable=sex,fg="black")
    # sexentry.pack()

    # Label(screen1,text="Phone Number",fg="white",bg="blue").pack()
    # phone_numberentry=Entry(screen1,textvariable=phone_number,fg="black")
    # phone_numberentry.pack()

    Label(screen1,text="Address",fg="white",bg="blue").pack()
    addressentry=Entry(screen1,textvariable=address,fg="black")
    addressentry.pack()

    Label(screen1,text="Method Of Payment",fg="white",bg="blue").pack()
    paymententry=Entry(screen1,textvariable=method_of_payment,fg="black")
    paymententry.pack()

    Label(screen1,text="Card Number",fg="white",bg="blue").pack()
    card_numberentry=Entry(screen1,textvariable=card_number,fg="black")
    card_numberentry.pack()

    Label(screen1,text="Card Hold Number",fg="white",bg="blue").pack()
    card_holdnumberentry=Entry(screen1,textvariable=card_holdnumber,fg="black")
    card_holdnumberentry.pack()

    Label(screen1,text="Expiry Date",fg="white",bg="blue").pack()
    expiry_dateentry=Entry(screen1,textvariable=expiry_date,fg="black")
    expiry_dateentry.pack()


    Label(screen1,text="Security Code",fg="white",bg="blue").pack()
    security_codeentry=Entry(screen1,textvariable=security_code,fg="black")
    security_codeentry.pack()

    Label(screen1,text="Password",fg="white",bg="blue").pack()
    userpasswordentry=Entry(screen1,textvariable=password,fg="black")
    userpasswordentry.pack()
    Label(screen1,text="Repassword",fg="white",bg="blue").pack()
    userrepasswordentry=Entry(screen1,textvariable=repassword,fg="black")
    userrepasswordentry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Register",width=10,height=1,command=registerverify,bg="red").pack()
    


def registerdriver():
    firstnameinfo=first_name.get()
    last_nameinfo=last_name.get()
    vehiclenoinfo=vehicle_no.get()
    phone_numberinfo=phone_number.get()
    emailinfo = email.get()
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    s="INSERT INTO Driver (first_name,last_name,vehicle_no,phone_number,email) VALUES(%s,%s,%s,%s,%s)"
    b1=(firstnameinfo,last_nameinfo,vehiclenoinfo,phone_numberinfo,emailinfo)
    mycursor.execute(s,b1)
    mydb.commit()
    sucessregister()


def Driver():
    global screen1
    screen1=Toplevel(root)
    screen1.title("Register")
    screen1.geometry("1000x750")
    screen1.configure(background="blue")
    global first_name,last_name,vehicle_no,phone_number,email
    first_name=StringVar()
    last_name=StringVar()
    vehicle_no=StringVar()
    phone_number=StringVar()
    email=StringVar()


    global usernameentry,userpasswordentry,userrepasswordentry

    Label(screen1,text="Please enter details below to register Driver",fg="white",bg="red",font=("comicsansms",8,"bold")).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="First Name",fg="white",bg="blue").pack()
    firstnameentry=Entry(screen1,textvariable=username,fg="black")
    firstnameentry.pack()

    Label(screen1,text="First Name",fg="white",bg="blue").pack()
    firstnameentry=Entry(screen1,textvariable=first_name,fg="black")
    firstnameentry.pack()

    Label(screen1,text="Last Name",fg="white",bg="blue").pack()
    middlenameentry=Entry(screen1,textvariable=last_name,fg="black")
    middlenameentry.pack()

    Label(screen1,text="Vehicle No.",fg="white",bg="blue").pack()
    lastnameentry=Entry(screen1,textvariable=vehicle_no,fg="black")
    lastnameentry.pack()

    Label(screen1,text="Email Address",fg="white",bg="blue").pack()
    emailentry=Entry(screen1,textvariable=email,fg="black")
    emailentry.pack()

    # Label(screen1,text="Date of Birth",fg="white",bg="blue").pack()
    # dateof_birthentry=Entry(screen1,textvariable=dateof_birth,fg="black")
    # dateof_birthentry.pack()

    # Label(screen1,text="Sex",fg="white",bg="blue").pack()
    # sexentry=Entry(screen1,textvariable=sex,fg="black")
    # sexentry.pack()

    # Label(screen1,text="Phone Number",fg="white",bg="blue").pack()
    # phone_numberentry=Entry(screen1,textvariable=phone_number,fg="black")
    # phone_numberentry.pack()

    Label(screen1,text="Phone Number",fg="white",bg="blue").pack()
    addressentry=Entry(screen1,textvariable=phone_number,fg="black")
    addressentry.pack()

 
    Label(screen1,text="").pack()
    Button(screen1,text="Register Driver",width=10,height=1,command=registerdriver,bg="red").pack()

def add():
    global username
    username0=username.get()
    first_name0=first_name.get()
    middle_name0=middle_name.get()
    last_name0=last_name.get()

    email0=email.get()
    dateof_birth0=dateof_birth.get()
    sex0=sex.get()
    phone_number0=phone_number.get()

    address0=address.get()
    method_of_payment0=method_of_payment.get()
    card_number0=card_number.get()
    card_holdnumber0=card_holdnumber.get()

    expiry_date0=expiry_date.get()
    security_code0=security_code.get()
    password0=password.get()

    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    s="INSERT INTO game1 (username,first_name,middle_name,last_name,email,dateof_birth,sex,phone_number,address,method_of_payment,card_number,card_holdnumber,expiry_date,security_code,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    b1=[username0,first_name0,middle_name0,last_name0,email0,dateof_birth0,sex0,phone_number0,address0,method_of_payment0,card_number0,card_holdnumber0,expiry_date0,security_code0,password0]
    mycursor.execute(s,b1)
    mydb.commit()
    mydb.close()


def passwordincorrect():
    global screen3
    screen3=Toplevel(root)
    screen3.title("Passwordincorrect")
    screen3.geometry("150x100")
    Label(screen3,text="Password Incorrect").pack()
    Button(screen3,text="OK",command=delete2).pack()


def usernotfound():
    global screen3
    screen3=Toplevel(root)
    screen3.title("usernotfound")
    screen3.geometry("150x100")
    Label(screen3,text="UserNotFound").pack()
    Button(screen3,text="OK",command=delete2).pack()    

def paswordverify():
    global username2,password2,a,b
    username2=username1.get()
    password2=password1.get()
 
    listoffiles= os.listdir()
    if username2=="" or password2=="":
        empty()
    else:    
        if username2 in listoffiles:
          file1= open(username2,'r') 
          verify=file1.read().splitlines()
          if password2 in verify:

              if logdatabase()==1:
                 a=username2
                 b=password2
                 if a == "admin" and b == "admin":
                    admindashboard()
                 else:
                    logregsetting()

             
              else:
                  usernotfound()
          else:
             passwordincorrect()
        else:
            usernotfound()   

def login():
    global screen2
    screen2=Toplevel(root)
    screen2.title("Register")
    screen2.geometry("300x250")
    screen2.configure(background="blue")
    global username1,password1
    username1=StringVar()
    password1=StringVar()

    global usernameentry1,userpasswordentry1
    Label(screen2,text="Please enter details below to login",fg="white",bg="red",font=("comicsansms",8,"bold")).pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Username",bg="blue",fg="white").pack()
    usernameentry1=Entry(screen2,textvariable=username1)
    usernameentry1.pack()
    Label(screen2,text="Password",bg="blue",fg="white").pack()
    userpasswordentry1=Entry(screen2,textvariable=password1,show="*")
    userpasswordentry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Submit",width=10,height=1,command=paswordverify,bg="red").pack()


def myfunc():
    print('i am bohot chada ladka hu')

def stop():
   pygame.mixer.music.stop()

def Melody():
    pygame.mixer.init()
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play()
    time.sleep(10)

def rocking():
    pygame.mixer.init()
    pygame.mixer.music.load('mus.mp3')
    pygame.mixer.music.play()

def serious():
    pygame.mixer.init()
    pygame.mixer.music.load('serious.mp3')
    pygame.mixer.music.play()

def nepali():
    pygame.mixer.init()
    pygame.mixer.music.load('nepali.mp3')
    pygame.mixer.music.play()

def romantic():
    pygame.mixer.init()
    pygame.mixer.music.load('romantic.mp3')
    pygame.mixer.music.play()

def setting():
    global screen5
    screen5=Toplevel(root)
    screen5.title("Setting")
    screen5.geometry("300x250")
    screen5.configure(background="blue")
  
    yourmenu=Menu(screen5)
    m2=Menu(yourmenu, tearoff=0)
    m2.add_command(label="Melody",command=Melody) 
    m2.add_command(label="rocking",command=rocking) 
    m2.add_command(label="serious",command=serious) 
    m2.add_command(label="romantic",command=romantic) 
    m2.add_command(label="Nepali",command=nepali) 
   

    m2.add_command(label="Stop",command=stop) 
    screen5.config(menu=yourmenu)
    yourmenu.add_cascade(label="Music",menu=m2)
    
    m3=Menu(yourmenu, tearoff=0)
    m3.add_command(label="green",command=green) 
    m3.add_command(label="blue",command=blue) 
    m3.add_command(label="white",command=white) 
    m3.add_command(label="red",command=red) 
    m3.add_command(label="black",command=black) 
    m3.add_command(label="yellow",command=yellow) 
    screen5.config(menu=yourmenu)
    yourmenu.add_cascade(label="Color",menu=m3)
    
def blue():
        root.configure(background="blue")
        screen5.configure(background="blue")
       
def green():
        root.configure(background="green")
        screen5.configure(background="green")
def white():
        root.configure(background="white")
        screen5.configure(background="white")
def black():
        root.configure(background="black")
        screen5.configure(background="black")
def red():
        root.configure(background="red")
        screen5.configure(background="red")

def yellow():
        root.configure(background="yellow")
        screen5.configure(background="yellow")        
def blue1():
        root.configure(background="blue")
        screen6.configure(background="blue")

def green1():
        root.configure(background="green")
        screen6.configure(background="green")
def white1():
        root.configure(background="white")
        screen6.configure(background="white")
def black1():
        root.configure(background="black")
        screen6.configure(background="black")
def red1():
        root.configure(background="red")
        screen6.configure(background="red")

def yellow1():
        root.configure(background="yellow")
        screen6.configure(background="yellow")                

def main_screen():
    global root
    root=Tk()    
    root.configure(background='blue')
    root.geometry("644x434")
    root.title("Taxi Booking App")
    Label(root,text="",bg="grey",width="300",height="1",font=("Calibri,13")).pack()
    Label(root,text="").pack()
    Button(root,text="Login",height="1",width="10",command=login,bg="red",fg="white",font=("comicsansms",20,"bold")).pack()
    Label(root,text="").pack()
    Button(root,text="Register",height="1",width="10",command=register,bg="red",fg="white",font=("comicsansms",20,"bold")).pack()
    Label(root,text="").pack()
    Button(root,text="Setting",height="1",width="10",command=setting,bg="red",fg="white",font=("comicsansms",20,"bold")).pack()
    root.mainloop()   

main_screen()    