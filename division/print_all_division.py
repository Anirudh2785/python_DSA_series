num = int(input("enter number : "))
n = num + 1

print("Divisors of ",num," are : ", end="")

for i in range ( 1, n):
    remainder = num % i 
    if remainder == 0 :
        print( i, end=", " )
    else :
        print(end="")

