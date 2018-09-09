from .app import db


class Drug(db.Model):
    __tablename__ = 'drugs'

    id = db.Column(db.Integer, primary_key=True)
    var1 = db.Column(db.String(64))
    var2 = db.Column(db.Float)
    var3 = db.Column(db.Float)

    def __repr__(self):
        return '<Drug %r>' % (self.var1)
