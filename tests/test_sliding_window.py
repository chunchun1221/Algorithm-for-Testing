import pytest
from


class TestSlidingWindow:
    def test_basic_case(self):
        assert check_inclusion("ab", "eidbaooo") == True

    def test_no_match(self):
        assert check_inclusion("abc", "ccccbbbbaaaa") == False