import numpy as np

#Rozmiar programu
SIZE = 50

#Ilośc kombinacji
combination_counter = 0

#Funkcja sprawdzająca czy liczba odpowiadająca ułożeniu spełnia odpowiednie warunki
def IsCorrect(a):
    length = 0
    for i in range(SIZE):
        if(a[i]==1):
            length=length+1
        else:
            if(length<3 and length != 0):
                return False
            length = 0
    if(length<3 and length != 0):
        return False
    return True


a = np.zeros(SIZE)
for j in range(2**SIZE-1):
    if(IsCorrect(a)):
        combination_counter = combination_counter + 1
        print(a)
    for i in range(SIZE):
        if(a[i]==0):
            a[i]=1
            break
        else:
            a[i]=0

#Inkremenctacja - pętla nie uwględnia sytuacji całkowitego wypełnienia przez jedynki
combination_counter = combination_counter + 1
print(combination_counter)
