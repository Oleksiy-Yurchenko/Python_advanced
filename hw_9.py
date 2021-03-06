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
            raise ValueError #('{0} is not a valid email.'.format(value))

class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
# my_class.email = "validemail@gmail.com"
# print(my_class.email)
my_class.email = "novalidemail"
print(my_class.email)
# Raised Exception


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


# c = MyClass()
# b = MyClass()
# assert id(c) == id(b)


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
    VAT = 0.20

    class PriceDescriptor:
        def __get__(self, instance, owner):
            return instance.price * (1 + Material.VAT)

    price = PriceDescriptor()

    def __init__(self, name, details, quantity, availability, price):
        self.name = name
        self.details = details
        self._quantity = quantity
        self.availability = availability
        self.price = price
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
        self.baskets = []
        self.orders = []

    def find_material(self, name):
        if self.stock:
            for material in self.stock:
                if material.name == name:
                    return material
        return None

    def add_material(self, name, details, quantity, availability, price):
        material = Material(name, details, quantity, availability, price)
        self.stock.append(material)

    def remove_material(self, material):
        material = self.find_material(material)
        if material:
            self.stock.remove(material)

    def current_quantity(self, material):
        material = self.find_material(material)
        if material:
            print('Current stock of {0} is {1}'.format(material.name, material.quantity))
        else:
            print('Material does not exist.')

    def current_quantity_all(self):
        if self.stock:
            for material in self.stock:
                self.current_quantity(material.name)
        else:
            print('Warehouse is empty.')

    def create_basket(self):
        basket = Basket()
        self.baskets.append(basket)
        print('Basket with number ', basket.basket_id, ' was created.')
        return basket

    def find_basket(self, basket_id):
        if self.baskets:
            for basket in self.baskets:
                if basket.basket_id == basket_id:
                    return basket
        return None

    def generate_order(self, basket_id):
        basket = self.find_basket(basket_id)
        if basket:
            order = Order()
            self.orders.append(order)
            for material in basket.content:
                #if isinstance(material, Material):
                    #warehouse_material = self.find_material(material.name)
                    #print(warehouse_material)
                if basket.content[material] <= material.quantity:
                    order.items[material] = basket.content[material]
                    material.quantity -= basket.content[material]
                else:
                    print('Quantity of material {0} is not enough to process your order, so it will not be added.'
                          .format(material.name))
            return order

    def find_order(self, order_id):
        if self.orders:
            for order in self.orders:
                if order.order_id == order_id:
                    return order
        return None


class Category(Warehouse):
    def __init__(self, name):
        self.name = name
        self.members = []
        super().__init__()

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


basket_id = 0


class Basket(Warehouse):
    def __init__(self):
        global basket_id
        basket_id += 1
        self.basket_id = basket_id
        self.content = {}
        self.total = 0
        super().__init__()

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
            print('Basket Id: ', self.basket_id)
            for material in self.content:
                id += 1
                print(id, 'Material: ', material.name, 'Quantity: ', self.content[material], 'Price: ', material.price,
                      'Total: ', self.content[material] *  material.price)
            print('Grand Total: ', self.total)


order_id = 0


class Order(Basket):
    def __init__(self):
        self.items = {}
        global order_id
        order_id += 1
        self.order_id = order_id
        self.date_purchased = datetime.datetime.today()
        super().__init__()

    def print_order(self):
        id = 0
        print('Order ID: ', self.order_id)
        print('Date purchased: ', self.date_purchased)
        for material in self.items:
            id += 1
            print(id, 'Material: ', material.name, 'Quantity: ', self.items[material])


warehouse = Warehouse()

warehouse.add_material('apples', 'some details', 10, True, 5)
apples = warehouse.find_material('apples')
warehouse.add_material('bananas', 'some other details', 20, True, 7)
bananas = warehouse.find_material('bananas')
warehouse.add_material('pineapples', 'another details', 20, True, 7)
warehouse.current_quantity('pineapples')
warehouse.remove_material('pineapples')
warehouse.current_quantity('pineapples')
warehouse.current_quantity_all()
warehouse.create_basket()
fruits = Category('fruits')
warehouse.add_material('pineapples', 'another details', 20, True, 7)
pineapples = warehouse.find_material('pineapples')
fruits.add_to_category(pineapples)
fruits.add_to_category(apples)
fruits.add_to_category(bananas)
fruits.print_category()
basket = warehouse.create_basket()
basket.add_to_basket(pineapples, 1)
basket.add_to_basket(apples, 1)
basket.print_basket()
order = warehouse.generate_order(2)
order.print_order()
warehouse.current_quantity_all()

