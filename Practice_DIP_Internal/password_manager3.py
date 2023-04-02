from tkinter import * #Imports all tkinter codes


root = Tk() # sets the root 
root.title("Login") # Adding a title to the top of the window called log in
root.geometry("550x350") # sets size of window

unpw = {} #sets the dictionary to nothing, this will store the information and share it to the password3.txt file
with open("password3.txt") as file: #opens text file
    password_true = file.readline().strip() #reads the first line and stores it in a variable called password_true

'''Sub Functions - This will be used in the frames (Main Functions)'''

def clear_all_passwords(): #this function clears the passwords by writing the text file to nothing
    global unpw
    unpw = {}
    with open("Results3.txt", "w") as file:
        file.write("")

def clear_app_password(): #this function clears the app passwords by writing the text file to nothing
    global password_true
    password_true = "!password_placeholder_text!"
    with open("password3.txt", "w") as file:
        file.write(password_true)
    frame3.destroy()    # this hides the frame and sets it back to the first frame as they have to set a new password
    frames1()

def accounts(entryAccount, entryPass): #this function is writes the saved passwords into the dictionary adn into the txt file
    unpw[entryAccount] = entryPass
    with open("Results3.txt", "a") as file:
        file.write(f"{entryAccount}: {entryPass}\n")
    print(entryAccount, entryPass)



def frames1(): # This function places the modules into the first frame 
    global frame1
    frame1 = Frame(root)
    frame1.grid(row=0, column=0, sticky="nsew")

    #placing objects in frame one
    lblPass = Label(frame1, text="Please enter new App Password") #label 
    lblPass.grid(row=0, column=0) # places label in row 0 and column 0

    entryPass = Entry(frame1, show="*") # changes the viewable characters as a dot to hide what they are typing
    entryPass.grid(row=0, column=1)

    btnLogin = Button(frame1, text="LogIn", command=lambda: set_password(entryPass.get())) # this button has a text and stores the entyPass into the variable 
    btnLogin.grid(row=2, column=1)

    lblPass = Label(frame1, text="Make sure to remember this password! \n - We will ask you for it next time you sign in.") #\n line makes a new line
    lblPass.grid(row=4, column=1)

def set_password(password): # this function makes it so that when the user enters their password, the code writes it into the password3.txt file
    with open("password3.txt", "w") as file:
        file.write(password)

    global password_true
    password_true = password 
    frames2()   # runs next frame

def frames2(): # This frame asks for the password, so any returning users will have to enter their password before entering and viewing their acount naems and passwords
    global frame2
    frame2 = Frame(root)
    frame2.grid(row=0, column=0, sticky="nsew")

    lblPass = Label(frame2, text="Password (App Sign In)")
    lblPass.grid(row=1, column=0)

    entryPass = Entry(frame2, show="*") # changes the viewable characters as a dot to hide what they are typing
    entryPass.grid(row=1, column=1)

    btnLogin = Button(frame2, text="LogIn", command=lambda: check_password(entryPass.get(), error_label))
    btnLogin.grid(row=2, column=1)

    error_label = Label(frame2)
    error_label.grid(row=3, column=1, pady=10)

def check_password(password, error_label): # this is the main frame where the user can add passwords, view passwords, remove passwords and change app password
    global frame3
    if password == password_true:
        frame3 = Frame(root)
        frame3.grid(row=0, column=0, sticky="NSEW")

        lblAccount = Label(frame3, text="Account Name")
        lblAccount.grid(row=0, column=0)

        entryAccount = Entry(frame3)
        entryAccount.grid(row=0, column=1)

        lblPass = Label(frame3, text="Password")
        lblPass.grid(row=1, column=0)

        entryPass = Entry(frame3, show="*")
        entryPass.grid(row=1, column=1)
        
        def clear_text():       #This function clears the text in the box so that the user knows the username and password has been entered succesfully
            entryAccount.delete(0, END) 
            entryPass.delete(0, END)
        
        btnEnter = Button(frame3, text="Enter", command=lambda: (accounts(entryAccount.get(), entryPass.get()), clear_text()))
        btnEnter.grid(row=2, column=1)

        btnView = Button(frame3, text="View Your Saved Passwords", command=view_passwords) # viewed saved passwords 
        btnView.grid(row=3, column=1)

        btnClearAll = Button(frame3, text="Clear Your Passwords", command=clear_all_passwords)
        btnClearAll.grid(row=4, column=1)

        btnClearAppPassword = Button(frame3, text="Clear Your App Password", command=clear_app_password)
        btnClearAppPassword.grid(row=5, column=1)

        btnView = Button(frame3, text="View Your Saved Passwords", command=view_passwords)
        btnView.grid(row=3, column=1)

    else:
        error_label.config(text="Password is incorrect! Please try again")  #shows incorrect password text if they enter wrong password 


def view_passwords(): #this function opens a new frame to show the existing passwords
    global frame3
    frame3 = Frame(root)
    frame3.grid(row=0, column=0, sticky="NSEW")

    with open("Results3.txt", "r") as f: #reads passwords
        data = f.read()

    text_box = Text(frame3)
    text_box.insert(INSERT, data) #inserts the data from the results text file
    text_box.grid(row=0, column=0)

    btnClose = Button(frame3, text="Back", command=frame3.destroy) # destroys the frame if the user closes the frame
    btnClose.grid(row=1, column=0)

if password_true == "!password_placeholder_text!": #this is the actual main code it decides what function to run depending on the contents of the txt file. If the file has the placeholder text,it will run the first frame otherwise it will run the second frmae
    frames1()
else:
    frames2()

root.mainloop() # ends the main loop
