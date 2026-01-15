num = int(input("enter number : "))

n = int(num**0.5)
no = n + 1

print("Divisors of ",num," are : ", end="")

sorting = []

for i in range ( 1, no ):
    rem = num % i
    if rem == 0:
        div = num  // i 
        if i == div :
            sorting.append(i)
        else:
            sorting.append(i)
            sorting.append(div)
    else:
        print(end="")

sorting.sort()

for a in sorting:
    print(a , end=" , ")
