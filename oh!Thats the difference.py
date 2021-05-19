Project 3: 
Oh! That’s the difference! 
Create a func,on difference which takes a string S and character K. Find the difference between 
first occurrence of K and last occurrence of K in string S. Convert the input to lower case before 
processing. 
Check for following condi,ons : 
1. If K not occurred in S, return “K not found in S”. 
2. If K occurred only once in S, return “Difference can’t be calculated”. 
3. If K occurs more than once, return count of difference. 
Sample I/O: 
• Input: S= ‘talentpy', K=‘a’ => output: “Difference can’t be calculated”, 
• Input: S=“science”, K=‘c’ => output: 3.

def fun(s,k):
    
    string=s.lower()
    charac=k.lower()
    count=0
    for _ in string:
        
        if(_==charac):
          count=count+1
    if count==1:
        print("Difference cant be calculated")
    elif(count>1):
        return count
    else:
        print("K not found in S")
i=input("Enter the string:")
j=input("Enter the character:")
print(fun(i,j))
