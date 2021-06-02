#Write python script to add elements of list L using reduce() function.

from functools import reduce
ls=[2,3,5,64,2,6,75]
fun=lambda x,y:x+y
reduce_obj=reduce(fun,ls)
print(reduce_obj)
