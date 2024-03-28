import pytest
from main import Category, Product, Smartphone, LawnGrass

@pytest.fixture
def sample_category():
    return Category("Electronics", "Products related to electronics")

@pytest.fixture
def sample_product():
    return Product("Laptop", "High-performance laptop", 1000, 10)

@pytest.fixture
def sample_smartphone():
    return Smartphone("iPhone", 1500, 5, "High", "12 Pro", "128GB", "Space Gray")

@pytest.fixture
def sample_lawn_grass():
    return LawnGrass("Grass", 20, 100, "USA", "2 weeks", "Green")

def test_category_add_product(sample_category, sample_product, sample_smartphone, sample_lawn_grass):
    sample_category.add_product(sample_product)
    sample_category.add_product(sample_smartphone)
    sample_category.add_product(sample_lawn_grass)
    assert sample_category.get_products_info() == [
        "Laptop, 1000 руб. Остаток: 10 шт.",
        "iPhone, 1500 руб. Остаток: 5 шт. Модель: 12 Pro, Память: 128GB, Цвет: Space Gray",
        "Grass, 20 руб. Остаток: 100 шт. Страна-производитель: USA, Срок прорастания: 2 weeks, Цвет: Green"
    ]

def test_product_price_setter(sample_product):
    sample_product.price = 1500
    assert sample_product.price == 1500

def test_product_price_setter_incorrect_value(sample_product, capsys):
    sample_product.price = -500
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена введена некорректно"
    assert sample_product.price == 1000  # Предполагается, что цена осталась без изменений

def test_product_price_deleter(sample_product, capsys):
    del sample_product.price
    captured = capsys.readouterr()
    assert captured.out.strip() == "Удаление атрибута 'price' не разрешено"
    assert hasattr(sample_product, "price")  # Предполагается, что атрибут 'price' не был удален
