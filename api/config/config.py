from os import environ

class Config:

    ENV = environ.get("NEPTUNE_API_ENV", "development")

    DEBUG = bool(environ.get("NEPTUNE_API_DEBUG", "0"))

    TESTING = bool(environ.get("NEPTUNE_API_TESTING", "0"))

    JSONIFY_PRETTYPRINT_REGULAR = True

    RESTFUL_JSON = { "indent": 2, "sort_keys": True }
