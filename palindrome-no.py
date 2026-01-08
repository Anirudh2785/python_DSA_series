no = input("enter number : ")
no = (list(map(int,no))) 

a = (no[::-1])
b = (no[0::])

if a == b :
    print("yes, this is a palindrome number.")
elif a != b :
    print("no, this is not a palindrome number.")
else :
    print("error")

