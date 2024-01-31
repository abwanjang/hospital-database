from tkinter import *
from tkinter import ttk
import sqlite3
import random
import main as main
#import PIL
#from tkinter import messagebox
#from flask import Flask


class Appointments(Tk):
    def __init__(self):
        super().__init__()
        screen_width = int(self.winfo_screenwidth())
        screen_height = int(self.winfo_screenheight())
        self.resizable(False, False)

        # setting window size to fit screen
        self.configure(width=screen_width, height=screen_height, bg='#5454d1')
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

        namelevel = Label(
            canvas,
            fg="white",
            bg='#373d63',
            width=55,
            height=2,
            text="HOSPITAL MANAGEMENT INFORMATION SYSTEM",
            font=('arial', 8),
            borderwidth=1,
            relief='groove',
            padx=15,
            anchor='w'
        )
        namelevel.pack()

        makerlevel = Label(
            topframe,
            fg="white",
            bg='#376346',
            width=100,
            height=2,
            text="Produced by Kawasaki technologies",
            font=('arial', 8)
        )
        makerlevel.grid(row=0, column=1)

        #adding a new frame to take all clickable links ------------------------------
        buttons = Frame(
            self,
            bg='#f5f3ed'
        )
        buttons.place(rely=0.07)

        Registration_button=Button(
            buttons,
            text="Registration",
            fg='black',
            font=("comic sans", 11),
            padx=5,
            command=lambda:self.registerPatient()

        )
        Registration_button.grid(row=0, column=0, sticky='w', padx=10)
        
        Appointmemt_button=Button(
            buttons,
            text="Appointments",
            fg='black',
            font=("comic sans", 11),
            padx=5,
            state='normal'

        )
        Appointmemt_button.grid(row=0, column=1, sticky='w', padx=10)

        BedAdmin_button=Button(
            buttons,
            text="BedAmin",
            fg='black',
            font=("comic sans", 11),
            padx=5

        )
        BedAdmin_button.grid(row=0, column=2, sticky='w', padx=10)

        Master_button=Button(
            buttons,
            text="Masters",
            fg='black',
            font=("comic sans", 11),
            padx=5

        )
        Master_button.grid(row=0, column=3, sticky='w', padx=10)

        RADTM_button=Button(
            buttons,
            text="RADT Mastres",
            fg='black',
            font=("comic sans", 11),
            padx=5

        )
        RADTM_button.grid(row=0, column=4, sticky='w', padx=10)

        Report_button=Button(
            buttons,
            text="Reports",
            fg='black',
            font=("comic sans", 11),
            padx=5

        )
        Report_button.grid(row=0, column=5, sticky='w', padx=10)

        insurance_button=Button(
            buttons,
            text="Insurance",
            fg='black',
            font=("comic sans", 11),
            padx=5

        )
        insurance_button.grid(row=0, column=6, sticky='w', padx=10)
#----------------------------------end of buttons------------------------------------------------

#----------------field frame---------------------------------------------------------------------
        appointments_fields = Frame(
            self, 
            bg='white',
            width=400, height=100
        )
        appointments_fields.place(rely=0.14, anchor='n', relx=0.41)


        #********seach bar for patient id to check appointments******************************

        #---------------------------water mark om search---------------------------------------

        def on_search_entry_click(event):
            if search.get() == "Search...":
                search.delete(0, 'end')
                search.config(fg='gray')
        
        def on_search_entry_leave(event):
            if search.get()=="":
                search.insert(0, "Search...")
                search.config(fg='gray')
#--------------------------------------------------------------------------------------

        search = Entry(
        appointments_fields,
        width=15,
        font=('arial', 20, 'bold'),
        fg="gray",
        bg='lightgray',  # Set a different background color for the entry widget
        textvariable='search'
        )
        search.insert(0, "Search...")  # Set the default text
        search.bind('<FocusIn>', on_search_entry_click)
        search.bind('<FocusOut>', on_search_entry_leave)

        search.grid(row=1, column=3, pady=30)
        
        #*****seach button********************
        search_button = Button(
        appointments_fields,
        text='Search',
        font=('arial', 12, 'bold'),
        cursor='hand2',
        height=int(0.6),
        fg='lightgray',
        activebackground='blue',
        activeforeground='purple',
        bg='green'  # Set a different background color for the entry widget
        )
        search_button.grid(row=1, column=4)
#*************************************************************************************

#***********seting entry feilds*******************************************************
        patientsID=Label(
            appointments_fields,
            text='patientID',
            fg='black',
            font=('arial', 11,) 
        )
        patientsID.grid(row=3, column=0)

        patientsID=Entry(
            appointments_fields,
            text='patientID',
            fg='black',
            font=('arial', 11,),
            textvariable='patientsID',
            width=15
        )
        patientsID.grid(row=3, column=1)


        date=Label(
            appointments_fields,
            text='Appointment Date',
            fg='black',
            font=('arial', 11,)
        )
        date.grid(row=3, column=2)

        dateOfaAppointment=Entry(
            appointments_fields,
            text='patientID',
            fg='black',
            font=('arial', 11,),
            textvariable='dateOfaAppointment',
            width=15
        )
        dateOfaAppointment.grid(row=3, column=3)


        time=Label(
            appointments_fields,
            text='Appointment Time',
            fg='black',
            font=('arial', 11,)
        )
        time.grid(row=3, column=4)

        timeOfAppointment=Entry(
            appointments_fields,
            text='patientID',
            fg='black',
            font=('arial', 11,),
            textvariable='timeOfAppointment',
            width=15
        )
        timeOfAppointment.grid(row=3, column=5)


        docId=Label(
            appointments_fields,
            text='Doctor ID',
            fg='black',
            font=('arial', 11,)
        )
        docId.grid(row=2, column=0)

        DoctorID=Entry(
            appointments_fields,
            text='patientID',
            fg='black',
            font=('arial', 11,),
            textvariable='DoctorID',
            width=15
        )
        DoctorID.grid(row=2, column=1)


        docname=Label(
            appointments_fields,
            text='Doctor name',
            fg='black',
            font=('arial', 11,)
        )
        docname.grid(row=2, column=2)

        DoctorName=Entry(
            appointments_fields,
            text='patientID',
            fg='black',
            font=('arial', 11,),
            textvariable='DoctorName',
            width=15
        )
        DoctorName.grid(row=2, column=3)


        type=Label(
            appointments_fields,
            text='Appointment Type',
            fg='black',
            font=('arial', 11,)
        )
        type.grid(row=2, column=4)

        AppType=Entry(
            appointments_fields,
            fg='black',
            font=('arial', 11,),
            textvariable='AppType',
            width=15
        )
        AppType.grid(row=2, column=5)

        facility=Label(
            appointments_fields,
            text='Facility',
            fg='black',
            font=('arial', 11,)
        )
        facility.grid(row=4, column=0)

        Facility=Entry(
            appointments_fields,
            fg='black',
            font=('arial', 11,),
            textvariable='Facility',
            width=15
        )
        Facility.grid(row=4, column=1)


        notes=Text(
            appointments_fields,
            fg='black',
            font=('arial', 11,),
            #textvariable='notes',
            width=100,
            height=15
        )
        notes.grid(row=5, column=1, columnspan=5)







#*******************************************************************************

#---------------------------------grid styles-------------------------------
        children = appointments_fields.winfo_children()

        #giving all the styles to the children
        for child in children:
            
            child.grid_configure(pady=5, padx=15, sticky='w')

#---------------------------------------------------------------------------




#-----------------------------button functions---------------------
    def registerPatient(self):
        main.Registration()
        self.destroy()

#----------------------------


def run():
    root = Appointments()
    root.mainloop()


if __name__ == "__main__":
    run()
