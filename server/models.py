from flask_sqlalchemy import SQLAlchemy

# Create an instance of the SQLAlchemy class
db = SQLAlchemy()

# Define the Owner model
class Owner(db.Model):
    # Set the table name
    __tablename__ = 'owners'

    # Define columns in the 'owners' table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for the owner
    name = db.Column(db.String, unique=True)  # Name of the owner (unique)

    # Establish a relationship with the Pet model using backref
    pets = db.relationship('Pet', backref='owner')  # Relationship with the Pet model

    # String representation of the Owner object
    def __repr__(self):
        return f'<Pet Owner {self.name}>'

# Define the Pet model
class Pet(db.Model):
    # Set the table name
    __tablename__ = 'pets'

    # Define columns in the 'pets' table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for the pet
    name = db.Column(db.String)  # Name of the pet
    species = db.Column(db.String)  # Species of the pet

    # Establish a foreign key relationship with the 'owners' table
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))  # Foreign key linking to the Owner table

    # String representation of the Pet object
    def __repr__(self):
        return f'<Pet {self.name}, {self.species}>'
