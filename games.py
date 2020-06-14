from tkinter import *
from snake import start
from fire import start1
def screen():
    global root
    root=Tk()    
    root.configure(background='black')
    root.geometry("644x434")
    root.title("Entertainment Console")
    # Label(root,text="",bg="grey",width="300",height="1",font=("Calibri,13")).pack()
    Label(root,text="").pack()
    Label(root,text="Games",fg="white",bg="gray",font=("comicsansms",20,"bold"),width="20",height="1").pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Button(root,text="Snakes",height="1",width="10",command=start,bg="blue",fg="white",font=("comicsansms",10,"bold")).pack()
    Label(root,text="").pack()
    Button(root,text="Firing",height="1",width="10",command=start1,bg="blue",fg="white",font=("comicsansms",10,"bold")).pack()
    root.mainloop()   
if __name__ == "__main__":
    
   screen()    

