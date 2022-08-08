from func_arguments import __version__
from func_arguments import question, print_point, foo


def test_version():
    assert __version__ == '0.1.0'

def question():
    assert 42 == question()
    assert 14 == question(14)

def test_point():
    pos = (4,5)
    param = {"color": "blue", "w":2, "h":1}
    print_point(*pos, **param)

def test_foo():
    assert 5 == foo(3, bar=2)
    assert 7 == foo(3, 4)
    assert 3 == foo(1, 2, pre=4)

def test_format():
    params = {"first": 34, "last": 42}
    result = "{first} is not {last}".format(**params)
    assert "34 is not 42" == result
