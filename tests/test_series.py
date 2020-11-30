from math_series import __version__
from math_series.series import fibonacci,lucas,sum_series
from math_series.series import series_new


def test_version():
    assert __version__ == '0.1.0'

def test_six():
    actual= fibonacci(6)
    expected = 8
    assert actual == expected

def test_four():
    actual = lucas(4)   
    expected = 7
    assert actual == expected

def test_new():
    actual =  series_new(5,4,3)
    expected = 27
    assert actual == expected    

def test_sum1():
    actual = sum_series(4,0,1)
    expected = 3
    assert actual == expected

def test_sum2():
    actual = sum_series(4,2,1)
    expected = 7
    assert actual == expected

def test_sum3():
    actual = sum_series(5)
    expected = 5
    assert actual == expected
    
def test_sum4():
    actual = sum_series(5,3,1)
    expected = 14
    assert actual == expected

def test_fibonacci_negative():
    actual =  fibonacci(-5)
    expected  = "Don't use  Negative values "
    assert actual == expected




 