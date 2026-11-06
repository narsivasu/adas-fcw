from is_safe import is_safe_distance

def test_true():
    assert is_safe_distance(22,2)==True

def test_false():
    assert is_safe_distance(2,2)==False
