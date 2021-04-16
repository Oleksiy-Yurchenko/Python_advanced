import unittest
from unittest.mock import patch
from hw_9_corr import *
import io
from freezegun import freeze_time


class Hw9TestCase(unittest.TestCase):
    """Unit tests for the module hw_9_corr.py."""

    def test_1_email_descriptor_correct_input(self):
        """Test #1. Testing an email_descriptor behavior in case of the correct input."""
        my_class = MyClass()
        my_class.email = "validemail@gmail.com"
        self.assertEqual(my_class.email, "validemail@gmail.com")

    def test_2_email_descriptor_wrong_input(self):
        """Test #2. Testing an email_descriptor behavior in case of the wrong input."""
        my_class = MyClass()
        with self.assertRaises(ValueError):
            my_class.email = "novalidemail"

    def test_3_email_descriptor_empty_input(self):
        """Test #3. Testing an email_descriptor behavior in case of the empty input."""
        my_class = MyClass()
        with self.assertRaises(ValueError):
            my_class.email = ""

    def test_4_class_singleton(self):
        """Test #4. Testing class Singleton."""
        a = MySingletonClass()
        b = MySingletonClass()
        self.assertEqual(a, b)

    def test_5_class_integer_field(self):
        """Test #5. Testing class IntegerField."""
        data_row = Data()
        new_data_row = Data()
        data_row.number = 5
        new_data_row.number = 10
        self.assertNotEqual(data_row.number, new_data_row.number)

    def test_6_create_warehouse(self):
        """Test #6. Testing class Warehouse, create instance of the class."""
        warehouse = Warehouse()
        self.assertEqual(isinstance(warehouse, Warehouse), True)

    def test_7_add_material(self):
        """Test #7. Testing method add_material of the class Warehouse."""
        warehouse = Warehouse()
        warehouse.add_material('apples', 'some details', 10, True, 5)
        apples = warehouse.find_material('apples')
        self.assertEqual(apples.name, 'apples')

    def test_8_price_descriptor(self):
        """Test #8. Testing price_descriptor of the instance of the class Warehouse."""
        warehouse = Warehouse()
        warehouse.add_material('apples', 'some details', 10, True, 5)
        apples = warehouse.find_material('apples')
        self.assertEqual(apples.price, 6)

    def test_9_quantity(self):
        """Test #9. Testing property quantity of the instance of the class Warehouse."""
        warehouse = Warehouse()
        warehouse.add_material('apples', 'some details', 10, True, 5)
        apples = warehouse.find_material('apples')
        self.assertEqual(apples.quantity, 10)

    def test_10_add_material_without_all_args(self):
        """Test #10. Testing method add_material of the class Warehouse without all required arguments."""
        warehouse = Warehouse()
        with self.assertRaises(TypeError):
            warehouse.add_material('apples', 'some details', 10, True)

    def test_11_remove_material(self):
        """Test #11. Testing method remove_material of the class Warehouse."""
        warehouse = Warehouse()
        warehouse.add_material('apples', 'some details', 10, True, 5)
        warehouse.remove_material('apples')
        self.assertEqual(warehouse.find_material('apples'), None)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_12_print_current_quantity_exists(self, mock_stdout):
        """Test #12. Testing method print_current_quantity of the class Warehouse in case of material exists."""
        warehouse = Warehouse()
        warehouse.add_material('apples', 'some details', 10, True, 5)
        warehouse.print_current_quantity('apples')
        self.assertEqual(mock_stdout.getvalue(), 'Current stock of apples is 10\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_13_print_current_quantity_not_exists(self, mock_stdout):
        """Test #13. Testing method print_current_quantity of the class Warehouse in case of material does not exist."""
        warehouse = Warehouse()
        warehouse.print_current_quantity('apples')
        self.assertEqual(mock_stdout.getvalue(), 'Material does not exist.\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_14_print_current_quantity_all_non_empty(self, mock_stdout):
        """Test #14. Testing method print_current_quantity_all of the class Warehouse of the non empty warehouse."""
        warehouse = Warehouse()
        warehouse.add_material('apples', 'some details', 10, True, 5)
        warehouse.add_material('bananas', 'some other details', 20, True, 7)
        warehouse.print_current_quantity_all()
        self.assertEqual(mock_stdout.getvalue(), 'Current stock of apples is 10\nCurrent stock of bananas is 20\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_15_print_current_quantity_all_empty(self, mock_stdout):
        """Test #15. Testing method print_current_quantity_all of the class Warehouse of the empty warehouse."""
        warehouse = Warehouse()
        warehouse.print_current_quantity_all()
        self.assertEqual(mock_stdout.getvalue(), 'Warehouse is empty.\n')

    def test_16_create_category(self):
        """Test #16. Testing creation of the instance of the Category Class."""
        fruits = Category('fruits')
        self.assertEqual(fruits.name, 'fruits')

    def test_17_add_to_category_1(self):
        """Test #17. Testing method add_to_category of the Category Class."""
        fruits = Category('fruits')
        bananas = Material('bananas', 'some other details', 20, True, 7)
        fruits.add_to_category(bananas)
        self.assertEqual(fruits.members[0], bananas)

    def test_18_add_to_category_2(self):
        """Test #18. Testing method add_to_category of the Category Class."""
        fruits = Category('fruits')
        bananas = Material('bananas', 'some other details', 20, True, 7)
        fruits.add_to_category(bananas)
        self.assertEqual(fruits.name, bananas.category)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_19_add_to_category_non_material_class(self, mock_stdout):
        """Test #19. Testing method add_to_category of the Category Class with material on non material class."""
        fruits = Category('fruits')
        something = MyClass()
        fruits.add_to_category(something)
        self.assertEqual(mock_stdout.getvalue(), 'Material does not belong to material class.\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_20_print_category_non_empty(self, mock_stdout):
        """Test #20. Testing method print_category of the Category Class of the non empty category."""
        fruits = Category('fruits')
        bananas = Material('bananas', 'some other details', 20, True, 7)
        fruits.add_to_category(bananas)
        fruits.print_category()
        self.assertEqual(mock_stdout.getvalue(), '1 Material name:  bananas Material quantity : 20\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_21_print_category_empty(self, mock_stdout):
        """Test #21. Testing method print_category of the Category Class of the non empty category."""
        fruits = Category('fruits')
        fruits.print_category()
        self.assertEqual(mock_stdout.getvalue(), '')

    def test_22_create_basket(self):
        """Test #22. Testing creation of the instance of the Basket Class."""
        basket = Basket()
        self.assertEqual(basket.total, 0)

    def test_23_add_to_basket_with_correct_value(self):
        """Test #23. Testing method add_to_basket of the Basket Class with value of the material less than in warehouse."""
        basket = Basket()
        bananas = Material('bananas', 'some other details', 20, True, 7)
        basket.add_to_basket(bananas, 10)
        self.assertEqual(basket.content[bananas], 10)

    def test_24_add_to_basket_with_wrong_value(self):
        """Test #24. Testing method add_to_basket of the Basket Class with value of the material more than in warehouse."""
        basket = Basket()
        bananas = Material('bananas', 'some other details', 20, True, 7)
        with self.assertRaises(ValueError):
            basket.add_to_basket(bananas, 25)

    def test_25_add_to_basket_wrong_material(self):
        """Test #25. Testing method add_to_basket of the Basket Class the material of not Material class."""
        basket = Basket()
        something = MyClass()
        with self.assertRaises(TypeError):
            basket.add_to_basket(something, 100)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_26_print_basket_non_empty(self, mock_stdout):
        """Test #26. Testing method print_category of the Category Class of the non empty basket."""
        basket = Basket()
        bananas = Material('bananas', 'some other details', 20, True, 7)
        basket.add_to_basket(bananas, 10)
        basket.print_basket()
        self.assertEqual(mock_stdout.getvalue(), 'Basket\n1 Material:  bananas Quantity:  10 Price:  8.4 Total:  '
                                                 '84.0\nGrand Total:  84.0\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_27_print_basket_empty(self, mock_stdout):
        """Test #27. Testing method print_category of the Category Class of the empty basket."""
        basket = Basket()
        basket.print_basket()
        self.assertEqual(mock_stdout.getvalue(), '')

    def test_28_create_order_id(self):
        """Test #28. Testing creation of the instance of the class Order with order_id."""
        order = Order()
        self.assertEqual(order.order_id, 1)

    def test_29_create_order_date_purchased(self):
        """Test #29. Testing creation of the instance of the class Order with date_purchased."""
        with freeze_time('2021-02-03 12:00:03.123456'):
            order = Order()
        self.assertEqual(order.date_purchased, datetime.datetime(2021, 2, 3, 12, 0, 3, 123456))

    def test_create_order_manager(self):
        """Test #30. Testing creation of the instance of the class OrderManager."""
        order_manager = OrderManager()
        self.assertEqual(order_manager.orders, [])

    def test_31_generate_order_output(self):
        """Test #31. Testing method generate_order of the class OrderManager to return instance of the class Order."""
        order_manager = OrderManager()
        basket = Basket()
        warehouse = Warehouse()
        warehouse.add_material('bananas', 'some other details', 20, True, 7)
        bananas = warehouse.find_material('bananas')
        basket.add_to_basket(bananas, 10)
        order = order_manager.generate_order(basket, warehouse)
        self.assertEqual(isinstance(order, Order), True)

    def test_32_generate_order_orders(self):
        """Test #32. Testing method generate_order of the class OrderManager to add instance of the class Order to the
        attribute orders."""
        order_manager = OrderManager()
        basket = Basket()
        warehouse = Warehouse()
        warehouse.add_material('bananas', 'some other details', 20, True, 7)
        bananas = warehouse.find_material('bananas')
        basket.add_to_basket(bananas, 10)
        order = order_manager.generate_order(basket, warehouse)
        self.assertEqual(order_manager.orders[0], order)

    def test_33_generate_order_substruct_from_warehouse(self):
        """Test #33. Testing method generate_order of the class OrderManager to substruct value of the order from the
        warehouse stock."""
        order_manager = OrderManager()
        basket = Basket()
        warehouse = Warehouse()
        warehouse.add_material('bananas', 'some other details', 20, True, 7)
        bananas = warehouse.find_material('bananas')
        basket.add_to_basket(bananas, 10)
        order = order_manager.generate_order(basket, warehouse)
        self.assertEqual(bananas.quantity, 10)

    def test_34_find_order_real_id(self):
        """Test #34. Testing method find_order of the class OrderManager to find the order with true id."""
        order_manager = OrderManager()
        basket = Basket()
        warehouse = Warehouse()
        warehouse.add_material('bananas', 'some other details', 20, True, 7)
        bananas = warehouse.find_material('bananas')
        basket.add_to_basket(bananas, 10)
        order = order_manager.generate_order(basket, warehouse)
        self.assertEqual(order_manager.find_order(order.order_id), order)

    def test_35_find_order_unreal_id(self):
        """Test #35. Testing method find_order of the class OrderManager to find the order with unreal id."""
        order_manager = OrderManager()
        basket = Basket()
        warehouse = Warehouse()
        warehouse.add_material('bananas', 'some other details', 20, True, 7)
        bananas = warehouse.find_material('bananas')
        basket.add_to_basket(bananas, 10)
        order = order_manager.generate_order(basket, warehouse)
        self.assertEqual(order_manager.find_order(10), None)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_36_print_order(self, mock_stdout):
        """Test 36. Testing method print_order of the class Order."""
        order_manager = OrderManager()
        basket = Basket()
        warehouse = Warehouse()
        warehouse.add_material('bananas', 'some other details', 20, True, 7)
        bananas = warehouse.find_material('bananas')
        basket.add_to_basket(bananas, 10)
        with freeze_time('2021-02-03 12:00:03.123456'):
            order = order_manager.generate_order(basket, warehouse)
        order.print_order()
        self.assertEqual(mock_stdout.getvalue(), 'Order ID:  8\nDate purchased:  2021-02-03 12:00:03.123456\n1 '
                                                 'Material:  bananas Quantity:  10\n')


if __name__ == "__main__":
    unittest.main()
