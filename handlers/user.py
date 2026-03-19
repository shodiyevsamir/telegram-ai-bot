users = {}
allowed_users = set()

def save_user(user_id):
    users[user_id] = True

def get_users():
    return list(users.keys())

def allow_user(user_id):
    allowed_users.add(user_id)

def is_allowed(user_id):
    return user_id in allowed_users
