nR1=int(input("enter no of rows for x: " ))
nC1=int(input("enter no of column for x: " ))
X=[]

for (j)in range (nR1):
    a1=[]

    for (i) in range (nC1):
        x=float(input("enter: "))
        a1.append(x)
    X.append(a1)
print(X)


nR2=int(input("enter no of rows for y: "))
nC2=int(input("enter no of column for y: "))
    
Y=[]

for (j)in range (nR2):
    a2=[]
    for (i) in range (nC2):
        x=float(input("enter: "))
        a2.append(x)
    Y.append(a2)
print(Y)        

    
nR=nR1
nC=nC1

result=[]

for (j)in range (nR):
    a1=[]

    for (i) in range (nC):
            z=0
            a1.append(z)
        
    result.append(a1)
for i in range (len(X)):
    for j in range (len(X[0])):
        result[i][j]=X[i][j]+Y[i][j]

print(result)       
        

