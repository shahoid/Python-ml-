def perfectnumber(num):
    add = 0
    for div in range(1,(num//2)+1):
        if num % div ==0:
            add = add + div
            
    if(add == num):
        print("the number is perfect number !!!")
    else:
        print("not perfect number!!!")

num = int(input("enter the number : "))
n = perfectnumber(num)
