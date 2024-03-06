# -*- config: utf8 -*-


def is_prime(func):
    def wrapper(*args, **kwargs):
        primes = []
        result = func(*args, **kwargs)
        for num in range(2, result + 1):
            for i in range(2, int(num / 2) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
        if result == primes[-1]:
            print('Простое')
        else:
            print('Составное')
        return result, primes
    return wrapper


@is_prime
def sum_three(*args, **kwargs):
    if len(args) != 3:
        print('Должно быть три параметра')
    return sum(args)


result = sum_three(50, 100, 19)
print(result)

