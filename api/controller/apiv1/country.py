from flask import request
from sqlalchemy import or_ as OR

from api.api import db
from api.model import Country
from api.schema.apiv1 import CountrySchema
from api.util import jsonify

class CountryController:

    def get_countries():
        if request.is_json is False:
            return jsonify(status=405, code=101)
        countries_schema = CountrySchema(many=True)
        try:
            countries = Country.query.all()
        except:
            return jsonify(status=500, code=102) # Database error.
        return jsonify(
            {"countries": countries_schema.dump(countries)}
        )

    def get_country(country_id):
        if request.is_json is False:
            return jsonify(status=405, code=101)
        country_schema = CountrySchema()
        try:
            country = Country.query.get(country_id)
        except:
            return jsonify(status=500, code=102) # Database error.
        if country is None:
            return jsonify(status=404, code=103) # Country is not found.
        return jsonify(
            {"country": country_schema.dump(country)}
        )

    def create_country():
        if request.is_json is False:
            return jsonify(status=405, code=101)
        country_schema = CountrySchema()
        try:
            data = country_schema.load(request.get_json())
        except:
            return jsonify(status=400, code=104) # Request validation failed.
        if not data["code"] or not data["name"] or not data["capital"]:
            return jsonify(status=400, code=105) # Empty data.
        try:
            country = Country.query.filter(
                OR(
                    Country.code == data["code"].upper(),
                    Country.name == data["name"].lower()
                )
            ).first() # Select country to find any conflicts.
        except:
            return jsonify(status=500, code=102) # Database error.
        if country is not None:
            return jsonify(status=409, code=106)
        country = Country(
            code=data["code"].upper(),
            name=data["name"].lower(),
            capital=data["capital"].lower(),
            longitude=data["longitude"] if "longitude" in data else 1,
            latitude=data["latitude"] if "latitude" in data else 1,
        )
        db.session.add(country)
        try:
            db.session.commit() # Database INSERT query.
        except:
            db.session.rollback()
            return jsonify(status=500, code=102) # Database error.
        return jsonify(
            {"country": country_schema.dump(country)},
            status=201
        )
