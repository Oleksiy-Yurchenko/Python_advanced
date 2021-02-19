import json, os.path, re

# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)
#


class IpManager:
    ip_template = re.compile(r'^(?P<oct_1>[0-9]{,3})\.(?P<oct_2>[0-9]{,3})\.(?P<oct_3>[0-9]{,3})\.(?P<oct_4>[0-9]{,3})')

    def __init__(self, ip_list):
        if isinstance(ip_list, list):
            self.ip_list = ip_list
        else:
            raise TypeError('ip_list must be a list.')

    def get_ip_list(self):
        return self.ip_list

    def reverse_ip_list(self):
        return self.ip_list[::-1]

    def remove_first_oct(self):
        ip_list_wout_first_oct = []
        if self.ip_list:
            for ip in self.ip_list:
                if IpManager.ip_template.match(ip):
                    ip_oct_list = ip.split('.')
                    ip_wout_first_oct = '.'.join(ip_oct_list[1:])
                    ip_list_wout_first_oct.append(ip_wout_first_oct)
                else:
                    raise ValueError('List of ips should contain ips in correct format.')
        return ip_list_wout_first_oct

    def get_last_oct_list(self):
        last_oct_list = []
        if self.ip_list:
            for ip in self.ip_list:
                if IpManager.ip_template.match(ip):
                    ip = ip.split('.')
                    last_oct_list.append('.'.join(ip[-2:]))
                else:
                    raise ValueError('List of ips should contain ips in correct format.')
        return last_oct_list

# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу

class JsonFileHandler:

    def __init__(self, file):
        if os.path.exists(file) and file.endswith('.json'):
            self.file = file
        else:
            raise ValueError('Class Instance attribute should be a path to a JSON file.')

    def read_json(self):
        with open(self.file, 'r') as file:
            return json.load(file)

    def write_json(self, data):
        with open(self.file, 'w') as file:
            return json.dump(data, file)

    def merge_files(self, other_json_file, output_file):
        with open(self.file, 'r') as file:
            data_1 = json.load(file)
        if os.path.exists(other_json_file) and other_json_file.endswith('.json'):
            with open(other_json_file, 'r') as file:
                data_2 = json.load(file)
        else:
            raise ValueError('File has to be a JSON file.')
        merged_data = [data_1, data_2]
        with open(output_file, 'w') as merged_file:
            return json.dump(merged_data, merged_file)

    def get_abs_path(self):
        return os.path.abspath(self.file)

    def get_rel_path(self):
        return os.path.relpath(self.file)

# 
# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.

class SwitchParameters:
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @ property
    def unit_name(self):
        return self._unit_name

    @ unit_name.setter
    def unit_name(self, unit_name):
        self._unit_name = unit_name

    @ property
    def mac_address(self):
        return self._mac_address

    @ mac_address.setter
    def mac_address(self, mac_address):
        self._mac_address = mac_address

    @ property
    def ip_address(self):
        return self._ip_address

    @ ip_address.setter
    def ip_address(self, ip_address):
        self._ip_address = ip_address

    @ property
    def login(self):
        return self._login

    @ login.setter
    def login(self, login):
        self._login = login

    @ property
    def password(self):
        return self._password

    @ password.setter
    def password(self, password):
        self._password = password


if __name__ == '__main__':

    ip = ['.02..1', '3.3.3.', '3.0.0.0']
    manager = IpManager(ip)
    print(manager.ip_list)
    print(manager.reverse_ip_list())
    print(manager.remove_first_oct())
    print(manager.get_last_oct_list())

    data = {'@odata.context': '/redfish/v1/$metadata#EthernetInterface.EthernetInterface',
            '@odata.etag': 'W/"9C785D2A"', '@odata.id': '/redfish/v1/Systems/1/EthernetInterfaces/1/',
            '@odata.type': '#EthernetInterface.v1_0_3.EthernetInterface', 'FullDuplex': True, 'Id': '1',
            'MACAddress': '48:df:37:33:fc:20', 'Name': '', 'SpeedMbps': None,
            'UefiDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)'}

    c = JsonFileHandler(r'example_json_1.json')

    print('Read json_1: ', c.read_json())
    print(c.write_json(data))
    print(c.read_json())
    c.merge_files(r'example_json_2.json', r'merged.json')
    c = JsonFileHandler(r'merged.json')
    print('Read json: ', c.read_json())
    print(c.get_rel_path())
    print(c.get_abs_path())

    switch = SwitchParameters('switch_net_a', '80-12-AF-0D-05-14', '72.145.85.241', 'switch_login', 'sTronG_pAsswOrd')
    print(switch.unit_name)
    switch.unit_name = 'switch_net_b'
    print(switch.unit_name)
    print(switch.mac_address)
    switch.mac_address = '14-75-DE-A7-47-11'
    print(switch.mac_address)
    print(switch.ip_address)
    switch.ip_address = '123.123.123.123'
    print(switch.ip_address)
    print(switch.login)
    switch.login = 'login'
    print(switch.login)
    print(switch.password)
    switch.password = 'another_password'
    print(switch.password) 

