import pytest

from api.util import uuidgen

@pytest.mark.run(order=2)
def test_uuidgen_func():
    assert len(uuidgen()) == 32
