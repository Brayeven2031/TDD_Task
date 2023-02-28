
from funciones import min_array

def test_min_array():
    assert min_array([1,2,3,4,0]) == 0
    assert min_array([2,14,15,-5]) == -5
    assert min_array([1,2,7,5,6]) == 1
