#3. Write a generator to get even numbers from 1 to infinity. 

n=int(input("Enter the limit:"))
Gen_val=(i for i in range(0,n+1) if(i%2==0))
for val in Gen_val:
    print(val)
