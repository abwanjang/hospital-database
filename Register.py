import tkinter
from tkinter import*
import os
from datetime import date
import sqlite3
from tkinter.ttk import Combobox
from tkinter import messagebox
import pathlib
from tkinter import filedialog
from PIL import ImageTk, Image
import pathlib
import random


class student_registration:
    def __init__(self):
        self.window = Tk()
        self.self_main_window()

    def run(self):
        self.window.mainloop()

    def self_main_window(self):
        self.window.title("REGISTER")
        screen_width=self.window.winfo_width()
        screen_height=self.window.winfo_height()
        self.window.resizable(width=False, height=False)
        x =(screen_width//2)-(screen_width//2)
        y = (screen_height//2)-(screen_height//2)
        self.window.geometry(f"1250x700+{x}+{y}")
        background = "#06283D"
        framebg = "#EDEDED"
        framefg = "#06283D"
        self.window.configure(bg=background)

        pic= "C:\\Users\\NEVILLE\\PycharmProjects\\shool_registration\\pictures\\profileicon.png"
        pic2= "C:\\Users\\NEVILLE\\PycharmProjects\\shool_registration\\pictures\\logo_icon.ico"
        icon = PhotoImage(file=pic)
        self.window.iconphoto(True, icon)
        self.window.iconbitmap(pic2)


        def query():

            def run_query():

                reg_query=registration_no_query.get()
                f_guery=firstname_query.get()
                l_query=lastname_query.get()
                o_query=owing_query.get()
                c_query=contact_query.get()
                g_guery=gender_query.get()
                p_query=payed_query.get()
                d_query=date_reg.get()

                print(reg_query, f_guery, l_query, o_query, c_query, g_guery, p_query, d_query)

            root = tkinter.Tk()
            root.geometry(f'1200x600')
            root.title('QUERY REGISTER')
            root.resizable(False, False)
            root.config(bg='green')

            # top frames
            Label(root, text='contact: abwaneville@gmail.com', width=10, height=3, bg="#f0687c",
                  anchor='e').pack(side=TOP, fill=X)
            Label(root, text="QUERY REGISTRATION", width=10, height=2, bg="blue",
                  font=('arial bold', 20), fg='#fff').pack(side=TOP, fill=X)

            run_button = Button(root, text='run', width=5, bd=2, font='arial 20', compound=TOP,
                                command=run_query)
            run_button.place(relx=0.03, rely=0.09)

            Label(root, text="Select Query", bg="red", font=('arial', 20)).place(relx=0.4, rely=0.2)

            # frmae to store the health query
            frame1 = LabelFrame(root, text="registration number", width=210, height=200)
            frame1.place(rely=0.3, relx=0.03)
            frame1.pack_propagate(False)

            frame2 = LabelFrame(root, text="first name", width=210, height=200)
            frame2.place(rely=0.3, relx=0.25)
            frame2.pack_propagate(False)

            frame3 = LabelFrame(root, text="last name", width=210, height=200)
            frame3.place(rely=0.3, relx=0.45)
            frame3.pack_propagate(False)

            frame10 = LabelFrame(root, text="contact", width=210, height=200)
            frame10.place(rely=0.3, relx=0.65)
            frame10.pack_propagate(False)

            frame4 = LabelFrame(root, text="class", width=210, height=200)
            frame4.place(rely=0.65, relx=0.03)
            frame4.pack_propagate(False)

            frame5 = LabelFrame(root, text="payed", width=210, height=200)
            frame5.place(rely=0.65, relx=0.25)
            frame5.pack_propagate(False)

            frame6 = LabelFrame(root, text='owing', width=210, height=200)
            frame6.place(rely=0.65, relx=0.45)
            frame6.grid_propagate(0)
            frame6.config(width=210, height=200)

            frame7 = LabelFrame(root, text="gender", width=210, height=200)
            frame7.place(rely=0.65, relx=0.65)
            frame7.pack_propagate(False)

            frame8 = LabelFrame(root, text="health", width=210, height=200)
            frame8.place(rely=0.65, relx=0.03)
            frame8.pack_propagate(False)

            frame9 = LabelFrame(root, text="date of registration", width=210, height=200)
            frame9.place(rely=0.65, relx=0.03)
            frame9.pack_propagate(False)

            owing_query = StringVar()
            Entry(frame6, textvariable=owing_query).grid(row=2, column=3, pady=50)

            registration_no_query = StringVar(value='NOT Disabled')
            Checkbutton(frame1, variable=registration_no_query, text="Disabled", offvalue="NOT Disabled"
                        , onvalue="Disabled").pack(pady=50)

            firstname_query = StringVar(value='NOT Disabled')
            Checkbutton(frame2, variable=firstname_query, text="Disabled", offvalue="NOT Disabled"
                        , onvalue="Disabled").pack(pady=50)

            lastname_query = StringVar(value='NOT Disabled')
            Checkbutton(frame3, variable=lastname_query, text="Disabled", offvalue="NOT Disabled"
                        , onvalue="Disabled").pack(pady=50)

            date_reg = StringVar(value='NOT Disabled')
            Checkbutton(frame4, variable=date_reg, text="Disabled4", offvalue="NOT Disabled"
                        , onvalue="Disabled").pack(pady=50)

            payed_query = StringVar(value='NOT Disabled')
            Checkbutton(frame5, variable=payed_query, text="Disabled", offvalue="NOT Disabled"
                        , onvalue="Disabled").pack(pady=50)

            gender_query = StringVar(value='NOT Disabled')
            Checkbutton(frame7, variable=gender_query, text="Disabled", offvalue="NOT Disabled"
                        , onvalue="Disabled").pack(pady=50)

            contact_query = StringVar(value='NOT Disabled')
            Checkbutton(frame10, variable=contact_query, text="Disabled", offvalue="NOT Disabled"
                        , onvalue="Disabled").pack(pady=50)

            root.mainloop()


        def save_changes():
            first_name = firstname.get()
            last_name = lastname.get()
            dob = date_of_birth.get()
            Gender = gender.get()
            Classvar = Class.get()
            schoolfee = school_fee.get()
            schoolfee_payed = school_fee_payed.get()
            Owing = owing.get()
            father_name = fathername.get()
            mother_name = mothername.get()
            Occupation = occupation.get()
            Occupation2 = occupation2.get()
            Contact = contact.get()
            Contact2 = contact2.get()
            Address = address.get()
            Health = health.get()
            registation_no = Registration.get()
            date_reg = Date.get()

            conn = sqlite3.connect('student_database.db')

            cursor=conn.cursor()
            cursor.execute("UPDATE student_database SET FIRSTNAME=? , LASTNAME=? , CLASS=? , GENDER=? " \
                                     ",SCHOOL_FEE=?  , PAYED=? , OWING=? , DATE_OF_BIRTH=? , HEALTH=?, ADDRESS=?," \
                                     " DATE_REGISTERED=?, FATHERS_NAME=? , MOTHERS_NAME=? , FATHERS_CONTACT=?,"\
                                     " MOTHERS_CONTACT=?, FATHERS_OCCUPATION=?,MOTHERS_OCCUPATION=? "
                                     "WHERE REGISTRATION=?",(first_name, last_name, Classvar, Gender, schoolfee,
                                           schoolfee_payed, Owing, dob, Health, Address, date_reg, father_name,
                                           mother_name, Contact, Contact2,Occupation,Occupation2,registation_no))
            conn.commit()
            conn.close()

            messagebox.showinfo(message="save successfull")

        def find(primary_key):
           # search = Search.get()

            conn = sqlite3.connect('student_database.db')
            cursor = conn.cursor()

            cursor.execute ("SELECT REGISTRATION ,FIRSTNAME , LASTNAME , CLASS , GENDER ,SCHOOL_FEE  , PAYED"
                            " , OWING , DATE_OF_BIRTH , HEALTH,ADDRESS, DATE_REGISTERED,FATHERS_NAME , MOTHERS_NAME"
                            " , FATHERS_CONTACT, MOTHERS_CONTACT, FATHERS_OCCUPATION, MOTHERS_OCCUPATION"
                            " ADDRESS, PROFILE FROM student_database WHERE REGISTRATION =?"
                            , (primary_key,))
            result =cursor.fetchone()

            if result is not None:
                registation_no, first_name, last_name, Classvar, Gender,\
                schoolfee, schoolfee_payed, Owing, dob, Health, Address, date_reg, father_name, mother_name,\
                Contact, Contact2, Occupation, Occupation2, filename = result

                firstname.set(first_name)
                lastname.set(last_name)
                date_of_birth.set(dob)
                gender.set(Gender)
                Class.set(Classvar)
                school_fee.set(schoolfee)
                school_fee_payed.set(schoolfee_payed)
                fathername.set(father_name)
                mothername.set(mother_name)
                occupation.set(Occupation)
                occupation2.set(Occupation2)
                contact.set(Contact)
                contact2.set(Contact2)
                address.set(Address)
                health.set(Health)
                Registration.set(registation_no)
                Date.set(date_reg)
                ibl.set(filename)


            else:
                messagebox.showerror(message=f"no registerd student with registration number {primary_key}, please"
                                             f"check the rgistration number entered is correct ")



        def calculate():
            # balnce calcualtion
            V2 = int(school_fee_payed.get())
            V1 = int(school_fee.get())
            result = V1 - V2
            owing.set(str(result))

        def exit():
            self.window.destroy()

        def upload():
            global filename
            filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="select image file"
                                                  , filetypes=(('JPG File', '*.jpg'), ('PNG File', '*png'),
                                                               ('ALL Files', '*txt')))

            img = (Image.open(filename))
            resized_image = img.resize((190,190))
            photo = ImageTk.PhotoImage(resized_image)
            ibl.config(image=photo)
            ibl.image=photo

            print(filename)

        def reset():

            firstname.set("")
            lastname.set("")
            date_of_birth.set("")
            gender.set("")
            Class.set("")
            school_fee.set(int(0))
            school_fee_payed.set(int(0))
            fathername.set("")
            mothername.set("")
            occupation.set("")
            occupation2.set("")
            contact.set("")
            contact2.set("")
            address.set("")
            health.set(value= "NOT Disabled")
            Registration.set(random.randint(0000, 9999))
            pass



        def save():

            first_name=firstname.get()
            last_name = lastname.get()
            dob = date_of_birth.get()
            Gender = gender.get()
            Classvar = Class.get()
            schoolfee = school_fee.get()
            schoolfee_payed = school_fee_payed.get()
            Owing = owing.get()
            father_name = fathername.get()
            mother_name = mothername.get()
            Occupation = occupation.get()
            Occupation2 = occupation2.get()
            Contact = contact.get()
            Contact2 = contact2.get()
            Address = address.get()
            Health = health.get()
            registation_no = Registration.get()
            date_reg = Date.get()


            # get the path to the user's desktop
            des_path = os.path.join(os.path.expanduser("~"), "Desktop")

            # create the full file path
            file_path = os.path.join(des_path, "student info.txt")

            print(file_path)

            if first_name and last_name  and dob and Gender and Classvar and schoolfee_payed and schoolfee and \
                    father_name and mother_name and contact and contact2 and Address != "":


                with open(file_path, "w") as file:
                     # write the input text to the file
                    file.write(f"""  
    
                        *****************STUDENT INFORMATION**************************
                        
                        Full Name: {first_name} {last_name}
                        Date of Birth : {dob}
                        Gender: {Gender}
                        Class: {Classvar}
                        School fee : {schoolfee}
                        Amount payed: {schoolfee_payed}
                        owing: {Owing}
                        Disabled: {Health}
                        Address: {Address}
                        Registration number: {registation_no}
                        
                        ***********************PARENT INFORMATION********************
                        
                        Father's name: {father_name}
                        Mother's name: {mother_name}
                        Father's occupation: {Occupation}
                        Mother's occupation: {Occupation2}
                        Father's contact: {Contact}
                        Mother's contact: {Contact2}
                        
                        **************RECEIPT***********************
                        ---------------------------------------------------------
                        
                        {first_name} {last_name} of {Classvar} has payed {schoolfee_payed} 
                        of his/her school feee and is left {Owing}
                        
                                                        signed the Vice Principal
                                                                            
                                                        _______________________
                        ----------------------------------------------------------                   
                        """)


                conn = sqlite3.connect('Student_database.db')

                table_query = """
                CREATE TABLE IF NOT EXISTS Student_database (REGISTRATION INT PRIMARY KEY, FIRSTNAME TEXT , 
                LASTNAME TEXT, CLASS TEXT, GENDER TEXT, SCHOOL_FEE  INT, PAYED INT, OWING INT, 
                DATE_OF_BIRTH TEXT, HEALTH TEXT, ADDRESS TEXT, DATE_REGISTERED TEXT, FATHERS_NAME TEXT,
                 MOTHERS_NAME TEXT, FATHERS_CONTACT INT, MOTHERS_CONTACT INT, FATHERS_OCCUPATION TEXT, 
                 MOTHERS_OCCUPATION TEXT)
                """
                conn.execute(table_query)

                table_query_input = """
                    INSERT INTO Student_database(REGISTRATION ,FIRSTNAME , LASTNAME , CLASS , GENDER ,
                    SCHOOL_FEE  , PAYED , OWING , DATE_OF_BIRTH , HEALTH, ADDRESS, DATE_REGISTERED, 
                    FATHERS_NAME , MOTHERS_NAME , FATHERS_CONTACT, MOTHERS_CONTACT, FATHERS_OCCUPATION,
                    MOTHERS_OCCUPATION) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                     
                """
                table_query_input_tuple = (registation_no, first_name, last_name, Classvar, Gender, schoolfee,
                                           schoolfee_payed, Owing, dob, Health, Address, date_reg, father_name,
                                           mother_name, Contact, Contact2,Occupation, Occupation2)
                cursor = conn.cursor()
                cursor.execute(table_query_input, table_query_input_tuple)
                conn.commit()
                conn.close()

                messagebox.showinfo(message=f"Registion info of {first_name} {last_name} \
                                        has been sent to your desktop on an editable word file saved as student info")
            else:
                messagebox.showwarning(title="ERROR", message="SPACE CAN'T BE LEFT EMPTY!! Please enter an info")




        #top frames
        Label(self.window,text='contact: abwaneville@gmail.com', width=10, height=3, bg="#f0687c",
              anchor='e').pack(side=TOP, fill=X)
        Label(self.window, text="STUDENT REGISTRATION", width=10, height=2, bg="#c36464",
              font=('arial bold', 20), fg='#fff').pack(side=TOP, fill=X)


        #seacch box update
        Search=StringVar()
        Entry(self.window, textvariable=Search, width=15, bd=2, font='arial 20').place(relx=0.7, rely=0.09)
        srch_button= Button(self.window, text='search', width=10, compound=LEFT, bg='#68ddfa', font="arial 13 bold",
                            command= lambda :find(Search.get()))
        srch_button.place(rely=0.09, relx=0.9)

        query_button = Button(self.window, text='query', width=5, bd=2, font='arial 20', compound=LEFT,
                                command=query)
        query_button.place(relx=0.03, rely=0.09)

        refresh_button =Button(self.window, text='refresh', width=5, bd=2, font='arial 20', compound=LEFT,
                               command=save_changes)
        refresh_button.place(relx=0.14, rely=0.09)


        #registration and date
        Label(self.window, text='Registration No:', fg=framebg, bg=background,
              font='arial 13').place(relx=0.03, rely=0.19)
        Label(self.window, text='Date:', fg=framebg, bg=background, font='arial 13').place(relx=0.4, rely=0.19)

        Registration =StringVar()
        Date = StringVar()

        reg_entry =Entry(self.window, textvariable=Registration, width=15, font="arial 10", state=DISABLED)
        reg_entry.place(relx=0.15, rely=0.19)

        mat= random.randint(0000, 9999)
        Registration.set(mat)

        today = date.today()
        day1 = today.strftime("%d/%m/%Y")
        date_entry = Entry(self.window, textvariable=Date, width=15, font="arial 10")
        date_entry.place(rely=0.19, relx=0.45)
        Date.set(day1)


        #student information
        #xxx =  Frame (self.window, width=900, height=250).place(relx=0.02, rely=0.25)


        student_labelframe = LabelFrame(self.window, width=900, height=250, text="student infomation",
                                        font=('times new romans', 18), bg=framebg, fg=framefg)
        student_labelframe.place(relx=0.02, rely=0.25)

        student_labelframe.grid_propagate(0)
        student_labelframe.config(width=900, height=250)

        firstname=StringVar()
        Label(student_labelframe, text="Fistname:").grid(row=0, column=0)
        Entry(student_labelframe, textvariable=firstname).grid(row=0, column=1)

        lastname = StringVar()
        Label(student_labelframe, text="Lastname:").grid(row=0, column=2)
        Entry(student_labelframe, textvariable=lastname).grid(row=0, column=3)

        date_of_birth = StringVar()
        Label(student_labelframe, text="Date of birth:").grid(row=1, column=0)
        Entry(student_labelframe, textvariable=date_of_birth).grid(row=1, column=1)

        Class = StringVar()
        Label(student_labelframe, text="Class:").grid(row=1, column=2)
        Entry(student_labelframe, textvariable=Class).grid(row=1, column=3)

        gender = StringVar()
        Label(student_labelframe, text="Gender:").grid(row=2, column=0)
        Combobox(student_labelframe, textvariable=gender, values=["male", "female", "costom"]).grid(row=2, column=1)

        health =StringVar(value="NOT Disabled")
        Label(student_labelframe, text="Disabled:").grid(row=2, column=2)
        Checkbutton(student_labelframe, variable=health, text="Disabled", offvalue="NOT Disabled"
                    , onvalue="Disabled").grid(row=2, column=3)

        school_fee=IntVar()
        Label(student_labelframe, text="Student School fee:").grid(row=0, column=4)
        Entry(student_labelframe, textvariable=school_fee).grid(row=0, column=5)

        school_fee_payed=IntVar()
        Label(student_labelframe, text="Ammount payed:").grid(row=1, column=4)
        Entry(student_labelframe, textvariable=school_fee_payed).grid(row=1, column=5)

        owing = StringVar()
        Label(student_labelframe, text="Balance:").grid(row=2, column=4)
        Entry(student_labelframe, textvariable=owing, state="readonly").grid(row=2, column=5)

        school_fee.trace_add("write", lambda *args:calculate())
        school_fee_payed.trace_add("write", lambda *args:calculate())




        for widget in student_labelframe.winfo_children():
            widget.grid_configure(pady=20, padx=10)




        parent_labelframe = LabelFrame(self.window, width=900, height=250, text="parent infomation",
                                       font=('times new romans', 18), bg=framebg, fg=framefg)
        parent_labelframe.place(relx=0.02, rely=0.63)

        parent_labelframe.grid_propagate(0)
        parent_labelframe.config(width=900, height=250)

        fathername = StringVar()
        Label(parent_labelframe, text="Father's name:").grid(row=0, column=0)
        Entry(parent_labelframe, textvariable=fathername).grid(row=0, column=1)

        mothername = StringVar()
        Label(parent_labelframe, text="Mother's name:").grid(row=0, column=2)
        Entry(parent_labelframe, textvariable=mothername).grid(row=0, column=3)

        occupation = StringVar()
        Label(parent_labelframe, text="Occupation:").grid(row=1, column=0)
        Entry(parent_labelframe, textvariable=occupation).grid(row=1, column=1)

        occupation2 = StringVar()
        Label(parent_labelframe, text="Occupation:").grid(row=1, column=2)
        Entry(parent_labelframe, textvariable=occupation2).grid(row=1, column=3)

        contact = StringVar()
        Label(parent_labelframe, text="Contact:").grid(row=2, column=0)
        Entry(parent_labelframe, textvariable=contact).grid(row=2, column=1)

        contact2 = StringVar()
        Label(parent_labelframe, text="Contact:").grid(row=2, column=2)
        Entry(parent_labelframe, textvariable=contact2).grid(row=2, column=3)

        address = StringVar()
        Label(parent_labelframe, text="Address:").grid(row=1, column=4)
        Entry(parent_labelframe, textvariable=address).grid(row=1, column=5)

        for widget in parent_labelframe.winfo_children():
            widget.grid_configure(pady=20, padx=10)


        # iamge frame

        img_frame=Frame(self.window, width=200, height=200, relief=GROOVE, bd=3,
                        bg='black').place(anchor='e', rely=0.4, relx=0.93)
        img =PhotoImage()
        ibl = Label(img_frame, bg='black', image=img, compound='left')
        ibl.place(anchor='e', rely=0.4, relx=0.93)

        Button(self.window, text='UPLOAD',width=24, height=2, relief=GROOVE, bd=3, bg='lightblue',
               command= upload).place(relx=0.78, rely=0.57)
        Button(self.window, text='SAVE',width=24, height=2, relief=GROOVE, bd=3, bg='lightgreen',
               command= save).place(relx=0.78, rely=0.67)
        Button(self.window, text='RESET',width=24, height=2, relief=GROOVE, bd=3, bg='lightpink',
               command= reset).place(relx=0.78, rely=0.77)
        Button(self.window, text='EXIT',width=24, height=2, relief=GROOVE, bd=3, bg='gray',
               command=exit).place(relx=0.78, rely=0.87)


if __name__ == "__main__":
    app = student_registration()
    app.run()
