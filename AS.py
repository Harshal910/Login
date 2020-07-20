from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk


class Student:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Attendance Sheet")
        self.root.geometry("1350x700+0+0")
         #=======background colors==================================
        left_lbl=Label(self.root,bg="#031F3C",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,relwidth=1)
        
        title=Label(self.root,text="Attendance Sheet",bd=1,font=("times new roman",40,"bold"),bg="#031F3C",fg="white")
        title.pack(side=TOP,fill=X)     
        
        
        #====all variable====#
        self.Branch_var=StringVar()
        self.En_Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        
        
#===manageframe===#
        
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#031F3C")
        Manage_Frame.place(x=20,y=100,width=450,height=675)
        
        m_title=Label(Manage_Frame,text="Manage Students",bg="#031F3C",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        lbl_Branch=Label(Manage_Frame,text="Branch",bg="#031F3C",fg="white",font=("times new roman",20,"bold"))
        lbl_Branch.grid(row=1,column=0,pady=10,padx=20,sticky="W")
        
        combo_Branch=ttk.Combobox(Manage_Frame,textvariable=self.Branch_var,font=("times new roman",13,"bold"),state='readonly')
        combo_Branch['values']=("Computer","Electrical","Machanical","Civil")
        combo_Branch.grid(row=1,column=1,pady=10,padx=20,sticky="W")
        
        lbl_En_Roll_No=Label(Manage_Frame,text="En_Roll No.",bg="#031F3C",fg="white",font=("times new roman",20,"bold"))
        lbl_En_Roll_No.grid(row=2,column=0,pady=10,padx=20,sticky="W")
        
        txt_En_Roll_No=Entry(Manage_Frame,textvariable=self.En_Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_En_Roll_No.grid(row=2,column=1,pady=10,padx=20,sticky="W")
        
        lbl_name=Label(Manage_Frame,text="Name",bg="#031F3C",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=3,column=0,pady=10,padx=20,sticky="W")
        
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=3,column=1,pady=10,padx=20,sticky="W")
        
        lbl_Email=Label(Manage_Frame,text="Email",bg="#031F3C",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=4,column=0,pady=10,padx=20,sticky="W")
        
        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=4,column=1,pady=10,padx=20,sticky="W")
        
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="#031F3C",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=5,column=0,pady=10,padx=20,sticky="W")
        
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=5,column=1,pady=10,padx=20,sticky="W")
        
        
        
        lbl_Contact=Label(Manage_Frame,text="Contact",bg="#031F3C",fg="white",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=6,column=0,pady=10,padx=20,sticky="W")
        
        txt_Contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=6,column=1,pady=10,padx=20,sticky="W")
        
        lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="#031F3C",fg="white",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=7,column=0,pady=10,padx=20,sticky="W")
        
        txt_DOB=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=7,column=1,pady=10,padx=20,sticky="W")
        
        
        lbl_Address=Label(Manage_Frame,text="Address",bg="#031F3C",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=8,column=0,pady=10,padx=20,sticky="W")
        
        self.txt_Address=Text(Manage_Frame,width=20,height=3,font=("",15))
        self.txt_Address.grid(row=8,column=1,pady=10,padx=20,sticky="W")
        
         #===butttonframe===#
        
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#031F3C")
        btn_Frame.place(x=15,y=600,width=420)
        
        
        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text=" Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear_students).grid(row=0,column=3,padx=10,pady=10)
        
        
        
        
     #===detailframe===#   
        
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#031F3C")
        Detail_Frame.place(x=500,y=100,width=1000,height=675)
        
        
        lbl_Search=Label(Detail_Frame,text="Search By",bg="#031F3C",fg="white",font=("times new roman",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="W")
        
        
        combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_Search['values']=("En_Roll_No","Name","Contact")
        combo_Search.grid(row=0,column=1,pady=10,padx=20,sticky="W")
        
        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="W")
        
        Searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        ShowAllbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
        Take_Imgbtn=Button(Detail_Frame,text="Take_Img",width=10,pady=5,command=self.take_img).grid(row=0,column=5,padx=10,pady=10)
        
        #========table frame==============#
        
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#031F3C")
        Table_Frame.place(x=10,y=70,width=760,height=500)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Branch","En_Roll_No","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Branch",text="Branch")
        self.Student_table.heading("En_Roll_No",text="En_Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("Branch",width=100)
        self.Student_table.column("En_Roll_No",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_students(self):
        if self.En_Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:
               conn=pymysql.connect(host='localhost',user='root',password='',database='unique')
               cur=conn.cursor()
               cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.Branch_var.get(),
                                                                            self.En_Roll_No_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_Address.get('1.0',END)
            
                                                                            ))
               conn.commit()
               self.fetch_data()
               self.clear_students()
               conn.close()
               messagebox.showinfo("Success","Record has been inserted")
    def fetch_data(self):
         conn=pymysql.connect(host='localhost',user='root',password='',database='unique')
         cur=conn.cursor()
         cur.execute("select * from students")
         rows=cur.fetchall()
         if len(rows)!=0:
             self.Student_table.delete(*self.Student_table.get_children())
             for row in rows:
                 self.Student_table.insert('',END,values=row)
                 
         conn.commit()
         conn.close()
    def clear_students(self):
            self.Branch_var.set("")
            self.En_Roll_No_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.txt_Address.delete('1.0',END)
            
    def get_cursor(self,ev):
        curosor_row=self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row=contents['values']
        self.Branch_var.set(row[0])
        self.En_Roll_No_var.set(row[1])
        self.name_var.set(row[2])
        self.email_var.set(row[3])
        self.gender_var.set(row[4])
        self.contact_var.set(row[5])
        self.dob_var.set(row[6])
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END,row[7])  
    def update_data(self):
        conn=pymysql.connect(host='localhost',user='root',password='',database='unique')
        cur=conn.cursor()
        cur.execute("update students set Branch=%s,name=%s,email=%s,gender=%s,contact=%s,dob=%s,Address=%s where En_Roll_No=%s",(
                                                                            self.Branch_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_Address.get('1.0',END),
                                                                            self.En_Roll_No_var.get()
            
                                                                            ))
        conn.commit()
        self.fetch_data()
        self.clear_students()
        conn.close()
    def delete_data(self):
        conn=pymysql.connect(host='localhost',user='root',password='',database='unique')
        cur=conn.cursor()
        cur.execute("delete from students where En_Roll_No=%s",self.En_Roll_No_var.get())
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear_students()
        
    def search_data(self):
        conn=pymysql.connect(host='localhost',user='root',password='',database='unique')
        cur=conn.cursor()
        
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            conn.commit()
            conn.close()
            
    def take_img(self):
        global filename
        filename = filedialog.askopenfilename()
        self.root.destroy()
        import DE
        
            
            
root=Tk()
ob=Student(root)
root.mainloop()