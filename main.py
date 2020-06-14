#yo example matrai ho primary key nai chaideaina yesto gare pugchamaile bujeko main select *from game where games=%s,[---]
from tkinter import *
import os
from games import screen
import mysql.connector
import time
import pygame  

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
    Label(screen11,text="Search Name",fg="white",bg="blue").pack()
    original3=Entry(screen11,textvariable=originalname2,fg="black")
    original3.pack()
    Label(screen11,text="").pack()
    Button(screen11,text="Press",width=7,height=1,command=delote,bg="red").pack()

def delote():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    mycursor.execute("delete from game1 where name=%s",[originalname2.get()])
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

def add():
    global name0
    name0=name.get()
    email0=email.get()
    phone0=phone.get()
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    s="INSERT INTO game1 (name,email,phone,username,password) VALUES(%s,%s,%s,%s,%s)"
    b1=[name0,email0,phone0,username2,password2]
    mycursor.execute(s,b1)
    mydb.commit()
    mydb.close()
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    mycursor.execute("UPDATE game SET username=%s,password=%s,id=%s WHERE id=%s",[
        a,
        b,
        phone0,
        1
    ])
    mydb.commit()
    mydb.close()
    global screen8
    screen8=Toplevel(root)
    screen8.title("Add")
    screen8.geometry("150x100")
    Label(screen8,text="Sucessfully Added").pack()
    Button(screen8,text="OK",command=delete3).pack()

def update1():    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    
    mycursor.execute("select * from game1 where name=%s",[originalname.get()])
    result=mycursor.fetchall()
    for row in result:  
           
       Label(screen9,text="").pack()
       name3.set(row[0])
       email3.set(row[1])
       phone3.set(row[2])
       username3.set(row[3])
       password3.set(row[4])
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
    Label(screen9,text="Search Name",fg="white",bg="blue").pack()
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
    
    mycursor.execute("UPDATE  game1 SET name=%s,email=%s,phone=%s,username=%s,password=%s WHERE name=%s",[
        name3.get(),
        email3.get(),
        phone3.get(),
        username3.get(),
        password3.get(),
        originalname.get()
    ])

    mydb.commit()
    mydb.close()
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    mycursor.execute("UPDATE game SET username=%s,password=%s WHERE id=%s",[
        username3.get(),
        password3.get(),
        phone3.get()
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

def show1():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor() 
    mycursor.execute("select * from game1 where name=%s",[originalname.get()])
    result=mycursor.fetchall()
    print(result)
    for row in result:             
       Label(screen7,text="").pack()
       Label(screen7,text='Playername:'+row[0],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
       Label(screen7,text='Email:'+row[1],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
       Label(screen7,text='Phonenumber:'+str(row[2]),fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
       Label(screen7,text='Username:'+row[3],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
       Label(screen7,text='Password:'+row[4],fg="white",bg='blue',font=("comicsansms",20,"bold")).pack()
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
    Label(screen7,text="Search Name",fg="white",bg="blue").pack()
    original3=Entry(screen7,textvariable=originalname,fg="black")
    original3.pack()
    Label(screen7,text="").pack()
    Button(screen7,text="Press",width=7,height=1,command=show1,bg="red").pack()

   
def logregsetting():
    global screen6
    screen6=Toplevel(root)
    screen6.title("Playerdetails")
    screen6.geometry("750x450")
    screen6.configure(background="blue")
    global name,email,phone
    name=StringVar()
    email=StringVar()
    phone=StringVar()
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
    Label(screen6,text="Player Name",fg="white",bg="blue").pack()
    nameentry=Entry(screen6,textvariable=name,fg="black")
    nameentry.pack()
    Label(screen6,text="Player Email",fg="white",bg="blue").pack()
    emailentry=Entry(screen6,textvariable=email,fg="black")
    emailentry.pack()
    Label(screen6,text="Phonenumber",fg="white",bg="blue").pack()
    phoneentry=Entry(screen6,textvariable=phone,fg="black")
    phoneentry.pack()
    Label(screen6,text="").pack()
    Button(screen6,text="Add",width=10,height=1,command=add,bg="red").pack()
    Button(screen6,text="Play",width=10,height=1,command=screen,bg="red").pack()

def database():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="games")
    mycursor=mydb.cursor()
    s="INSERT INTO game (username,password,id) VALUES(%s,%s,%s)"
    b1=(usernameinfo,passwordinfo,1)
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
    screen3.destroy()

def delete4():
    screen10.destroy()  


def delete5():
    screen11.destroy()        

def delete3():
    screen8.destroy()    

def register():
    global screen1
    screen1=Toplevel(root)
    screen1.title("Register")
    screen1.geometry("300x250")
    screen1.configure(background="blue")
    global username,password,repassword
    username=StringVar()
    password=StringVar()
    repassword=StringVar()
    global usernameentry,userpasswordentry,userrepasswordentry

    Label(screen1,text="Please enter details below to register",fg="white",bg="red",font=("comicsansms",8,"bold")).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username",fg="white",bg="blue").pack()
    usernameentry=Entry(screen1,textvariable=username,fg="black")
    usernameentry.pack()
    Label(screen1,text="Password",fg="white",bg="blue").pack()
    userpasswordentry=Entry(screen1,textvariable=password,fg="black")
    userpasswordentry.pack()
    Label(screen1,text="Repassword",fg="white",bg="blue").pack()
    userrepasswordentry=Entry(screen1,textvariable=repassword,fg="black")
    userrepasswordentry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Register",width=10,height=1,command=registerverify,bg="red").pack()
    
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
                 logregsetting()
                 a=username2
                 b=password2
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
    root.title("Entertainment Console")
    Label(root,text="",bg="grey",width="300",height="1",font=("Calibri,13")).pack()
    Label(root,text="").pack()
    Button(root,text="Login",height="1",width="10",command=login,bg="red",fg="white",font=("comicsansms",20,"bold")).pack()
    Label(root,text="").pack()
    Button(root,text="Register",height="1",width="10",command=register,bg="red",fg="white",font=("comicsansms",20,"bold")).pack()
    Label(root,text="").pack()
    Button(root,text="Setting",height="1",width="10",command=setting,bg="red",fg="white",font=("comicsansms",20,"bold")).pack()
    root.mainloop()   

main_screen()    