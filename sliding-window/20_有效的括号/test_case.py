import pytest
from solution import isVail

def test_isVail():
    assert isVail("()") == True
    assert isVail("()[]{}") == True
    assert isVail("(]") == False
    assert isVail("([)]") == False
    assert isVail("{[]}") == True


if __name__ == "__main__":
    pytest.main()