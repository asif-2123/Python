def check_line():
    word="doing"
    data=True
    line_no=1
    with open("demo.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
            line_no+=1
    f.close()

check_line()
                