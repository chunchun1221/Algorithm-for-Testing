from solution import inPalindrome
import pytest

def test_inPalindrome():
    assert inPalindrome("") == True
    assert inPalindrome("a") == True
    assert inPalindrome("aa") == True
    assert inPalindrome("aba") == True
    assert inPalindrome("abba") == True
    assert inPalindrome("abcba") == True
    assert inPalindrome("abc") == False
    assert inPalindrome("abca") == False
    assert inPalindrome("abcb") == False
    assert inPalindrome("abcd") == False

if __name__ == "__main__":
    pytest.main()