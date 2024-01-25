from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create a Flask application instance
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Initialize the Flask-Migrate extension with the Flask app and SQLAlchemy instance
migrate = Migrate(app, db)

# Initialize the SQLAlchemy instance with the Flask app
db.init_app(app)

# Entry point of the application
if __name__ == '__main__':
    # Run the Flask application on port 5555
    app.run(port=5555)
