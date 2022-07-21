import pytest

import chekers.check
from title_converter import cut_title_until_value
from testdata.data import positive_suit, positive_suit_with_length


class TestPositive:

    @pytest.mark.parametrize("param", positive_suit)
    def test_func_positive_with_strict_new_title_length(self, param):
        result = cut_title_until_value(param)
        chekers.check.function_works_correctly(param, 25, result)

    @pytest.mark.parametrize("param", positive_suit_with_length)
    def test_func_positive_with_random_new_title_length(self, param):
        title, length = param
        result = cut_title_until_value(title, length)
        chekers.check.function_works_correctly(title, length, result)
