''' s={2,3}     #output : error
 print(s*3)

a=("A")
b = "B"         #AB
print(a+b)

a='pythonHub'   #True
b="pythonHub"
print(a==b)'''

for i in range(len('python')):     #str error
    python[i]=i
#print('python')
print(i)

'''x='pqrs'
for i in range(len(x)):     #pqrs
    x[i].upper()
print(x)

i=0
while i<5:
    print(i,end=" ")    #0 1 2
    i+=1
    if i==3:
        break
else:
    print(0)

x=0             #21
while x<20:
    x=x+3
print(x)

y=10            #syntaxerror
x=y += 2
print(x) 


a=2+2j           #(2+5j)
b=3j
print(a+b)

myDict={'a':1,'b':2,'a':3}      #a is not defined
print(myDict[a])'''

#s=set('abcd')                   #true
#print('a' in s)'''

#tup=(0,1,2,3)                   #(3,2,1,0)
#print(tup[::-1])