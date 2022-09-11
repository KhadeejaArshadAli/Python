def selection_sort(a):
    

    for i in range(len(a)):
        minpos=i
        for j in range(i+1,len(a)):
            if (a[j]<a[minpos]):
                minpos=j

        temp=a[i]
        a[i]=a[minpos]
        a[minpos]=temp
    return(a)



print(selection_sort([1,8,10,5,2,5,9]))

