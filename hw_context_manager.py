import os, time
from contextlib import contextmanager, ContextDecorator


#Задача-1

#Создать объект менеджера контекста который будет переходить в папку которую
# он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять
# Если флаг об исключении отсутствует, исключение должно быть поднято.

class DirectoryChanger:
    def __init__(self, path, exception):
        self._current_folder = os.getcwd()
        self._path = path
        self._exception = exception

    def __enter__(self):
        try:
            os.chdir(self._path)
        except FileNotFoundError:
            print('Folder does not exist')

    def __exit__(self, type, value, traceback):
        os.chdir(self._current_folder)
        if type is self._exception:
            return True

os.chdir(r'C:')
with DirectoryChanger(r'G:\Python_pro', FileNotFoundError):
    print(os.getcwd())


#Задача -2

#Описать задачу выше но уже с использованием @contexmanager

@contextmanager
def change_directory(path, exception):
    current_directory = os.getcwd()
    try:
        yield os.chdir(path)
    except (FileNotFoundError, exception):
        os.chdir(current_directory)


os.chdir(r'C:')
with change_directory(r'F:\Python_advanced', FileNotFoundError):
    print(os.getcwd())


#Задача -3

#Создать менеджер контекста который будет подсчитывать время выполнения вашей функции

class TimeCounter(ContextDecorator):
    def __enter__(self):
        self.t1 = time.time()

    def __exit__(self, type, value, traceback):
        self.t2 = time.time()
        result = self.t2 - self.t1
        print('Function evaluation time is ', result)


with TimeCounter():
    time.sleep(2)
