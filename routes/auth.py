from models.user import User
from extensions import db
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
auth_bp = Blueprint('auth', __name__)





# Authentication routes
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """ 
    1. Get user input from the registration form (username, email, password)
    2. Validate the input (check for empty fields, validate email format, etc.)
    3. Check if the user already exists
    4. Hash the password
    5. Create a new user and save to the database
    6. Redirect to the login page after successful registration
    
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        session['username'] = username # Store the username in the session for later use

        if not username or not email or not password:
            return "All fields are required. Please fill out the form completely.", 400
        
        # Check if user already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return "Username or email already exists. Please choose another.", 400
        
        # Create new user
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('pages.index')) # Redirect to the homepage after successful login
        else:
            return "Invalid username or password. Please try again.", 400
    
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    # Remove user_id from session to log out the user
    session.pop('user_id', None)
    return redirect(url_for('pages.index')) # Redirect to the homepage after logout