def validate(num):
    if num>=0 and num<=100:
            return True
    else:
        return False
number = int(input("Enter an integer:"))
    
print(validate(number))