from flask import Flask, request, jsonify

app = Flask(__name__)

# Contoh database sederhana (sementara)
data_store = []

@app.route('/get', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/add', methods=['POST'])
def add_data():
    content = request.json
    data_store.append(content)
    return jsonify({"message": "Data added!", "data": content}), 201

if __name__ == '__main__':
    app.run()
