instruction=["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
values=[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
d={}
for i in range(1,len(instruction)):
    if(instruction[i]=="put"):
        d[values[i][0]]=values[i][1]
    if(instruction[i]=="get"):
        if(values[i][0] in d):
            print(d[values[i][0]])
        else:
            print(-1)
    if(instruction[i]=="remove"):
        if(values[i][0] in d):
            del d[values[i][0]]
        else:
            print(-1)        
print(d)



