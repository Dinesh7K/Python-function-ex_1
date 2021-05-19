Project 5: 
Star Genera?on: Create a python func,on which takes a number N and generates following star 
pacern accordingly. N ranges from 1 to any posi,ve number. Make sure if N is not passed as 
argument while calling func,on, it should take 3 as it’s default value. 
Example: N = 4 
Output: 
* 
@@ 
*** 
@@@@


def star(N):
    for i in range(1,N+1):
        if(i%2==0):
            print('@'*i)
        else:
            print('*'*i)
            
print(star(4))
