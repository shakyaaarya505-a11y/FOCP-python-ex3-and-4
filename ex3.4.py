BAD_PASSWORD = ['password','letmein','sesame','hello','justinbieber']
password1 = input("Enter a new password:")
password2 = input("Enter the password again:")
if password1 == password2:
    if len(password1)>= 8 and len(password1)<= 12:
        if password1 not in BAD_PASSWORD:
            print("Password set")
        else:
            print("This is a common password")
    else:
        print("password must be 8 to 12 characters long")
else:
    print("password does not match")