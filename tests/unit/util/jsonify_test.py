import pytest

from api.util import jsonify

@pytest.mark.run(order=2)
def test_jsonify_func(app):
    with app.app_context():
        result = jsonify()
    assert result[0]["code"] == 100
    assert result[0]["message"] == "OK"
    assert result[1] == 200
