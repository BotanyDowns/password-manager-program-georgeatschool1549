passwords = {} #sets the dictionary to nothing, this will store the information and share it to the password2.txt file
user_set_password = ("password2.txt") # puts the file under a variable

def enter():  #this function asks for the password and if it matches with the password2.txt file it allows the user in
    pass_enter = input("Please enter your password to access your passwords:") 
    if pass_enter == password_true:
        main() 
    else:
        print("Password is INCORRECT! Please try again")
        enter()
       
def userpass(username, password): #adds the password and username to the file
    with open("Results2.txt", "a") as file:
        file.write(f"{username}:{password}\n")

def view_password(): # reads and prints the data from the text file
    print("")
    with open("Results2.txt", "r") as file:
        contents = file.read()
        print(contents)
    print("_________________________________")

def clear(): # clears the file with the password results in it
    with open("Results2.txt", "w") as file:
        file.write("") #replaces the file with nothing 
    print("")
    print("----------CLEARED!----------")
    print("")

def clear2(): # clears the app password
    with open("password2.txt", "w") as file:
        file.write("!password_placeholder_text!") #replaces it with the placeholder text 
    print("----------CLEARED!----------")

def main(): # main function which asks for the options

    while True:
        print("1. Add Password:")
        print("2. View Passwords:")
        print("3. Clear your Stored Passwords")
        print("4. Exit:")
        print("5. Clear Entry Password")
        print("")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("")
            username = input("Enter username: ")
            password = input("Enter password: ")
            userpass(username, password)
            print("_________________")
            print("Saved Succesfully")
            print("_________________")
            print("")
        elif choice == "2":
           print("")
           view_password()
        elif choice == "3":
            clear() # runs clear code 
        elif choice == "4":
            break # stops app
        elif choice == "5":
            clear2()
            print("Please Run App again to enter your new password.")
            print("")
            break
        else:
            print("Invalid choice")  
            print("")

file = open("password2.txt")
line1 = file.readlines()
password_true = line1[0] # this picks the first line of the text file and puts it in variable

if password_true == "!password_placeholder_text!": # this is main code where it checks to see if a password ahs been set and runs the appropritate function
    print("")
    print("---------------------------------------------")
    user_set_password = input("Hello new user, please add a password: ")
    print("")
    with open("password2.txt", "w") as file:
        file.write(user_set_password)
    main()
else:
    enter()





