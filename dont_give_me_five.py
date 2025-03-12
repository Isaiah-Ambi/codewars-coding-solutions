def dont_give_me_five(start,end):
    n = 0
    l = []
    for i in range(start,end+1):
        if '5' not in str(i):
            l.append(i)
            n =+ i
    return len(l)  # amount of numbers



print(dont_give_me_five(1,9)) # 8