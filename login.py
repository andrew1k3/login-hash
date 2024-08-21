import hashlib
import database

db = database.Database("database.txt")

def login() -> None:
    username = input("username: ")
    password = input("password: ")
    h = hashlib.new('sha256')
    h.update(password.encode('utf-8'))
    hashed_password = h.hexdigest()

    entry = db.find_entry(username)
    if not entry:
        print("username not found")
        return
    if entry[1] == hashed_password:
        print(f"succesfully logged in as {entry[0]}")
        return
    else:
        print("password doesn't match")
    return


def register() -> None:
    username = input("username: ")
    password = input("password: ")
    
    if db.find_entry(username):
        print("username already exists")
        return
    
    h = hashlib.new('sha256')
    h.update(password.encode('utf-8'))
    hashed_password = h.hexdigest()
    
    db.add_entry((username, hashed_password))
    print("user succesfully created")
    return

def main_loop() -> None:
    while True:
        choice = input("1: Login, 2: Register: ")
        if (choice == '1'):
            login()
        elif (choice == '2'):
            register()
        else:
            print("invalid")

        print()
    
print("-------- ANDREW'S DATABASE --------")
main_loop()
