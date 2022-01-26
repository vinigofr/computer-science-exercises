from testing_fail import divide
import pytest

def test_divide_when_other_number_is_zero_raises_an_exception():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
      divide(2, 0)