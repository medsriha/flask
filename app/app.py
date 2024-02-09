from flask import Flask, request, jsonify
import requests
import json
from collections import deque
from sentence_transformers import SentenceTransformer


app = Flask(__name__)
model = SentenceTransformer('thenlper/gte-base')
queue = deque()

def distance(v):
    return v[0] @ v[1]

def process_pairs(pairs, n_batch = 100):
    prediction = []
    for i in range(n_batch):
        prediction.append(1)

    return prediction

@app.route('/infr', methods=['POST']ççç)
def get():
    data = request.json
    id_ = data.get('id')
    pairs = data.get('pairs')
    
    queue.extend(pairs)

    if len(queue) > 100:
        predictions = process_pairs(pairs)
        queue.clear()
        return jsonify({'prediction': predictions})
    return jsonify({'prediction': ""})

      