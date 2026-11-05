from fcw import time_to_collision, warning_level

def test_ok():
    assert warning_level(time_to_collision(50, 20, 20)) == "OK"

def test_warn():
    assert warning_level(time_to_collision(25, 30, 20)) == "WARN"

def test_brake():
    assert warning_level(time_to_collision(20, 30, 10)) == "BRAKE"