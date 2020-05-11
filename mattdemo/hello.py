"""Demo Hello function."""


def hello(target='stranger'):
    if target:
        return f'Hello {target}!'
    else:
        return f'Hello!'
