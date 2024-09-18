from flask import Flask, render_template, redirect, session, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import stripe
from sqlalchemy import select, text
from sqlalchemy import desc, create_engine
import requests, json
from sqlalchemy.sql import func
from models import db, Product, connect_db
import os
import pandas as pd

app = Flask(__name__)
# db=SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SQLALCHEMY_ECHO'] = True
    
with app.app_context():

    db.app= app
    db.init_app(app)
    db.create_all()
    
app.app_context().push() 
connect_db(app)

stripe.api_key = os.environ.get("API_KEY")
BASE_URL = 'https://api.stripe.com'

# query = "SELECT title from products WHERE category LIKE '%Motorbike%';"
# engine = create_engine("postgresql://postgres:postgres@localhost:5431/postgres")
# with engine.connect() as connection:
#     load_products = connection.execute(text(query))
# print(load_products)

# for ele in load_products:
#     stripe.Product.create(name= f"{ele[0]}")  


# df= pd.read_pickle('~/Downloads/main.pkl')

# response = requests.get(BASE_URL+'/v1/products')
# print(stripe.Product.list())
# resp_dict = response.json()
# print(resp_dict)


# for index, row in df.iterrows():
#     price = row.price
#     title= row.title
#     resp = requests.post(BASE_URL+'/v1/prices')
#     stripe.Price.create(
#         currency='usd',
#         unit_amount_decimal= f"{price}",
#         product_data= {'name': f"{title}"},
#     )
    
    
answer = requests.get(BASE_URL+'/v1/prices')
stripe.Price.list()
answer.json()

if __name__ == '__main__':
    app.run(debug = True)