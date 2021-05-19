Project: 2 
Sam College of Cartoon 
You have to create different func,ons for Sam’s college of cartoon. Please find the func,ons list 
below - 
• Give me a random cartoon character: - Func?on 1 
• This func,on should take N arguments, where N is not fixed and ranges from 0 to 
many. This func,on should return a random character from the N argument. 
• For example: If arguments are “Dora”, “Shin Chan”, “Poke mon” etc… this func,on 
should return any one of the above character. (Eg: “Dora”) and must be random. 
• If the argument length for the func,on is 0, then this func,on should return False 
(boolean) as output. 
• Swap the cartoon character: - Func?on 2 
• This func,on should call Func,on 1 (above) and if func,on 1 returns False, then this 
func,on should also return False. 
• Else, get the character and swap the lecers of characters. (Upper case to lower case 
and vice versa) 
• For example: if the func,on gives you “Dora”, then output should be “dORA”. 
• Return the swapped output as result. • Mul?ply the swap: - Func?on 3 
• This func,on should take 2 arguments. First one is cartoon_character and second one as 
mul,plier. If the user is not specifying mul,plier value it should take 3. Else if user 
specified any value, take that value into account. 
• Mul,ply the cartoon_character (first argument) with the mul,plier value given. 
• Example: If cartoon_character is “Dora”, mul,plier is 5, then DoraDoraDoraDoraDora 
should be the output. 
• Main func?on: - Func?on 4 
• Create a func,on with name main() 
• Call func,on 2, if it is not returning False, pass the output of func,on 2 as a first 
parameter to func,on 3 and get the output from F3 and print it. 
• If call to func,on 2, gives False, print the message “Oops! No cartoon selected”.


import random

def character(N):
    name=random.choice(N)
    return name
    if(len(name==0)):
        return False

def swap_character():
    
    if(call==False):
        return False
    else:
         return call.swapcase()
def multiply(cartoon_character,multiplier=3):
    
    
    print(cartoon_character*5)

def main1():
    call1=swap_character()
    if(call1==False):
        print("oops No cartoon selected")
    else:
        return(multiply(call1))
call=character(["Dora","Pokemoon","Chin shan"])
print(call)
print(swap_character())
main1()
