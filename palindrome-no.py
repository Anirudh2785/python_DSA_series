no = input("enter number :")
no = (list(map(int,no))) 

a = (no[::-1])
b = (no[0::])

if a == b :
    print("true")
elif a != b :
    print("false")
else :
    print("error")

