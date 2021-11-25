arr=[7,0,2,0,3,0,4,0,5]
temp=0
for i in range(0,len(arr)) :
    if arr[i] == 0 :
        #temp=arr[i]
        arr.remove(arr[i])
        arr.append(temp)
print(arr)
