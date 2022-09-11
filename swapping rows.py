nR1=int(input("enter no of rows for M1: " ))
nC1=int(input("enter no of column for M1: " ))
M1=[]

for (i)in range (nR1):
    a1=[]

    for (j) in range (nC1):
        x=float(input("enter: "))
        a1.append(x)
        
    M1.append(a1)
    
print(M1)
i=int(input("enter the row number to swap: "))
k=int (input("enter the row number to swap with: "))


for j in range(nC1):
    t=M1[i][j]
    M1[i][j]=M1[k][j]
    M1[k][j]=t    
    
print (M1)        

    
    
