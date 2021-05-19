Project 4: 
Be Posi?ve! Create a func,on to sum up all posi,ve argument inputs. Inputs ranges from 0 to N, 
where N can be any posi,ve number.

def add(n):
    s=0
    for i in range(0,n+1,1):
        s=s+i
    return s
no=eval(input("Enter the number:"))
print(add(no))
