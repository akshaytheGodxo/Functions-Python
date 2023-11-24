def eligbilty(age):
    if age >= 18:
        return True
    else:
        return False
x = int(input("Enter the age of the candidate: "))

result = eligbilty(x)
if result:
    print("He/She is eligible!")
else:
    print("He/She is not eligible")