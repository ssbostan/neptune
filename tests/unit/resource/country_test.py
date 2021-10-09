import pytest

from conftest import ValueStorage

from api.api import db
from api.model import Country

@pytest.mark.parametrize(
    ("is_json", "data", "status", "code"),
    (
        (False, "", 405, 101),
        (False, {}, 405, 101),
        (True, {}, 400, 104),
        (True, {"":""}, 400, 104),
        (True, {"code": "large"}, 400, 104),
        (True, {"code": "", "name": "", "capital": ""}, 400, 105),
        (True, {"code": "irn", "name": "iran", "capital": "tehran"}, 201, 100),
        (True, {"code": "irn", "name": "iran", "capital": "tehran"}, 409, 106)
    )
)
@pytest.mark.run(order=4)
def test_endpoint_create_country(client, is_json, data, status, code):
    result = client.post("/api/v1/countries", json=data) \
      if is_json else client.post("/api/v1/countries", data=data)
    result_data = result.get_json()
    assert result.status_code == status
    assert result_data["code"] == code
    if result.status_code == 201:
        ValueStorage.country = result_data["country"]

@pytest.mark.parametrize(
    ("is_json", "status", "code"),
    (
        (False, 405, 101),
        (True, 200, 100)
    )
)
@pytest.mark.run(order=4)
def test_endpoint_get_countries(client, is_json, status, code):
    result = client.get(
        "/api/v1/countries",
        headers={"Content-Type": "application/json"} if is_json else {}
    )
    result_data = result.get_json()
    assert result.status_code == status
    assert result_data["code"] == code

@pytest.mark.parametrize(
    ("is_json", "country_id", "status", "code"),
    (
        (False, "test", 405, 101),
        (True, "test", 404, 103),
        (True, "storage", 200, 100)
    )
)
@pytest.mark.run(order=4)
def test_endpoint_get_country(client, is_json, country_id, status, code):
    result = client.get(
        f"/api/v1/countries/{ValueStorage.country['id']}" if country_id == "storage" \
          else f"/api/v1/countries/{country_id}",
        headers={"Content-Type": "application/json"} if is_json else {}
    )
    result_data = result.get_json()
    assert result.status_code == status
    assert result_data["code"] == code

@pytest.mark.run(order=4)
def test_endpoint_create_country_cleanup(app):
    with app.app_context():
        country = Country.query.get(ValueStorage.country["id"])
        db.session.delete(country)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise AssertionError()
