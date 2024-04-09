#importing the necessary modules
import mysql.connector as mysql
from tkinter import *
from tkinter import messagebox

# MySQL database connection configuration
mypass = "saajan376"
mydatabase = "library"
con = mysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued"
bookTable = "addbook"
allBid = []  # To store all the Book ID’s

#creating the function
def issue():
    # Get book ID and issue-to information from the GUI input fields
    bid = inf1.get()
    issueto = inf2.get()

    # Check if the book ID is valid
    check_bid_query = "SELECT * FROM addbook WHERE bid ="+bid
    cur.execute(check_bid_query)
    result = cur.fetchone()

    if result:
        # Book ID is valid, insert into books_issued table
        insert_query = "INSERT INTO books_issued (bid, issuedto) VALUES (%s, %s)"
        cur.execute(insert_query, (bid, issueto))
        con.commit()

        # Update status in addbook table
        update_query = "UPDATE addbook SET status = 'avail' WHERE bid = %s"
        cur.execute(update_query, (bid,))
        con.commit()

        messagebox.showinfo("Book Issued", "The book has been successfully issued.")

        root.destroy()
    else:
        messagebox.showerror("Error", "Invalid Book Id")
        inf1.delete(0, END)
        inf2.delete(0,END)
        
#creating a function to invoke the above function
def issueBook():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1

    #creating the window for the function
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    #creating the canvas
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    #creating the heading frames and labels
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    
    #creating the entry fields
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)
    
    #issue button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #quit button
    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    #running the mainloop
    root.mainloop()
