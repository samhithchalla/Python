# Login System which can access system files to store and verify user details.


def menu():
    print("***Menu***")
    inp = input("Welcome user... \nWant to Login(lgn) or Register(reg) (lgn/reg)? ")
    if inp == 'lgn':
        loginAcct()
    elif inp == 'reg':
        regAcct()
    else:
        print("\nInvalid choice...")
        menu()

def regAcct():
    print("\n*** Registration ***\nPlease fill the details to Register")
    uname = input("\nEnter your name: ")
    password = input("\nEnter your password: ")
    cpassword = input("\nRe-enter your password: ")
    if password != cpassword:
        print("Passwords donot match. Try again...")
        regAcct()
    elif password == cpassword:
        reg(uname,password)    

def loginAcct():
    print("\n*** Login ***\nPlease fill the details to Login")
    uname = input("\nEnter your name: ")
    password = input("\nEnter your password: ")
    login(uname,password)

def reg(uname,password):
    exists = False
    file = open("login_details.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if a == uname and b == password:
            exists = True
            file.close()
            break
    if exists == True:
        print("User already exists...")
        loginAcct()
    elif exists == False:
        file = open("login_details.txt","a")
        file.write("\n"+uname+","+password)
        print("User Registration successful. Login to continue...")
        file.close()
        loginAcct()

def login(uname,password):
    login = False
    file = open("login_details.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if a==uname and b==password:
            login = True
            break
    file.close()
    if login == True:
        print(f"Logged in successfully as {uname}...")
    elif login == False:
        print("Invalid credentials. Try again")
        loginAcct()

if __name__ == "__main__":
    
    print("Welcome to Samhith's Login System...")

    menu()