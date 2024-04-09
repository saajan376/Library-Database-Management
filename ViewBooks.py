#running the mainloop
import mysql.connector
from tkinter import *
from tkinter import messagebox

# MySQL database connection configuration
db_config = {
    'user': 'root',
    'password': 'saajan376',
    'host': 'localhost',
    'database': 'library'
}

#creating the function
def viewbook():
    try:
        # Establish a MySQL connection
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # SQL query to fetch books from the database
        query = "SELECT * FROM addbook"
        cursor.execute(query)
        books = cursor.fetchall()
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to connect to the database: {err}")
        return
    
    # Create a Tkinter window
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    #creating the canvas for the window
    canvas = Canvas(root, bg="#12a4d9")
    canvas.place(relwidth=1, relheight=1)

    #creating heading frames and labels
    heading_frame = Frame(root, bg="#FFBB00", bd=5)
    heading_frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    
    heading_label = Label(heading_frame, text="View Books", bg='black', fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    label_frame = Frame(root, bg='black')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    
    y = 0.25
    
    Label(label_frame, text="%-10s%-40s%-30s%-20s" % ('BID', 'Title', 'Author', 'Status'),
          bg='black', fg='white').place(relx=0.07, rely=0.1)
    
    Label(label_frame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    
    for book in books:
        Label(label_frame, text="%-10s%-30s%-30s%-20s" % (book[0], book[1], book[2], book[3]), bg='black', fg='white').place(
            relx=0.07, rely=y)
        
        y += 0.1

    #quit button
    quit_btn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_btn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    #running the mainloop
    root.mainloop()


