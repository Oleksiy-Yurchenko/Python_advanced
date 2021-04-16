import re
import datetime

# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить


class EmailDescriptor:
    def __get__(self, instance, owner):
        return self.email

    def __set__(self, instance, value):
        email_template = re.compile(r'^([a-z0-9_.-]+)@(([a-z0-9-]+\.)+[a-z]{2,6})$', re.I | re.S)
        if email_template.search(value):
            self.email = value
        else:
            raise ValueError('{0} is not a valid email.'.format(value))

class MyClass:
    email = EmailDescriptor()


# my_class = MyClass()
# my_class.email = "validemail@gmail.com"
# print(my_class.email)
# my_class.email = "novalidemail"
# print(my_class.email)
# Raised Exception


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MySingletonClass(metaclass=Singleton):
    pass


c = MySingletonClass()
b = MySingletonClass()
assert id(c) == id(b)


# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IntegerField:
    def __init__(self,number):
        self.number = number

    def __get__(self, instance, owner):
        return instance.__dict__[self.number]

    def __set__(self, instance, value):
        instance.__dict__[self.number] = value

class Data:
    number = IntegerField('number')


# data_row = Data()
# new_data_row = Data()
#
# data_row.number = 5
# new_data_row.number = 10
#
# assert data_row.number != new_data_row.number


# Задача4
# Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров.
# Cписок требований:
# 1) Создайте товар с такими свойствами, как имя(name), подробные сведения(description or details),
# количество на складе(quantity), доступность(availability), цена(price).
# 2) Добавить товар на склад
# 3) Удалить товар со склада
# 4) Распечатать остаток товара по его имени
# 5) Распечатать остаток всех товаров
# 6) Товар может принадлежать к категории
# 7) Распечатать список товаров с заданной категорией
# 8) Корзина для покупок, в которой может быть много товаров с общей ценой.
# 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
# 10) Распечатать элементы корзины покупок с ценой и общей суммой
# 11) Оформить заказ и распечатать детали заказа по его номеру
# 12) Позиция заказа, созданная после оформления заказа пользователем.
# Он будет иметь идентификатор заказа(order_id), дату покупки(date_purchased), товары(items), количество(quantity)
# 13) После оформления заказа количество товара уменьшается на количество товаров из заказа.


# Добавить к этой задаче дескриптор для аттрибута цена.
# При назначении цены товара будет автоматически добавлен НДС 20%
# При получении цены товара, цена возврщается уже с учетом НДС


class Material:
    VAT = 0.2

    class PriceDescriptor:
        def __get__(self, instance, owner):
            return instance._price * (1 + Material.VAT)

    price = PriceDescriptor()

    def __init__(self, name, details, quantity, availability, price):
        self.name = name
        self.details = details
        self._quantity = quantity
        self.availability = availability
        self._price = price
        self.category = None

    @ property
    def quantity(self):
        return self._quantity

    @ quantity.setter
    def quantity(self, value):
        self._quantity = value


class Warehouse:
    def __init__(self):
        self.stock = []

    def find_material(self, name):
        if self.stock:
            for material in self.stock:
                if material.name == name:
                    return material

    def add_material(self, name, details, quantity, availability, price):
        material = Material(name, details, quantity, availability, price)
        self.stock.append(material)

    def remove_material(self, material):
        material = self.find_material(material)
        if material:
            self.stock.remove(material)

    def print_current_quantity(self, material):
        material = self.find_material(material)
        if material:
            print('Current stock of {0} is {1}'.format(material.name, material.quantity))
        else:
            print('Material does not exist.')

    def print_current_quantity_all(self):
        if self.stock:
            for material in self.stock:
                self.print_current_quantity(material.name)
        else:
            print('Warehouse is empty.')


class Category():
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_to_category(self, material):
        if isinstance(material, Material):
            self.members.append(material)
            material.category = self.name
        else:
            print('Material does not belong to material class.')

    def print_category(self):
        id = 0
        if self.members:
            for material in self.members:
                id += 1
                print(id, 'Material name: ', material.name, 'Material quantity :', material.quantity)


class Basket():
    def __init__(self):
        self.content = {}
        self.total = 0

    def add_to_basket(self, material, value):
        if isinstance(material, Material):
            if material.quantity >= value:
                self.content[material] = value
                self.total += value * material.price
            else:
                raise ValueError('Material quantity in Warehouse is not enough to process your order.')
        else:
            raise TypeError('Material has to be an instance of class Material.')

    def print_basket(self):
        id = 0
        if self.content:
            print('Basket')
            for material in self.content:
                id += 1
                print(id, 'Material: ', material.name, 'Quantity: ', self.content[material], 'Price: ', material.price,
                      'Total: ', self.content[material] *  material.price)
            print('Grand Total: ', self.total)


class Order(Basket):
    order_id = 0

    def __init__(self):
        self.items = {}
        self.order_id = Order._generate_order_id()
        self.date_purchased = datetime.datetime.today()
        super().__init__()

    @ classmethod
    def _generate_order_id(cls):
        Order.order_id += 1
        return Order.order_id

    def print_order(self):
        id = 0
        print('Order ID: ', self.order_id)
        print('Date purchased: ', self.date_purchased)
        for material in self.items:
            id += 1
            print(id, 'Material: ', material.name, 'Quantity: ', self.items[material])


class OrderManager():
    def __init__(self):
        self.orders = []

    def generate_order(self, basket, warehouse):
        if isinstance(basket, Basket) and isinstance(warehouse, Warehouse):
            order = Order()
            self.orders.append(order)
            for material in basket.content:
                if material in warehouse.stock:
                    warehouse_material = warehouse.find_material(material.name)
                    if basket.content[material] <= warehouse_material.quantity:
                        order.items[material] = basket.content[material]
                        warehouse_material.quantity -= basket.content[material]
                    else:
                        print('Quantity of material {0} is not enough to process your order, so it will not be added.'
                              .format(material.name))
                else:
                    raise TypeError('Material is not in the warehouse.')
            return order

    def find_order(self, order_id):
        if self.orders:
            for order in self.orders:
                if order.order_id == order_id:
                    return order
        return None


# warehouse = Warehouse()
#
# warehouse.add_material('apples', 'some details', 10, True, 5)
# apples = warehouse.find_material('apples')
# warehouse.add_material('bananas', 'some other details', 20, True, 7)
# bananas = warehouse.find_material('bananas')
# warehouse.add_material('pineapples', 'another details', 20, True, 7)
# warehouse.print_current_quantity('pineapples')
# warehouse.remove_material('pineapples')
# warehouse.print_current_quantity('pineapples')
# warehouse.print_current_quantity_all()
# fruits = Category('fruits')
# warehouse.add_material('pineapples', 'another details', 20, True, 7)
# pineapples = warehouse.find_material('pineapples')
# fruits.add_to_category(pineapples)
# fruits.add_to_category(apples)
# fruits.add_to_category(bananas)
# fruits.print_category()
# basket_1 = Basket()
# basket_1.add_to_basket(apples, 1)
# basket_1.add_to_basket(pineapples, 1)
# basket_1.print_basket()
# order_manager = OrderManager()
# order_1 = order_manager.generate_order(basket_1, warehouse)
# order_1.print_order()
# warehouse.print_current_quantity_all()
