"""Service year,net salary, number of children, and gender information belonging to 10 workers
are entered from the keyboard.According to this:
    Service Year:                            Bonus:
Less than or equal to 6 years       %22 of net's half of 3 times
Between 7-14 years                  2 times net's 1/4 of 5 times
Between 15-19 years                 2/3 of net's 7 times
20 years and above                  3 times net

Male employees wil receive  housing allowance of %12 of the bonus as an additional benefit.
Employees with 1 child will receive %75 of 1/10 net.
Employees with 2 or more children will receive %50 of 2/10 of net.Accordingly,calculate the bonus and
print it to the screen with a flowchart"""

w=3 #workforce
sy=0 #service year
ns=0 #net salary
c=0 #number of children
g=0 #gender information
a=0 #house allowance
i=1
sy=[0]*w
ns=[0]*w
c=[0]*w
g=[0]*w
for i in range(w+1):
    print(i+1,".worker service year= ")
    sy[i]= int (input( ))
    print(i+1,".worker net salary=  ")
    ns[i]=int(input())
    print(i+1,".workers number of children=  ")
    c[i]=int(input())
    print(i+1,".worker gender information: (Female=0 / Male=1)=  ")
    g[i]=int(input())
    
    if sy[i]<=6 and c[i]==1 and g[i]==1:
        b=ns*int(0.33)
        a=b*int(0.12)
        print(a+b)
    if sy[i]<=6 and c[i]==1 and g[i]==0:
        b=ns*0.33
        print(b)
    if sy[i]<=6 and c[i]>=2 and g[i]==1:
        b=ns*0.33+ns*0.1
        a=b*0.12
        print(a+b)
    if sy[i]<=6 and c[i]>=2 and g[i]==0:
        b=ns*0.33+ns*0.1
    if sy[i]>=7 and sy[i]<=14 and c[i]==1 and g==1:
        b=ns*2.5+ns*0.075
        a=b*0.12
        print(a+b)
    if sy[i]>=7 and sy[i]<=14 and c[i]==1 and g[i]==0:
        b=ns*2.5+ns*0.075
        print(b)
    if sy[i]>=7 and sy[i]<=14 and c[i]>=2 and g[i]==1:
        b=ns*2.5+ns*0.1
        a=b*0.12
        print(a+b)
    if sy[i]>=7 and sy[i]<=14 and c[i]>=2 and g[i]==0:
        b=ns*2.5+ns*0.1
    if sy[i]>=15 and sy[i]<=19 and c[i]==1 and g[i]==1:
        b=ns*14/3+ns*0.075
        a=b*0.12
        print(a+b)
    if sy[i]>=15 and sy[i]<=19 and c[i]==1 and g[i]==0:
        b=ns*14/3+ns*0.075
    if sy[i]>=15 and sy[i]<=19 and c[i]>=2 and g[i]==1:
        b=ns*14/3+ns*0.1
        a=b*0.12
        print(a+b)
    if sy[i]>=15 and sy[i]<=19 and c[i]>=2 and g[i]==0 :
         b=ns*14/3+ns*0.075
    if sy[i]>=20 and c[i]==1 and g[i]==1:
         b=ns*3+ns*0.075
         a=b*0.12
         print(a+b)
    if sy[i]>=20 and c[i]==1 and g[i]==0:
         b=ns*3+ns*0.075
    if sy[i]>=20 and c[i]>=2 and g[i]==1:
         b=ns*3+ns*0.1
         a=b*0.012
         print(a+b)
    if sy[i]>=20 and c[i]>=2 and g[i]==0:
         b=ns*3+ns*0.075
    
    
    
    
        
    
    
    

