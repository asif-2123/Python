n=int(input("Enter a number to find its factorial: "))
i=1
for i in range(1,n):
    n=n*i
    i+=1
print("The factorial is: ",n)