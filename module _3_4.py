
#def test_func(*params):
#    print('Тип', type(params))
#    print('Аргумент', params)


#test_func(1,2,3,4)

#def summator(txt,*values, type='sum'):
#    s = 0
#    for i in values:
#        s += i
#    return f'{txt}{s} {type}'

#print(summator(f'Сумма чисел: ', 1,2,3,4,5, type='summator'))


#def info(**values):
#    print('Тип', type(values))
#    print('Аргумент', values)
#    for key, value in values.items():
#        print(key, value)


#info(name='Patrik', course='Python')


def info(value, *types, **values):
    print('Тип', type(values))
    print('Аргумент', values)
    for key, value in values.items():
        print(key, value)
    print(types)
    print(value, types, values)


info('Пример использования:',1,2,3,4, name='Patrik', course='Python')