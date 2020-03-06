def IsIncreasing(a):
    temp = str(a)
    start = 0
    for i in range(len(temp)):
        if not int(temp[i])>=start:
            return False
        start = int(temp[i])
    return True

def IsDecreasing(a):
    temp = str(a)
    start = 9
    for i in range(len(temp)):
        if not int(temp[i])<=start:
            return False
        start = int(temp[i])
    return True

def IsBouncy(a, b):
    if(a is False and b is False):
        return True
    return False

i = 100
b_counter=0
while(not b_counter/(i-1) == 0.99 ):
    if(IsBouncy(IsIncreasing(i),IsDecreasing(i)) is True):
        b_counter=b_counter+1
    i=i+1



print(i-1)
print(b_counter)
print(b_counter/(i-1))
