from flask_cors import cross_origin
from config import app, db
from flask import request, jsonify
from models import Contact

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    # A list of contact objects that have the to_json function, and runs through all the elements and applies the function to all of them
    return (jsonify({"contacts": json_contacts}), 200) # Returning an object with the name of "contacts" that contains all the contacts that we created in the above line

@app.route("/create_contact", methods=["POST"])
@cross_origin()
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name and email"}), 
            400,
        )
    
    new_contact = Contact(first_name=first_name, last_name= last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return (jsonify({"message" : str(e)}), 400)
    
    return (jsonify({"message": "User created!"}), 201)


@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id) # Runs a query to get the contact that has the user id
    
    if not contact:
        return (jsonify({"message": "User not found"}), 404)
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    
    db.session.commit() # Commit the session changes
    
    return jsonify({"message": "User updated."}), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id) # Runs a query to get the contact that has the user id
    
    if not contact:
        return (jsonify({"message": "User not found"}), 404)
    
    db.session.delete(contact)
    db.session.commit()
    
    return jsonify({"message": "User deleted!"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all() # When we start the app, get the context and then create all the different models that we have defined in our database
    
    app.run(debug=True)

