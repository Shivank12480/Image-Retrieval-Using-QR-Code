import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog, messagebox
import os
import mysql.connector
import cv2
import face_recognition
import shutil
from PIL import Image, ImageTk
import threading

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")
        self.root.geometry("1530x790+0+0")
        
        self.target_image_path = ""
        self.output_dir = ""
        self.retake_button = None  # Initialize retake_button attribute
        self.matched_images = []  # Initialize matched_images attribute

        img = Image.open(r"C:\Users\shivank\OneDrive\Desktop\All_images\IMG-20240403-WA0001.jpg")
        img = img.resize((1530, 790))
        self.photoimg = ImageTk.PhotoImage(img)  # Initialize photoimg attribute
        self.create_widgets()

    def create_widgets(self):
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0)

        self.camera_frame = LabelFrame(self.root, font=('times new roman', 12, 'bold'), bg='#a7e8dc')
        self.camera_frame.place(x=325, y=180, height=300, width=250)
        image_path = "C:/Users/shivank/OneDrive/Desktop/face/app/OIG4.jpeg"
        img = Image.open(image_path)
        img = img.resize((250, 300))  # Resize the image to fit the LabelFrame
        photoimg = ImageTk.PhotoImage(img)

        # Create a Label widget to display the image
        image_label = Label(self.camera_frame, image=photoimg)
        image_label.image = photoimg
        image_label.pack() 

        target_label = Label(self.root, text="Select Target Image:", bg='#f5f5f5', font=('Lobster', 14))
        target_label.place(x=325, y=180, height=25, width=250)

        camera_button = tk.Button(self.root, text="Take Picture", bg="black", fg="white", font=('Lobster', 12),
                                  command=self.capture_image)
        camera_button.place(x=395, y=480, height=45, width=100)

        self.register_frame = Frame(self.root, bg="white")

        output_label = tk.Label(self.register_frame, text="Select Output Directory:", bg='#f5f5f5', font=('Lobster', 14), pady=10)
        output_label.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

        select_output_button = tk.Button(self.register_frame, text="Browse", bg="black", fg="white", font=('Lobster', 12),
                                         command=self.select_output_directory)
        select_output_button.grid(row=3, column=2, columnspan=2, pady=5)

        run_button = tk.Button(self.register_frame, text="Run Face Recognition", bg="black", fg="white", font=('Lobster', 12),
                               command=self.start_face_recognition)
        run_button.grid(row=4, column=1, columnspan=2, pady=10)

        self.progress_bar = ttk.Progressbar(self.register_frame, orient="horizontal", length=100, mode="determinate")
        self.progress_bar.grid(row=5, column=1, columnspan=2, pady=5)

        self.progress_label = tk.Label(self.register_frame, text='', bg='#f5f5f5', font=('Arial', 12), pady=5)
        self.progress_label.grid(row=6, column=1, columnspan=2)

        back_button = Button(root, text="Back", command=self.go_back)
        back_button.grid(row=0, column=0, padx=10, pady=10)

        back_button = Button(self.register_frame, text="Back", command=self.go_back)
        back_button.grid(row=0, column=0, padx=5, pady=5)

        show_button = tk.Button(self.root, text="Show Images", bg="black", fg="white", font=('Lobster', 12),
                                command=self.show_matched_images)
        show_button.place(x=560,y=600,height=50,width=200)

        self.show_images = Frame(self.root, bg="white")

    def show_images_frame(self):
        self.register_frame.place(x=0, y=190, height=250, width=300)

        # Create and place the back button
        back_button = Button(self.register_frame, text="Back", command=self.hide_register_frame)
        back_button.grid(row=0, column=0)

    def show_register_frame(self):
        # Show the register frame when Sign Up button is clicked
        self.register_frame.place(x=800, y=190, height=250, width=300)

        # Create and place the back button
        back_button = Button(self.register_frame, text="Back", command=self.hide_register_frame)
        back_button.grid(row=0, column=0)

    def hide_register_frame(self):
        # Hide the register frame
        self.register_frame.place_forget()

    def capture_image(self):
        def clear_image():
            image_label.config(image=None)
            self.target_image_path = ""
            if self.retake_button:
                self.retake_button.destroy()  # Destroy the retake button

        def finalize_capture(frame):
            cv2.imwrite("captured_image.jpg", frame)

            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img.thumbnail((300, 300))  # Resize image if necessary
            img = ImageTk.PhotoImage(image=img)

            image_label.config(image=img)
            image_label.image = img

            self.target_image_path = "captured_image.jpg"

            if self.retake_button:
                self.retake_button.destroy()  # Destroy the retake button

        capture = cv2.VideoCapture(0)

        # Add a small delay before capturing the frame
        # This allows the camera to initialize properly
        for _ in range(5):
            capture.read()

        ret, frame = capture.read()
        if ret:
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(image=img)

            global image_label
            image_label = Label(self.camera_frame, image=img)
            image_label.image = img
            image_label.place(x=5, y=10, height=230, width=240)

            finalize_button = tk.Button(self.camera_frame, text="Finalize", bg="black", fg="white", font=('Lobster', 12),
                            command=lambda: (finalize_capture(frame), self.show_register_frame()))

            finalize_button.place(x=40, y=240, height=50, width=75)

            self.retake_button = tk.Button(self.camera_frame, text="Retake", bg="black", fg="white",
                                           font=('Lobster', 12), command=self.capture_image)
            self.retake_button.place(x=120, y=240, height=50, width=75)

            capture.release()
        else:
            messagebox.showerror("Error", "Failed to capture image from camera.")

    def select_output_directory(self):
        self.output_dir = filedialog.askdirectory()

    def start_face_recognition(self):
        threading.Thread(target=self.run_face_recognition).start()

    def run_face_recognition(self):
        if not self.target_image_path or not self.output_dir:
            messagebox.showerror("Error", "Please select target image and output directory.")
            return

        # Fetch group photos directory from MySQL
        group_photos_dir = self.fetch_folder_paths_from_mysql()

        if not group_photos_dir:
            messagebox.showerror("Error", "Failed to fetch group photos directory.")
            return

        target_image = face_recognition.load_image_file(self.target_image_path)
        target_face_encodings = face_recognition.face_encodings(target_image)

        if len(target_face_encodings) == 0:
            messagebox.showerror("Error", "No faces found in the target image.")
            return

        target_face_encodings = target_face_encodings[0]

        matched_images = []

        image_files = [filename for filename in os.listdir(group_photos_dir) if filename.endswith(".jpg")]
        image_count = len(image_files)
        self.progress_bar['maximum'] = image_count

        for index, filename in enumerate(image_files):
            group_image_path = os.path.join(group_photos_dir, filename)
            group_image = face_recognition.load_image_file(group_image_path)

            group_image = cv2.resize(group_image, (0, 0), fx=0.5, fy=0.5)

            face_locations = face_recognition.face_locations(group_image)
            if len(face_locations) == 0:
                self.progress_bar.step(1)
                self.progress_label.config(text=f'Processing: {int((index+1) * 100 / image_count)}%')
                self.root.update_idletasks()
                continue

            group_face_encodings = face_recognition.face_encodings(group_image, face_locations)

            for face_encoding in group_face_encodings:
                match = face_recognition.compare_faces([target_face_encodings], face_encoding, tolerance=0.5)
                if match[0]:
                    matched_images.append(group_image_path)
            self.progress_bar.step(1)
            self.progress_label.config(text=f'Processing: {int((index+1) * 100 / image_count)}%')
            self.root.update_idletasks()
        self.matched_images = matched_images  # Store matched images in the instance variable

        for image_path in matched_images:
            filename = os.path.basename(image_path)
            output_path = os.path.join(self.output_dir, filename)
            shutil.copy(image_path, output_path)

        messagebox.showinfo("Face Recognition", "Process completed. Matched images copied to the output directory.")
        
        # Show "Show Images" button after processing
        

    def show_matched_images(self):
        # Create a new window to display matched images
        matched_window = Toplevel(self.root)
        matched_window.title("Matched Images")

        canvas = Canvas(matched_window)
        scroll_y = Scrollbar(matched_window, orient="vertical", command=canvas.yview)

        frame = Frame(canvas)
        for index, img_path in enumerate(self.matched_images):
            img = Image.open(img_path)
            img.thumbnail((200, 200))
            img = ImageTk.PhotoImage(img)
            img_label = Label(frame, image=img)
            img_label.image = img
            img_label.grid(row=index // 3, column=index % 3, padx=10, pady=10)

        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')

        back_button = Button(matched_window, text="Back", command=matched_window.destroy)
        back_button.pack(pady=10)

    def fetch_folder_paths_from_mysql(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="12480", database="user")
            cursor = conn.cursor()
            cursor.execute("SELECT  search_folder FROM events")
            folder_paths = cursor.fetchall()
            cursor.close()
            conn.close()
            if folder_paths:
                return folder_paths[0][0]  # Return the first folder path from the result
            else:
                return None
        except Exception as e:
            print("Error:", e)

    def go_back(self):  
        # Close the entire window
        self.root.destroy()

    def show_main_frame(self):
        self.main_frame.lift()  # Lift the main_frame to the top layer

if __name__ == '__main__':
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
