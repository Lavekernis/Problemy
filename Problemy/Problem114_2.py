

#Wcześniejsza próba implementacji za pomocą rekurecji z zapisywaniem
'''from memorised.decorators import memorise

@memorise()
def possib(n):
    if n < 3:
        return 1
    else:
        sum = 1
        for i in range(0,n-3):
            sum += possib(i)
        return possib(n-1)+sum'''

#Iteracyjna wersja
SIZE = 50
combinations = [0]
#Tworzymy tabelę do zapisu poprzednich sytuacji
for i in range(SIZE):
    combinations.append([0])

#Uzupełniamy powoli tabelę
for n in range(len(combinations)):
		#Dla sytuacji w której mamy n mniejsze niż 3 możliwe miejsca mamy jedną mozliwość i jest nią brak czerwonych kratek
        if n < 3:
            combinations[n] = 1
        else:
            #Sytuację można rozważyć tak jak problem wieży Hanoi, tylko w tym przyadku zrobimy to "iterując rekurencyjnie"
            #dla danego n możemy mieć sytuację w której: 
            # - mamy wypełnione wszystkie bloczki czyli 1
            # - mamy na ostatnim miejscu jeden pusty bloczek, a wiec sytuacja tak naprawdę sprowadza się dla planszy n-1 
            # sytuacja gdy na końcu będą 2, 3, 4, 5, ... wolnych miejsc jest juz zawarta wyżej
            # - dojdziemy do stuacji, gdy n-3-1, to w wolne miejsce po prawej możemy wpisać bloczek (ponieważ są 3 wolne miejsca z odstępem),
            # a więc należy to odpowiednio uwaględnić. Robimy to poprzez warunek sum(combinations[ : n - 3]), który jest zapisany odwrotnie, ponieważ bierze pod uwagę, że nasze
            # rozumowanie prowadzimy od końca, natomiast liczymy od początku
            combinations[n] = combinations[n - 1] + sum(combinations[ : n - 3]) + 1

print(combinations[-1])

