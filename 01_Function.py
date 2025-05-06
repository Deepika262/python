s_username="Deepi"
s_password="123"

uname=input("Enter a username")
upass=input("Enter a password")

def validate():
    if s_username==uname and s_password==upass:
        print("true")
    else:
        print("False")
validate()
