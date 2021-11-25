arr=[]
n=int(input("enter the no.of element:"))
result=0
for i in range(0,n):
    tmp=int(input())
    arr.append(tmp)
    arr.sort()

for i in range(0,3):
    temp=arr[i]+arr[i+1]
    arr.append(temp)
    arr.pop(0)
    arr.pop(1)
    

print(arr)


