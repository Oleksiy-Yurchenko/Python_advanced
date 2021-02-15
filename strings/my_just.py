import os 

#3) Получить файл, в котором текст выровнен по правому краю путем равномерного
#добавления пробелов.


def calculate_ip_stats(input_file, output_file):
    '''Function my_just takes an input file and adds required number of the whitespaces
    to align all the lines to the right side of the screen. Afterwards, function writes
    all of the lines to the output file. 
    It is assumed that the screen width is 80 characters.'''
    
    rjust_lines = []
    
    if not os.path.exists(input_file):
        raise FileNotFoundError('File does not exist.')
    with open(input_file, 'r+') as file:
        lines = file.readlines()
        for line in lines:
            rjust_lines.append(line.rjust(80))

    with open(output_file, 'w') as file:
        file.writelines(rjust_lines)


if __name__ == '__main__':
    calculate_ip_stats('just.txt', 'my_rjust.txt')
