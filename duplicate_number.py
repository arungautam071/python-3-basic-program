a=[] #empty list1
d=[] #empty list2 for final list to show duplicate number
print("enter the number of elements you want to insert")
number=int(input()) #take number of elements in list
for i in range(number):
    data=int(input()) #take elements for list
    a.append(data)    #add elements in list1
print(a) #print the lsit1
alen=len(a) #finding the length of list1
for i in range(alen):
    for j in range(i+1,alen):
        if(a[i]==a[j]): #compare the elements of list
            dom=a[i]
            d.append(dom)
print("the duplicate number are",d)  #print the final list2          
            


