arr= [ 1, 2, 3, 4, 5, 5  ]
key=5
l=[]
for i in range(len(arr)):
    if(arr[i]==key):
        l.append(i)
print(l[0],l[1])
