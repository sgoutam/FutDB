__author__ = 'Rahul'
from flask import Flask

app1 = Flask(__name__)
from app import myview
app1.config.from_object('config')
