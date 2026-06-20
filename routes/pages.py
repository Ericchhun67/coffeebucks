""" 
Date: june-5-2026
Purpose: this file defines the routes for the main pages of the Good Days coffee


"""



from flask import Flask, Blueprint, render_template, request, redirect, url_for
from extensions import db

# Blueprint for handling page routes
pages_bp = Blueprint('pages', __name__)

# Route for the home page
@pages_bp.route('/')
def index() -> str:
    return render_template('index.html')

# Route for the contact page
@pages_bp.route('/contact')
def contact() -> str:
    return render_template('contact.html')


# Route for the about page
@pages_bp.route('/about')
def about() -> str:
    return render_template('about.html')

@pages_bp.route('/locations')
def locations() -> str:
    return render_template('locations.html')
