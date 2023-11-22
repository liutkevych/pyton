from hello import hello

def test_hello():
    assert hello() == 'Hello, World'

def test_argument():
    assert hello("alex") == "Hello, Alex"

