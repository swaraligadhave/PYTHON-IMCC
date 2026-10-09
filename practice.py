#print the table of odd numbers from 1 to 10

for i in range(1,11):
    for j in range(1,11):
        if i % 2 != 0:
            print(i, "x" ,j , "=" ,i*j) # because we have to print table of odd numbers
    print()

        

