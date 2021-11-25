def ip_address(ip,count):
    if ((len(ip)==4)) and (not(ip[0]=='0')):         #ip address
            for i in range(0,len(ip)):
                if not(ip[i].isalpha()):
                    ip[i]=int(ip[i])
                    if (0<=ip[i] and ip[i]<=255):
                        count+=1
            return count 
    else:
        return 0; 
ipaddress=input("Enter the ip address:")
ipaddress=ipaddress.split('.')
count=0
result=ip_address(ipaddress,count)
if (result==4):
    if ((1<=ipaddress[0]) and (ipaddress[0]<=126)):
        print("class A ip address")
    elif((128<=ipaddress[0]) and (ipaddress[0]<=191)):
        print("class B ip address")
    elif ((192<=ipaddress[0]) and (ipaddress[0]<=223)):
        print("class C ip address")
    elif ((224<=ipaddress[0]) and (ipaddress[0]<=239)):
        print("class D ip address")
    elif ((240<=ipaddress[0]) and (ipaddress[0]<=255)):
        print("class E ip address")
else:
    print("it is not a valid ip address, to give a proper ip address")
