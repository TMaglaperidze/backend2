from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    service_name = os.getenv('NAME', 'Unknown Service')
    return jsonify({"status": "up", "service_name": service_name}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
