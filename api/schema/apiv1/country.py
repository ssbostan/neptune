from api.api import ma
from api.model import Country

class CountrySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Country

    id = ma.auto_field(dump_only=True)
    code = ma.auto_field()
    name = ma.auto_field()
    capital = ma.auto_field()
    longitude = ma.auto_field()
    latitude = ma.auto_field()
