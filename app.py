from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt, generate_password_hash

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1111@localhost:5432/Grocery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Routes

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def home1():
    return render_template('home.html')

# Products Route
@app.route('/products.html')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

# User Registration
@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists.", "error")
            return redirect(url_for('signup'))

        # Add new user
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registered successfully! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')


# User Login
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # Retrieve plain text password

        # Fetch user from the database
        user = User.query.filter_by(username=username).first()

        # Directly compare the passwords
        if user and user.password == password:
            session['user_id'] = user.id
            flash("Logged in successfully!", "success")
            return redirect(url_for('home1'))
        else:
            flash("Invalid credentials.", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

# Cart Route
@app.route('/cart.html')
def cart():
    # Assuming you would query the cart items here
    # cart_items = Cart.query.filter_by(user_id=session.get('user_id')).all()
    return render_template('cart.html')

# Checkout Route
@app.route('/checkout.html')
def checkout():
    # Assuming you would query cart items and calculate the total price
    # and render them in the checkout.html
    return render_template('checkout.html')

@app.route('/profile.html')
def profile():
    # Check if user is logged in
    if 'user_id' not in session:
        flash("Please log in to view your profile.", "error")
        return redirect(url_for('login'))

    # Fetch the user from the database using the stored user_id
    user = User.query.get(session['user_id'])

    if user:
        return render_template('profile.html', username=user.username)
    else:
        flash("User not found.", "error")
        return redirect(url_for('login'))

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Logged out", "success")
    return redirect(url_for('home'))

# Run the App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)


