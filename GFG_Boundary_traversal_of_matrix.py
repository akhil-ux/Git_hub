n = 4
m = 4
matrix= [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15,16]]
border_element=[]
i,j=0,1
while(i!=0 and j!=0):
    if(i==0 and j==1):
        border_element.append(matrix[i][j])
        j+=1
    if(i==0 and j==m-1):
        i+=1
        j+=1
        border_element.append(matrix[i][j])
    if(i==n-1 and j==m-1):
        j-=1
        border_element.append(matrix[i][j])
    if(i==n-1 and j==0):
        i-=1
        border_element.append(matrix[i][j])
print(border_element)

    
    

