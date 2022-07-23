import pytest
from title_converter import trim_a_string_to_a_word
from testdata.data import negative_suit


@pytest.mark.parametrize("param", negative_suit)
def test_func_negative(param):
    if not isinstance(param, str):
        with pytest.raises(TypeError):
            assert trim_a_string_to_a_word(param) == param, "Not suitable type of error"
    else:
        pytest.fail("unexpectedly the string got in the test")
