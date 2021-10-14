def square_number(nums):
    for i in nums:
        yield i*i


nums=[1,2,3,4,5,6,7,8,9]
x=square_number(nums)

#single value at a time 
#print(next(x))
#print(next(x))

#for loop to generate all the value
for i in x:
    print(i)