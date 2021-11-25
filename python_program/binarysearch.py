def binary_search(a,search_element,low,high):
    while low<=high:
        mid=(low+high)//2
        if (a[mid]==search_element ):
            return data[mid]
        elif (a[mid]<search_element) :
            low=mid+1
        else:
            high=mid-1
    return 1
data=[14,8,50,26,2,33,41]
search_element=14
size=len(data)
data.sort()
result=binary_search(data,search_element,0,size-1)
if (result==1):
    print("search element not found.")
else:
    print("element is found {}".format(result))
