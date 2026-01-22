a = 4
i = 0 

while i <= 4 :
    j = 0
    while j <= i :
        print(end="  ")
        j += 1
    k = 4  + a
    while k >= i :
        print("*",end=" ")
        k -= 1
    print()
    i += 1
    a -= 1

