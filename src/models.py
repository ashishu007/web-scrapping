from app import db

class Hotels(db.Model):
    """"""
    __tablename__ = "hotels"

    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String)
    hsr_layout = db.Column(db.String)
    location = db.Column(db.String)
    cordinates = db.Column(db.String)
    s_room = db.Column(db.String)
    p_room = db.Column(db.String)