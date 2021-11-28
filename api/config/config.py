from os import environ

class Config:

    ENV = environ.get("NEPTUNE_API_ENV", "production")

    DEBUG = bool(int(environ.get("NEPTUNE_API_DEBUG", "0")))

    TESTING = bool(int(environ.get("NEPTUNE_API_TESTING", "0")))

    JSONIFY_PRETTYPRINT_REGULAR = True

    RESTFUL_JSON = { "indent": 2, "sort_keys": True }

    SQLALCHEMY_DATABASE_URI = environ.get("NEPTUNE_API_DATABASE_URI", None)

    SQLALCHEMY_ECHO = TESTING

    SQLALCHEMY_RECORD_QUERIES = TESTING

    SQLALCHEMY_TRACK_MODIFICATIONS = TESTING
