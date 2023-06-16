"""Flask app for Cupcakes"""
from flask import Flask, request, redirect, render_template, jsonify
from models import db, connect_db, Cupcake
from forms import AddCupcake
from secret import secret
import json
import pdb

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{secret}@localhost/cupcake'
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

def dictify(cupcake):
    return {
        'id': cupcake['id'],
        'flavor': cupcake['flavor'],
        'size': cupcake['size'],
        'rating': cupcake['rating'],
        'image': cupcake['image']
    }

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/api/cupcakes')
def all_cupcakes():
    allCupcakes = Cupcake.query.all()
    res = []
    for cupcake in allCupcakes:
        res.append(
            dictify(cupcake.__dict__)
        )
    return jsonify(cupcakes=res)

@app.route('/api/cupcakes/<int:cupcake_id>')
def one_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    res = dictify(cupcake.__dict__)
    return jsonify(cupcake=res)

@app.route('/api/cupcakes', methods=['post'])
def add_cupcake():
    cd = request.json
    cupcake = Cupcake(flavor=cd['flavor'], size=cd['size'], rating=cd['rating'])
    if 'image' in cd:
        cupcake.image = cd['image']
    db.session.add(cupcake)
    db.session.commit()
    db.session.refresh(cupcake)
    res = dictify(cupcake.__dict__)
    return (jsonify(cupcake=res), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['patch'])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    ud = request.json
    cupcake.flavor = ud['flavor']
    cupcake.size = ud['size']
    cupcake.rating = ud['rating']
    cupcake.image = ud['image']
    res = dictify(cupcake.__dict__)
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=res)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['delete'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    res = dictify(cupcake.__dict__)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(deleted=res)