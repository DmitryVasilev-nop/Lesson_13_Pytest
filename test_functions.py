from functions import salary, hello_who, beta
def test_hello_who_max():
    assert hello_who('Max') == 'Hello, Max'
    assert hello_who('Ivan') == 'Hello, Ivan'
    assert hello_who('Oleg') == 'Hello, Oleg'
    assert hello_who('Dima') == 'Hello, Dima'
def test_salary():
    assert salary(2, 4) == 16
    assert salary(3, 5) == 30
    assert salary(4, 6) == 48
def test_beta():
    assert beta(3) == 'не четное'
    assert beta(2) == 'четное'