from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
db = client["testdb"]
collection = db["testcollection"]

@app.route('/api1', methods=['GET'])
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
