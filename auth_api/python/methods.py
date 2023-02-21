class Token:
    def __init__(self):
        self.users = users
        
    def generate_token(self, username, password):
        if username not in self.users:
            return {"error": "Invalid username."}, 403
        
        # Verify the password
        user = self.users[username]
        hashed_password = hashlib.sha512((user['salt'] + password).encode()).hexdigest()
        if user['password'] != hashed_password:
            return {"error": "Invalid password."}, 403
        
        # Generate the JWT Token
        payload = {
            'sub': username,
            'name': username,
            'role': user['role']
        }
        token = jwt.encode(payload, key=SECRET_KEY, algorithm='HS256')
        return {"data": token}, 200


