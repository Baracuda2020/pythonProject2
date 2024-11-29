# "Распаковка позиционных параметров"

values_list = [9, 'boom', True]
values_dict = {'a': 777, 'b': 'old', 'c': True}
values_list_2 = [54.32, 'Elefant']

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(*[6])
print_params(list[2, 3, 4])
print_params(2, 'xxx', c=False)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
