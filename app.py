from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    # Here you can call your selenium script or logic
    # For demo, just echo back the query
    return jsonify({"result": f"Searched for {query}"})

if __name__ == '__main__':
    app.run(debug=True)