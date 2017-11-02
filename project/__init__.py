from flask import Flask, jsonify

# Instantiate the app
app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping_pong:
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
