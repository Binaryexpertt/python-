"""The company calculates the expenses of its subscribes as follows:
    It examines its customers in 3 groups:
        Subscriber Type          Normal                 Increased
        Residence:1           50kW-100000             Over 50kW - 150000
        Business:2            150kW-150000            Over 150kW-200000
        Industry:3            100kW-75000             Over 100kW-100000
    Accordingly, the flow chart to calculate the amount to be paid by the person with %18 tax."""
    
print("Select subscriber type: (Residence=1, Business=2, Industry=3)== ")
n=int(input())
print("Consumption amount=    ")
y=int(input())
if n==1 and y<=50:
    c=1.18*y*100000
    print(c)
if n==1 and y>50:
    c=1.18*y*150000
    print(c)
if n==2 and y<=150:
    c=1.18*y*150000
    print(c)
if n==2 and y>150:
    c=1.18*y*200000
    print(c)
if n==3 and y<=100:
    c=1.18*y*75000
    print(c)
if n==3 and y>100:
    c=1.18*y*100000
    print(c)
    
    

