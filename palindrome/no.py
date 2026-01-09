no = int(input("enter num :"))

a = no 
b = 0 

while a > 0:
    n = a % 10 
    b = b*10+n
    a//=10
if a == b :
    print("True,",no)
else :
     print("False,",no)
