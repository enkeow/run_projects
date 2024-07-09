from flask import Flask 

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import relationship

from db import Base, engine
from sqlalchemy import Column, Integer, String


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    data_birth = db.Column(db.Date, nullable=True)
    club_runners = relationship('Club_run_user', backref='user', lazy=True)
    races = relationship('Race_user', backref='user', foreign_keys='Race_user.user_id', lazy=True)

    def __repr__(self):
        return '<User {} {}>'.format(self.name, self.email)


class Race(db.Model):
    __tablename__ = 'race'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    info = db.Column(db.Text, nullable=False)
    users = relationship('Race_user', backref='race', foreign_keys='Race_user.race_id', lazy=True)

    def __repr__(self):
        return '<Race {} {}>'.format(self.name, self.location)


class Club_run(db.Model):
    __tablename__ = 'club_run'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    users = relationship('Club_run_user', backref='club_run', lazy=True)

    def __repr__(self):
        return '<Club_run {} {}>'.format(self.location, self.type)


class Article_run(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return 'Article id: {}, title: {}'.format(self.id, self.title)


class Race_user(db.Model):
    __tablename__ = 'race_users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=False)

    def __repr__(self):
        return '<Race_user {} {}>'.format(self.user_id, self.race_id)


class Club_run_user(db.Model):
    __tablename__ = 'club_run_users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('club_run.id'), nullable=False)

    def __repr__(self):
        return '<Club_run_user {} {}>'.format(self.user_id, self.club_id)
