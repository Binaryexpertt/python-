"""The Company charges its subscribers according to the following criteria:
    Subscriber Type    Location   Consumption(normal)  Consumption(excess) Tax  Discount
    1.Residential      1.Center   50<=100000            50>150000          %18  None
                       2.Village  70<=100000            70>130000          %15  NONE
                       3.Hamlet   80<=100000            80>110000          %12  %5
            
    2.Business         1.Center   100<=120000           100>200000         %20  %3
                       2.Village  150<=110000           150>180000         %18 %5
                       3.Hamlet   200<=100000           200>160000         %16  %8
    
According to this table, create a flowchart that calculates the bill to be paid by a person
based on the information entered from the keyboard(T:type A:area H:consumption) and displays it
on the screen."""


s=int(input("Subcriber Type: (Residental=1 / Business=2)=="))
l=int(input("Location: (Center=1 / Village=2 / Hamlet=3)=="))
c=int(input("Consumption: "))

if c<=50 and s==1 and l==1:
    b=c*100000+0.18*c*100000
    print(b)
if c>50 and s==1 and l==1: 
    b=1.18*c*150000
    print(b)
if  s==1 and l==2 and c<=70 :
    b=1.15*c*100000
    print(b)
if  s==1 and l==2 and c>70 :
    b=1.15*c*130000
    print(b)
if s==1 and l==3 and c<=80:
    b=1.12*c*100000-c*100000*0.05
    print(b)
if s==1 and l==3 and c>80:
    b=1.12*c*110000-c*110000*0.05
    print(b)
if  s==2 and l==1 and c<=100 :
    b=1.2*c*120000-c*120000*0.03
    print(b)
if  s==2 and l==1 and c>100 :
    b=1.2*c*200000-c*200000*0.03
    print(b)
if  s==2 and l==2 and c<=150 :
    b=1.18*c*110000-0.05*c*110000
    print(b)
if  s==2 and l==2 and c>150 :
    b=1.18*c*180000-0.05*c*180000
    print(b)
if  s==2 and l==3 and c<=200 :
    b=1.16*c*100000-0.08*c*100000
    print(b)
if  s==2 and l==3 and c>200 :
    b=1.16*c*160000-0.08*c*160000
    print(b)
    

