from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Service is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
