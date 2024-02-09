from flask import Flask, request, jsonify
import requests
import json
from sentence_transformers import SentenceTransformer


app = Flask(__name__)

model = SentenceTransformer('thenlper/gte-base')

def distance(v):
    return v[0] @ v[1]

@app.route('/infr', methods=['POST'])
def get():
    data = request.json
    id_ = data.get('id')
    pairs = data.get('pairs')
    enc = model.encode(pairs)
    # Distance between v1 and v2
    mag = distance(enc)

    return jsonify({'prediction': str(mag)})

      