from hello import more_hello


def test_more_hello():
    assert "hi" == more_hello()


def test_more_hello2():
    assert "hai" == more_hello()
