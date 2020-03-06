import numpy as np

def IsCorrect(a):
    length = 0
    for i in range(50):
        if(a[i]==1):
            length=length+1
        else:
            if(length<3 and length != 0):
                return False
            length = 0
    if(length<3 and length != 0):
        return False
    return True


combination_counter = 0
a = np.zeros(50)
for j in range(2**50-1):
    if(IsCorrect(a)):
        combination_counter = combination_counter + 1
    for i in range(50):
        if(a[i]==0):
            a[i]=1
            break
        else:
            a[i]=0
    print(a)
combination_counter = combination_counter + 1
print(combination_counter)
