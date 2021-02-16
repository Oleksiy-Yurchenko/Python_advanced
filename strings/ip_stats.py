import os, collections, datetime


#4)Дан текстовый файл со статистикой посещения сайта за неделю. Каждая строка содержит
#ip адрес, время и название дня недели (например, 139.18.150.126 23:12:44 sunday).
#Создайте новый текстовый файл, который бы содержал список ip без повторений из первого
#файла. Для каждого ip укажите количество посещений, наиболее популярный день недели.
#Последней строкой в файле добавьте наиболее популярный отрезок времени в сутках длиной
#один час в целом для сайта.


def calculate_ip_stats(input_file, output_file):
    '''Function calculates statistics of ip addresses visiting a web page. It opens an input file, performs several checks for
    file existance, and non-emptyness, calculates stistics and writes it into  the output file.    
    To complete the function information from the following resources were utilized:
    https://docs.python.org/3/library/collections.html
    https://docs.python.org/3/library/datetime.html
    '''
    
    ip_addresses = collections.defaultdict(int)
    hours = collections.defaultdict(int)
    ip = collections.defaultdict(dict)
    ip_days_dict_of_lists = collections.defaultdict(list)
    ip_days_counter = collections.Counter()
    ip_days = []
    times = []
    result = []
    one_hour = datetime.timedelta(hours=1)

    if not os.path.exists(input_file):
        raise FileNotFoundError('File does not exist.')
    with open(input_file, 'r+') as file:
        for entry in file:
            ip_list = entry.split()
            ip_addresses[ip_list[0]] += 1 
            ip_days.append((ip_list[0], ip_list[2]))
            times.append(datetime.datetime.strptime(ip_list[1], '%H:%M:%S'))

        ip_addresses = sorted(ip_addresses.items(), key=lambda x: x[1], reverse=True)
        
        for k, v in ip_days:
            ip_days_dict_of_lists[k].append(v)

        for k, v in ip_days_dict_of_lists.items():
             ip[k] = collections.Counter(ip_days_dict_of_lists[k]).most_common(1)[0][0]

        for k, v in ip_addresses:
            result.append('ip address: {0}, visits: {1}, most hits on {2}.\n'.format(k, v, ip[k]))

        for time in times:
            time_plus_one_hour = time + one_hour
            for t2 in times:
                if time_plus_one_hour >= t2 > time:
                    hours[time] += 1

        peak_start = sorted(hours.items(), key=lambda x: x[1], reverse=True)[0][0]
        peak_stop = peak_start + one_hour
        result.append('One hour period with the most hits started at {0} and ended at {1}.'
                      .format(peak_start.strftime('%H:%M:%S'),peak_stop.strftime('%H:%M:%S')))
        
    with open(output_file, 'w') as file:
        file.writelines(result)
                      

if __name__ == '__main__':
    calculate_ip_stats('ip_visits.txt', 'stats.txt')
