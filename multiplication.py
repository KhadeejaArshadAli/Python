import sys
nR1=int(input("enter no of rows for M1: " ))
nC1=int(input("enter no of column for M1: " ))
x=[]

for (j)in range (nR1):
    a1=[]

    for (i) in range (nC1):
        z=float(input("enter: "))
        a1.append(z)
        
    x.append(a1)


nR2=int(input("enter no of rows for M2: "))
nC2=int(input("enter no of column for M2: "))
if(nR2!=nC1):
    print("ERROR CAN'T BE MULTIPLIED")
    sys.exit()

y=[]

for (j)in range (nR2):
    a2=[]
    
    for (i) in range (nC2):
        z=float(input("enter: "))
        a2.append(z)
        
    y.append(a2)
    

nR=nR1
nC=nC2

result=[]

for (j)in range (nR):
    a1=[]

    for (i) in range (nC):
            z=0
            a1.append(z)
        
    result.append(a1)

for i in range (len(x)):  #rows
     for j in range (len(y[0])): #columns
        for k in range(len(y)): #rows
            result[i][j]+=x[i][k]*y[k][j]


print(result)
        
   
