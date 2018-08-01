
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Variation(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(250))
    keyword = db.Column(db.String)

    def to_dict(self):
        variations = Variation.query.all()
        v_all = []

        for v in variations:
            variation = dict(
                id=v.id,
                label=v.label
            )
            v_all.append(variation)
        return v_all