#Write a function called is_unique. This function should take a string and should check 
#whether all characters of the string is unique/not. Example: If the input string is 
#“abcd”, all characters are unique, hence it should return True. Another example, if the 
#string is “abaa”, then this function should return False.
#1. Create a List L of size 10 with random strings of length > 1.
#2. Write a python snippet to check is_unique nature for all elements of L. (Hint: 
#Use map function)
#3. Apply filter function, to get only unique elements from L

def is_unique(name):
    for i in range(0,len(name)):
        for j in range(i+1,len(name)):
            if(name[i]==name[j]):
              return False
            else:
                return True
ls =["ron","bam","mes","joi","kri"]
fun=lambda x:is_unique(x)
map_obj=map(fun,ls)
print(list(map_obj))
filter_obj=filter(fun,ls)
print(list(filter_obj))
