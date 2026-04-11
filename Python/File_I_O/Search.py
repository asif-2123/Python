with (open("demo.txt","r")) as f:
    data=f.read()
    if(data.find("doing")!=-1):
        print("Found")
    else:
        print("Not found")
f.close()