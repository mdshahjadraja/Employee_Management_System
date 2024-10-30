import mysql.connector
from tkinter import *
from tkinter import messagebox

# Establish MySQL connection
def connect_db():
    try:
        global conn
        global cursor
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@24Mca20291",
            database="CompanyDB",
            port=3306
        )
        cursor = conn.cursor()
        messagebox.showinfo("Connection Status", "Connected to the MySQL database!")
    except mysql.connector.Error as err:
        messagebox.showerror("Connection Error", f"Error: {err}")

# Add employee to the database
def add_employee():
    name = entry_name.get()
    position = entry_position.get()
    salary = entry_salary.get()
    date_hired = entry_date.get()

    if not name or not position or not salary or not date_hired:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return
    
    try:
        cursor.execute(
            "INSERT INTO employees (name, position, salary, date_hired) VALUES (%s, %s, %s, %s)",
            (name, position, salary, date_hired)
        )
        conn.commit()
        messagebox.showinfo("Success", "Employee added successfully!")
        clear_fields()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Clear input fields
def clear_fields():
    entry_name.delete(0, END)
    entry_position.delete(0, END)
    entry_salary.delete(0, END)
    entry_date.delete(0, END)

# GUI setup
root = Tk()
root.title("Employee Management System")

# Connect to database button
btn_connect = Button(root, text="Connect to Database", command=connect_db)
btn_connect.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entry fields
Label(root, text="Name:").grid(row=1, column=0, sticky=W)
entry_name = Entry(root, width=30)
entry_name.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Position:").grid(row=2, column=0, sticky=W)
entry_position = Entry(root, width=30)
entry_position.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Salary:").grid(row=3, column=0, sticky=W)
entry_salary = Entry(root, width=30)
entry_salary.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Date Hired (YYYY-MM-DD):").grid(row=4, column=0, sticky=W)
entry_date = Entry(root, width=30)
entry_date.grid(row=4, column=1, padx=10, pady=5)

# Add Employee button
btn_add = Button(root, text="Add Employee", command=add_employee)
btn_add.grid(row=5, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()