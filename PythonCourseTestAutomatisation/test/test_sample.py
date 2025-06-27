import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
#muzeme si vytvorit tag pro sposteni testu, ktery ale musime inicializovat v pytestinit
@pytest.mark.sum
def test_answer_two():
    assert func(5) == 6

@pytest.mark.parametrize("a,vysledek", [(4,5),(6,7), (1,1)])
def test_answer_two(a, vysledek):
    assert func(5) == 6

def test_answer_two():
    assert func(7) == 8
