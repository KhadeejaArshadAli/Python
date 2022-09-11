def MatrixInput(numberofrows,numberofcolumn,message=":"):
    M=[]


    for (j)in range (numberofrows):
        a=[]

        for (i) in range (numberofcolumn):
            x=float(input("enter a value for matrix "+message))
            a.append(x)
        M.append(a)
    return(M)   


#------------------------------------------------------------






x=MatrixInput(3,2)
print(x)
y=MatrixInput(2,3,"Y:")
print(y)

nR=3
nC=3

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

for r in result:
    print(r)
        
   
