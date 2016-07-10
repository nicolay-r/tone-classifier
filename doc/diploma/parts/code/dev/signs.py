def signs_feature(msg, chars):
    signs = 0
    for char in chars:
        signs += msg.count(char)
    return signs
