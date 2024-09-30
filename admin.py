from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import subprocess

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Background image
        img = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\drbdru-9106f17d-3698-465e-ba8a-9a503a7d0b05.jpg")
        img = img.resize((1530, 790))
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0)

        # Login Frame
        login_frame = LabelFrame(self.root, text='Admin', font=('times new roman', 32, 'bold'), bg='#000099')
        login_frame.place(x=425, y=180, height=400, width=670)

        # Login Form
        lbl_user = Label(login_frame, text="Username:", font=("times new roman", 18, "bold"), bg="white")
        lbl_user.grid(row=0, column=0, pady=50, padx=30, sticky="w")
        self.txt_user = Entry(login_frame, font=("times new roman", 18), bd=5)
        self.txt_user.grid(row=0, column=1, pady=1, padx=2)

        lbl_pass = Label(login_frame, text="Password:", font=("times new roman", 18, "bold"), bg="white")
        lbl_pass.grid(row=1, column=0, pady=0, padx=25, sticky="w")
        self.txt_pass = Entry(login_frame, font=("times new roman", 18), bd=5, show="*")
        self.txt_pass.grid(row=1, column=1, pady=1, padx=2)

        btn_login = Button(login_frame, text="Log In", command=self.login, font=("times new roman", 18, "bold"), bd=5, relief=RIDGE, bg="crimson", fg="white")
        btn_login.grid(row=4, columnspan=3, pady=10)

        # Registration Frame
        self.register_frame = Frame(self.root, bg="white")
        lbl_new_user = Label(self.register_frame, text="New Admin", font=("times new roman", 20, "bold"), bg="white", fg="red")
        lbl_new_user.grid(row=0, columnspan=2, pady=10)

        lbl_reg_user = Label(self.register_frame, text="Username:", font=("times new roman", 18, "bold"), bg="white")
        lbl_reg_user.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        self.txt_reg_user = Entry(self.register_frame, font=("times new roman", 18), bd=5)
        self.txt_reg_user.grid(row=1, column=1, pady=10, padx=20)

        lbl_reg_pass = Label(self.register_frame, text="Password:", font=("times new roman", 18, "bold"), bg="white")
        lbl_reg_pass.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        self.txt_reg_pass = Entry(self.register_frame, font=("times new roman", 18), bd=5, show="*")
        self.txt_reg_pass.grid(row=2, column=1, pady=10, padx=20)

        btn_register = Button(self.register_frame, text="Register", command=self.register, font=("times new roman", 18, "bold"), bd=5, relief=RIDGE, bg="crimson", fg="white")
        btn_register.grid(row=3, columnspan=2, pady=10)

        # Initially hide the register frame
        self.register_frame.place_forget()

        # Sign Up button to show the registration frame
        btn_regs = Button(login_frame, text='Sign Up', command=self.show_register_frame, font=("times new roman", 18, "bold"), bd=5, relief=RIDGE, bg="crimson", fg="white")
        btn_regs.grid(row=5, columnspan=4, pady=10)
        
        
        # Back button
        back_button = Button(root, text="Back", command=self.go_back)
        back_button.place(x=0,y=0)

    def go_back(self):
        # Close the entire window
        self.root.destroy()

    
    def show_register_frame(self):
    # Show the register frame when Sign Up button is clicked
        self.register_frame.place(x=800, y=150)

        # Create and place the back button
        back_button = Button(self.register_frame, text="Back", command=self.hide_register_frame)
        back_button.grid(row=0, column=0)

    def hide_register_frame(self):
        # Hide the register frame
        self.register_frame.place_forget()


    def login(self):
    # Connect to MySQL database
        conn = mysql.connector.connect(host="localhost", user="root", password="12480", database="user")
        cursor = conn.cursor()

        # Retrieve username and password from entry fields
        username = self.txt_user.get()
        password = self.txt_pass.get()

        # Check if username or password fields are empty
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        # Execute SQL query to check user credentials
        cursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            program_path = r"C:\Users\shivank\OneDrive\Desktop\face\app\MainAdmin1.py"
        
        # Open the other Python program using subprocess
            subprocess.Popen(["python", program_path])
            
            
            # Perform actions after successful login
        else:
            messagebox.showerror("Error", "Invalid username or password. Please try again.")

        # Close database connection
        cursor.close()
        conn.close()

    def register(self):
        # Connect to MySQL database
        conn = mysql.connector.connect(host="localhost", user="root", password='12480', database="user")
        cursor = conn.cursor()

        # Retrieve username and password from entry fields
        username = self.txt_reg_user.get()
        password = self.txt_reg_pass.get()

        # Check if username or password fields are empty
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        # Execute SQL query to insert new user
        cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful! Please log in.")

        # Close database connection
        cursor.close()
        conn.close()
   

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
