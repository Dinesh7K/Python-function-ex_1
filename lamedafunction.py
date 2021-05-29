#1. Create a lambda function which takes two inputs X and Y and performs X power Y 
#operation and returns the output. For Example: If X is 2 and Y is 3, then 2 power 3 = 2 
#* 2 * 2 = 8.


power_fun=lambda x, y :pow(x,y)
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
output=power_fun(a,b)
print(output)
