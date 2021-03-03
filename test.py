import pytest


# Проверка конкатенации строк через оператор "+"
def test_string1():
    a = 'AndreySidorchuk'
    b = 'MyName'
    assert a + b == 'AndreySidorchukMyName'


# Негативный тест проверки свойства неизменяемости у типа str
def test_neg_string2():
    try:
        a = 'AndreySidorchuk'
        a[0] = 'S'
        assert a == 'AndreySidorchukMyname'
    except TypeError:
        pass


# Параметризованный тест у типа str на работу count
@pytest.mark.parametrize('slovo,bukva', [['Grey', 'y'], ['Krym', 'y']])
def test_string3_params(slovo, bukva):
    a = slovo.count(bukva)
    assert a == 1


# Проверка работы сложения кортежей
def test_tuple1():
    a = ('1', 1, '2', 2, '3', 3)
    b = ('4', 4, '5', 5, '6', 6)
    assert a + b == ('1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6)


# Негативный тест работы индексации у tuple
def test_neg_tuple2():
    try:
        a = ('One', 1, 'Two', 2, 'Three', 3)
        g = a[10]
        assert g == a[10]
    except IndexError:
        pass


# Параметризованный тест у типа tuple на работу count()
@pytest.mark.parametrize('l, el, count', [[(1,), 1, 1], [('One', 1, 'One'), 'One', 2]])
def test_params_tuple3(l, el, count):
    a = l.count(el)
    assert a == count
