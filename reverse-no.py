# no = input("enter number :")
# no = (list(map(int,no))) 
# print(no[::-1])

n = int(input("enter number : "))

b = 0 

while n > 0 :
    a = n % 10  
    b = b * 10 + a 
    n//=10

print("So the no. : ",b)