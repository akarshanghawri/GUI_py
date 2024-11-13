from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer App")  # title of the window

# Load images and add them to an image list
my_img1 = ImageTk.PhotoImage(Image.open("imageViewerApp/img/img1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("imageViewerApp/img/img2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("imageViewerApp/img/img3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("imageViewerApp/img/img4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("imageViewerApp/img/img5.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# Display the first image at the start
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

# Function to go to the next image
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # Remove the current image
    my_label.grid_forget()

    # Update the label and button commands
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    # Disable forward button at the last image
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    # Display updated image and navigation buttons
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

# Function to go to the previous image
def back(image_number):
    global my_label
    global button_forward
    global button_back

    # Remove the current image
    my_label.grid_forget()

    # Update the label and button commands
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    # Disable back button at the first image
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    # Display updated image and navigation buttons
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

# Initial button setup
button_back = Button(root, text="<<", command=back, state=DISABLED)  # Back button starts as disabled
button_exit = Button(root, text="Close App", command=root.quit)       # Exit button to close the app
button_forward = Button(root, text=">>", command=lambda: forward(2))  # Forward button to go to the next image

# Display buttons
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
