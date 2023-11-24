def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact
x = int(input("Enter a range: "))
ans = {}
for i in range(1 , x+1):
    st = factorial(i)
    ans[i] = st
    
print(ans)