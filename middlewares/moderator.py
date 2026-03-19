BAD_WORDS = ["so'kinish", "spam"]

def is_bad(text):
    text = text.lower()
    for word in BAD_WORDS:
        if word in text:
            return True
    return False
