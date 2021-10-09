from api.api import apiv1 as api
from api.resource.apiv1.country import CountryResource

api.add_resource(
    CountryResource,
    "/countries",
    methods=["GET", "POST"],
    endpoint="countries"
)
api.add_resource(
    CountryResource,
    "/countries/<country_id>",
    methods=["GET"],
    endpoint="country"
)
