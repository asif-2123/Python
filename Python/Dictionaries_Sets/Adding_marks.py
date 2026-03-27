marks={}

x=int(input("Enter physics marks: "))
marks.update({"Physics":x})

y=int(input("Enter chemistry marks: "))
marks.update({"Chemistry":y})

z=int(input("Enter maths marks: "))
marks.update({"Maths":z})

print(marks)