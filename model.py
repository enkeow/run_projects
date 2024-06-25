from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    data_birth = db.Column(db.Integer, nullable=True)
    races = relationship('Race_user', backref='user', lazy=True)
    club_runners = relationship('Club_run_user', backref='user', lazy=True)

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String, nullable=False)
    info = db.Column(db.Text, nullable=False)
    users = relationship('Race_user', backref='race', lazy=True)

class Club_run(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    users = relationship('Club_run_user', backref='club_run', lazy=True)

class Article_run(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

class Race_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=False)

class Club_run_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('club_run.id'), nullable=False)
