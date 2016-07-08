def uppercase_words(msg):
    uppercase_words = 0
    for word in msg.split(' '):
        if len(word) > 0 and word.upper() == word:
            uppercase_words += 1
    return uppercase_words
