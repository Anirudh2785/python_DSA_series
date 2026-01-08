word = input("enter word : ")
word = (list(map(str,word))) 

a = (word[::-1])
b = (word[0::])

if a == b :
    print("yes, this is a palindrome word.")
elif a != b :
    print("no, this is not a palindrome word.")
else :
    print("error")

