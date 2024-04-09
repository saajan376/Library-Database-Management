#importing the necessary modules

from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import mysql.connector as mysql
from tkinter import messagebox

#importing the user created modules
from Addbook import *
from ViewBooks import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *

#creating mysql connection
mypassword= "saajan376" #use your own password
mydatabase="library" #The database name

con = mysql.connect (host="localhost",user="root", passwd=mypassword, database=mydatabase)
cur=con.cursor()
# Create the root window
root = Tk()
root.title("Library")
root.geometry('1200x700')

# Load the image
image_path = "C:/Users/admin/Downloads/library.png"  # Replace with your image path
image = PhotoImage(file=image_path)

# Create a label to display the image
image_label = Label(root, image=image)
image_label.pack()

#creating heading frame
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

#creating heading label
headingLabel = Label(headingFrame1, text="Welcome to \n Saajan's Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Creating the buttons
btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white',command=delete)
btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=viewbook)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white',command=issueBook)
btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command=returnBook)
btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

def open1():
    f = open('aboutlib.txt', 'r')
    x = f.read()
    print(x)
    f.close()
    
btn6 = Button(root, text="About Library", bg='black', fg='white', command=open1)
btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)   

#running the mainloop
root.mainloop()
