import pytest

from api.api import db

@pytest.mark.run(order=1)
def test_app_env(app):
    assert app.config["ENV"] == "testing"

@pytest.mark.run(order=1)
def test_app_db_name(app):
    with app.app_context():
        result = db.engine.execute("SELECT database();").first()
    assert result[0] == "testing"
