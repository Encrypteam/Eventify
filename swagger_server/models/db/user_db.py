from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    identity_document = db.Column(db.String(255), nullable=False)
    inscriptions = db.relationship('InscriptionModel', back_populates="user",
                                    primaryjoin="InscriptionModel.user_id==UserModel.id", cascade="all, delete-orphan")