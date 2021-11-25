current=int(input("enter the current unit:"))
if 0<current and current<=100 :
        print("No EB Bill amount")
elif 100<current and current<=200 :
        unit=(current-100)*2.5 
        print("your EB Bill amount",+unit)
elif 200<current and current<=500 :
        unit=(current-100)*3.5
        print("your EB Bill amount",+unit)
elif 500<current and current<=750 :
        unit=(current-100)*4.5
        print("your EB Bill amount",+unit)
elif 750<current and current<=1000 :
        unit=(current-100)*7
        print("your EB Bill amount",+unit)
    
