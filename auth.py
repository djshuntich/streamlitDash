import json
import hashlib
import os

class AuthManager:
    def __init__(self):
        self.users_file = "db/users.json"
        self._ensure_users_file()
    
    def _ensure_users_file(self):
        if not os.path.exists("db"):
            os.makedirs("db")
        if not os.path.exists(self.users_file):
            with open(self.users_file, "w") as f:
                json.dump({"admin": self._hash_password("admin123")}, f)
    
    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_user(self, username, password):
        try:
            with open(self.users_file, "r") as f:
                users = json.load(f)
            stored_hash = users.get(username)
            if stored_hash and stored_hash == self._hash_password(password):
                return True
        except Exception as e:
            print(f"Authentication error: {e}")
        return False
    
    def add_user(self, username, password):
        try:
            with open(self.users_file, "r") as f:
                users = json.load(f)
            users[username] = self._hash_password(password)
            with open(self.users_file, "w") as f:
                json.dump(users, f)
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            return False
