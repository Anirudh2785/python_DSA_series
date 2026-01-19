num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

n1 = int(num1*0.5)
n2 = int(num2*0.5)

up = []
down = []

for i in range (1,n1+1) :
    rem1 = num1%i
    if rem1 == 0 :
        div1 = int(num1/i)
        if div1 == i :
            up.append(i)
        else :
            up.append(i)
            up.append(div1)

for o in range (1,n2+1) :
    rem2= num2%o
    if rem2 == 0 :
        div2 = int(num2/o)
        if div2 == o :
            down.append(o)
        else :
            down.append(o)
            down.append(div2)
    else :
        print(end="")

com = set(up) & set(down)

print(com)



