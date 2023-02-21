from flask import Flask, jsonify, request
import hashlib
import hmac
import jwt
from methods import Token, Restricted

app = Flask(__name__)
login = Token("my2w7wjd7yXF64FIADfJxNs1oupTGAuW")
protected = Restricted()

# Define the users database

users = {
    'admin': {
        'password': 'encrypted-password',
        'salt': 'F^S%QljSfV',
        'role': 'admin'
    },
    'noadmin': {
        'password': 'encrypted-password',
        'salt': 'KjvFUC#K*i',
        'role': 'editor'
    },
    'bob': {
        'password': 'encrypted-password',
        'salt': 'F^S%QljSfV',
        'role': 'viewer'
    }
}


# Just a health check
@app.route("/")
def url_root():
    return "OK"


# Just a health check
@app.route("/_health")
def url_health():
    return "OK"


# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=['POST'])
def url_login():
    username = request.form['username']
    password = request.form['password']
    res, status_code = login.generate_token(username, password)
    return jsonify(res), status_code


# e.g. http://127.0.0.1:8000/protected
@app.route("/protected")
def url_protected():
    auth_token = request.headers.get('Authorization').split(" ")[1]
    res = {
        "data": protected.access_data(auth_token)
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)