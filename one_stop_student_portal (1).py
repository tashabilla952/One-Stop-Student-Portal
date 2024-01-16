#firstly, import tkinter as tk, 
#and then import tkinter as ttk to use the comobox for gender 
#and lastly import mysql.connector to make sure it will connect to database
import tkinter as tk
from tkinter import ttk
import mysql.connector
# Connect to your MySQL database
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_cgpa_protal"
    )

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()


def student_data_collect():
    student_name = student_name_entry.get()
    print("NAME: ", student_name)
    student_id = int (student_id_entry.get())
    print("STUDENT ID: ", student_id)
    programme_code = (programme_code_combobox.get())
    print ("PROGRAMME CODE: ", programme_code )
    semester = int (semester_combobox.get())
    print(" SEMESTER : ", semester)

    for  widget in enter_button.winfo_children ():
        widget.update ()


def delete_data ():
    print ("Data has been deleted") #for deleting data
    student_name_entry.delete (0, tk.END)
    student_id_entry.delete(0, tk.END)
    programme_code_combobox.set('')
    semester_combobox.set ('')


    for  widget in course_outline.winfo_children ():
        widget.destroy ()

#In this it will determine the course outline for student. 
#in this part after student choose their programe code and the semester they are in, they need to click to the 'SHOW COURSE OUTLINE BUTTON'
#after that they can see the outline course for the code programme they choose and semester they choose
def course_outline_data ():
    programme_code = programme_code_combobox.get()
    semester = semester_combobox.get()

    if  programme_code == "IM110" and semester == "1" :
        course_outline_data = [
            "FUNDAMENTAL OF ISLAM (CTU101)",
            "FUNDAMENTALS OF MANAGEMENT (MGT162)",
            "STUDY SKILLS (UED102)",
            "INTEGRATED LANGUAGE SKILLS I (ELC121)",
            "NATIONAL KESATRIA I (HBU111)",
            "INTRODUCTION TO INFORMATION SKILLS (IMD111)",
            "INTRODUCTION TO INFORMATION MANAGEMENT (IMD112)",
            "INFORMATION AND COMMUNICATION TECHNOLOGY APPLICATION (IMD113)"
        ]
    
    elif programme_code == "IM110" and semester == "2" :
        course_outline_data = [
            "VALUES AND CIVILIZATION (CTU152)",
            "INTEGRATED LANGUAGE SKILLS II (ELC151)",
            "NATIONAL KESATRIA II (HBU121)",
            "COMMUNICATION SKILLS FOR INFORMATION PROFESSIONALS (IMD121)",
            "INTRODUCTION TO SCHOOL RESOURCE CENTER (IMD122)",
            "FOUNDATION OF RECORDS MANAGEMENT (IMD123)",
            "ACCESS TO INFORMATION (IMD124)"
        ] 
        
    if programme_code == "IM110"  and semester == "3":
         course_outline_data = [
            "ISLAMIC INFORMATION MANAGEMENT (CTU264)",
            "INTEGRATED LANGUAGE SKILLS III (ELC231)",
            "NATIONAL KESATRIA III (HBU131)",
            "INFRASTRUCTIONAL MEDIA APPLICATION (IMD211)",
            "ORGANIZATION OF INFORMATION (IMD231)",
            "ELCTRONIC PUBLISHING (IMD214)"
        ]
    elif programme_code == "IM110"  and semester == "4":
        course_outline_data = [ 
            "SOCIAL MEDIA LITERACY (IMD221)",
            "TECHNICAL SUPPORT SERVICES AND MAINTENANCE FOR INFORMATION AGENCIES (IMD222)",
            "INTRODUCTION TO CATALOGING (IMD223)",
            "MANAGEMENT OF RECORDS CENTER (IMD224)",
            "INFORMATION TECHNOLOGY APPLICATION IN INFORMATION AGENCIES (IMD225)",
            "MULTIMEDIA FOR INFORMATION PRESENTATION (IMD226)",
            "PROMOTION OF INFORMATION PRODUCT AND SERVICES (IMD227)"
        ]
    if programme_code == "IM110"  and semester == "5":
        course_outline_data =[
            "FUNDAMENTALS OF ENTREPRENEURSHIP (ENT300)",
            "INTRODUCTION TO WEB CONTENT MANAGEMENT AND DESIGN (IMD311)",
            "REFERENCE AND INFORMATION SERVICES FOR INFORMATION AGENCIES (IMD312)",
            "FOUNDATION OF ARCHIVES (IMD313)",
            "EXTENSION SERVICES FOR INFORMATION AGENCIES (IMD314)",
            "MANAGEMENT OF LIBRARIES AND RESOURCE CENTER (IMD315)"
        ]
    elif programme_code == "IM144"  and semester == "1":
        course_outline_data = [
            "FUNDAMENTAL OF ISLAM (CTU101)",
            "INTEGRATED LANGUAGE SKILLS I (ELC121)",
            "NATIONAL KESATRIA I (HBUIII)",
            "INTRODUCTION TO INFORMATION SKILLS (IMC111)",
            "INTRODUCTION TO INFORMATION MANAGEMENT (IMC112)",
            "INFORMATION AND COMMUNICATION TECHNOLOGY APPLICATION (IMC113)"
            "FUNDAMENTALS OF MANAGEMENT (MGT162)",
            "STUDY SKILLS (UED102)"
        ]
    if programme_code == "IM144"  and semester == "2":
        course_outline_data =[
            "VALUES AND CIVILIZATION (CTU152)",
            "INTEGRATED LANGUAGE SKILLS II (ELC151)",
            "NATIONAL KESATRIA II (HBU121)",
            "ORGANIZATION AND ACCESS TO INFORMATION (IMC151)",
            "INTRODUCTION TO LIBRARY MANAGEMENT (IML152)",
            "FUNDAMENTAL OF DATA MANAGEMENT (IML153)",
            "COMMUNICATION SKILLS FOR INFORMATION PROFESSIONAL (IML155)"
        ]
    elif programme_code == "IM144"  and semester == "3":
        course_outline_data = [
            "ISLAMIC INFORMATION MANAGEMENT (CTU264)",
            "INTEGRATED LANGUAGE SKILLS III (ELC231)",
            "NATIONAL KESATRIA III (HBU131)",
            "DIGITAL PRESERVATION IN LIBRARY ENVIRONMENT (IML206)",
            "INFORMATION SECURITY FOR LIBRARIES (IML207)",
            "PROGRAMMING FOR LIBRARIES (IML208)",
            "DESCRIPTIVE CATALOGING (IML209)"
        ]
    if programme_code == "IM144"  and semester == "4":
        course_outline_data = [
            "METADATA DEVELOPMENT IN INFORMATION ENVIRONMENT (IMC258)",
            "INTRODUCTION TO WEB CONTENT DEVELOPMENT (IML254)",
            "SUBJECT CATALOGING AND CLASSIFICATION (IML255)",
            "MULTIMEDIA AND DIGITAL PUBLISHING IN LIBRARIES (IML256)",
            "LIBRARIES AND CUSTOMERS (IML257)",
        ]
    elif programme_code == "IM144"  and semester == "5":
        course_outline_data = [
            "FUNDAMENTALS OF ENTREPRENEURSHIP (ENT300)",
            "LIBRARY OUTREACH (IML301)",
            "DIGITAL REFERENCE AND INFORMATION ANALYTICS (IML302)",
            "INNOVATION IN LIBRARIES (IML303)",
            "LIBRARY FIELDWORKS (IML310)"
        ]
    if programme_code == "IM244"  and semester == "3":
        course_outline_data = [
            "PHILOSOPHY AND CURRENT ISSUES (CTU552)",
            "ENGLISH FOR CRITICAL ACADEMIC WRITING (ELC501)",
            "PRINCIPLES OF ENTREPRENEURSHIP (ENT530)", 
            "THIRD LANGUAGE (I)",
            "INFORMATION SOURCES & SERVICES IN SOCIAL (IML503)",
            "INFORMATION SOURCES & SERVICES IN SCINCE AND TECHNOLGY (IML504)",
            "ORGANIZATION OF INFORMATION: DESCRIPTIVE CATALOGING (IML507)",
            "SUBJECT ELECTIVE 1",
            "SUBJECT ELECTIVE 2"
        ]
    elif programme_code == "IM244"  and semester == "4":
        course_outline_data = [
            "VALUES AND CIVILIZATION II (CTU554)",
            "ENGLISH FOR REPORT WRITING (EWC661)",
            "THRID LANGUAGE (II)",
            "PUBLIC RELATIONS IN INFORMATION WORK (IML553)",
            "COMPUTERIZED TEXTUAL INFORMATION MANAGEMENT (IML554)",
            "ORGANIZATION OF INFORMATION: SUBJECT CATALOGING AND CLASSIFICATION (IML555)",
            "SUBJECT ELECTIVE 3",
            "SUBJECT ELECTIVE 4"
        ]
    if programme_code == "IM244"  and semester == "5":
        course_outline_data =[
            "ENGLISH FOR MEETINGS AND DISCUSSIONS (EWC663)",
            "THIRD LANGUAGE (III)",
            "PUBLICATION AND PRODUCTION OF INFORMATION MATERIALS (IML601)",
            "ORGANIZATION OF INFORMATION: ABSTRACTING AND INDEXING (IML605)",
            "CHILDREN'S LIBRARIANSHIP (IML606)",
            "SUBJECT ELECTIVE 5",
            "SUBJECT ELECTIVE 6"
        ]
    elif programme_code == "IM244"  and semester == "6":
        course_outline_data = [
            "ENGLISH EXIT TEST (EET699)",
            "EVALUATION OF INFORMATION SERVICES (IMC651)",
            "DIGITAL LIBRARIES (IML651)",
            "ORGANIZATION OF INFORMATION: COMPUTERIZED CATALOGING (IML655)",
            "PLANNING AND DESIGN OF LIBRARIES AND INFORMATION CENTERS (IML656)",
            "SUBJECT ELECTIVE 7",
            "SUBJECT ELECTIVE 8"
        ]

    print ("Course outline : ", course_outline_data )
    course_outline_data_str = "\n".join(course_outline_data)
    for widget in course_outline.winfo_children ():
        widget.destroy ()
#in this part we use for loop to make sure the attribute student choose will loop the data that we state only
    
    tk.Label(course_outline,  bg= "light blue").grid(row=0, column=0, pady= 5)
    for i, course in enumerate (course_outline_data, start=1) :
            tk.Label (course_outline, text= f"{i}. {course}", font= ("Times New Roman",  9), bg="light blue").grid (row=i, column=0, sticky="w")
        
    sql = "INSERT INTO student_protal (student_name, student_id, programme_code, semester) VALUES (%s, %s, %s, %s)"
    val= (student_name, student_id, programme_code, semester )


    mycursor.execute(sql, val)

    # Commit the changes to the database
    mydb.commit()

    # Close the database connection
    mydb.close()  

# Create GUI
root = tk.Tk()
root.configure(background="light blue")
root.title("ONE STOP STUDENT PROTAL")
root.geometry('760x710')
# To center the root on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# the big title for the protal page
label = tk.Label(root, text='ONE STOP STUDENT PROTAL', font=("Baskerville Old Face", '14', "bold"), bg="light blue")
label.grid(row=0, column=2, padx=10, pady=10, sticky= 'nsew')

frame = tk.Frame(root, bg="light blue")
frame.grid(row=1, column=0)

student_name = tk.Label(text="NAME", font=("Times New Roman", 11), bg= "light blue" )
student_name.grid(row=1, column=2, padx=(0,5))
student_name_entry = tk.Entry (width=27)
student_name_entry.grid(row=2, column=2)

student_id = tk.Label(text="STUDENT ID", font=("Times New Roman", 11), bg= "light blue" )
student_id.grid(row=3, column=2, padx=(0,5))
student_id_entry = tk.Entry(width=27)
student_id_entry.grid(row=4, column=2)

programme_code = tk.Label(text="PROGRAMME CODE", font=("Times New Roman", 11), bg= "light blue")
programme_code.grid (row=5, column=2, padx=(0,5))
programme_code_combobox = ttk.Combobox (width=25, values= ["IM110", "IM144", "IM244"]) #looping for only IM student
programme_code_combobox.grid (row=6, column=2)

semester = tk.Label(text="SEMESTER", font=("Times New Roman", 11), bg= "light blue")
semester.grid (row=7, column=2, padx=(0,5) )
semester_combobox = ttk.Combobox (width=25, values= ["1", "2", "3", "4","5","6"]) 
semester_combobox.grid(row=8, column=2)

#creating course_outline_button to show the main time course outline for student
course_outline_button = tk.Button (text= "SHOW COURSE OUTLINE", font=("Times New Roman", 11), bg="gray", command= course_outline_data)
course_outline_button.grid(row=9,column=2, pady=20)
course_outline_button.config

#create course outline frame for student to see their course outline
course_outline = tk.LabelFrame (text= "COURSE OUTLINE" , font=("Times New Roman", 11), bg= "light blue")
course_outline.grid(row=10, column=2, padx=20, pady=10)

course_outline.grid_propagate (False) # we use this format to make sure the frame will stay at the place even there is no content in it
course_outline.config (width=600, height=266)

# delete button. if user click to this button all of the data will be delete
delete_button = tk.Button( text="DELETE", font=("Times New Roman", 11), bg="gray", command=delete_data)
delete_button.grid(row=20, column=2, pady=10)
delete_button.config

#submit button to complete the process
enter_button = tk.Button (text= "SUBMIT",font=("Times New Roman", 11), bg="gray", command=student_data_collect )
enter_button.grid(row=21,column=2, pady=10)
enter_button.config

# Configure grid weights to make the frames expandable
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

root.mainloop()
