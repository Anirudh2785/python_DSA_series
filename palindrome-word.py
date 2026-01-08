word = input("enter number :")
word = (list(map(str,word))) 

a = (word[::-1])
b = (word[0::])

if a == b :
    print("true")
elif a != b :
    print("false")
else :
    print("error")

