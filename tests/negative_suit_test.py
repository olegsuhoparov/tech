import pytest
from title_converter import cut_title_until_value
from testdata.data import negative_suit


@pytest.mark.parametrize("param", negative_suit)
def test_func_negative(param):
    if not isinstance(param, str):
        with pytest.raises(TypeError):
            assert cut_title_until_value(param) == param, "Not suitable type of error"
    elif len(param) == 0:
        with pytest.raises(ValueError):
            assert cut_title_until_value(param) == param, "Not suitable type of error"
    else:
        pytest.fail("Length string for this test has to be 0")
