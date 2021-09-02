import pytest

class Fruit:
    def __init__(self, name) :
        self.name= name
    
    def __eq__(self, other):
        return self.name == other.name
    
def test_my_fruit_in_basket(my_fruit, basket) :
    assert my_fruit in basket

def test_fruit(my_fruit, my_fruit2):
    assert my_fruit, my_fruit2
    
def test_basket(my_fruit, basket) :
    pass

def test_name(my_name, my_fruit) :
    assert "jobs", my_name
    assert Fruit("apple"), my_fruit
    pass


def test_name2(my_name, my_fruit) :
    assert "jobs", my_name
    pass