from flask import Blueprint, render_template

# Blueprint lets us separate routes from main file
main = Blueprint('main', __name__)

# When someone visits the home page ('/'), show index.html
@main.route('/')
def home():
    return render_template('index.html')