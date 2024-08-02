#  `test_` is required prefixed in filename and its functions

from myproject import main

def test_function1():
    res : str = main.myFunc()
    assert res == "Hello World"

def test_function2():
    res : str = main.myFunc()
    assert res != "Pakistan"