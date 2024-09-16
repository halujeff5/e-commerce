from flask import Flask
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt
from sqlalchemy import Table, Column, Numeric, Integer, VARCHAR

db= SQLAlchemy()

def connect_db(app):
    db.app= app

    db.create_all()


class Product(db.Model):
    
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable= False)
    title = db.Column(db.String, nullable=False)
    image= db.Column(db.String, nullable=False)
    price= db.Column(db.Numeric, nullable=False)
    category= db.Column(db.String, nullable=False)
    stars= db.Column(db.Numeric, nullable=False)