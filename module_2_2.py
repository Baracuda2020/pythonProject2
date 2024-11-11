# Все ли равны
first = 24
second = 36
third = 55
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second and first != third and second != third:
    print(0)