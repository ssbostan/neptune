import pytest

from api.api import db
from api.model import Country

@pytest.mark.run(order=3)
def test_app_cli_seed(runner):
    result = runner.invoke(args=["app", "seed"])
    assert result.exit_code == 0

@pytest.mark.run(order=3)
def test_app_cli_seed_cleanup(app):
    with app.app_context():
        country1 = Country.query.filter_by(code="IRN").first()
        country2 = Country.query.filter_by(code="GBR").first()
        db.session.delete(country1)
        db.session.delete(country2)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise AssertionError()
