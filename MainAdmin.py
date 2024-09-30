from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess
from tkinter import messagebox
import random
import qrcode
import mysql.connector
import datetime
import os

class EventPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Background image
        img = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\hot-pink-nawpic-20.jpg")
        img = img.resize((1530, 790))
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(root, image=self.photoimg)
        bg_img.place(x=0, y=0)

        back_button = Button(self.root, text="Back", command=self.go_back)
        back_button.place(x=0,y=0)

        # Buttons
        previous_btn = Button(self.root, text="Previous Event", command=self.open_previous_event)
        previous_btn.place(x=500, y=190,height=150,width=150)

        new_btn = Button(self.root, text="New Event", command=self.open_new_event)
        new_btn.place(x=800, y=190,height=150,width=150)

    def open_previous_event(self):
        # Code to open the previous event page
        program_path = r"C:\Users\shivank\OneDrive\Desktop\face\app\MainAdmin2.py"
        
        # Open the other Python program using subprocess
        subprocess.Popen(["python", program_path])

    def open_new_event(self):
        # Code to open the new event page
        program_path = r"C:\Users\shivank\OneDrive\Desktop\face\app\MainAdmin1.py"
        
        # Open the other Python program using subprocess
        subprocess.Popen(["python", program_path])
    def go_back(self):  
        # Close the entire window
        self.root.destroy()

        
if __name__ == "__main__":
    root = Tk()
    app = EventPage(root)
    root.mainloop()