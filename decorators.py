# -*- config: utf8 -*-


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 == 0 or (result % 3 == 0 and result % 7 == 0) or (result % 3 == 0 and result % 5 == 0) or (
                result % 7 == 0 and result % 5 == 0):
            print('Составное')
        else:
            print('Простое')
        return result
    return wrapper


@is_prime
def sum_three(*args, **kwargs):
    if len(args) != 3:
        print('Должно быть три параметра')
    return sum(args)


result = sum_three(3, 30, 1)
print(result)
