from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017')
db = client['signup']
collection = db['users']




@app.route('/signup', methods=['POST'])
def signup():
    # Extract form data
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    # Prepare data to be inserted
    user_data = {
        'username': username,
        'password': password,
        'email': email
    }

    # Insert data into MongoDB
    collection.insert_one(user_data)
    # Query documents from the collection
    result = collection.find({'name': 'John'})
    for document in result:
        print(document)
    # Close MongoDB connection
    client.close()

    # Redirect or return a response
    return 'Signup successful!'

if __name__ == '__main__':
    app.run()
