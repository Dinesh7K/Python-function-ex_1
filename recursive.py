#Write python recursive function to perform multiplication of all elements of list L.

def recusrive(l):
    if(len(l) == 1):
        return l[0]
    else:
        value = l.pop()
        return value*recusrive(l)


list1 = [1, 2, 10, 5, 6]
    
print(recusrive(list1))
