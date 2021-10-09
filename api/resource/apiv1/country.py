from flask_restful import Resource

from api.controller.apiv1 import CountryController

class CountryResource(Resource):

    def get(self, country_id=None):
        """
        GET /countries --> List of countries.
        GET /countries/<country_id> --> Country info.
        """
        if country_id is None:
            return CountryController.get_countries() # List of countries.
        return CountryController.get_country(country_id) # Country info.

    def post(self):
        """
        POST /countries --> Create new country.
        POST /countries/<country_id> --> Not allowed.
        """
        return CountryController.create_country() # Create new country.
