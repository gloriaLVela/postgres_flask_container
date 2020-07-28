import json
from flask import request

from models import Cats, db
from init import create_app

# Create the app by calling the create_app() from __init__.py. 
# Defines four functions for our four routes for the "RESTful" API. 
app = create_app()

@app.route('/', methods=['GET'])
# Get the information about all cats 
def fetch():
    cats = Cats.query.all()
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed            
        }

        all_cats.append(new_cat)
    return json.dumps(all_cats), 200

@app.route('/add', methods=['POST'])
# Add a new cat
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    cat = Cats(name =name, price=price, breed=breed)
    db.session.add(cat)
    db.session.commit()

    return json.dumps("Added"), 200

@app.route('/remove/<cat_id>', methods=['DELETE'])
# Remove a cat
def remove(cat_id):
    Cats.query.filter_by(id=cat_id).delete()
    db.session.commit()
    return json.dumps("Deleted"), 200

@app.route('/edit/<cat_id>', methods=['PATCH'])
# Edit a cat's price
def edit(cat_id):
    data = request.json()
    new_price = data['price']
    cat_to_update = Cats.query.filter_by(id=cat_id).all()[0]
    cat_to_update.price= new_price
    db.session.commit()
    return json.dumps("Edited"), 200