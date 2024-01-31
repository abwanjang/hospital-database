from tkinter import *
from tkinter import ttk
import datetime
import random
from PIL import*
from PIL import Image, ImageTk
import cv2
from tkinter.ttk import Combobox
from database import process_registration
#from tkinter import messagebox
#from flask import Flask


class Registration(Tk):
    def __init__(self):
        super().__init__()
        screen_width = int(self.winfo_screenwidth())
        screen_height = int(self.winfo_screenheight())
        self.resizable(False, False)
        #self.wm_iconwindow(r"C:\Users\lenovo\Desktop\hospital _data_base_project\logo.png")
        background_color='#000000'
        entryColror='#bbb6b6'

        # setting window size to fit screen
        self.configure(width=screen_width, height=screen_height, bg=background_color)
        self.grid()

        # creating top-level label frame
        topframe = Frame(self, pady=15,padx=5)
        topframe.place(anchor='nw')
   
        # creating a canvas to store the name label in a round label shape
        canvas = Canvas(
            topframe,
            bg="#373d63",
            width=600,
            height=50,
            highlightthickness=0
        )
        canvas.grid(row=0, column=0, sticky='w')

        # shaping the canvas with curved ends
        radius = 10
        canvas.create_arc(
            0, 0, 2 * radius, 2 * radius,
            start=120, extent=380,
            fill='#373d63', outline=''
        )
        canvas.create_arc(
            590 - 2 * radius, 0, 590, 2 * radius,
            start=90, extent=180,
            fill='#373d63', outline=''
        )
        canvas.create_rectangle(
            radius, 0, 590 - radius, 50,
            fill='#373d63', outline=''
        )

        namelevel = Label(canvas,fg="white",bg='#373d63',width=55,height=2,
            text="HOSPITAL MANAGEMENT INFORMATION SYSTEM",font=('arial', 8),borderwidth=1,
            relief='groove',padx=15,anchor='w')
        namelevel.pack()

        makerlevel = Button(topframe,fg="white",bg='#376346',width=100,height=2,
            text="Produced by Kawasaki technologies",font=('arial', 8),command=lambda:self.to_web())
        makerlevel.grid(row=0, column=1)

        #adding a new frame to take all clickable links ------------------------------
        buttons = Frame(
            self,
            bg='#f5f3ed'
        )
        buttons.place(rely=0.07)

        Registration_button=Button(buttons,text="Registration",fg='black',font=("comic sans", 11),
        padx=5,state='normal'

        )
        Registration_button.grid(row=0, column=0, sticky='w', padx=10)
        
        Appointmemt_button=Button(buttons,text="Appointments",fg='black',font=("comic sans", 11),
            padx=5,command=lambda:self.Appointment()
        )
        Appointmemt_button.grid(row=0, column=1, sticky='w', padx=10)

        BedAdmin_button=Button(buttons,text="BedAmin",fg='black',font=("comic sans", 11),
            padx=5)
        BedAdmin_button.grid(row=0, column=2, sticky='w', padx=10)

        Master_button=Button(buttons,text="Masters",fg='black',font=("comic sans", 11),
            padx=5

        )
        Master_button.grid(row=0, column=3, sticky='w', padx=10)

        RADTM_button=Button(buttons,text="RADT Mastres",fg='black',font=("comic sans", 11),
            padx=5

        )
        RADTM_button.grid(row=0, column=4, sticky='w', padx=10)

        Report_button=Button(buttons,text="Reports",fg='black',font=("comic sans", 11),
            padx=5

        )
        Report_button.grid(row=0, column=5, sticky='w', padx=10)

        insurance_button=Button(buttons,text="Insurance",fg='black',font=("comic sans", 11),
            padx=5)
        insurance_button.grid(row=0, column=6, sticky='w', padx=10)
#----------------------------------end of buttons------------------------------------------------

    
#frame to get registration infomation----------------------------------------------

        Reg_getinfo_frame = Frame(self,bg=background_color)
        Reg_getinfo_frame.place(rely=0.13)

       
        Label(Reg_getinfo_frame,text='Title:').grid(row=2, column=0, pady=15, sticky='w')

        Label(Reg_getinfo_frame,text='Frist name:').grid(row=3, column=0, padx=5, sticky='w')

        Label(Reg_getinfo_frame,text='Surname:').grid(row=4, column=0, padx=5, sticky='w')

        Label(Reg_getinfo_frame,text='Parent/spouse name:').grid(row=5, column=0, padx=5, sticky='w')

        Label(Reg_getinfo_frame,text='Date of Birth:').grid(row=6, column=0, padx=5, sticky='w')
        
        Label(Reg_getinfo_frame,text='Sex:').grid(row=7, column=0, padx=5, sticky='w')

        Label(Reg_getinfo_frame,text='Religion:').grid(row=8, column=0, padx=5, sticky='w')

        Label(Reg_getinfo_frame,text='Occupation:').grid(row=9, column=0, padx=5, sticky='w')

        Label(Reg_getinfo_frame, text='Patient Catigory:').grid(row=10, column=0, padx=5, sticky='w')

        Label(Reg_getinfo_frame,text='Remark:').grid(row=11, column=0, padx=5, sticky='w')

        Reg_getinfo_frame.grid_rowconfigure(0, weight=1)
        Reg_getinfo_frame.grid_columnconfigure(0, weight=1)

           # Create the initial Entry widget
        global initial
        initial = StringVar()
        Entry(Reg_getinfo_frame,width=10,fg="black",cursor='arrow',bg=entryColror,textvariable=initial).grid(row=2, column=1)
         
        global firstname
        firstname = StringVar()
        Entry(Reg_getinfo_frame, width=35, fg="black",cursor='arrow', bg=entryColror,
            textvariable=firstname).grid(row=3, column=1)

        global lastname
        lastname = StringVar()
        Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',bg=entryColror,
            textvariable=lastname).grid(row=4, column=1)

        global Othername
        Othername = StringVar(); Entry(Reg_getinfo_frame, width=35,fg="black",cursor='arrow',bg=entryColror,
            textvariable=Othername).grid(row=5, column=1)

        global dateOfBirth
        dateOfBirth = StringVar(); Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',bg=entryColror,
            textvariable=dateOfBirth,
        ).grid(row=6, column=1)


        #**************GENDER SELECT***************************************************
        # Define a variable to store the selected option
        global gender
        gender = StringVar()
        Combobox(Reg_getinfo_frame, textvariable=gender, values=["MALE", "FEMALE", "COSTOM"]).grid(row=7, column=1)
        
        global relgion
        relgion = StringVar(); Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',bg=entryColror,
            textvariable=relgion).grid(row=8, column=1)


        global occupation
        occupation =StringVar(); Entry(Reg_getinfo_frame, width=35,fg="black",cursor='arrow', bg=entryColror,
            textvariable=occupation).grid(row=9, column=1)


        #************PATION CATIGORY SELECT*******************************************
         # Define a variable to store the selected option
        global patient_cat_option
        patient_cat_option = StringVar()
        Combobox(Reg_getinfo_frame, textvariable=patient_cat_option, 
                 values=["General Patients", "IN-Patients", "OUT-Patients", "Emergncy", "Padiatric","Geriatric"
                   "Surgical", "Chronic Disease Management", "Rehabilitation" ]).grid(row=10, column=1)
        #**********************************************************************************

        global Remark
        Remark = StringVar(); Text(Reg_getinfo_frame, width=20,height=3,fg="black",cursor='arrow',bg=entryColror,
            ).grid(row=11, column=1)

        Label(Reg_getinfo_frame,text='Age:').grid(row=2, column=2, pady=15, sticky='w')

        Label(Reg_getinfo_frame,text='Blood Group:').grid(row=3, column=2, padx=5, sticky='w')

        Label(Reg_getinfo_frame,text='Region:').grid(row=4, column=2, padx=5, sticky='w')

        Label(Reg_getinfo_frame,text='Place of Birth:').grid(row=5, column=2, padx=5, sticky='w')

        Label(Reg_getinfo_frame,text='Language:').grid(row=6, column=2, padx=5, sticky='w')

        global Age
        Age =StringVar()
        Entry(Reg_getinfo_frame,width=10,fg="black",cursor='arrow',bg=entryColror,
            textvariable= Age).grid(row=2, column=3)
        

        #***********BLOOD GROUP SELECT**********************
         # Define a variable to store the selected option
        global Bloodgrp
        Bloodgrp = StringVar()
        Combobox(Reg_getinfo_frame, textvariable=Bloodgrp, values=
                 ['A+', 'A-', 'B+', 'B-','AB+','AB-', 'O+', 'O-' ]).grid(row=3, column=3)
        #*******************************************************************

        #************************REGION SELECT*******************
         # Define a variable to store the selected option
        global Region
        Region = StringVar()
        Combobox(Reg_getinfo_frame, textvariable=Region, values=
                 ["ADAMAWA", "CENTER", "EAST", "FAR NORTH","LITTORAL",
                   "NORTH", "NORTHWEST", "SOUTH", "SOUTHWEST", "WEST" ]).grid(row=4, column=3)
        #*********************************************************

        global PlaceOfBirth
        PlaceOfBirth= StringVar()
        Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',
                bg='white',textvariable=PlaceOfBirth,).grid(row=5, column=3)


        #*****LANGUEGE SELECTION********************************************
        # Define a variable to store the selected option
        global language
        language = StringVar()
        Combobox(Reg_getinfo_frame, textvariable= language, values= ["ENGLISH", "FRENCH" ]).grid(row=6, column=3)
        #********************************************************************

        Label(Reg_getinfo_frame,text="Patient ID NO.",fg="black").grid(row=7, column=2)

        global patientID
        patientID=StringVar()
        Entry(Reg_getinfo_frame,fg='black',width=10, textvariable=patientID, bg=entryColror).grid(row=7, column=3)



        #****************************GETTING PHOTO OF VICTIM************************
    
        global patient_iamge

        patient_iamge=LabelFrame( #************create frame
            self,
            text="Patient Image",
            width=300,
            height=300
        )
        patient_iamge.place(rely=0.18, relx=0.65)

        capture=Button(self,text='CAPTURE',fg='red',bg='black',command=lambda:self.capture_camera_image())
        capture.place(rely=0.6, relx=0.89)

        register=Button(self,text='REGITER',fg='red',bg='black',command=lambda:self.register(), font=('arial', 15))
        register.place(rely=0.5, relx=0.89)


        #***************************************************************************


        Label(Reg_getinfo_frame,text='Local Adress',fg='black',
                   font=('arial', 12, 'italic'),anchor='w').grid(row=12)#idex 10

        Label(Reg_getinfo_frame,text='House Adress No.:',).grid(row=13, column=0)

        Label(Reg_getinfo_frame,text="Contact",fg='black').grid(row=14, column=0)

        Label(Reg_getinfo_frame,text="current region:",fg='black').grid(row=15, column=0)

        Label(Reg_getinfo_frame,text="Town/ City/ Village:",fg='black').grid(row=16, column=0)

        Label(Reg_getinfo_frame,text="E-mail Address:",fg='black').grid(row=13, column=2)

        Label(Reg_getinfo_frame,text="Office phone:",fg='black').grid(row=14, column=2)

        Label(Reg_getinfo_frame,text="Other Cantact:",fg='black').grid(row=15, column=2)

        Label(Reg_getinfo_frame,text="P.O.BOX No.:",fg='black').grid(row=16, column=2)

        global house_no
        house_no= StringVar()
        Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',bg=entryColror,
            textvariable=house_no).grid(row=13, column=1)

        global contact 
        contact= IntVar()
        Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',bg=entryColror,
            textvariable=contact).grid(row=14, column=1)

        #*****RESIDENT REGION SELECTION********************************************
        # Define a variable to store the selected option
        global residentRegion
        residentRegion = StringVar(Reg_getinfo_frame)
        Combobox(Reg_getinfo_frame, textvariable=residentRegion, values=
                 ["ADAMAWA", "CENTER", "EAST", "FAR NORTH","LITTORAL","NORTH", "NORTHWEST", "SOUTH", "SOUTHWEST", "WEST" ]).grid(row=15, column=1)
        #********************************************************************

        global currentCity
        currentCity=StringVar() 
        Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',bg=entryColror,
            textvariable=currentCity).grid(row=16, column=1)

        global e_mail
        e_mail= StringVar()
        Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',bg=entryColror,
            textvariable=e_mail).grid(row=13, column=3)

        global office_phone
        office_phone= IntVar()
        Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',bg=entryColror,
            textvariable=office_phone).grid(row=14, column=3)

        global other_phone
        other_phone=IntVar()
        Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',bg=entryColror,
              textvariable=other_phone).grid(row=15, column=3)

        global mail_box
        mail_box= StringVar()
        Entry(Reg_getinfo_frame,width=35,fg="black",cursor='arrow',bg=entryColror,
            textvariable=mail_box).grid(row=16, column=3)

        Label(Reg_getinfo_frame,text='Additional Information',fg='black',font=('arial', 12, 'italic'),
              anchor='w').grid(row=18, column=0, columnspan=1000, sticky="w")
        
        children = Reg_getinfo_frame.winfo_children()

        #giving all the styles to the children
        for index, child in enumerate(children):
            for x in range(10, 20):
                if index==x:
                    child.configure()
                else:
                    
                    child.grid_configure(pady=5, padx=15, sticky='w') 

    def new_method(self):
        return 'white' 

#---------------end frame-----------------------------------------------------------------------


#----------------------------- functions---------------------------------------------------
    def Appointment(self):
        import appointmemts as apt
        apt.Appointments()
        self.destroy()
    
    def register (self):
        patientId = patientID.get()
        firstName= firstname.get()
        lastName=lastname.get()
        Initial=initial.get()
        othername=Othername.get()
        DOB=dateOfBirth.get()
        Gender=gender.get()
        Relgion=relgion.get()
        job=occupation.get()
        type=patient_cat_option.get()
        more=Remark.get()
        age=Age.get()
        blood=Bloodgrp.get()
        region=Region.get()
        POB=PlaceOfBirth.get()
        Languuage=language.get()
        houseNo=house_no.get()
        Contact=contact.get()
        Residentregion=residentRegion.get()
        Currentcity=currentCity.get()
        Email=e_mail.get()
        OfficePhone=office_phone.get()
        OtherPhone=other_phone.get()
        Mail=mail_box.get()

        process_registration(patientId, firstName, lastName, Initial, othername,
        DOB, Gender, Relgion,job,type, more, age, blood, region, POB, Languuage,
        houseNo, Contact, Residentregion, Currentcity, Email, OfficePhone,
        OtherPhone, Mail)
      

    def to_web(self):
        import webbrowser as web
        web.open('hospital_DB_downlad.html')
    
    def image_placing(patient_image):
        
        pass

    def capture_camera_image(patient_image):
            
            capture = cv2.VideoCapture(0)  # 0 represents the default camera
                        
            # Check if the camera is opened successfully
            if not capture.isOpened():
                print("Failed to open camera")
                return
            
            
            ret, frame = capture.read()  # Read the frame from the camera
            ret =Canvas(
                patient_iamge
            )
            # Check if the frame was successfully read
            if not ret:
                print("Failed to capture frame")
                return

            cv2.imshow("Camera Image", frame)  # Display the captured image
            
            

            # Save the image to a file
            cv2.imwrite("camera_image.jpg", frame)

            capture.release()  # Release the camera
            
            #cv2.destroyAllWindows()  # Close the image window
   
#------------------------------------------------------------------------------------------------

def run():
    root = Registration()
    root.mainloop()


if __name__ == "__main__":
    run()
