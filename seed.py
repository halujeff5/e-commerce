from flask import Flask
from sqlalchemy.orm import Session
from models import Product
from models import db, connect_db, Product
import pandas as pd
import numpy as np
from sqlalchemy import text
from sqlalchemy import create_engine

from app import app

app.app_context().push()
# db.engine.execute('CREATE SCHEMA e-commerce;')
db.create_all()


df=pd.read_pickle('~/Downloads/file1.pkl')


for i in range(0, 50000):
    
    stuff = Product(
    title = df['title'][i],
    image= df['imgUrl'][i],
    price = df['price'][i],
    category = df['categoryName'][i],
    stars = df['stars'][i]
    )
    db.session.add(stuff)

db.session.commit()