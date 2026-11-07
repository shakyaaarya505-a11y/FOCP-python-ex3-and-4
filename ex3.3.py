password1 = input("enter a new password:")
password2 = input("enter the password again:")
if password1 == password2:
        if len(password1) >= 8 and len(password1) <=12:
            print("password set")
        else:
            print("Password must be 8 to 12 characters long:")
else:
        print("Password does not match")