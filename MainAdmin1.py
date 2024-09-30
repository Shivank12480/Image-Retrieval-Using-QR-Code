from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
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
        self.search_folder = None  # Initialize search folder variable
        self.qr_frame = None  # Initialize qr_frame variable
        self.random_number = None

        # Background image
        img = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\hot-pink-nawpic-20.jpg")
        img = img.resize((1530, 790))
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0)

        # Event Details Frame
        event_frame = Frame(self.root, bd=5, relief=RIDGE, bg="#b30059")
        event_frame.place(x=425, y=180, height=400, width=630)

        # Event Name
        lbl_event_name = Label(event_frame, text="Event Name:", font=("times new roman", 18, "bold"), bg="white")
        lbl_event_name.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.txt_event_name = Entry(event_frame, font=("times new roman", 18), bd=5)
        self.txt_event_name.grid(row=0, column=1, padx=20, pady=10, sticky="w")
        

        # Event Date
        lbl_event_date = Label(event_frame, text="Event Date :", font=("times new roman", 18, "bold"), bg="white")
        lbl_event_date.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.txt_event_date = Entry(event_frame,font=("times new roman", 18), bd=5)
        self.txt_event_date.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        
        # Search Folder
        lbl_search_folder = Label(event_frame, text="Search Folder:", font=("times new roman", 18, "bold"), bg="white")
        lbl_search_folder.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.txt_search_folder = Entry(event_frame, font=("times new roman", 18), bd=5)
        self.txt_search_folder.grid(row=2, column=1, padx=20, pady=10, sticky="w")
        btn_browse = Button(event_frame, text="Browse", command=self.browse_folder, font=("times new roman", 14), bd=3, relief=RIDGE, bg="crimson", fg="white")
        btn_browse.grid(row=2, column=2, padx=10, pady=10)


       
        

        # Submit Button
        btn_submit = Button(event_frame, text="Submit", command=self.submit_event, font=("times new roman", 18, "bold"), bd=5, relief=RIDGE, bg="crimson", fg="white")
        btn_submit.grid(row=3,column=0,columnspan=2)
        btn_regs = Button(event_frame, text='Qr code',command=self.show_qr_frame, font=("times new roman", 18, "bold"), bd=5, relief=RIDGE, bg="crimson", fg="white")
        btn_regs.grid(row=3,column=1,columnspan=10)


        # Show Images Button
        btn_show_images = Button(event_frame, text="Show Images", command=self.show_images, font=("times new roman", 18, "bold"), bd=5, relief=RIDGE, bg="crimson", fg="white")
        btn_show_images.grid(row=4 ,column=1,pady=10)
        
        
        back_button = Button(root, text="Back", command=self.go_back)
        back_button.grid(row=0, column=0, padx=10, pady=10)

        
        
        

        

    def show_qr_frame(self):
        # Show the QR frame when the QR code button is clicked
        self.qr_frame = Frame(self.root, bd=5, relief=RIDGE, bg="#b30059")
        self.qr_frame.place(x=25, y=180, height=300, width=330)
        lbl_new_user = Label(self.qr_frame, text="QR CODE", font=("times new roman", 20, "bold"), bg="white", fg="red")
        lbl_new_user.place(x=0,y=0,height=30,width=325)

        print("Showing QR frame")  # Debug print

        # Generate a random event ID
        self.random_number = random.randint(10000, 99999)

        # Create QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=4)
        qr.add_data(self.random_number)
        qr.make(fit=True)

        # Create an image from the QR code
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Display the QR code image on a Label widget
        qr_code_image = ImageTk.PhotoImage(qr_image)
        qr_label = Label(self.qr_frame, image=qr_code_image, bg="white")
        qr_label.image = qr_code_image
        qr_label.place(x=50, y=40)

        # Display the event ID
        event_id_label = Label(self.qr_frame, text='Event ID:', bg="white", font=("times new roman", 20, "bold"))
        event_id_label.place(x=10, y=200)
        event_id_entry = Entry(self.qr_frame, font=("times new roman", 16),bd=3)
        event_id_entry.insert(END, str(self.random_number))  # Insert the random number into the Entry widget
        event_id_entry.place(x=140, y=200)
        
        try:
            # Insert the event ID into the database
            conn = mysql.connector.connect(host="localhost", user="root", password='12480', database="user")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO events (eventid) VALUES (%s)", (self.random_number,))
            conn.commit()
            cursor.close()
            conn.close()
            print("Event ID inserted successfully:",self. random_number)  # Debug print
        except Exception as e:
            print("Error inserting event ID:", e)  # Print any error that occurs
    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.txt_search_folder.delete(0, END)
        self.txt_search_folder.insert(0, folder_path)
        self.search_folder = folder_path  # Update search folder variable

    def submit_event(self):
        event_name = self.txt_event_name.get()
        event_date = datetime.datetime.strptime(self.txt_event_date.get(), "%d/%m/%Y").strftime("%Y-%m-%d")

        if not self.search_folder:
            messagebox.showerror("Error", "Please select a search folder.")
            return

        conn = mysql.connector.connect(host="localhost", user="root", password="12480", database="user")
        cursor = conn.cursor()

        try:
            for file_name in os.listdir(self.search_folder):
                if file_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    image_path = os.path.join(self.search_folder, file_name)
                    # Provide values for all the fields in the database table
                    cursor.execute("INSERT INTO events (event_name, event_date, image_path, search_folder, eventid) VALUES (%s, %s, %s, %s, %s)", (event_name, event_date, image_path, self.search_folder, self.random_number))
                    conn.commit()
        except Exception as e:
            print("Error:", e)

        cursor.close()
        conn.close()

    def show_images(self):
        # Check if search folder is selected
        if not self.search_folder:
            messagebox.showerror("Error", "Please select a search folder.")
            return

        print("Searching for images in folder:", self.search_folder)  # Debug print

        # Fetch images from the database
        conn = mysql.connector.connect(host="localhost", user="root", password="12480", database="user")
        cursor = conn.cursor()

        # Retrieve images from the database based on the search folder
        cursor.execute("SELECT image_path FROM events WHERE search_folder = %s", (self.search_folder,))
        image_paths = cursor.fetchall()

        # Close database connection
        cursor.close()
        conn.close()

        # Create a new window to display images
        show_images_window = Toplevel(self.root)
        show_images_window.title("Images")
        show_images_window.geometry("800x600")

        # Create a frame for images and scrollbar
        frame = Frame(show_images_window)
        frame.pack(fill=BOTH, expand=True)

        # Create a canvas
        canvas = Canvas(frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create another frame inside the canvas to hold the images
        inner_frame = Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # Display images in the inner frame
        for path in image_paths:
            image_path = path[0]  # Assuming the image path is stored in the 'image_path' column
            img = Image.open(image_path)
            img.thumbnail((200, 200))  # Resize the image to fit the frame
            photo = ImageTk.PhotoImage(img)
            label = Label(inner_frame, image=photo)
            label.image = photo  # Prevent image from being garbage collected
            label.pack(padx=10, pady=10)

        # Function to destroy the window and go back
        def go_back():
            show_images_window.destroy()

        # Back button which close show images window
        back_button = Button(show_images_window, text="Back", command=go_back)
        back_button.pack(pady=10)
    
    def go_back(self):  
        # Close the entire window
        self.root.destroy()
    
if __name__ == "__main__":
    root = Tk()
    obj = EventPage(root)
    root.mainloop()
