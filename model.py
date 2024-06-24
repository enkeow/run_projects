from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    data_birth = db.Column(db.Integer, nullable=True)

class Races(db.Model):
    id_racers = db.Column(db.Integer, primary_key=True)
    name_races = db.Column(db.String, nullable=False)
    distance_races = db.Column(db.Integer, nullable=False)
    data_races = db.Column(db.Integer, nullable=False)
    location_races = db.Column(db.String, nullable=False)
    info_races = db.Column(db.Text, nullable=False)

class Club_runners():
    id_club = db.Column(db.Integer, primary_key=True)
    location_club = db.Column(db.String, nullable=False)
    type_club = db.Column(db.String, nullable=False)

class Articles_run():
    id_articles = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)



    