from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os

class EventPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        img = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\hot-pink-nawpic-20.jpg")
        img = img.resize((1530, 790))
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0)

        # Connect to MySQL database
        self.conn = mysql.connector.connect(host="localhost", user="root", password="12480", database="user")
        self.cursor = self.conn.cursor()

        # Event ID Entry
        self.event_id_label = Label(root, text="Event ID:")
        self.event_id_label.pack()
        self.event_id_entry = Entry(root)
        self.event_id_entry.pack()

        # Buttons
        self.show_button = Button(root, text="Show Images", command=self.display_images)
        self.show_button.pack()
        self.update_button = Button(root, text="Update Image", command=self.update_image)
        self.update_button.pack()
        self.delete_button = Button(root, text="Delete Image", command=self.delete_image)
        self.delete_button.pack()
        self.insert_button = Button(root, text="Insert Image", command=self.insert_image)
        self.insert_button.pack()

        # Image Display Area
        self.image_frame = Frame(root)
        self.image_frame.pack()

    def retrieve_images(self, eventid):
        # Execute SELECT query to retrieve images based on event_id
        query = "SELECT image_path FROM events WHERE eventid = %s"
        self.cursor.execute(query, (str(eventid),))

        image_paths = self.cursor.fetchall()
        return image_paths

    def display_images(self):
        eventid = self.event_id_entry.get()
        if not eventid:
            messagebox.showerror("Error", "Please enter an Event ID")
            return

        image_paths = self.retrieve_images(eventid)

        # Clear existing images
        for widget in self.image_frame.winfo_children():
            widget.destroy()

        # Display images
        for image_path in image_paths:
            path = image_path[0]
            img = Image.open(path)
            img.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(img)
            label = Label(self.image_frame, image=photo)
            label.image = photo
            label.pack(padx=5, pady=5)

    def update_image(self):
        # Implement update functionality
        pass

    def delete_image(self):
        # Implement delete functionality
        pass

    def insert_image(self):
        # Implement insert functionality
        pass

    def __del__(self):
        # Close database connection when object is destroyed
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    root = Tk()
    app = EventPage(root)
    root.mainloop()
