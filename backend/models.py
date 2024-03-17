from config import db # Import the database from the db file (the db variable) in order to give us access to SQLAlchemy


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def to_json(self):
        # JavaScript Object Notation
        # We are going to make all the above into a JSON object to return to the frontend, using Camel case, but in Python we are writting snake case
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }
    
    