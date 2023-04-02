passwords = {} # sets dictionary to nothing 

def add_password(account, password):
    passwords[account] = password #puts parameter in varibale

def get_password(account) :
    return passwords.get(account, None)

def main() : # main function where user has multipile options 
    while True:
        print("1. Add Password:")
        print("2. Get Password:")
        print("3. Exit:")

        choice = input("Enter your choice: ")

        if choice == "1":
            account = input("Enter account name: ")
            password = input("Enter Password: ")
            add_password(account, password) # adds passwords to empty dictionary 
        elif choice == "2":
            account = input("Enter account name: ")
            password = get_password(account)
            if password:
                print(f"Password for {account} :  {password}") #porints statment with passwords and usernames in it
            else:
                print(f"No password found for {account}")
        elif choice == "3" :
            break
        else:
            print("Invalid choice")      


if __name__ == "__main__":      #this runs the code
 main()    

