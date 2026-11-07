BAD_PASSWORD = ['password','letmein','sesame','hello','justinbieber']
while True:
    password1 = input("Enter a password:")
    password2 = input("Confirmed password")
if password1 != password2:
    print("password does not match ")
elif len(password1)< 8 or len(password1)>12:
    print("Password must be 8 to 12 characters long")
elif password in BAD_PASSWORD:
    print("This is a common password")
else:
    print("Password has been set")  
