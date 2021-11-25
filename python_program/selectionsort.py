def selection_sort(a,length):
    for i in range(length):
        min_idx=i;
        for j in range(i+1,length):
            if a[j]<a[min_idx]:
                min_idx=j
        a[i],a[min_idx]=a[min_idx],a[i]
       #temp=a[min_idx]
       #a[min_idx]=a[i]
       #a[i]=temp
data = [10,5,2,17,8,4,12]
length = len(data)
#selection_sort(data,length)
data.sort()
print(data)