import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='one_stop_student_portal'
)
mycursor = mydb.cursor()

# Function to collect data from entries and insert into the database
def collect_data():
    course_codes = [entry.get() for entry in course_entries]
    credit_hours = [entry.get() for entry in credit_hour_entries]
    grades = [entry.get() for entry in grade_entries]

    for i in range(7):
        course_code = course_codes[i]
        print("Course code:", course_code)
        credit_hour = credit_hours[i]
        print("Credit hour:", credit_hour)
        grade = grades[i]
        print("Grade:", grade)

        # Insert data into the database
        sql = "INSERT INTO cgpa_data (course_code, credit_hour, `grade`) VALUES (%s, %s, %s)"
        values = (course_code, credit_hour, grade)
        mycursor.execute(sql, values)
        mydb.commit()

# Function to calculate CGPA
def calculate_cgpa():
    total_credit_hours = 0
    total_grade_points = 0

    for i in range(7):
        credit_hour_entry = credit_hour_entries[i].get()
        grade = grade_entries[i].get()

        try:
            credit_hour = int(credit_hour_entry)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for credit hours.")
            return

        grade_points = 0.0

        if grade.upper() == 'A+':
            grade_points = 4.0
        elif grade.upper() == 'A':
            grade_points = 3.8
        elif grade.upper() == 'A-':
            grade_points = 3.67
        elif grade.upper() == 'B+':
            grade_points = 3.3
        elif grade.upper() == 'B':
            grade_points = 3.0
        elif grade.upper() == 'B-':
            grade_points = 2.7
        elif grade.upper() == 'C+':
            grade_points = 2.3
        elif grade.upper() == 'C':
            grade_points = 2.0
        elif grade.upper() == 'C-':
            grade_points = 1.7
        elif grade.upper() == 'D':
            grade_points = 1.0
        else:
            grade_points = 0.0

        total_credit_hours += credit_hour
        total_grade_points += (credit_hour * grade_points)

    if total_credit_hours == 0:
        cgpa = 0.0
    else:
        cgpa = total_grade_points / total_credit_hours

    total_CGPA_var.set(f'Total CGPA: {cgpa:.2f}')
    total_credit_hour_var.set(f'Total Credit Hour: {total_credit_hours}')

# GUI Setup
root = tk.Tk()
root.title("CGPA Calculator")
root.geometry('600x500')
root.resizable(False, False)

# Apply a theme for a modern look
style = ttk.Style(root)
style.theme_use("clam")

# Create and configure frames
frame = ttk.Frame(root, padding="20", style="My.TFrame")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Header
label = ttk.Label(frame, text="CGPA CALCULATOR", font=("Arial", 20, "bold"), style="Header.TLabel")
label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

# Content
labels = ["Course Code", "Credit Hour", "Grade"]
for i, text in enumerate(labels):
    ttk.Label(frame, text=text, font=("Arial", 14), style="InputLabel.TLabel").grid(row=1, column=i, padx=10, pady=5)

course_entries = [ttk.Entry(frame, width=15, font=("Arial", 12)) for _ in range(7)]
for i, entry in enumerate(course_entries):
    entry.grid(row=i + 2, column=0, padx=10, pady=5)

credit_hour_entries = [ttk.Entry(frame, width=15, font=("Arial", 12)) for _ in range(7)]
for i, entry in enumerate(credit_hour_entries):
    entry.grid(row=i + 2, column=1, padx=10, pady=5)

grade_entries = [ttk.Entry(frame, width=15, font=("Arial", 12)) for _ in range(7)]
for i, entry in enumerate(grade_entries):
    entry.grid(row=i + 2, column=2, padx=10, pady=5)

calculate_button = ttk.Button(frame, text="Calculate CGPA", command=calculate_cgpa, style="CalcButton.TButton")
calculate_button.grid(row=9, column=0, columnspan=3, pady=(20, 0))

# Display Results
result_frame = ttk.Frame(frame)
result_frame.grid(row=10, column=0, columnspan=3)

total_CGPA_var = tk.StringVar()
total_credit_hour_var = tk.StringVar()

ttk.Label(result_frame, textvariable=total_CGPA_var, font=("Arial", 14, "bold"), style="ResultLabel.TLabel").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(result_frame, textvariable=total_credit_hour_var, font=("Arial", 14, "bold"), style="ResultLabel.TLabel").grid(row=1, column=0, padx=10, pady=10)

# Styling
style.configure("My.TFrame", background="#FFD700")  # Light Goldenrod Yellow
style.configure("InputLabel.TLabel", foreground="#333333")  # Dark Gray
style.configure("Header.TLabel", foreground="#0066cc")  # Royal Blue
style.configure("CalcButton.TButton", font=("Arial", 14), background="#4CAF50", foreground="white")  # Green
style.configure("ResultLabel.TLabel", foreground="#FF4500")  # Orange Red

root.mainloop()
