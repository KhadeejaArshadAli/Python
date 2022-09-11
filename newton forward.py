x1=float(input("Enter1: "))
delta=0.00000001
x2=x1+delta
x=x1
y1=x**2+3*x-10
x=x2
y2=x**2+3*x-10
d=(y1-y2)/(x1-x2)
print ("slope is",d)          
