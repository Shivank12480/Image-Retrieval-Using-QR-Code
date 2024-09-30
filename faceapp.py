from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import Image
import subprocess


class FaceRecognitonSystem:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
#first image
        img = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\OIP (4).jpeg")
        img = img.resize((250, 130))

        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg,bg='#1aa3ff')
        f_lbl.place(x=0, y=0, height=132, width=250)
        img1_1 = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\AdobeStock_248645369-scaled.jpeg")
        img1_1 = img1_1.resize((250, 130))

        self.photoimg1_1 = ImageTk.PhotoImage(img1_1)

        f_lbl = Label(self.root, image=self.photoimg1_1)
        f_lbl.place(x=250, y=0, height=132, width=250)
        
#second image
        img1 = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\Untitled.png")
        img1 = img1.resize((500, 130))

        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1,background='#004d00')
        f_lbl.place(x=500, y=0, height=132, width=550)
#third image
        img3 = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\OIP (1).jpeg")
        img3 = img3.resize((250, 130))

        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1050, y=0, height=132, width=250)
        img3_1 = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\OIP (2).jpeg")
        img3_1 = img3_1.resize((250, 130))

        self.photoimg3_1 = ImageTk.PhotoImage(img3_1)

        f_lbl = Label(self.root, image=self.photoimg3_1)
        f_lbl.place(x=1300, y=0, height=132, width=250)
#background image
        img4 = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\e7043444136efd6c472e185af121dbf4.jpg")
        img4 = img4.resize((1530, 790))

        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, height=650, width=1530)

        title_lb1=Label(bg_img,text='Face Recognition APP',font=('times new roman',35,'bold'),bg='#003300',fg='#1aa3ff')
        title_lb1.place(x=0,y=0,width=1530,height=45)
#button 1
        img5 = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\admin.jpg")
        img5 = img5.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2", command=open_admin)
        b1.place(x=400,y=200,width=220,height=220)
        #title_lb1=Button(bg_img,text='Admin',font=('times new roman',28,'bold'),bg='white',cursor="hand2", command=open_admin)
        #title_lb1.place(x=415,y=415,width=200,height=25)
#button 2
        img6 = Image.open(r"C:\Users\shivank\OneDrive\Desktop\face\app\user.jpg")
        img6 = img6.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=open_user)
        b2.place(x=850,y=200,width=220,height=220)
        #title_lb1=Button(bg_img,text='User',font=('times new roman',28,'bold'),bg='white',cursor="hand2",command=open_user)
        #title_lb1.place(x=815,y=415,width=200,height=25)
  
def open_admin():

  program_path = r"C:\Users\shivank\OneDrive\Desktop\face\app\admin.py"
        
        # Open the other Python program using subprocess
  subprocess.Popen(["python", program_path])

def open_user():
    program_path=r"C:\Users\shivank\OneDrive\Desktop\face\app\user.py"
    subprocess.Popen(["python",program_path])

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitonSystem(root)
    root.mainloop()

