from ..hello import hello


def test_hello():
    assert hello() == 'Hello stranger!'
    assert hello('') == 'Hello!'
    assert hello('Matt') == 'Hello Matt!'
