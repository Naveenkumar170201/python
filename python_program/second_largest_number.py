list1 = [10,5,17,44,99,58,3,14]
firstmx = max(list1[0],list1[1])
secondmx = min(list1[0],list1[1])
n = len(list1)
for i in range(2,n):
    if list1[i] > firstmx:
        secondmx = firstmx
        firstmx = list1[i]
    elif list1[i] >  secondmx and firstmx != list1[i]:
        secondmx = list1[i]
print("second highest number is :", str(secondmx))    
