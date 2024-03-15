A = [30 ,66 ,78 ,74 ,91 ,76 ,60 ,20 ,13 ,67]
result_list = []
A = A[::-1]
i =0
j=1
mx=-999999999
for j in range(1,len(A)):
    if(i==0):
        result_list.append(A[i])
        mx=A[i]
    if(A[i]>A[j] and A[i]>mx):
        mx=A[i]
        result_list.append(mx)
    i+=1
print(result_list[::-1])