import getpass
database = {"cleartext": "123456", "pythonpass": "2502"}
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again!!: ")
        break
print("Verified")