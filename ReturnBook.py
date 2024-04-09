#importing the necessary modules
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as mysql

#mysql and python connection and configuration
mypass = "saajan376"
mydatabase="library"

con = mysql.connect(host="localhost",user="root", password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" 
bookTable = "addbook"
allBid = []  #To store all the Book ID’s

#creating the function
def returnn():
    bid = bookInfo1.get()

    # Check if the book ID is valid
    check_bid_query = "SELECT * FROM addbook WHERE bid ="+bid
    cur.execute(check_bid_query)
    result = cur.fetchone()

    if result:
        # Book ID is valid, delete from books_issued
        delete_query = "DELETE FROM books_issued WHERE bid = %s"
        cur.execute(delete_query, (bid,))
        con.commit()

        # Update status in addbook table
        update_query = "UPDATE addbook SET status = 'avail' WHERE bid = %s"
        cur.execute(update_query, (bid,))
        con.commit()

        messagebox.showinfo("Book Issued", "The book has been successfully returned")

        root.destroy()
    else:
        messagebox.showerror("Error", "Invalid Book Id")
        bookInfo1.delete(0, END)

#creating the function to invoke the above function        
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    #creating a window for the function
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    #creating a canvas for the window
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)

     #creating heading frames and labels   
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    #quit button
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    #running the mainloop
    root.mainloop()
    
