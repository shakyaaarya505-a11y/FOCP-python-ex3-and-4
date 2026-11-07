def countUpper(msg):
    count = 0
    for x in msg:
        if x.isupper():
            count+=1
        return count
    print(countUpper('AArya'))