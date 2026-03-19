from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.secret_key = 'SecretKey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Classes and Databases
# User class to store user information
#code example:
#   new_user = User(username=u, password=p) # Create a new user instance with the provided username and password
#   db.session.add(new_user) # Add the new user to the session
#   db.session.commit() # Commit the session to save the user to the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    balance = db.Column(db.Float, default=10000.0)
    holdings = db.relationship('Holding', backref='owner', lazy=True)

class Holding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    symbol = db.Column(db.String(10))
    quantity = db.Column(db.Integer)

# Make the tables
with app.app_context():
    db.create_all()


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/trade')
def trade():
    return render_template('trade.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)