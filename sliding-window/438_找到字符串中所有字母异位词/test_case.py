import pytest
from solution import fin_anagrams

def test_case():
    s = "cbaebabacd"
    p = "abc"
    expected = [0, 6]
    assert fin_anagrams(s, p) == expected

def test_case2():
    s = "abab"
    p = "ab"
    expected = [0, 1, 2]
    assert fin_anagrams(s, p) == expected


if __name__ == "__main__":
    pytest.main([__file__])