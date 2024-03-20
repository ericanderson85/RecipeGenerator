import hashlib
import json

def signup():
    users = []
    with open("loginSystem/credentials.json", "r") as f:
        users = json.load(f)

    email = input("Enter Email Adress : ")
    username = input("Enter Username : ")
    pwd = input("Enter Password : ")
    conf_pwd = input("Confirm Password : ")

    for r in users:
        if r["Email"] == email or r["Username"] == username:
            print("Email or Username already in use")
            return
        
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        new_user = {"Email": email,
                    "Username": username,
                    "Password": hash1}
        users.append(new_user)
        with open("loginSystem/credentials.json", "w") as f:
             json.dump(users, f, indent=4)

        f.close()
        print("You Have Registered Successfully")
    else:
        print("Password is not the Same")

def login():
    users = []
    with open("loginSystem/credentials.json", "r") as f:
        users = json.load(f)
    f.close()
    email = input("Enter Email : ")
    pwd = input("Enter Password : ")

    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()

    for r in users:
        if r["Email"] == email and r["Password"] == auth_hash:
            print("Logged in Successfully!")
        else :
            print("Login Failed")

while 1:
    print("Login System")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your Choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Try Again")