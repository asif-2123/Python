n=int(input("Enter a number: "))

def even_odd(n):
    if n & 1 == 1:
        return "Odd"
    else:
        return "Even"
print(even_odd(n))

