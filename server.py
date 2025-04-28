from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Pas de texte fourni'}), 400
    
    user_text = data['text']

    #on mettra ici l e model
    fake_prediction = "positif" if "bien" in user_text.lower() else "négatif"

    return jsonify({'prediction': fake_prediction})

if __name__ == "__main__":
    app.run(debug=True)
