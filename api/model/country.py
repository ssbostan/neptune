from api.api import db
from api.util import uuidgen

class Country(db.Model):

    id = db.Column(db.String(32), primary_key=True, default=uuidgen)
    code = db.Column(db.String(3), unique=True, index=True, nullable=False)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    capital = db.Column(db.String(64), index=True, nullable=False)
    longitude = db.Column(db.Float, nullable=False, default=1)
    latitude = db.Column(db.Float, nullable=False, default=1)
