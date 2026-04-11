count = 0
with open('num.txt', 'r') as f:
    data = f.read()
    j = data.split(",")
    for i in j:
        if(int(i) % 2 == 0):
            count += 1
print(count)