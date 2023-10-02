colors = "AA"
Alice=0
Bob=0
for i in range(1,len(colors)-1):
    if(colors[i]=='A' and colors[i-1]=='A' and colors[i+1]=='A'):
        Alice+=1
    if(colors[i]=='B' and colors[i-1]=='B' and colors[i+1]=='B'):
        Bob+=1
if(Alice>Bob):
    print(True)
else:
    print(False)

