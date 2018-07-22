from database import create_app, marsh, appObj
db = create_app()
ma = marsh()
app = appObj()
#  Products Model
class Product(db.Model):
    ind = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120),primary_key=True)
    datetime = db.Column(db.String(120), primary_key=True)
    longitude = db.Column(db.Integer, unique=False, nullable=False)
    latitude = db.Column(db.Integer, unique=False, nullable=False)
    elevation = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, ind, description, datetime, longitude, latitude, elevation):
        self.ind = ind
        self.description = description
        self.datetime = datetime
        self.longitude = longitude
        self.latitude = latitude 
        self.elevation = elevation

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('ind', 'description', 'datetime', 'longitude', 'latitude', 'elevation')