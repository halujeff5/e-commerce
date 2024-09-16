from flask import Flask, render_template, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, text
from sqlalchemy import desc, create_engine
from sqlalchemy.sql import func
from flask_cors import CORS
import requests, json
import os
from models import db, Product, connect_db

app = Flask(__name__) 

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


  
with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    app.config['SQLALCHEMY_RECORD_QUERIES'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    db.app= app
    db.init_app(app)
    db.create_all()
    
app.app_context().push()
connect_db(app)

@app.route('/')
def home():
    query = "SELECT DISTINCT category FROM products WHERE category LIKE '%Motorbike%';"
    engine = create_engine(os.environ.get("URL"))
    with engine.connect() as connection:
        results = connection.execute(text(query))
    
    query = "SELECT * FROM PRODUCTS WHERE category LIKE '%Motorbike%' LIMIT 25;" 
    engine = create_engine(os.environ.get("URL"))
    with engine.connect() as connection:
        resp = connection.execute(text(query))    
    return render_template('intro.html', results=results, resp= resp)