users = {}

def save_user(user_id):
    users[user_id] = True

def get_users():
    return list(users.keys())
