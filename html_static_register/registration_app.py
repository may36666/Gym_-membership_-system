# facial_recognition_login.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
import face_recognition
import json
import os

app = Flask(__name__)

# Function to check if member exists
def member_exists(name):
    with open("members.json", 'r') as json_file:
        members_data = json.load(json_file)
        for member in members_data['members']:
            if member['name'] == name:
                return True
    return False

# Define route for registration page
@app.route('/')
def registration_page():
    return render_template('registration.html')

# Define route for registration action
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']

    if member_exists(name):
        return render_template('registration_failed.html')

    # Save image to file
    file = request.files['image']
    image_path = os.path.join("uploads", f"{name}.jpg")
    file.save(image_path)

    # Encode face
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]

    # Add member to JSON
    with open("members.json", 'r') as json_file:
        members_data = json.load(json_file)
        members_data['members'].append({"name": name, "encoding": face_encoding.tolist()})

    with open("members.json", 'w') as json_file:
        json.dump(members_data, json_file)

    return render_template('registration_success.html')

if __name__ == '__main__':
    app.run(debug=True)
