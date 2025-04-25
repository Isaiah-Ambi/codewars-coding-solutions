def solution(s):
    l = len(s)
    n = ''
    for i in range(l):
        if s[i] == ' ':
            continue
        if s[i].isupper():
            n += ' '
        n += s[i]
    return n.strip()  # remove trailing space


print(solution('break CamelCase'))
# solution('helloWorld')