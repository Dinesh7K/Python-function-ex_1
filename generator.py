#Write a simple generator which can give prime numbers from range 1 to 5000.



def prime_gen():

 for Number in range (1, 5000):
    count=0
   
    
    for i in range(2, Number):
        if(Number % i == 0):
           count+=1
           break
        
    if(count==0 and Number!=1):
        yield(Number)       

for val in prime_gen():
    print (val)
