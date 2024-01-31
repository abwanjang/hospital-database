import sqlite3
import random
 
def process_registration(patientId, firstName, lastName, Initial, othername,
        DOB, Gender, Religion, job, type, more, age, blood, region, POB, Language,
        houseNo, Contact, Residentregion, Currentcity, Email, OfficePhone,
        OtherPhone, Mail):
    # Process the received data
    print("Received data in module2:")
    print("Patient ID:", patientId)
    print("First Name:", firstName)
    print("Last Name:", OfficePhone)

    con = sqlite3.connect("hospitalDataBase.db")
    table_create = """
    CREATE TABLE IF NOT EXISTS hospitalDataBase (
        PATIENT_ID TEXT, 
        FIRST_NAME TEXT, 
        LAST_NAME TEXT, 
        INITIAL TEXT, 
        OTHERNAME TEXT,
        DATE_OF_BIRTH TEXT, 
        SEX TEXT, 
        RELIGION TEXT,
        OCCUPATION TEXT, 
        PATIENT_CAT_OPTION TEXT, 
        REMARK TEXT, 
        AGE INT, 
        BLOODGROUP TEXT, 
        REGION TEXT, 
        PLACE_OF_BIRTH TEXT, 
        LANGUAGE TEXT,
        HOUSE_NO TEXT,
        CONTACT INT,
        RESIDENT_REGION TEXT,
        CURRENT_CITY TEXT,
        EMAIL TEXT,
        OFFICE_PHONE INT,
        OTHER_PHONE INT,
        MAIL_BOX TEXT
    )
    """
    con.execute(table_create)

    table_inputs = """
    INSERT INTO hospitalDataBase (
        PATIENT_ID, 
        FIRST_NAME, 
        LAST_NAME, 
        INITIAL, 
        OTHERNAME,
        DATE_OF_BIRTH, 
        SEX, 
        RELIGION, 
        OCCUPATION, 
        PATIENT_CAT_OPTION, 
        REMARK, 
        AGE, 
        BLOODGROUP, 
        REGION, 
        PLACE_OF_BIRTH, 
        LANGUAGE,
        HOUSE_NO,
        CONTACT,
        RESIDENT_REGION,
        CURRENT_CITY,
        EMAIL,
        OFFICE_PHONE,
        OTHER_PHONE,
        MAIL_BOX
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """

    table_tupples = (patientId, firstName, lastName, Initial, othername,
        DOB, Gender, Religion, job, type, more, age, blood, region, POB, Language,
        houseNo, Contact, Residentregion, Currentcity, Email, OfficePhone,
        OtherPhone, Mail)

    cursor = con.cursor()
    cursor.execute(table_inputs, table_tupples)
    con.commit()
    con.close()