import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import pymysql

con=pymysql.connect(host='localhost',user='root',password='manish123@',database='userdata')
mycursor=con.cursor()

root = ctk.CTk()


root.title("CBRE_KEYISGHT")
root.geometry("1920x1080-10+0+10")
ctk.set_appearance_mode("system")

tabview=ctk.CTkTabview(master=root,width=1300,height=700)
tabview.place(x=300,y=75)

t3=tabview.add("Profile")
tabview.set("Profile")


logo = ctk.CTkLabel(root,text="KEYSIGHT SPACE DATA MANAGEMENT",anchor="center",text_color="RED",corner_radius=40,height=50,width=200,font=('Abadi',50,'bold'))
logo.pack(padx=5,pady=5)

#code for Frame
Frame= ctk.CTkFrame(root,width=7000,height=3,fg_color='white')
Frame.pack(padx=0,pady=0)



def userright():
    
    t1=tabview.add("Add New Emplyoee")
    t2=tabview.add("Workstation Assign")

    def clear():
        fi.delete(0,END)
        la.delete(0,END)
        lm.delete(0,END)
        ed.delete(0,END)
        option1.set(" ")
        og.delete(0,END)
        mc.delete(0,END)
        cd.delete(0,END)
        md.set(" ")
        ad.delete(0,END)
        dp.delete(0,END)
    
    def clearsavedata():
        t2ed.delete(0,END)
        t2og.delete(0,END)
        t2lm.delete(0,END)
        t2ad.delete(0,END)
        t2dp.delete(0,END)
        floor.set(" ")
        t2md.delete(0,END)
        occ.set(" ")
        set1.set(" ")


    #-------------------------------------------------------------------------------------START NEW EMPLOYEE TAB CODE--------------------------------------------------#
    first = ctk.CTkLabel(master=t1,text="First Name",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    first.place(x=50,y=37)

    fi= Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color="black",font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=155,y=35)
    
    last = ctk.CTkLabel(master=t1,text="Last Name",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    last.place(x=450,y=37)

    la=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=560,y=35)

    lmanager = ctk.CTkLabel(master=t1,text="Immediate Manager",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    lmanager.place(x=860,y=37)

    lm=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=1020,y=35)

    Email = ctk.CTkLabel(master=t1,text="Email ID",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    Email.place(x=50,y=120)

    ed=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=155,y=115)

    Std = ctk.CTkLabel(master=t1,text="Emp Std",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    Std.place(x=450,y=120)

    Emp = ["FTE","NKW","ETW","INTERN"]
    option1 = ctk.CTkOptionMenu(master=t1, values=Emp,corner_radius=20,height=35,width=220,fg_color='white',text_color="black",font=('Aptos Narrow',15))
    option1.place(x=560,y=115)
    option1.set(" ")

    org = ctk.CTkLabel(master=t1,text="Organization",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    org.place(x=860,y=120)

    og=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=1020,y=115)

    MU = ctk.CTkLabel(master=t1,text="MU_Code",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    MU.place(x=50,y=205)

    mc=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=155,y=200)

    code = ctk.CTkLabel(master=t1,text="Work Place",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    code.place(x=450,y=205)

    cd=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=565,y=200)

    mode = ctk.CTkLabel(master=t1,text="Work mode",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    mode.place(x=860,y=205)

    mode = ["Work For Home","Office","Visitor Village"]
    md=code = ctk.CTkOptionMenu(master=t1, values=mode,corner_radius=20,height=35,width=220,fg_color='white',text_color="black",font=('Aptos Narrow',15))
    code.place(x=1020,y=200)
    code.set(" ")

    admin = ctk.CTkLabel(master=t1,text="Admin Name",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    admin.place(x=450,y=295)

    ad=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=565,y=290)

    deptm = ctk.CTkLabel(master=t1,text="Department Manager",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    deptm.place(x=860,y=295)

    dp=Entry = ctk.CTkEntry(master=t1,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=1020,y=290)
    
    def adddata():
        email=ed.get()
        if fi.get()=='' or la.get()=='' or lm.get()=='' or ed.get()=='' or option1.get()=='' or og.get()=='' or mc.get()=='' or cd.get()=='' or md.get()=='' or ad.get()=='' or dp.get()=='':
            messagebox.showerror('Error','All Fields are Required')
        
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='manish123@')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Connection is not established try again')
                return
            try:
                query='use userdata'
                mycursor.execute(query)
                query='use userdata'
                mycursor.execute(query)
                query='create table emprecord(id int auto_increment primary key not null,firstname varchar(50),lastname varchar(50),immediateManager varchar(50),emailid varchar(100),empstd varchar(50),organization varchar(50),mucode varchar(50),division varchar(50),workmode varchar(50),adminname varchar(50),departmentmanager varchar(50))'
                mycursor.execute(query)
            except:
                mycursor.execute('use userdata')
        query='select * from emprecord where emailid=%s'
        
        mycursor.execute(query,(ed.get()))

        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','EmailID already exits')
        
        else:
            if '@' not in email or email.count('@') != 1:
                messagebox.showerror('Error', 'Invalid email format')
                #return False
            
            domain = email.split('@')[1].strip().lower()
            allowed_domains = ["keysight.com", "non.keysight.com"]

    
            if domain not in allowed_domains:
                messagebox.showerror('Error', 'Invalid email domain')
                #return False
            else:
                query='insert into emprecord(firstname,lastname,immediateManager,emailid,empstd,organization,mucode,division,workmode,adminname,departmentmanager)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(fi.get(),la.get(),lm.get(),ed.get(),option1.get(),og.get(),mc.get(),cd.get(),md.get(),ad.get(),dp.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Registration is Successful')
                clear()
            

    Button = ctk.CTkButton(master=t1, text="Add New Employee",height=35,corner_radius=15,font=('Aptos Narrow',15),command=adddata)
    Button.place(x=1030,y=400)

    #---------------------------------------END NEW EMPLOYEE TAB CODE--------------------------------------------------#    

    #------------------------------------------START WORKSTATION TAB---------------------------------------------------#

    t2email = ctk.CTkLabel(master=t2,text="Email ID",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    t2email.place(x=430,y=75)

    t2ed=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=270,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=520,y=70)

    def fetchdata():
        e2=t2ed.get()
        if t2ed.get()=='':
            messagebox.showerror('Error','Email_ID Field is required')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='manish123@',database='userdata')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Connection is not established try again')
                return
            try:
                mycursor.execute("select * from emprecord where emailid = '"+ e2 +"'")
                r=mycursor.fetchall()
                for row in r:
                    pass
                t2og.delete(0, END)
                t2og.insert(END, row[6])
                t2lm.delete(0, END)
                t2lm.insert(END, row[3])
                t2ad.delete(0, END)
                t2ad.insert(END, row[10])
                t2dp.delete(0, END)
                t2dp.insert(END, row[11])
                t2md.delete(0, END)
                t2md.insert(END, row[9])
            except Exception as e:
                print(e)
                con.rollback()
                con.close()

    Button = ctk.CTkButton(master=t2, text="Fetch",height=35,corner_radius=15,font=('Aptos Narrow',15),command=fetchdata)
    Button.place(x=800,y=70)

    t2org = ctk.CTkLabel(master=t2,text="Organization",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    t2org.place(x=220,y=200)

    t2og=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white',state='normal')
    Entry.place(x=350,y=195)

    t2lmanager = ctk.CTkLabel(master=t2,text="Immediate Manager",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    t2lmanager.place(x=710,y=200)

    t2lm=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=900,y=195)

    t2admin = ctk.CTkLabel(master=t2,text="Admin Name",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    t2admin.place(x=220,y=260)

    t2ad=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=350,y=265)

    t2deptm = ctk.CTkLabel(master=t2,text="Department Manager",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    t2deptm.place(x=710,y=260)

    t2dp=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=900,y=265)

    t2floor = ctk.CTkLabel(master=t2,text="floor name",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    t2floor.place(x=460,y=390)

    query="SELECT DISTINCT(floorname) FROM seatrecord"
    mycursor.execute(query)
    r=mycursor.fetchall()
    list=[r1 for r1, in r]
            
    sel=ctk.StringVar() 
            
    floor = ctk.CTkOptionMenu(master=t2,values=list,variable=sel,corner_radius=20,height=35,width=220,fg_color='white',text_color="black",font=('Aptos Narrow',15))
    floor.place(x=590,y=385)

    t2mode = ctk.CTkLabel(master=t2,text="Work Mode",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    t2mode.place(x=220,y=330)

    t2md=Entry = ctk.CTkEntry(master=t2,corner_radius=20,width=220,height=35,fg_color="white",text_color='Black',font=('Aptos Narrow',15),border_color='white')
    Entry.place(x=350,y=325)

    occpany = ctk.CTkLabel(master=t2,text="Occupancy",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    occpany.place(x=460,y=440)
            
    option4 = ["Occupied"]
    occ = ctk.CTkOptionMenu(master=t2, values=option4,corner_radius=20,height=35,width=220,fg_color='white',text_color="black",font=('Aptos Narrow',15))
    occ.place(x=590,y=435)
    occ.set(" ")
    seat = ctk.CTkLabel(master=t2,text="Seat Number",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
    seat.place(x=460,y=490)
            
    list23=[]
            
    def my_upd(*args):
        set1.set('')
        query="SELECT seatnumber FROM seatrecord where floorname='"+ sel.get() +"'"
        mycursor.execute(query)
        r=mycursor.fetchall()
        list23=[r1 for r1, in r]
        set1.configure(values=list23)
    
    set1 = ctk.CTkOptionMenu(master=t2,values=[" "],corner_radius=20,height=35,width=220,fg_color='white',text_color="black",font=('Aptos Narrow',15))
    set1.place(x=590,y=485)
    
    sel.trace_add('write',my_upd)
    #create function for save the data
            
    def save_data():
        if t2md.get()=='Visitor Village':
            messagebox.showerror('Error','they are comes in Hybrid mode')
        elif t2ed.get()=='':
            messagebox.showerror('Error','E-mail is Required')
        elif t2ed.get()=='' or t2og.get()=='' or t2lm.get()=='' or t2ad.get()=='' or t2dp.get()=='' or t2md.get()=='' or occ.get()=='' or set1.get()=='':
            messagebox.showerror('Error','All Fields are Required')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='manish123@')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Connection is not established try again')
                return
            try:
                query='use userdata'
                mycursor.execute(query)
                query='create table assign_emp_seatrecord(email_id varchar(50),organization varchar(50),admin_name varchar(50),seat_number varchar(50))'
                mycursor.execute(query)
            except:
                mycursor.execute('use userdata')
            query='select * from assign_emp_seatrecord where email_id=%s'
            mycursor.execute(query,(t2ed.get()))
                    
            row=mycursor.fetchone()
            if row != None:
                messagebox.showerror('Error','Seat has been assigned to this E-Mail Id Requester')
            else:
                query='insert into assign_emp_seatrecord(email_id,organization,admin_name,seat_number)values(%s,%s,%s,%s)'
                mycursor.execute(query,(t2ed.get(),t2og.get(),t2ad.get(),set1.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Workstation is assigned Successful')
                clearsavedata()
                

    Button = ctk.CTkButton(master=t2, text="Save Data",height=35,corner_radius=15,font=('Aptos Narrow',15),command=save_data)
    Button.place(x=990,y=550)
    
    #-------------------------------END WORK STATION ASSIGN TAB CODE--------------------------------------------------#

#-------------------------------END WORK STATION ASSIGN TAB CODE--------------------------------------------------#

t1Label = ctk.CTkLabel(master=t3,text="Hi,User",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
t1Label.place(x=610,y=100)

t1Label = ctk.CTkLabel(master=t3,text="Please select your Profile",compound='left',text_color="White",font=('Aptos Narrow',15,'bold'))
t1Label.place(x=560,y=150)




Button = ctk.CTkButton(master=t3, text="Admin",height=35,corner_radius=15,font=('Aptos Narrow',15),command=userright)
Button.place(x=500,y=200)

Button = ctk.CTkButton(master=t3, text="WPS Admin",height=35,corner_radius=15,font=('Aptos Narrow',15))
Button.place(x=650,y=200)

root.mainloop()




