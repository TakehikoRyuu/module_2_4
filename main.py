# Цикл for. Элементы списка. Полезные функции в цикле 2.4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
count = 0
for i in numbers[1:]:
    prosto = True
    for j in range(2, i):
        if i % j == 0:
            prosto = False
            not_primes.append(i)
            break
    if prosto:
        primes.append(i)
print('primes: ', primes)
print('not_primes: ', not_primes)
