#Login System


users = {}
inp = ""
var = ""


def loginMenu():
    inp = input("Create new account? (y / n): ")
    if inp == 'y':
        createAcct()
    elif inp == 'n':
        loginAcct()
    else:
        print("Invalid choice. Try again...")
        loginMenu()


def createAcct():
    print("**Create Account**\nPlease fill the details:")
    f1 = input("\nEnter your name: ")
    f2 = input("\nCreate new password: ")
    f3 = input("\nConfirm password: ")
    if f1 in users and f2 == users[f1]:
        print("User already exists. Login to continue...")
        loginAcct()
    else:
        if f2 != f3:
            print("\nPasswords donot match. Try again...")
            createAcct()
        elif f2 == f3:
            users[f1] = f2
            print("\nAccount created successfully.\nLogin to continue")
            loginAcct()



def loginAcct():
    uname = input("\nEnter user name: ")
    upass = input("\nEnter password: ")

    if uname in users and upass == users[uname]:
        print("\nLogin successful")
    
    else:
        var = input("\nInvalid login credentials.\nPress 'y' to try again\nPress 'n' to create new account: ")
        if var == 'y':
            loginAcct()
        elif var == 'n':
            createAcct()
        else:
            print('Invalid option')
            loginMenu()

if __name__ == "__main__":
    
    print("Welcome to Login System\n")

    loginMenu()
