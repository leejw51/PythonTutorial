import pytest
from test_pear import Fruit


@pytest.fixture(scope="session")
def my_fruit() :
    return Fruit("apple")

@pytest.fixture(scope="session")
def my_fruit2() :
    return Fruit("apple2")

@pytest.fixture(scope="session")
def basket():
    return [Fruit("strawberry"), Fruit("pear"), Fruit("apple")]


@pytest.fixture(scope="session")
def my_name() :
    return Fruit("jobs")