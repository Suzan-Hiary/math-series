from math_series import __version__
from math_series.math_series import   Fibonacci , lucas ,sum_series

# 2, 1, 3, 4, 7, 11, 18, 29, 47,76,123,199,322,521,843,1364    lucas

def test_version():
    assert __version__ == '0.1.0'

#fibonacci :

def test_zer0():
  expected = 0
  actual = Fibonacci(0)
  assert actual == expected

def test_six():
    expected = 8 
    actual =  Fibonacci(6)
    assert actual == expected

def test_fiftten():
    expected = 610 
    actual =  Fibonacci(15)
    assert actual == expected

#lucas :

def test_two():
    expected = 4
    actual =  lucas(3)
    assert actual == expected

def test_ten():
    expected = 123
    actual =  lucas(10)
    assert actual == expected  


def test_thirteen():
    expected = 521
    actual =  lucas(13)
    assert actual == expected  

#sum_series :

def test_three_parameters():
    expected = 11
    actual = sum_series(5,2,1)
    assert actual == expected


def test_two():
    expected = 1
    actual = sum_series(2)
    assert actual == expected 


def test_three_parameterssss():
    expected = 10
    actual = sum_series(3,4,3)
    assert actual == expected

def test_four():
    expected = 3
    actual = sum_series(4)
    assert actual == expected    