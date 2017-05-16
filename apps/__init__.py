"""
Simple Yelp with Python and Flask
"""

from flask import Flask

app = Flask(__name__)
# views will import app so this is to avoid any import failures
from apps import views
