from online_ordering import app
from flask import render_template
from online_ordering.models import MenuItem


@app.route('/')
def home():
    items = MenuItem.query.all()
    return render_template('home.html', items=items)