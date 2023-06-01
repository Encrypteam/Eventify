from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class InscriptionModel(db.Model):
    __tablename__ = 'inscriptions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    invitation_code = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    event = db.relationship('EventModel', back_populates='inscriptions', lazy=True)
    user = db.relationship('UserModel', back_populates='inscriptions', lazy=True)

