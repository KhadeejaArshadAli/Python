#def MatrixInput(nr,nc,message=":"):
nr=3
nc=4
M=[1,2,3,4],[5,6,7,8],[9,10,11,12]


    #for (r)in range (nr):
       # a=[]

        #for (c) in range (nc):
           # x=float(input("enter a value for matrix "+message))
            #a.append(x)
       # M.append(a)
    #return(M)
pr=int(input("Enter pivot row number: "))
pc=int(input ("Enter pivot column number: "))
pivotelement =M[pr][pc]
print(pivotelement)
for c in range (nc):
    M[pr][pc]=M[pr][pc]/pivotelement
print(M[pr][c])
  

###
#while((pr>=0) and (pc>=0):
      #pivotElement=M[pr][pc]
#for c in range (nc):
    #M[pr][c]=M[pr][c]/pivot element
  
#for r in ramge(nr):
      #if(r!=pr):
      #pivot element=M[r][pc]
    #for c in range (nc):
     #   print("%10.3f" %(M[r][c], end="  ")
    #print()
#pr=int(input("Enter pivot row number: "))
#pc=int(input ("Enter pivot column number: "))
#pr-=1
#pc-=1
              
