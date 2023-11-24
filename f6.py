def checkPrime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
            
    if count == 2:
        print("It's a Prime Number!")
    else:
        print("It's not a Prime Number!")
        
a = int(input("Enter the number: "))
checkPrime(a)