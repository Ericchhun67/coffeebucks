from flask import Flask, Blueprint, render_template, request, redirect, url_for
from extensions import db


pages_bp = Blueprint('pages', __name__)


@pages_bp.route('/')
def index():
    return render_template('index.html')


@pages_bp.route('/contact')
def contact():
    return render_template('contact.html')



@pages_bp.route('/about')
def about():
    return render_template('about.html')




@pages_bp.route('/orders')
def orders():
    return render_template('orders.html')


@pages_bp.route('/edit_orders')
def edit_orders():
    return render_template('edit_orders.html')


@pages_bp.route('/locations')
def locations():
    return render_template('locations.html')
