tuple=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number to search: "))  
i=0
while i<len(tuple):
    if tuple[i]==x:
        print("The index of", x, "is: ",i)
        break
    i+=1