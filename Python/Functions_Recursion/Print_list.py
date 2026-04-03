list=["a","b","c","d","e"]

def print_list(list,index=0):
    if index==len(list):
        return
    print(list[index],end=" ")
    print_list(list,index+1)

print_list(list)
