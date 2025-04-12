# Main backend script
# app/main.py
from flask import Flask, request, jsonify
from app.model_handler import validate_claim

app = Flask(__name__)

@app.route('/')
def home():
    return "Insurance Claim Validator API is running."

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    treatment = data.get('treatment')
    policy = data.get('policy')

    if not treatment or not policy:
        return jsonify({'error': 'Missing treatment or policy details'}), 400

    result = validate_claim(treatment, policy)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
