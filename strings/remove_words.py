import os, string, re

#1)Из текстового файла удалить все слова, содержащие от трех до пяти символов, но при
#этом из каждой строки должно быть удалено только четное количество таких слов.

def remove_words_from_file(filename):
    '''Function removes from the input file even number of the words containing from 3 to 5 characters.'''
    
    if not os.path.exists(filename):
        raise FileNotFoundError('File does not exist.')
    template = re.compile(r'\b[a-zA-Z]{3,5}\b')
    result_list = []
    with open(filename,'r') as file:
        for line in file:
            words_to_delete = template.findall(line)
            if len(words_to_delete) < 2:
                continue
            elif len(words_to_delete) % 2:
                words_to_delete = words_to_delete[:-1]
            for i in words_to_delete:
                line = re.sub(i, ' ', line)
            line = re.sub(r'\s{2,}', ' ', line)
            line = line.strip()
            result_list.append(line + '\n')
    with open(filename,'w') as file:
        file.writelines(result_list)
        


if __name__ == '__main__':
    remove_words_from_file('string_file.txt')
