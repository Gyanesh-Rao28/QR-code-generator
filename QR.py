from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+100")
        self.root.title("QR Generator | By (Gyanesh, Harshith, Aradhy)| Hello")
        self.root.resizable(False,False)

        title = Label(self.root, text="QR Generator", font=("times new roman", 42), bg='#f9004d', fg='black').place(x=0, y=0, relwidth=1)
        
          
        #______variables______

        self.var_emp_code = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_department = StringVar()
        self.var_emp_desgination = StringVar()


        #______Employee-Details______
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        title = Label(emp_Frame, text="Employee Details", font=("goudy old style", 24), bg='white', fg='black').place(x=0, y=0, relwidth=1)

        #______Label_emp_____
        lbl_emp_code = Label(emp_Frame, text="Employee ID", font=("times new roman", 16, "bold"), bg='white', fg='black').place(x=20, y=60)
        lbl_emp_name = Label(emp_Frame, text="Name", font=("times new roman", 16, "bold"), bg='white', fg='black').place(x=20, y=100)
        lbl_emp_department_ = Label(emp_Frame, text="Department", font=("times new roman", 16, "bold"), bg='white', fg='black').place(x=20, y=140)
        lbl_emp_desgination = Label(emp_Frame, text="Designation", font=("times new roman", 16, "bold"), bg='white', fg='black').place(x=20, y=180)

        #______Label_TXT_____
        txt_emp_code = Entry(emp_Frame, font=("times new roman", 16,), textvariable=self.var_emp_code, bg='#f9004d', fg='white').place(x=200, y=60,)
        txt_emp_name = Entry(emp_Frame, font=("times new roman", 16,), textvariable=self.var_emp_name, bg='#f9004d', fg='white').place(x=200, y=100,)
        txt_emp_department_ = Entry(emp_Frame, font=("times new roman", 16,), textvariable=self.var_emp_department, bg='#f9004d', fg='white').place(x=200, y=140,)
        txt_emp_desgination = Entry(emp_Frame, font=("times new roman", 16,), textvariable=self.var_emp_desgination, bg='#f9004d', fg='white').place(x=200, y=180,)

        #______Label_Button_____
        btn_generator = Button(emp_Frame,text="Generate Code", command=self.generate, font=("times new roman", 16, 'bold'), bg='#f9004d', fg='black').place(x=60, y=250,width=200,height=30)
        btn_clr = Button(emp_Frame,text="Clear", command=self.clear, font=("times new roman", 16, 'bold'), bg='#f9004d', fg='black').place(x=290, y=250,width=120,height=30)

        #______Label_Msg_____
        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=('times new roman',20,'bold'),fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)

        #______QR-Code_Window______
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        emp_title = Label(qr_Frame, text="Employee QR Code", font=("goudy old style", 18), bg='#f9004d', fg='black').place(x=0, y=0, relwidth=1)
        
        self.qr_code = Label(qr_Frame, text='QR Code \n Not Available!!!\n Right Now', font=('times new roman', 14), bg='#f9004d', fg='black', bd=1, relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    #______Data-Clear______

    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_name.set('')
        self.var_emp_department.set('')
        self.var_emp_desgination.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    
    #______Data-fecthing______
    def generate(self):
        if self.var_emp_code.get()=='' or self.var_emp_name.get()=='' or self.var_emp_department.get()=='' or self.var_emp_desgination.get()=='':
            self.msg='All Fields Are Required!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            #______QR Code Generation______

            qr_data = (f"Employee ID: {self.var_emp_code.get()}\nName: {self.var_emp_name.get()}\nDepartment: {self.var_emp_department.get()}\nDesgination: {self.var_emp_desgination.get()}")
            qr_code = qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])

            #______QR Code Softcopy______

            qr_code.save("F:\Python\Projects\QR_Code_Gen\QR_imgs/QR_icode"+"_"+str(self.var_emp_code.get())+'.png')


            #______QR Code Generation______

            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)


            #______Updating_notification______
            self.msg = 'QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg, fg='green')

root=Tk()
obj=Qr_Generator(root)
root.mainloop()