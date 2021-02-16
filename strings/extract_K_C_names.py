import os, re

#2)Текстовый файл содержит записи о телефонах и их владельцах. Переписать в другой файл
#телефоны тех владельцев, фамилии которых начинаются с букв К и С.

def extract_k_c_names(input_file, output_file):
    '''Function reads all entries from the input file and writes to the output file phones of the people which surnames start from "K" or "C". '''
    
    phones = []

    template = re.compile(r'^(?P<phone>[0-9]+) (?P<surname>[cCkK][a-zA-Z]+)$')
    
    if not os.path.exists(input_file):
        raise FileNotFoundError('File does not exist.')
    
    with open(input_file, 'r+') as file:
        for line in file:
            entry = template.search(line)
            if entry:
                phones.append(entry.group('surname') + '\n')

    with open(output_file, 'w') as file:
        file.writelines(phones)


if __name__ == '__main__':
    extract_k_c_names('entries.txt', 'phones.txt')
