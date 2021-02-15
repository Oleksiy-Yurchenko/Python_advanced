import os

#2)Текстовый файл содержит записи о телефонах и их владельцах. Переписать в другой файл
#телефоны тех владельцев, фамилии которых начинаются с букв К и С.

def extract_k_c_names(input_file, output_file):
    '''Function reads all entries from the input file and writes to the output file phones of the people which surnames start from "K" or "C". '''
    
    phones = []

    if not os.path.exists(input_file):
        raise FileNotFoundError('File does not exist.')

    with open('entries.txt', 'r+') as file:
        entries = file.readlines()
        for entry in entries:
            if entry[10].lower() == 'c' or entry[10].lower() == 'k':
                phones.append(entry[:9] + '\n')

    with open('phones.txt', 'w') as file:
        file.writelines(phones)



if __name__ == '__main__':
    extract_k_c_names('entries.txt', 'phones.txt')
