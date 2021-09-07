# content of test_ids.py
import pytest


@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param


def test_a(a):
    print(f'test_a a= {a}')
    pass


def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None


@pytest.fixture(params=[0, 1,2,3,4,5], ids=idfn)
def b(request):    
    print(f'id={request.node.callspec.id}')
    return request.param


def test_b(b):    
    print(f'test_b b= {b}')
    pass