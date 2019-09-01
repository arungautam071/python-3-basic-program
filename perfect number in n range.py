a=[]
lower =int(input("lower"))
upper=int(input("upper"))
for num in range(lower,upper+1):
    result=0
    for i in range(1,num):
        if(num%i==0):
            result=result+i
    if(num==result):
        a.append(result)
print(a)        