word = input("enter word : ") 

a = (word[::-1])
b = (word[0::])

if a == b :
    print("yes,", word, "is a palindrome word.")
elif a != b :
    print("no,", word, " is not a palindrome word.")
else :
    print("error")

