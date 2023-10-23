import pytest
from converter import fahrenheit

def test_conversion():
    assert fahrenheit(27) == 27 * (9/5) + 32
    assert fahrenheit(0) == 32
    assert fahrenheit(-4) == (-4) * (9/5) + 32

def test_exception():
    with pytest.raises(TypeError):
        fahrenheit(True)
    with pytest.raises(TypeError):
        fahrenheit("34")
