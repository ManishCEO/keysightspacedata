import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image



root = ctk.CTk()


root.title("CBRE_KEYISGHT")
root.geometry("1920x1080-10+0+10")
ctk.set_appearance_mode("system")


logo = ctk.CTkLabel(root,text=" SPACE DATA MANAGEMENT",anchor="center",text_color="RED",corner_radius=40,height=50,width=200,font=('Abadi',50,'bold'))
logo.pack(padx=5,pady=5)

#code for Frame
Frame= ctk.CTkFrame(root,width=7000,height=3,fg_color='white')
Frame.pack(padx=0,pady=0)

Frame = ctk.CTkFrame(master=root,width=500,height=400,fg_color='#1c2833')
Frame.pack(expand=True,fill="both")


image1=ctk.CTkImage(light_image=Image.open("C:\\Users\\kkumaaar\\Desktop\\datapython\\Project\\img\\account.png"),size=(25,25))
label=ctk.CTkLabel(root,image=image1,text=" ",bg_color='#1c2833')
label.place(x=900,y=405)

imagepass=ctk.CTkImage(light_image=Image.open("C:\\Users\\kkumaaar\\Desktop\\datapython\\Project\\img\\password.png"),size=(25,25))
label1=ctk.CTkLabel(root,image=imagepass,text=" ",bg_color='#1c2833')
label1.place(x=900,y=455)

imagelogo=ctk.CTkImage(light_image=Image.open("C:\\Users\\kkumaaar\\Desktop\\datapython\\Project\\img\\login.png"),size=(75,75))
label2=ctk.CTkLabel(root,image=imagelogo,text=" ",bg_color='#1c2833')
label2.place(x=1000,y=300)

#t3Email = ctk.CTkLabel(master=t3,text="Email ID",compound='left',text_color="black",font=('Aptos Narrow',15,'bold'),bg_color='white')
#t3Email.place(x=500,y=190)

t3ed=Entry = ctk.CTkEntry(root,corner_radius=30,width=220,height=35,fg_color='#1c2833',bg_color="#1c2833",text_color='white',font=('Aptos Narrow',15),border_color='white')
Entry.place(x=940,y=400)

#t3password = ctk.CTkLabel(master=t3,text="Password",compound='left',bg_color='white',text_color="black",font=('Aptos Narrow',15,'bold'))
#t3password.place(x=500,y=260)

t3pwd=Entry = ctk.CTkEntry(root,corner_radius=30,width=220,height=35,fg_color='#1c2833',bg_color="#1c2833",text_color='white',font=('Aptos Narrow',15),border_color='white',show='*')
Entry.place(x=940,y=450)

labelor=Label(root, text="--------------------------OR---------------------------",bd=0,fg='firebrick1')
labelor.place(x =910, y = 550)
labelor.config(bg="#1c2833")

labelline=Label(root, text="If you have get any issue,Please contact to WPS",bd=0,fg='White')
labelline.place(x =910, y = 570)
labelline.config(bg="#1c2833")

#get from chatgpt

def login():
    if t3ed.get()=='' or t3pwd.get()=='':
          messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='manish123@')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
            return
       
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where email=%s and password=%s'
        mycursor.execute(query,(t3ed.get(),t3pwd.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is sucessful')
            root.destroy()
            import Spacedatacode

       
                



Button = ctk.CTkButton(root, text="Login",height=35,width=100,corner_radius=15,font=('Aptos Narrow',15),bg_color="#1c2833",border_color="white",command=login)
Button.place(x=1000,y=500)

root.mainloop()




