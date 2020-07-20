from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import pymysql



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Regiseration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="lightblue")

# =============================================================================
#         ---- bg image ---
        self.bg=ImageTk.PhotoImage(file="D:/FR/images/bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
 
# 
# #        ---- left image ---
        self.left=ImageTk.PhotoImage(file="D:/FR/images/side.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=489)
        
        #self.label = Label(frame,image = self.img)
        #self.label.image = self.img
        
        #self.path = "F:/Register N Login/images/b2.jpg"
        #self.image = Image.open(self.path)
        #self.img = ImageTk.PhotoImage(self.image)
        
        
       #---register frame---
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=489)
        
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        
        
        #------------------------------------------------------------------------------row1
        #self.var_fname=StringVar()
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        #txt_fname = Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_fname).place(x=50,y=130,width=250)
        self.txt_fname = Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname = Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        
        #-------------------------------------------------------------------------------row2
        
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact = Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email = Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        
        
        #-------------------------------------------------------------------------------row3
        
        branch=Label(frame1,text="Branch",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        
        self.cmb_quest = ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Computer","Electrical","Mechanical","Civil")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        
        semester=Label(frame1,text="Semester",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        
        
        self.cmb_quest2 = ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest2['values']=("Select","Sem1","Sem2","Sem3","Sem4","Sem5","Sem6","Sem7","Sem8")
        self.cmb_quest2.place(x=370,y=270,width=250)
        self.cmb_quest2.current(0)
        
        
        #answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        #self.txt_answer = Entry(frame1,font=("times new roman",15),bg="lightgray")
        #self.txt_answer.place(x=370,y=270,width=250)
        
        
        
        #-------------------------------------------------------------------------------row4
        
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password = Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)
        
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword = Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        
        #---------------------------------------------------------------------------------terms
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        
        #self.btn_img=ImageTk.PhotoImage(file="F:/Register N Login/images/register.png")
        #self.btn_img = ImageTk.PhotoImage(Image.open('F:/Register N Login/images/register.png'))
        #btn=Button(frame1,text="Register Now->",bg="green",bd=0,cursor="hand2").place(x=50,y=420,width=250)
        #btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2").place(x=50,y=420,width=350)
        btn_register=Button(frame1,text="Register Now",font=("times new roman",20),bd=0,cursor="hand2",command=self.register_data,bg="lightblue").place(x=50,y=420,width=250)
        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=460,width=180)
        
        
        #self.img = ImageTk.PhotoImage(Image.open('F:/Register N Login/images/register.png'))
    
    def login_window(self):
        self.root.destroy()
        import login
        
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest2.current(0)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)
        
        
        
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="select" or self.cmb_quest2.get()=="select" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password Should Be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="studentreg")
                cur=con.cursor()
                cur.execute("select * from student where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                  messagebox.showerror("Error","User Already Exist,Please Try With Another Email",parent=self.root)
                else:
                    cur.execute("insert into student (f_name,l_name,contact,email,branch,semester,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (self.txt_fname.get(),
                                     self.txt_lname.get(),
                                     self.txt_contact.get(),
                                     self.txt_email.get(),
                                     self.cmb_quest.get(),
                                     self.cmb_quest2.get(),
                                     self.txt_password.get()
                                     ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successful",parent=self.root) 
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To: {str(es)}",parent=self.root)
                
            
            
           
            
            
# =============================================================================
#               self.txt_lname.get(),
#               self.txt_contact.get(),
#               self.txt_email.get(),
#               self.cmb_quest.get(),
#               self.txt_answer.get(),
#               self.txt_password.get(),
#               self.txt_cpassword.get()
#         
# =============================================================================
    
    
root=Tk()
obj=Register(root)
root.mainloop()


