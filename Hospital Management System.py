import tkinter
import tkinter as tk
from tkinter import ttk,messagebox
import tkinter.messagebox as tkMessageBox
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry

#====  Patient Details screen =============================================
def patient_details():
    root=Tk()
    root.title('Patient')
    root['bg']='lightgreen'

    width = 825
    height = 650
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    global eid
    global enic
    global efnmae
    global elname
    global ebod
    global eaddress
    global eage
    global ephonenumber
    global red1
    global red2
    global ehight
    global eweight
    global combo


    # patient Details Variables
    pid=StringVar()
    pnic=StringVar()
    pfname=StringVar()
    plname=StringVar()
    pbod=StringVar()
    paddress=StringVar()
    page=StringVar()
    pnumber=StringVar()
    pgender=StringVar()
    phight=StringVar()
    pweight=StringVar()
    pblood=StringVar()

    tk.Label(root,text='Nurse',font=(None,40,"bold")).place(x=210,y=40)
    img=Image.open("6.jpg")
    test=ImageTk.PhotoImage(img)

    la=tkinter.Label(image=test,width=825,height=610)
    la.image = test
    la.place (x=0,y=0)

    tk.Label(root,text='Patient Registration',font=(None,20), width=30).place(x=160,y=20)
   
    # patient Details clear code 
    def Clear():
        pid.set("")
        pnic.set("")
        pfname.set("")
        plname.set("")
        pbod.set("")
        paddress.set("")
        page.set("")
        pnumber.set("")
        pgender.set("")
        phight.set("")
        pweight.set("")
        pblood.set("")

        
    # patient Details add code 
    def Add():
        p_id=pid.get()
        p_nic=pnic.get()
        p_fname=pfname.get()
        p_lname=plname.get()
        p_bod=pbod.get()
        p_address=paddress.get()
        p_age=page.get()
        p_number=pnumber.get()
        p_gender=pgender.get()
        p_height=phight.get()
        p_weight=pweight.get()
        p_blood=pblood.get()

        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mysqldb.cursor()

        if(p_id !="" and p_nic !="" and p_fname !="" and p_lname !="" and p_bod!="" and p_address !="" and p_age !="" and p_number !="" and p_gender !="" and p_height !="" and p_weight !="" and p_blood !=""):
            try:
                sql="INSERT INTO patient(p_id,p_nic,p_fname,p_lname,p_bod,p_address,p_age,p_number,p_gender,p_height,p_weight,p_blood) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(p_id,p_nic,p_fname,p_lname,p_bod,p_address,p_age,p_number,p_gender,p_height,p_weight,p_blood)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid=mycursor.lastrowid
                messagebox.showinfo("patient","successfuly Added")
                Clear()
                treeView()
        
                #username.focus.set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
        else:
            messagebox.showinfo("patient","fill Details")

    # patient Details update code
    def Update():
        
        p_id=pid.get()
        p_nic=pnic.get()
        p_fname=pfname.get()
        p_lname=plname.get()
        p_bod=pbod.get()
        p_address=paddress.get()
        p_age=page.get()
        p_number=pnumber.get()
        p_gender=pgender.get()
        p_height=phight.get()
        p_weight=pweight.get()
        p_blood=pblood.get()

        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mysqldb.cursor()
        if(p_nic !="" and p_fname !="" and p_lname !="" and p_bod!="" and p_address !="" and p_age !="" and p_number !="" and p_gender !="" and p_height !="" and p_weight !="" and p_blood !="" ):
            try:
                sql="Update patient set p_nic=%s,p_fname=%s,p_lname=%s,p_bod=%s,p_address=%s,p_age=%s,p_number=%s,p_gender=%s,p_height=%s,p_weight=%s,p_blood=%s where p_id=%s"
                val=(p_nic,p_fname,p_lname,p_bod,p_address,p_age,p_number,p_gender,p_height,p_weight,p_blood,p_id)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid=mycursor.lastrowid
                messagebox.showinfo("patient","successfully Updated")
                Clear()
                treeView()
             
            except Exception as e:
                    print(e)
                    mysqldb.rollback()
                    mysqldb.close()
        else:
            messagebox.showinfo("patient","select Detail")


    # patient Details delete code
    def Delete():
        p_id=pid.get()
        p_nic=pnic.get()
        p_fname=pfname.get()
        p_lname=plname.get()
        p_bod=pbod.get()
        p_address=paddress.get()
        p_age=page.get()
        p_number=pnumber.get()
        p_gender=pgender.get()
        p_height=phight.get()
        p_weight=pweight.get()
        p_blood=pblood.get()


        if(p_id !="" and p_nic !="" and p_fname !="" and p_lname !="" and p_bod!="" and p_address !="" and p_age !="" and p_number !="" and p_gender !="" and p_height !="" and p_weight !="" and p_blood !="" ):
            mBox=messagebox.askquestion("patient","delete details?")
            if (mBox=='yes'):
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
                mycursor=mysqldb.cursor()
                sql="Delete from patient where p_id=%s"
                val=(p_id,)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid=mycursor.lastrowid
                messagebox.showinfo("patient","deleted")
                Clear()
                treeView()
              
            else:
                messagebox.showinfo('patient','cannot deleted ')
                Clear()
                mysqldb.close()
        else:
            messagebox.showinfo("patient","select patient Details")




    # Data load txt boxes
    def getData(event):
        Clear()
        selected_row=tv.focus()
        data=tv.item(selected_row)
        global row
        row=data["values"]
        pid.set(row[0])
        pnic.set(row[1])
        pfname.set(row[2])
        plname.set(row[3])
        pbod.set(row[4])
        paddress.set(row[5])
        page.set(row[6])
        pnumber.set(row[7])
        pgender.set(row[8])
        phight.set(row[9])
        pweight.set(row[10])
        pblood.set(row[11])


        
        
    # Tree view Show patient details
    def show():
    
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mysqldb.cursor()
        mycursor.execute("SELECT p_id,p_nic,p_fname,p_lname,p_bod,p_address,p_age,p_number,p_gender,p_height,p_weight,p_blood FROM patient")
        records=mycursor.fetchall()
        #print(Operation details)


        for i,(p_id,p_nic,p_fname,p_lname,p_bod,p_address,p_age,p_number,p_gender,p_height,p_weight,p_blood) in enumerate(records, start=1):
            tv.insert("","end",values=(p_id,p_nic,p_fname,p_lname,p_bod,p_address,p_age,p_number,p_gender,p_height,p_weight,p_blood))
            mysqldb.close()



    
    def treeView():
        global tv
        tree_frame = Frame(root, bg="#ecf0f1")
        tree_frame.place(x=10,y=380, width=800, height=230)
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 10),rowheight=30)  
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 12,'bold'))
        
        scrollbary = ttk.Scrollbar(tree_frame, orient=VERTICAL)
        scrollbarx = ttk.Scrollbar(tree_frame, orient=HORIZONTAL)
        
        cols=('PID','PNic','P_f_Name','P_L_Name','B_O_D','Address','Age','PHO_Number','Gender','Hight','Weight','Blood')
        ListBox=ttk.Treeview(tree_frame,columns=cols,show='headings',selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

        scrollbary.config(command=ListBox.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=ListBox.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)


        tv = ttk.Treeview(tree_frame, columns=(0,1, 2, 3, 4, 5, 6, 7,8,9,10,11),style="mystyle.Treeview")
        tv.heading("0", text="Patient ID")
        tv.column("0", width=50,anchor='center')
        tv.heading("1", text="Patient NIC")
        tv.column("1", width=50,anchor='center')
        tv.heading("2", text="Patient_f_name")
        tv.column("2", width=50,anchor='center')
        tv.heading("3", text="Patient _l_name")
        tv.column("3", width=50,anchor='center')
        tv.heading("4", text="BOD")
        tv.column("4", width=60,anchor='center')
        tv.heading("5", text="Address")
        tv.column("5", width=90,anchor='center')
        tv.heading("6", text="Age")
        tv.column("6", width=20,anchor='center')
        tv.heading("7", text="Phone number")
        tv.column("7", width=20,anchor='center')
        tv.heading("8", text="Gender")
        tv.column("8", width=20,anchor='center')
        tv.heading("9", text="Hight")
        tv.column("9", width=20,anchor='center')
        tv.heading("10", text="Weight")
        tv.column("10", width=20,anchor='center')
        tv.heading("11", text="Blood")
        tv.column("11", width=20,anchor='center')
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill=X,)
        show()









    

    tk.Label(root,text='Patient ID').place(x=50,y=90)
    tk.Label(root,text='Patient NIC').place(x=440,y=90)
    tk.Label(root,text='First Name').place(x=50,y=120)
    tk.Label(root,text='Last Name').place(x=440,y=120)
    tk.Label(root,text='Birth of date').place(x=50,y=150)
    tk.Label(root,text='Address').place(x=440,y=150)
    tk.Label(root,text='Age').place(x=50,y=180)
    tk.Label(root,text='Phone number').place(x=440,y=180)
    tk.Label(root,text='Gender').place(x=50,y=210)
    tk.Label(root,text='Hight').place(x=440,y=210)
    tk.Label(root,text='Weight').place(x=50,y=240)
    tk.Label(root,text='Blood group').place(x=440,y=240)

    # Entry box
    eid=Entry(root,width=30, textvariable = pid).place(x=190,y=90)      
    enic=Entry(root,width=30, textvariable = pnic).place(x=585,y=90)    
    efname=Entry(root,width=30, textvariable = pfname).place(x=190,y=120) 
    elname=Entry(root,width=30, textvariable = plname).place(x=585,y=120)  
    cal = DateEntry(root, width=28, year=2000, month=1, day=1, textvariable=pbod, background='darkblue', foreground='white').place(x=190,y=150)
    edaaress=Entry(root,width=30,  textvariable = paddress).place(x=585,y=150)
    eage=Entry(root,width=30,textvariable = page).place(x=190,y=180)
    ephonenumber=Entry(root,width=30, textvariable = pnumber).place(x=585,y=180)
    ttk.Combobox(root,textvariable=pgender,values=['--please select--','Male','Female'],font=('Arial',12),width=19).place(x=190,y=210)
    ehight=Entry(root,width=30, textvariable = phight).place(x=585,y=210)
    eweight=Entry(root,width=30,  textvariable = pweight).place(x=190,y=240)
    ttk.Combobox(root,textvariable=pblood,values=['--please select--','O-','O+','A-','A+','B-','B+','AB-','AB+'],font=('Arial',12),width=19).place(x=585,y=240)


    #button  window
    Button(root,text='Save', command=Add,height=2,width=13,font=(None,10)).place(x=55,y=325)
    Button(root,text='Update', command=Update,height=2,width=13,font=(None,10)).place(x=175,y=325)
    Button(root,text='Delete', command=Delete,height=2,width=13,font=(None,10)).place(x=295,y=325)
    Button(root,text='clear', command= Clear, height=2,width=13,font=(None,10)).place(x=415,y=325)
 
    treeView()  

    root.mainloop()


#====  Operation Details screen ===========================================
def Operation_details():
    root=Tk()
    root.title('Operation details')
    root['bg']='lightgreen'

    width = 825
    height = 650
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)


    # Operation Details Variables
    pid=StringVar()
    nid=StringVar()
    adate=StringVar()
    odate=StringVar()
    otime=StringVar()
    otype=StringVar()
    bp=StringVar()
    sl=StringVar()


    global pid_
    global nid_
    global adate_
    global odate_
    global otime_
    global otype_
    global bp_
    global sl_



    tk.Label(root,text='Operation',font=(None,20), width=30).place(x=150,y=20)
    tk.Label(root,text='Nurse',font=(None,40,"bold")).place(x=210,y=40)
    img=Image.open("5.jpg")
    test=ImageTk.PhotoImage(img)

    la=tkinter.Label(image=test,width=825,height=610)
    la.image = test
    la.place (x=0,y=0)

    # Operation Details clear code 
    def Clear():
        pid.set("")
        nid.set("")
        adate.set("")
        odate.set("")
        otime.set("")
        otype.set("")
        bp.set("")
        sl.set("")
        

    # Operation Details add code 
    def Add():
        p_id=pid.get()
        n_id=nid.get()
        ad_date=adate.get()
        op_date=odate.get()
        op_time=otime.get()
        op_type=otype.get()
        blood=bp.get()
        sugar=sl.get()
        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mysqldb.cursor()

        if(p_id !="" and n_id !="" and ad_date!="" and op_date !="" and op_time !="" and op_type !="" and blood !="" and sugar !=""):
            try:
                sql="INSERT INTO operation(p_id, n_id, ad_date, op_date, op_time, op_type, blood, sugar ) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(p_id, n_id, ad_date, op_date, op_time, op_type, blood, sugar)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid=mycursor.lastrowid
                messagebox.showinfo("operation","added")
                Clear()
             
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
        else:
            messagebox.showinfo("operation","fill Details")

    # Operation Details update code
    def Update():
        
        p_id=pid.get()
        n_id=nid.get()
        ad_date=adate.get()
        op_date=odate.get()
        op_time=otime.get()
        op_type=otype.get()
        blood=bp.get()
        sugar=sl.get()

        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mysqldb.cursor()
        if(n_id !="" and ad_date!="" and op_date!="" and op_time!="" and op_type!="" and blood!="" and sugar!=""):
            try:
                sql="Update operation set n_id=%s,ad_date=%s,op_date=%s,op_time=%s,op_type=%s,blood=%s,sugar=%s where p_id=%s"
                val=(n_id,ad_date,op_date,op_time,op_type,blood,sugar,p_id)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid=mycursor.lastrowid
                messagebox.showinfo("operation"," Updated successfully")
                Clear()
             
                pid_.focus.set()
            except Exception as e:
                    print(e)
                    mysqldb.rollback()
                    mysqldb.close()
        else:
            messagebox.showinfo("operation","select a Detailp;0")

    # Operation Details delete code
    def Delete():
        p_id=pid.get()
        n_id=nid.get()
        ad_date=adate.get()
        op_date=odate.get()
        op_time=otime.get()
        op_type=otype.get()
        blood=bp.get()
        sugar=sl.get()
        p_id=pid.get()
        if(n_id !="" and ad_date!="" and op_date!="" and op_time!="" and op_type!="" and blood!="" and sugar!=""):
            mBox=messagebox.askquestion("Delete operation","Are you sure you want to delete record details?")
            if (mBox=='yes'):
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
                mycursor=mysqldb.cursor()
                sql="Delete from operation where p_id=%s"
                val=(p_id,)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid=mycursor.lastrowid
                messagebox.showinfo("operation","record deleted...")
                Clear()
             
                #pid_.focus.set()
            else:
                messagebox.showinfo('operation','cannot deleted ')
                Clear()
                mysqldb.close()
        else:
            messagebox.showinfo("operation","select operation Details")


        
    # Data load txt boxes
    def getData(event):
        Clear()
        selected_row=tv.focus()
        data=tv.item(selected_row)
        global row
        row=data["values"]
        pid.set(row[0])
        nid.set(row[1])
        adate.set(row[2])
        odate.set(row[3])
        otime.set(row[4])
        otype.set(row[5])
        bp.set(row[6])
        sl.set(row[7])
        
    # Tree view Show Operation details
    def show():
    
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mysqldb.cursor()
        mycursor.execute("SELECT p_id,n_id,ad_date,op_date,op_time,op_type,blood,sugar FROM operation")
        records=mycursor.fetchall()
        #print(Operation details)


        for i,(p_id,n_id,ad_date,op_date,op_time,op_type,blood,sugar) in enumerate(records, start=1):
            tv.insert("","end",values=(p_id,n_id,ad_date,op_date,op_time,op_type,blood,sugar))
            mysqldb.close()


    # Operation Details treeView Frame
    def treeView():
        global tv
        tree_frame = Frame(root, bg="#ecf0f1")
        tree_frame.place(x=10,y=350, width=800, height=230)
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 10),rowheight=30)  
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 12,'bold'))

        scrollbarx = ttk.Scrollbar(tree_frame, orient=HORIZONTAL)

        tv = ttk.Treeview(tree_frame,xscrollcommand=scrollbarx.set, selectmode="none")
        

        scrollbarx.config(command=tv.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        

        tv = ttk.Treeview(tree_frame, columns=(0,1, 2, 3, 4, 5, 6, 7),style="mystyle.Treeview")
        tv.heading("0", text="Patient ID")
        tv.column("0", width=50,anchor='center')
        tv.heading("1", text="Nurse ID")
        tv.column("1", width=50,anchor='center')
        tv.heading("2", text="Admite Date")
        tv.column("2", width=60,anchor='center')
        tv.heading("3", text="Operation Date")
        tv.column("3", width=90,anchor='center')
        tv.heading("4", text="Operation Time")
        tv.column("4", width=20,anchor='center')
        tv.heading("5", text="Operation Type")
        tv.column("5", width=20,anchor='center')
        tv.heading("6", text="Blood Pressure")
        tv.column("6", width=20,anchor='center')
        tv.heading("7", text="Sugar Level")
        tv.column("7", width=20,anchor='center')
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill=X,)
        show()      


    
    #Operation Details window
    # Label
    tk.Label(root,text='Patient ID').place(x=50,y=140)
    tk.Label(root,text='nurse ID').place(x=440,y=140)
    tk.Label(root,text='Admite Date').place(x=50,y=170)
    tk.Label(root,text='Operation Date').place(x=440,y=170)
    tk.Label(root,text='Operation Time').place(x=50,y=200)
    tk.Label(root,text='Operation Type').place(x=440,y=200)
    tk.Label(root,text='Blood Pressure').place(x=50,y=230)
    tk.Label(root,text='Sugar Level').place(x=440,y=230)

    # Entry box
    pid_=Entry(root,width=30, textvariable=pid).place(x=190,y=140)
    nid_=Entry(root,width=30, textvariable=nid).place(x=585,y=140)
    cal = DateEntry(root, width=28, year=2020, month=1, day=1, textvariable=adate, background='darkblue', foreground='white').place(x=190,y=170)
    cal = DateEntry(root, width=28, year=2021, month=1, day=1, textvariable=odate, background='darkblue', foreground='white').place(x=585,y=170)
    otime_=Entry(root,width=30, textvariable=otime).place(x=190,y=200)
    ttk.Combobox(root,textvariable=otype,values=['--please select--','General surgery','Hand surgery','Hernia surgery','Neurosurgery','Reflux surgery','Robotic surgery','Thoracic surgery','Trauma surgery','Urologic surgery','Vascular surgery','Other'],font=('Arial',12),width=19).place(x=585,y=203)
    bp_=Entry(root,width=30, textvariable=bp).place(x=190,y=230)
    sl_=Entry(root,width=30, textvariable=sl).place(x=585,y=230)

    #buttons window 
    Button(root,text='Save', command=Add, height=2,width=13,font=(None,10)).place(x=55,y=285)
    Button(root,text='Update', command=Update, height=2,width=13,font=(None,10)).place(x=175,y=285)
    Button(root,text='Delete', command=Delete, height=2,width=13,font=(None,10)).place(x=295,y=285)
    Button(root,text='clear', command=Clear, height=2,width=13,font=(None,10)).place(x=415,y=285)

    treeView() 

    root.mainloop()

#====  patient Details view screen ========================================
def patient_details_view():
    root=Tk()
    root.title('Patient')
    root['bg']='lightgreen'
    width = 825
    height = 560
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    global eid
    # Patient Details Variables
    eid=StringVar()


    def search():
            
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mysqldb.cursor()

        p_id=eid.get()
        if(p_id!=""):
            dbp_id=""
            Select="select p_id,p_nic,p_fname,p_lname,p_bod,p_address,p_age,p_number,p_gender,p_height,p_weight,p_blood from Patient where p_id='%s'" %(p_id)
            mycursor.execute(Select)
            result=mycursor.fetchall()
            #print(result)
            for i in result:
                dbp_id=i[0]
                #print(dbadmission)
            if(p_id == dbp_id):
                global row
                row=i
                paid.config(text=row[0])      
                panic.config(text=row[1])
                pafn.config(text=row[2])
                paln.config(text=row[3])
                pabod.config(text=row[4])
                paad.config(text=row[5])
                paage.config(text=row[6])
                papn.config(text=row[7])
                pag.config(text=row[8])
                pah.config(text=row[9])
                paw.config(text=row[10])
                pabg.config(text=row[11])

            else:
                 messagebox.showerror("Error","this Patient ID not match in our database....")
                 Clear()

        
        else:
            messagebox.showerror("Error","please enter Patient ID in the text box....")
            Clear()
        



    def Clear():
        paid.config(text="")      
        panic.config(text="")
        pafn.config(text="")
        paln.config(text="")
        pabod.config(text="")
        paad.config(text="")
        paage.config(text="")
        papn.config(text="")
        pag.config(text="")
        pah.config(text="")
        paw.config(text="")
        pabg.config(text="")
        eid.set("")
        
        
        
   # Data load txt boxes
    def getData(event):
        Clear()
        selected_row=tv.focus()
        data=tv.item(selected_row)
        global row
        row=data["values"]
        paid.config(text=row[0])      
        panic.config(text=row[1])
        pafn.config(text=row[2])
        paln.config(text=row[3])
        pabod.config(text=row[4])
        paad.config(text=row[5])
        paage.config(text=row[6])
        papn.config(text=row[7])
        pag.config(text=row[8])
        pah.config(text=row[9])
        paw.config(text=row[10])
        pabg.config(text=row[11])

        




    ttk.Label(root,text='Patient ID :',font=('Arial',13)).place(x=10,y=60)
    paid=ttk.Label(root,font=('Arial',13))
    paid.place(x=150,y=60)

    ttk.Label(root,text='Patient NIC :',font=('Arial',13)).place(x=10,y=80)
    panic=ttk.Label(root,font=('Arial',13))
    panic.place(x=150,y=80)

    ttk.Label(root,text='First Name :',font=('Arial',13)).place(x=10,y=100)
    pafn=ttk.Label(root,font=('Arial',13))
    pafn.place(x=150,y=100)

    ttk.Label(root,text='Last Name :',font=('Arial',13)).place(x=10,y=120)
    paln=ttk.Label(root,font=('Arial',13))
    paln.place(x=150,y=120)
    
    ttk.Label(root,text='Birth of date :',font=('Arial',13)).place(x=10,y=140)
    pabod=ttk.Label(root,font=('Arial',13))
    pabod.place(x=150,y=140)

    ttk.Label(root,text='Address :',font=('Arial',13)).place(x=10,y=160)
    paad=ttk.Label(root,font=('Arial',13))
    paad.place(x=150,y=160)

    
    ttk.Label(root,text='Age :',font=('Arial',13)).place(x=10,y=180)
    paage=ttk.Label(root,font=('Arial',13))
    paage.place(x=150,y=180)

    ttk.Label(root,text='Phone number :',font=('Arial',13)).place(x=10,y=200)
    papn=ttk.Label(root,font=('Arial',13))
    papn.place(x=150,y=200)

    ttk.Label(root,text='Gender :',font=('Arial',13)).place(x=10,y=220)
    pag=ttk.Label(root,font=('Arial',13))
    pag.place(x=150,y=220)

    ttk.Label(root,text='Hight :',font=('Arial',13)).place(x=10,y=240)
    pah=ttk.Label(root,font=('Arial',13))
    pah.place(x=150,y=240)

    ttk.Label(root,text='Weigh :',font=('Arial',13)).place(x=10,y=260)
    paw=ttk.Label(root,font=('Arial',13))
    paw.place(x=150,y=260)
 
    ttk.Label(root,text='Blood group :',font=('Arial',13)).place(x=10,y=280)
    pabg=ttk.Label(root,font=('Arial',13))
    pabg.place(x=150,y=280)



    #Patient Details window
    tk.Label(root,text='     Patient Details view     ',font=(None,22), width=30).place(x=160,y=20)
    tk.Label(root,text='Enter Patient ID', width=20, height=2).place(x=50,y=400)
    # Entry box
    eid_=Entry(root,width=30,textvariable=eid).place(x=210,y=400)
    #buttons window 
    Button(root,text='Search', command=search ,height=2,width=13,font=(None,10)).place(x=450,y=400)    
 

    root.mainloop()


#====  Operation Details view screen ======================================
def Operation_details_view():
    root=Tk()
    root.title('operation')
    root['bg']='lightgreen'

    width = 825
    height = 560
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    global eid_
    # Operation Details Variables
    eid=StringVar()

    def search():
            
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mysqldb.cursor()

        p_id=eid.get()
        if(p_id!=""):
            dbp_id=""
            Select="select p_id,n_id,ad_date,op_date,op_time,op_type,blood,sugar from operation where p_id='%s'" %(p_id)
            mycursor.execute(Select)
            result=mycursor.fetchall()
            #print(result)
            for i in result:
                dbp_id=i[0]
                #print(dbp_id)
            if(p_id != dbp_id):
                global row
                row=i
                paid.config(text=row[0])      
                naid.config(text=row[1])
                addate.config(text=row[2])
                opdate.config(text=row[3])
                optime.config(text=row[4])
                optype.config(text=row[5])
                bp.config(text=row[6])
                sl.config(text=row[7])

            else:
                 messagebox.showerror("Error","this Patient ID not match in our database....")
                 Clear()

        
        else:
            messagebox.showerror("Error","please enter Patient ID in the text box....")
            Clear()
        



    def Clear():
        paid.config(text="") 
        naid.config(text="") 
        addate.config(text="") 
        opdate.config(text="") 
        optime.config(text="") 
        optype.config(text="") 
        bp.config(text="") 
        sl.config(text="") 
        eid.set("")
        
        
        
    # Data load txt boxes
    def getData(event):
        Clear()
        selected_row=tv.focus()
        data=tv.item(selected_row)
        global row
        row=data["values"]
        paid.config(text=row[0])      
        naia.config(text=row[1])
        addate.config(text=row[2])
        opdate.config(text=row[3])
        optime.config(text=row[4])
        optype.config(text=row[5])
        bp.config(text=row[6])
        sl.config(text=row[7])
        
        



    ttk.Label(root,text='Patient ID :',font=('Arial',13)).place(x=10,y=100)
    paid=ttk.Label(root,font=('Arial',13))
    paid.place(x=150,y=100)

    ttk.Label(root,text='Nurse ID :',font=('Arial',13)).place(x=10,y=120)
    naid=ttk.Label(root,font=('Arial',13))
    naid.place(x=150,y=120)
    
    ttk.Label(root,text='Admite Date :',font=('Arial',13)).place(x=10,y=140)
    addate=ttk.Label(root,font=('Arial',13))
    addate.place(x=150,y=140)

    ttk.Label(root,text='Operation Date :',font=('Arial',13)).place(x=10,y=160)
    opdate=ttk.Label(root,font=('Arial',13))
    opdate.place(x=150,y=160)

    
    ttk.Label(root,text='Operation Time :',font=('Arial',13)).place(x=10,y=180)
    optime=ttk.Label(root,font=('Arial',13))
    optime.place(x=150,y=180)

    ttk.Label(root,text='Operation Type :',font=('Arial',13)).place(x=10,y=200)
    optype=ttk.Label(root,font=('Arial',13))
    optype.place(x=150,y=200)
  
    ttk.Label(root,text='Blood Pressure :',font=('Arial',13)).place(x=10,y=220)
    bp=ttk.Label(root,font=('Arial',13))
    bp.place(x=150,y=220)

    ttk.Label(root,text='Sugar Level :',font=('Arial',13)).place(x=10,y=240)
    sl=ttk.Label(root,font=('Arial',13))
    sl.place(x=150,y=240)



    tk.Label(root,text='     Operation Details view     ',font=(None,22), width=30).place(x=140,y=20)

    tk.Label(root,text='Enter Patient ID', width=20, height=2).place(x=50,y=400)
    # Entry box
    eid_=Entry(root,width=30,textvariable=eid ).place(x=210,y=400)
    #buttons window 
    Button(root,text='Search', command=search ,height=2,width=13,font=(None,10)).place(x=450,y=400)



    

    root.mainloop()



#========= doctor panel ===================================================
def doctor_panel():
    root=Tk()
    root.title('Doctor Panel')
    root['bg']='lightgreen'
    width = 825
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    def open_patient_view():
        root.destroy()    
        patient_details_view()

    def open_Operation_view():
        root.destroy()    
        Operation_details_view()
    tk.Label(root,text='Doctor',font=(None,40,"bold")).place(x=210,y=40)

    img=Image.open("3.jpg")
    test=ImageTk.PhotoImage(img)

    la=tkinter.Label(image=test,width=825,height=610)
    la.image = test
    la.place (x=0,y=0)
    
    Button(root,text='Patient Details', command=open_patient_view, height=2,width=15,font=(None,10,"bold")).place(x=250,y=300)
    Button(root,text='Operation Details', command=open_Operation_view, height=2,width=15,font=(None,10,"bold")).place(x=250,y=420)

    root.mainloop()



#========= nurse panel ===================================================
def nurse_panel():
    root=Tk()
    root.title('Nurse Panel')
    root['bg']='lightgreen'
    width = 825
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    def open_patient():
        root.destroy()    
        patient_details()

    def open_Operation():
        root.destroy()    
        Operation_details()

    tk.Label(root,text='Nurse',font=(None,40,"bold")).place(x=210,y=40)
    img=Image.open("4.png")
    test=ImageTk.PhotoImage(img)

    la=tkinter.Label(image=test,width=825,height=610)
    la.image = test
    la.place (x=0,y=0)

    Button(root,text='Patient Details', command=open_patient, height=2,width=15,font=(None,10,"bold")).place(x=250,y=300)
    Button(root,text='Operation Details',command=open_Operation, height=2,width=15,font=(None,10,"bold")).place(x=250,y=420)

    root.mainloop()


#========= nurse screen ===================================================
def nurse():
    root=Tk()
    root.title('Nurse')
    root['bg']='lightgreen'

    width = 760
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    username=StringVar()
    password=StringVar()
    firstname=StringVar()
    lastname=StringVar()
    email=StringVar()
    phonenumber=StringVar()

    tk.Label(root,text='Your Care Hospitals Operation Theatre',fg='red',font=('Monaco',25),bg='Lightgreen',width=30).place(x=35,y=15)
    tk.Label(root,text='Nurses Only',fg='Black',font=(None,20),bg='Lightgreen', width=30).place(x=95,y=60)



    def LoginForm():
        global LoginFrame, lbl_result1
        LoginFrame = Frame(root)
        LoginFrame.place(x=140, y=91, width=475,height=350)


    
        lbl_username = Label(LoginFrame, text="Username:",font=('arial', 15), bd=8)
        lbl_username.place(x=100, y=70)
    
        lbl_password = Label(LoginFrame, text="Password:",font=('arial', 15), bd=8)
        lbl_password.place(x=100, y=120)
    
        ttk.Entry(LoginFrame,font=('arial', 10),textvariable=username, width=18).place(x=210, y=80)
    
        ttk.Entry(LoginFrame,font=('arial', 10),textvariable=password, width=18, show="*").place(x=210, y=130)
    
        btn_login = Button(LoginFrame,text="Login",font=('arial', 13), width=10, command=login_user)
        btn_login.place(x=170, y=190)
    
        btn_register = Button(LoginFrame, text="Register", fg="black", font=('arial', 12))
        btn_register.place(x=180, y=240)
    
    
        btn_register.bind('<Button-1>', ToggleToRegister)

    

    def RegisterForm():
        global RegisterFrame, lbl_result2
        RegisterFrame = Frame(root)
        RegisterFrame.place(x=140,y=91,width=475,height=440)

   
    
        lbl_username = Label(RegisterFrame,text="Username:",font=('arial',15),bd=8)
        lbl_username.place(x=110, y=55)
    
        lbl_password = Label(RegisterFrame,text="Password:",font=('arial',15),bd=8)
        lbl_password.place(x=110, y=105)
    
        lbl_firstname = Label(RegisterFrame,text="Firstname:",font=('arial',15),bd=8)
        lbl_firstname.place(x=110,y=160)
    
        lbl_lastname = Label(RegisterFrame,text="Lastname:",font=('arial',15),bd=8)
        lbl_lastname.place(x=110,y=215)

        lbl_email = Label(RegisterFrame,text="E-Mail:",font=('arial',15),bd=8)
        lbl_email.place(x=140,y=270)
    
        lbl_phone = Label(RegisterFrame,text="Phone number:",font=('arial',15),bd=8)
        lbl_phone.place(x=70,y=325)
    
    
        ttk.Entry(RegisterFrame,font=('arial',13),textvariable=username,width=14).place(x=220,y=65)
    
        ttk.Entry(RegisterFrame, font=('arial', 13), textvariable=password, width=14, show="*").place(x=220,y=115)
    
        ttk.Entry(RegisterFrame, font=('arial', 13), textvariable=firstname, width=14).place(x=220,y=170)
    
        ttk.Entry(RegisterFrame, font=('arial', 13), textvariable=lastname, width=14).place(x=220,y=225)

        ttk.Entry(RegisterFrame, font=('arial', 13), textvariable=email, width=14).place(x=220,y=280)
    
        ttk.Entry(RegisterFrame, font=('arial', 13), textvariable=phonenumber, width=14).place(x=220,y=335)
    
        btn_login = Button(RegisterFrame, text="Register", font=('arial', 13), width=10, command=Add)
        btn_login.place(x=170, y=380)
    

    def Clear():
        username.set("")
        password.set("")
        firstname.set("")
        lastname.set("")
        email.set("")
        phonenumber.set("")

    def Add():
        user_name=username.get()
        pass_word=password.get()
        first_name=firstname.get()
        last_name=lastname.get()
        e_mail=email.get()
        phone_number=phonenumber.get()
        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mysqldb.cursor()

 
        if(user_name !="" and pass_word !="" and first_name !="" and last_name !="" and e_mail!="" and phone_number !=""):
            try:
                sql="INSERT INTO nurse(user_name,pass_word,first_name,last_name,e_mail,phone_number) values(%s,%s,%s,%s,%s,%s)"
                val=(user_name,pass_word,first_name,last_name,e_mail,phone_number)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid=mycursor.lastrowid
                messagebox.showinfo("nurse","successfully")
                Clear()
                ToggleToLogin()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
        else:
            messagebox.showinfo("nurse","fill Details")

    def login_user():
        user_name = username.get()
        pass_word = password.get()

        if(user_name == "" or pass_word == ""):
            messagebox.showinfo("Login","empty")
            return

        mydb = mysql.connector.connect(host="localhost",user="root",password="",database = "hospital")
        mycursor = mydb.cursor()
        
        sql = "select user_name, pass_word from nurse where user_name=%s and pass_word=%s"
        val = (user_name, pass_word)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        Clear()
        if result:
            messagebox.showinfo("nurse","logged in")
            root.destroy()  
            nurse_panel()
        else:
            messagebox.showinfo("nurse","wrong credentials")
        


    def ToggleToLogin(event=None):
        RegisterFrame.destroy()
        LoginForm()

    def ToggleToRegister(event=None):
        LoginFrame.destroy()
        RegisterForm()

    LoginForm()

    #========================================INITIALIZATION===================================
    if __name__ == '__main__':
        root.mainloop()

#========= doctor screen ===================================================
def doctor():
    root=Tk()
    root.title('doctor')
    root['bg']='lightgreen'
    width = 760
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    screen_background='Lightgreen'
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    tk.Label(root,text='Your Care Hospitals Operation Theatre',fg='red',font=('Monaco',25),bg='Lightgreen',width=30).place(x=35,y=10)
    tk.Label(root,text=' Doctor ',font=(None,25),bg='Lightgreen',width=30).place(x=95,y=50)


    username=StringVar()
    password=StringVar()
    firstname=StringVar()
    lastname=StringVar()
    email=StringVar()
    phonenumber=StringVar()



    def LoginForm():
        global LoginFrame, lbl_result1
        LoginFrame = Frame(root)
        LoginFrame.place(x=140, y=91, width=475,height=440)
    
        lbl_username = Label(LoginFrame, text="Username:",font=('arial', 15), bd=8)
        lbl_username.place(x=100, y=70)
    
        lbl_password = Label(LoginFrame, text="Password:",font=('arial', 15), bd=8) 
        lbl_password.place(x=100, y=120)
    
    
        ttk.Entry(LoginFrame, textvariable=username,font=('arial', 10), width=18).place(x=210, y=80)
    
        ttk.Entry(LoginFrame, textvariable=password,font=('arial', 10), width=18, show="*").place(x=210, y=130)
    
        btn_login = Button(LoginFrame,text="Login", command=login_user,font=('arial', 13), width=10)
        btn_login.place(x=170, y=190)

    
        btn_register = Button(LoginFrame, text="Register", font=('arial', 12))
        btn_register.place(x=190, y=240)
    
    
        btn_register.bind('<Button-1>', ToggleToRegister)

    def RegisterForm():
        global RegisterFrame, lbl_result2
        RegisterFrame = Frame(root)
        RegisterFrame.place(x=140,y=91,width=475,height=440) 
    
        lbl_username = Label(RegisterFrame,text="Username:",font=('arial',15),bd=8)
        lbl_username.place(x=110, y=55)
    
        lbl_password = Label(RegisterFrame,text="Password:",font=('arial',15),bd=8)
        lbl_password.place(x=110, y=105)
    
        lbl_firstname = Label(RegisterFrame,text="Firstname:",font=('arial',15),bd=8)
        lbl_firstname.place(x=110,y=160)
    
        lbl_lastname = Label(RegisterFrame,text="Lastname:",font=('arial',15),bd=8)
        lbl_lastname.place(x=110,y=215)

        lbl_email = Label(RegisterFrame,text="E-Mail:",font=('arial',15),bd=8)
        lbl_email.place(x=140,y=270)
    
        lbl_phone = Label(RegisterFrame,text="Phone number:",font=('arial',15),bd=8)
        lbl_phone.place(x=70,y=325)
    

        ttk.Entry(RegisterFrame, textvariable=username,font=('arial',13),width=14).place(x=220,y=65)
    
        ttk.Entry(RegisterFrame, textvariable=password,font=('arial', 13), width=14, show="*").place(x=220,y=115)
    
        ttk.Entry(RegisterFrame, textvariable=firstname,font=('arial', 13), width=14).place(x=220,y=170)
    
        ttk.Entry(RegisterFrame, textvariable=lastname,font=('arial', 13), width=14).place(x=220,y=225)

        ttk.Entry(RegisterFrame, textvariable=email,font=('arial', 13), width=14).place(x=220,y=280)
    
        ttk.Entry(RegisterFrame, textvariable=phonenumber,font=('arial', 13), width=14).place(x=220,y=335)
    
        btn_login = Button(RegisterFrame, text="Register", font=('arial', 13), width=10, command=Add)
        btn_login.place(x=170, y=380)

    def Clear():
        username.set("")
        password.set("")
        firstname.set("")
        lastname.set("")
        email.set("")
        phonenumber.set("")

    def Add():
        user_name=username.get()
        pass_word=password.get()
        first_name=firstname.get()
        last_name=lastname.get()
        e_mail=email.get()
        phone_number=phonenumber.get()
        
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mysqldb.cursor()

 
        if(user_name !="" and pass_word !="" and first_name !="" and last_name !="" and e_mail!="" and phone_number !=""):
            try:
                sql="INSERT INTO doctor(user_name,pass_word,first_name,last_name,e_mail,phone_number) values(%s,%s,%s,%s,%s,%s)"
                val=(user_name,pass_word,first_name,last_name,e_mail,phone_number)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid=mycursor.lastrowid
                messagebox.showinfo("save","successfully")
                Clear()
                ToggleToLogin()
                
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
        else:
            messagebox.showinfo("doctor","fill Details")

    def login_user():
        user_name = username.get()
        pass_word = password.get()

        if(user_name == "" or pass_word == ""):
            messagebox.showinfo("Login","empty!")
            return

        mydb = mysql.connector.connect(host="localhost",user="root",password="",database = "hospital")
        mycursor = mydb.cursor()
        
        sql = "select user_name, pass_word from doctor where user_name=%s and pass_word=%s"
        val = (user_name, pass_word)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        Clear()
        if result:
            messagebox.showinfo("doctor","logged in")
            root.destroy()
            doctor_panel()
        else:
            messagebox.showinfo("doctor","wrong credentials")
        



    
    def ToggleToLogin(event=None):
        RegisterFrame.destroy()
        LoginForm()

    def ToggleToRegister(event=None):
        LoginFrame.destroy()
        RegisterForm()

    LoginForm()

    if __name__ == '__main__':
        root.mainloop()

#========= home screen ===================================================
def main():
    root=Tk()
    root.title('Operation Theater')
    root['bg']='lightgreen'
    width = 825
    height = 610
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

        
    def main_nurse():
        root.destroy()    
        nurse()

    def main_doctor():
        root.destroy()    
        doctor()
    img=Image.open("2.jpg")
    test=ImageTk.PhotoImage(img)

    la=tkinter.Label(image=test,width=825,height=610)
    la.image = test
    la.place (x=0,y=0)

    tk.Label(root,text='Your Care Hospitals',fg='Red',bg='Lightgreen',font=('Monaco',25)).place(x=200,y=20)
    tk.Label(root,text='Operation Theater',fg='black',bg='Lightgreen',font=(None,20,"bold")).place(x=280,y=80)

    #=============   button   ====================================================================================================
        
    Button(root,text='Nurse',command=main_nurse,height=3,width=15,font=(None,20,"bold")).place(x=180,y=400)
    Button(root,text='Doctor',command=main_doctor,height=3,width=15,font=(None,20,"bold")).place(x=450,y=400)

    root.mainloop()

  

main ()
