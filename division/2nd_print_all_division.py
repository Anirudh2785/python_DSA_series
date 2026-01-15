num = int(input("enter number : "))

n = int(num**0.5)
no = n + 1

print("Divisors of ",num," are : ", end="")

for i in range (1 , no):
    rem = num % i
    if rem == 0:
        div = int( num / i) 
        if i == div :
            print(i,end=" , ")
        else:
            print(i,",",div,end=" , ")
        
    else:
        print(end="")
