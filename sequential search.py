f="n"
a=[10,20,35,91,64,10,88,72,44,55,90]
v=int(input("enter: "))

for i in range(len(a)):
    if (a[i]==v):
        print("Found at position ",i+1)
        f="y"
        
    
if(f!="y"):
    print("Not Found")
