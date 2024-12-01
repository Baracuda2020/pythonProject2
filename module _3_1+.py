calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return [len(string), string.upper(), string.lower()]


def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [s.lower() for s in list_to_search]
    if string.lower() in list_to_search:
        return True
    else:
        return False


print(string_info('Anakonda'))
print(is_contains('Meymun', ['mun', 'mEyMuN', 'nuMYem']))
print(calls)
