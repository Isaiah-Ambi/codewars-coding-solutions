def generate_hashtag(s):
    tag ='#'
    if len(s) == 0:
        return False
    for i in s.split():
        tag += i.capitalize()
    if len(tag) > 140:
        return False
    return tag

