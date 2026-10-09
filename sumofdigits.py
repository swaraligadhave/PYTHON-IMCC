n = int(input("Enter digits: "))
sum = 0

while n > 0:
    d = n % 10 # getting the last digit 
    sum = sum + d
    n = n // 10 # for removing last digit

print(sum)
