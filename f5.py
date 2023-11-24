def checkEven(num):
    if num%2 == 0:
        return True
    else:
        return False

x = float(input("Enter the number:  "))

result = checkEven(x)
if result:
    print("It is even!")
    
else:
    print("It is odd!")