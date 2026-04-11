with (open("demo.txt","r")) as f:
    data=f.read()

new_data=data.replace("and","or")
print(new_data)

with (open("demo.txt","w")) as f:
    f.write(new_data)
    f.close()