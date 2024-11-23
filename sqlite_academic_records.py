from tkinter import *
from PIL import Image, ImageTk  # Importing PIL for future image use
from tkinter import messagebox  # For showing error messages
import sqlite3  # For SQLite database connection

# Initialize the main window
root = Tk()
root.title("Database")  # Set the window title
root.geometry("400x400")  # Set the window size

# Connect to the SQLite database or create it
conn = sqlite3.connect('student_data.db')
c = conn.cursor()

# Function to check if any input field is empty
def isempty():
    if f_name.get() == "" or l_name.get() == "" or college_name.get() == "" or degree.get() == "" or major.get() == "" or graduation_year.get() == "":
        return False
    return True

# Function to submit a new record to the database
def submit():
    if isempty() == False:
        messagebox.showwarning("Error", "Blank fields not allowed")  # Show warning for blank fields
    else:
        conn = sqlite3.connect("student_data.db")
        cur = conn.cursor()

        # Insert data into the database
        cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :college_name, :degree, :major, :graduation_year)",
                    {
                        'f_name': f_name.get(),
                        'l_name': l_name.get(),
                        'college_name': college_name.get(),
                        'degree': degree.get(),
                        'major': major.get(),
                        'graduation_year': graduation_year.get()
                    })

        conn.commit()  # Commit the changes
        conn.close()  # Close the database connection

        # Clear the input fields after submission
        f_name.delete(0, END)
        l_name.delete(0, END)
        college_name.delete(0, END)
        degree.delete(0, END)
        major.delete(0, END)
        graduation_year.delete(0, END)

# Function to display all records from the database
def show():
    conn = sqlite3.connect("student_data.db")
    cur = conn.cursor()

    # Fetch all records from the table
    cur.execute("SELECT * FROM addresses")
    records = cur.fetchall()

    # Display the records in the GUI
    gridrow = 9
    for i in range(len(records)):
        details = ""
        for record in records[i]:
            details += str(record) + " "
        gridrow += 1
        myLabel = Label(root, text=details)
        myLabel.grid(row=gridrow, column=0, columnspan=3)

    conn.commit()  # Commit changes
    conn.close()  # Close the database connection

# Uncomment and run this block once to create the table
'''
conn.execute("""CREATE TABLE addresses(
            f_name text,
            l_name text,
            college_name text,
            degree text,
            major text, 
            graduation_year int
            )""")
'''

# Create entry widgets for user input
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
college_name = Entry(root, width=30)
college_name.grid(row=2, column=1, padx=20)
degree = Entry(root, width=30)
degree.grid(row=3, column=1, padx=20)
major = Entry(root, width=30)
major.grid(row=4, column=1, padx=20)
graduation_year = Entry(root, width=30)
graduation_year.grid(row=5, column=1, padx=20)

# Create labels for the input fields
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
college_name_label = Label(root, text="Name Of College/Uni")
college_name_label.grid(row=2, column=0)
degree_label = Label(root, text="Degree")
degree_label.grid(row=3, column=0)
major_label = Label(root, text="Major/Field Of Study")
major_label.grid(row=4, column=0)
graduation_year_label = Label(root, text="Year Of Graduation")
graduation_year_label.grid(row=5, column=0)

# Create button to submit a new record
submit = Button(root, text="Add Record", command=submit)
submit.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create button to display all records
show = Button(root, text="Show Record", command=show)
show.grid(row=7, column=0, columnspan=2, padx=10, ipadx=100)

# Close the initial database connection
conn.close()
# Start the main event loop
root.mainloop()
