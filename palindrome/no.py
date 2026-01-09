no = int(input("enter num :"))

a = no 
b = 0 

while a > 0:
    n = a % 10 
    b = b * 10 + n
    a //= 10
if no == b :
    print("True,",no,"is a palindrome num" )
elif no != b :
    print("False,",no,"is a palindrome num")
else :
    print("error")
