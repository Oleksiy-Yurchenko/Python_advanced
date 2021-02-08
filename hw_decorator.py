import functools


# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.

def divide_by_hundred(my_func):
    """The decorator function which checks input for a valid type (int or float) and then checks if the result
        of my_func is divided by 100 without rest or not."""
    @functools.wraps(my_func)
    def is_hundred_div(arg_one, arg_two):
        if not isinstance(arg_one, int) or not isinstance(arg_one, int): #or
            if not isinstance(arg_one, float) or not isinstance(arg_one, float):
                raise ValueError("Only integer and float types are supported.")
        result =  my_func(arg_one, arg_two) % 100
        if not result:
            print('We are OK!')
        else:
            print('Bad news guys, we got {0}'.format(result))
    return is_hundred_div

@divide_by_hundred
def random_number_generator(arg_one, arg_two):
    return arg_one * arg_two

random_number_generator(25,12)
random_number_generator(7.1, 25.5)


# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

def validate_input_decorator(my_func):
    """The decorator function which checks the type of input argument."""
    @functools.wraps(my_func)
    def int_input_validator(int_input):
        if isinstance(int_input, str):
            raise ValueError("string type is not supported")
        my_func(int_input)
    return int_input_validator

@ validate_input_decorator
def adder(number):
    """Function adds input number to stored accumulator value."""
    accum = 10
    accum += number
    return print(accum)

adder(5)

# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.


def memorize(my_func):
    """This is a decorator function which stores calculation results of my_func function in cache and in returns them
        when required. """
    cache = {}
    @functools.wraps(my_func)
    def decorate(args):
        if not isinstance(args, int):
            raise ValueError('Only int type supported.')
        if args < 1:
            return 'Function factorial accepts only positive integers.'
        decorate.counter += 1
        if args in cache:
            decorate.cache_counter += 1
            print('Used cache with counter = {0}, function result = {1}  calls to cache = {2}'
                  .format(decorate.counter, cache[args], decorate.cache_counter))
            return cache[args]
        else:
            decorate.func_counter += 1
            cache[args] = my_func(args)
            print('Function executed with counter = {0}, function result = {1}, Function was executed {2} times'
                .format(decorate.counter, my_func(args), decorate.func_counter))
            return cache[args]
    decorate.counter = 0
    decorate.cache_counter = 0
    decorate.func_counter = 0
    return decorate

@ memorize
def factorial(number):
    """Function calculates factorial of the given argument. Function accepts positive integers as arguments only."""
    if number == 1:
        return 1
    return number * factorial(number - 1)


#factorial(3)
#factorial(6)
factorial(20)
