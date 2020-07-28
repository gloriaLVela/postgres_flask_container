import json
from flask import request

from . import create_app
from .models import Cats, db

app = create_app()

@app.route('/', methods-['GET'])
def fetch():
    cats = Cats.query.all()
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            
        }