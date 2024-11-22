from itertools import count

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info():
    count_calls()
    string = 'Anakonda'
    string_2 = len(string)
    string_3 = string.upper()
    string_4 = string.lower()
    string = tuple([string_2, string_3, string_4])
    return string


def is_contains():
    count_calls()
    string = 'Meymun'
    list_to_search = ['mun', 'mEyMuN', 'nuMYem']
    list_to_search = [s.lower() for s in list_to_search]
    if string.lower() in list_to_search:
        return True
    else:
        return False


print(string_info())
print(is_contains())
print(calls)
