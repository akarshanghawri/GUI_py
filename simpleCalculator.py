from tkinter import *

root = Tk()
root.title("Simple Calculator")  # Window title

# Entry widget for the display
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# adding a frame 
frame = LabelFrame(root,text="calculator",padx=10,pady=10)
frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Function to handle number button clicks
def button_click(number):
    current = e.get()      # Get the current text in the entry
    e.delete(0, END)       # Clear the entry
    e.insert(0, str(current) + str(number))  # Append the clicked number

# Function to clear the display
def button_clear():
    e.delete(0, END)

# Function to set up addition
def button_add():
    first_number = e.get()      # Get the current number in entry
    global f_num
    global operation
    operation = "addition"      # Set operation to addition
    f_num = int(first_number)   # Store first number globally
    e.delete(0, END)            # Clear the entry

# Function to set up subtraction
def button_sub():
    first_number = e.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

# Function to set up multiplication
def button_mul():
    first_number = e.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

# Function to set up division
def button_div():
    first_number = e.get()
    global f_num
    global operation
    operation = "division"
    f_num = int(first_number)
    e.delete(0, END)

# Function to perform the chosen operation and display the result
def button_equal():
    second_number = e.get()    # Get the second number
    e.delete(0, END)           # Clear the display
    if operation == "addition":
        e.insert(0, f_num + int(second_number))
    if operation == "subtraction":
        e.insert(0, f_num - int(second_number))
    if operation == "multiplication":
        e.insert(0, f_num * int(second_number))
    if operation == "division":
        e.insert(0, f_num / int(second_number))

# Define number buttons with their respective commands
button_1 = Button(frame, text="1", padx=42, pady=20, command=lambda: button_click(1))
button_2 = Button(frame, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(frame, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(frame, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(frame, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(frame, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(frame, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(frame, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(frame, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(frame, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Define operation and utility buttons
button_add = Button(frame, text="+", padx=39, pady=20, command=button_add)
button_sub = Button(frame, text="-", padx=39, pady=20, command=button_sub)
button_mul = Button(frame, text="*", padx=39, pady=20, command=button_mul)
button_div = Button(frame, text="/", padx=39, pady=20, command=button_div)
button_equal = Button(frame, text="=", padx=99, pady=20, command=button_equal)
button_clear = Button(frame, text="Clear", padx=89, pady=20, command=button_clear)

# Place the buttons on the screen 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()  # Run the main loop for the GUI
