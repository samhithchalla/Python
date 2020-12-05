# File system, where one can create and edit files protected with Login system. You can call it Personal Diary.


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
        print("User already exists. Login to continue...")
        loginAcct()
    elif exists == False:
        file = open("login_details.txt","a")
        file.write("\n"+uname+","+password)
        print("User Registration successful. Login to continue...")
        file.close()
        loginAcct()

def login(uname,password):
    global login
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
        print(f"\nLogged in successfully as {uname}...")
    elif login == False:
        print("Invalid credentials. Try again")
        loginAcct()

def userMenu():
    print("*** Your Personal Diary ***")
    print("1.Create new file. \n2.Read or Edit existing file.")
    uinp = int(input("Enter your choice: "))
    if uinp == 1:
        createFile()

    elif uinp == 2:
        editFile()

    else:
        print("Invalid Choice...")
        userMenu()

def createFile():
    fname = input("Enter the file name to create: ")
    fcontent = input("Enter the content of the file: ")
    try:
        cfile = open(f"{fname}.txt","x")
        cfile.write(fcontent)
        cfile.close()
        print(f"File {fname} created successfully")
    except Exception as e:
        e = "File already exists. Try editing it.\n"
        print(e)
        userMenu()



def editFile():
    fname = input("Enter the file name to edit: ")
    uchoice = input("Want to read(r) or add content(a) to the file (r/a)?: ")
    if uchoice == 'r':
        try:
            cfile = open(f"{fname}.txt","r")
            f1 = cfile.read()
            print(f1)
            cfile.close()
        except Exception as e:
            e = "File doesnot exist. Try creating one.\n"
            print(e)
            userMenu()
    elif uchoice == 'a':
        fcontent = input("Enter the content to be added: "+"\n")
        try:
            cfile = open(f"{fname}.txt","r+")
            cfile.write(fcontent)
            cfile.close()
            print(f"File {fname} edited successfully")
        except Exception as e:
            e = "File doesnot exists. Try creating one.\n"
            print(e)
            userMenu()


if __name__ == "__main__":
    
    print("Welcome to Samhith's Login System...")

    menu()

    if login == True:
        while True:
            
            userMenu()
            
            code = input("\nWant to exit (y/n): ")
            if code=='y':
                print("Thank you")
                exit()
            elif code=='n':
                continue
