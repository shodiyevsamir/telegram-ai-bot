import time

users = {}
allowed_users = {}
premium_users = {}

def save_user(user_id):
    users[user_id] = True

def get_users():
    return list(users.keys())

# ✅ RUXSAT
def allow_user(user_id, duration=None):
    if duration:
        allowed_users[user_id] = time.time() + duration
    else:
        allowed_users[user_id] = None

def is_allowed(user_id):
    if user_id not in allowed_users:
        return False

    expire = allowed_users[user_id]

    if expire is None:
        return True

    if time.time() < expire:
        return True
    else:
        del allowed_users[user_id]
        return False

# 💸 PREMIUM
def add_premium(user_id):
    premium_users[user_id] = True

def is_premium(user_id):
    return user_id in premium_users

def get_allowed_users():
    return list(allowed_users.keys())
