import string, random, math


#1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key). keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ожидаемый результат: {1: 1, 2: 4, 3: 9 …} 

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def squared_dict_generator(input_list):
    return {key: key * key for key in input_list}

print(squared_dict_generator(input_list))

#2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа. 

def even_filter(limit):
    return [number for number in range(2, limit, 2)]

print(even_filter(101))

#3)Заменить в произвольной строке согласные буквы на гласные.  

random_string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore 
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
anim id est laborum."""

def swap_consonants(random_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    string_list = list(random_string)
    for i in range(len(string_list) - 1):
        if string_list[i].lower() not in vowels and string_list[i].lower() in string.ascii_lowercase:
            string_list[i] = vowels[random.randrange(0, len(vowels) - 1, 1)]
    return ''.join(string_list)

print(swap_consonants(random_string))

#4)Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1] 

numbers_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

#4.1) убрать из него повторяющиеся элементы

def repetition_filter(numbers_list):
    numbers = {}
    for number in numbers_list:
        numbers[number] = numbers.get(number, 0) + 1
    return [k for k, v in numbers.items() if v < 2]

print(repetition_filter(numbers_list))

#4.2) вывести 3 наибольших числа из исходного массива

def n_largest(numbers_list, n=3):
    if len(set(numbers_list)) >= n:
        return sorted(set(numbers_list), reverse=True)[0:n]
    return sorted(set(numbers_list), reverse=True)[0:len(set(numbers_list))]

print(n_largest(numbers_list))

#4.3) вывести индекс минимального элемента массива

def min_index(numbers_list):
    min_number = min(numbers_list)
    return numbers_list.index(min_number)

print(min_index(numbers_list))

#4.4) вывести исходный массив в обратном порядке 

def reverse_list(numbers_list):
    numbers_list.reverse()
    return numbers_list

print(reverse_list(numbers_list))

#5) Найти общие ключи в двух словарях: 
dict_one = {'a':1, 'b':5, 'c':3, 'd':4}
dict_two = {'a':6, 'b':3, 'x':7, 'z':12}

def find_common_keys(dict_one, dict_two):
    return [key for key in dict_one if key in dict_two]

print(find_common_keys(dict_one, dict_two))

#6)Дан массив из словарей 
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

#6.1) отсортировать массив из словарей по значению ключа ‘age' 

def dicts_list_sort(data, key='age'):
    return sorted(data, key=lambda x: x[key])

print(dicts_list_sort(data))

#6.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :
result = {
   'Kiev': [
      {'name': 'Viktor', 'age': 30 },
      {'name': 'Andrey', 'age': 34}],

   'Dnepr': [ {'name': 'Maksim', 'age': 20 },
              {'name': 'Artem', 'age': 50}],
   'Lviv': [ {'name': 'Vladimir', 'age': 32 },
             {'name': 'Dmitriy', 'age': 21}]
}

def group_by_city(data):
    cities = {}
    for person in data:
        if person['city'] not in cities:
            cities.update({person['city']: [{'name': person['name'], 'age': person['age']}]})
        else:
            cities[person['city']].append({'name': person['name'], 'age': person['age']})
    return cities

print(group_by_city(data))

# =======================================================
# 7) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:

list_of_strings = ['a', 'a', 'bi', 'bi', 'bi']

def most_frequent(list_var):
    strings = {}
    for string in list_var:
        strings[string] = strings.get(string, 0) + 1
    return sorted(strings.items(), key=lambda x: x[1])[-1][0]

print(most_frequent(['a', 'a', 'bi', 'bi', 'bi'])) # == 'bi'
# =======================================================
# 8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

number = 123405

def digit_product(number):
    num_str= str(number)
    result = 1
    for digit in num_str:
        if int(digit):
            result *= int(digit)
    return result

print(digit_product(number))

# =======================================================
# 9) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.

def pow_array_member(array, n):
    if n >= len(array):
        return -1
    return math.pow(array[n], n)

print(pow_array_member(numbers_list, 2220))

print(pow_array_member(numbers_list, 7))

# =======================================================
# 10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.

test_string = "hello 1 2 one two three 15 world"

def three_words_row(input_string):
    words_count = 0
    array = input_string.split(' ')
    while (words_count < 3 or len(array)):
        first_item = array[0]
        array = array[1:]
        try:
            int(first_item)
            words_count = 0
        except ValueError:
            words_count += 1
    if words_count > 2:
        return True
    return False

print(three_words_row(test_string))
