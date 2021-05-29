#2. Write a list comprehension to find factorial of each numbers in a given list L if and only 
#if the numbers are even. For Example: If L = [1,2,3,4] then output should be [2, 24].

import math
list1=[1,2,4,7,15,30]
list2=[]
list2=[math.factorial(i) for i in list1 if(i%2==0)  ]
print(list2) 
