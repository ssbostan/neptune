from api.model import Country
from api.schema.apiv1 import CountrySchema
from api.util import jsonify

class CountryController:

    def get_countries():
        return jsonify(status=501, code=107)

    def get_country(country_id):
        return jsonify(status=501, code=107)

    def create_country():
        return jsonify(status=501, code=107)
