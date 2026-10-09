# #print the following pattern
#  *
# ##
# ***
# ####
# *****
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1,  2 *i): # 2 * i is used for j for the spacing purpose
        if i % 2 == 0:
            print("#", end="")
        else:
            print("*", end="")
    print() 

for i in range(n-1, 0, -1): # n-1 is used for spaces 
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if i % 2 == 0:
            print("#", end="")
        else:
            print("*", end="")
    print()