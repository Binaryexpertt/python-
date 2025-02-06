"""Example: The gender, year of birth, marital status and school of graduation information
of N workers working in a factory are entered from the keyboard.Accordingly, a flow chart that 
calculates the person's age and finds how many women and men there are between 20 and 30
how many are high school graduates, and finds the totals of school types by gender and he totals of
gender by marital status."""

"""gender: 0=female  1= male
birth year=byear
marital status=msta 0= single 1= married
graduated school 0=primary school 1=high school 2=university"""


m=0 #male headcount
f=0 #female headcount
s=0 #single headcount
mar=0 #married headcount
mmar=0 #male and married headcount
ms=0 #male and single headcount
fs=0 #female and single headcount
fmar=0 #female and married headcount
hs=0 #high school headcount
fps=0 #female and primary school
fhs=0 #female and high school
fu=0 #female and university
mps=0 #male and primary school
mhs=0 #male and high school
mu=0 #male and university
n=int(input("Work Force: "))
gender=[0]*n
byear=[0]*n
age=[0]*n
msta=[0]*n
school=[0]*n
for i in range(n):
    print("Gender (Female=0 / Male=1):")
    gender[i]=int(input())
    print("Birth year:")
    byear[i]=int(input())
    print("Marital status (Single=0 / Married=1):")
    msta[i]=int(input())
    print("Graduated school (Primary School=0 / High School=1 / University=2):")
    school[i]=int(input())
    age[i]=2025-byear[i]
    if age[i] >=20 and age[i]<=30 and gender[i]==1:
        m = m+1
    if age[i] >=20 and age [i]<=30 and gender[i]==0:
        f+=1
    if age[i] >= 20 and age[i]<=30 and msta[i]==0:
        s += 1
    if age[i]>=20 and age[i]<=30 and msta[i]==1:
        mar += 1
    if age[i]>=20 and age[i]<=30 and gender[i]==1 and school[i]==0:
        mps+=1
    if age[i]>=20 and age[i]<=30 and gender[i]==1 and school[i]==1:
        mhs+=1
    if age[i]>=20 and age[i]<=30 and gender[i]==1 and school[i]==2:
        mu+=1
    if age[i]>=20 and age[i]<=30 and gender[i]==0 and school[i]==0:
        fps+=1
    if age[i]>=20 and age[i]<=30 and gender[i]==0 and school[i]==1:
        fhs+=1
    if age[i]>=20 and age[i]<=30 and gender[i]==0 and school[i]==2:
        fu+=1
    if age[i]>=20 and age[i]<=30 and gender[i]==1 and msta[i]==0:
        ms+=1
    if age[i]>=20 and age[i]<=30 and gender[i]==1 and msta[i]==1:
        mmar+=1
    if age[i]>=20 and age[i]<=30 and gender[i]==0 and msta[i]==0:
        fs+=1
    if age[i]>=20 and age[i]<=30 and gender[i]==0 and msta[i]==1:
        fmar+=1
print("Male Count= ",m)
print("Female Count= ",f)
print("Single Count= ",s)
print("Married Count= ",mar)
print("Male and Primary School Graduated Count= ",mps)
print("Male and High School Graduated Count= ",mhs)
print("Male and University Graduated Count= ",mu)
print("Female and Primary School Graduated Count= ",fps)
print("Female and High School Graduated Count= ",fhs)
print("Female and University Graduated Count= ",fu)
print("Male and Single Count= ",ms)
print("Male and Married Graduated Count= ",mmar)
print("Female and Single Count= ",fs)
print("Female and Married Count= ",fmar)