from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EventModel(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Numeric(precision=8, scale=6), nullable=False)
    longitude = db.Column(db.Numeric(precision=9, scale=6), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    inscriptions = db.relationship("InscriptionModel", back_populates="event",
                                                  primaryjoin="InscriptionModel.event_id==EventModel.id",
                                                  cascade="all, delete-orphan")