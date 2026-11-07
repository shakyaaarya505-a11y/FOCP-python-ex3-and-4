number = int(input("enter a number:"))
if number<0:
    for i in range(12,-1,-1):
        print(i,"x",abs(number),"=" i*abs(number))
    else:
        for i in range(13):
            print(i,"x",number,"x",i*number)