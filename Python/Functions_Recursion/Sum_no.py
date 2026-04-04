n=int(input("Enter no. upto you want sum:"))

def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(n))