for word in words:
    if (word[0] == '@'):
        users.append(word)
    elif (word[0] == '#'):
        hash_tags.append(word)
    elif (word.find('http:') == 0):
        urls.append(word)
    elif(word == 'RT'):
        has_retweet = True

for f in urls + users + hash_tags + [retweet_term]:
    if f in words:
        words.remove(f)
