from abc import ABC, abstractmethod

class ZeroQuantityError(Exception):
    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        self.message = message
        super().__init__(self.message)

class AbstractProduct(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    @abstractmethod
    def get_info(self):
        pass

class Product(AbstractProduct):
    def get_info(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

class LogMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log_created_object()

    def log_created_object(self):
        class_name = self.__class__.__name__
        attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        print(f"Создан объект класса {class_name}: {attributes}")

class Smartphone(AbstractProduct, LogMixin):
    def __init__(self, name, price, quantity, performance, model, memory, color):
        super().__init__(name, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def get_info(self):
        return f"Смартфон: {self.name}, {self.price} руб. Остаток: {self.quantity} шт. Модель: {self.model}, Память: {self.memory}, Цвет: {self.color}"

class LawnGrass(AbstractProduct, LogMixin):
    def __init__(self, name, price, quantity, country, germination_period, color):
        super().__init__(name, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def get_info(self):
        return f"Трава газонная: {self.name}, {self.price} руб. Остаток: {self.quantity} шт. Страна-производитель: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"

class Category:
    total_categories = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только объекты классов Product, Smartphone и LawnGrass")
        if product.quantity == 0:
            raise ZeroQuantityError
        self.__products.append(product)

    def get_products_info(self):
        products_info = []
        for product in self.__products:
            products_info.append(str(product))
        return products_info

    def average_price(self):
        total_price = 0
        total_count = 0
        for product in self.__products:
            total_price += product.price
            total_count += 1
        try:
            return total_price / total_count
        except ZeroDivisionError:
            return 0



