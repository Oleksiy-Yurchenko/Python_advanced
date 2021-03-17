import os.path


# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем


def process_unique_string(file):
    lines = []
    while True:
        line = file.readline()
        if line:
            line = line.rstrip()
            if line not in lines:
                lines.append(line)
                yield line
        else:
            break


def print_from_file(file):
    if not os.path.exists(file):
        raise FileNotFoundError('File does not exist.')
    with open(file, 'r') as f:
        for line in process_unique_string(f):
            print(line)


# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
# ```

def coroutine(func):
    def start(*args, **kwargs):
        coroutine = func(*args, **kwargs)
        next(coroutine)
        return coroutine
    return start


@coroutine
def grep(pattern, target):
    while True:
        line = yield
        if pattern in line:
            target.send(line)


@coroutine
def printer():
    while True:
        line = yield
        print(line)


@coroutine
def dispenser(targets):
    while True:
        line = yield
        if targets:
            for target in targets:
                target.send(line)


def follow(file, target):
    file.seek(0,1)
    while True:
        line = file.readline()
        if not line:
            continue
        target.send(line)


#
# Каждый grep следит за определенной сигнатурой
#
# Как это будет работать:
#

f_open = open('log.txt') # подключаемся к файлу
follow(f_open, # делегируем ивенты
       dispenser([
           grep('python', printer()), # отслеживаем
           grep('is', printer()),     # заданные
           grep('great', printer()),  # сигнатуры
       ])
       )



# Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть
#
# Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.
#
# Если все плохо - план Б лекция Дэвида Бизли
# [warning] решение там тоже есть :)
# https://www.dabeaz.com/coroutines/Coroutines.pdf


# Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source ---send()--->coroutine1------send()---->coroutine2----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и обработку ошибки GeneratorExit.
#
# Например: Ваш source (это не корутина, не генератор и прочее, это просто функция ) в ней опеделите цикл из 10 элементов
# которые будут по цепочке отправлены в каждый из корутин и в каждом из корутив вызвано сообщение о полученном элементе.
# После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.


def source_function(target):
    for i in range(10):
        target.send(i)
    target.close()


@coroutine
def coroutine_1(target):
    try:
        while True:
            number = yield
            print('Coroutine 1 received: ', number)
            target.send(number)
    except GeneratorExit:
        print('Coroutine 1 closed.')
        target.close()


@coroutine
def coroutine_2(target):
    try:
        while True:
            number = yield
            print('Coroutine 2 received: ', number)
            target.send(number)
    except GeneratorExit:
        print('Coroutine 2 closed.')
        target.close()


@coroutine
def sink():
    try:
        while True:
            number = yield
            print('Sink received number: ', number)
    except GeneratorExit:
        print('Sink closed.')


if __name__ == '__main__':
    print_from_file(r'.\strings\task.txt')

    source_function(coroutine_1(coroutine_2(sink())))
