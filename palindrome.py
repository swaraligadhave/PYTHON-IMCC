# accept the name and check if it is a palindrome
name = input("Enter a name: ")
reverse = ""

for i in name:
    reverse = i + reverse

if name == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")