#"Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for xxx in numbers:
   Flag = True
   for divisor in range(2, xxx):
      if xxx % divisor == 0:
         Flag = False
         not_primes.append(xxx)
         break
   if Flag == True and xxx != 1:
      primes.append(xxx)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')







