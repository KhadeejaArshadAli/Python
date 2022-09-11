import sys
a=float(input("Enter the lower limt: "))
b=float(input("Enter the upper limt: "))

x=a
fa=x**2+3*x-10

x=b
fb=x**2+3*x-10
f=fa * fb

if(f>0):
    print("Given range doesnot contain a solution")
    sys.exit()
else:
    fc=2
    k=1
    while(fc!=0):
        c=(a+b)/2
        x=c
        fc=x**2+3*x-10
        f=fa*fc
        print("k={0}---> a={1}      c={2}      b={3}".format(k,a,b,c))
        if(f<0):
            b=c
        else:
            a=c
            
        k+=1
print("Solution of the given eqution is{}".format(c))           
    

