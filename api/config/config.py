from os import environ

class Config:

    ENV = environ.get("NEPTUNE_API_ENV", "development")

    DEBUG = bool(environ.get("NEPTUNE_API_DEBUG", "0"))

    TESTING = bool(environ.get("NEPTUNE_API_TESTING", "0"))
