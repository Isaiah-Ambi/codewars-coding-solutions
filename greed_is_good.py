def score(dice):
    points = 0
    triple = False
    scores = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
    for i in dice:
        # print(points)
        count = dice.count(i)
        # print(i, count)
        if i == 1 and count < 3:
            points += 100
        if i == 5 and count < 3:
            points += 50
            # print(points)
        if count == 3 and not triple:

            points += scores[i]
            triple = True
            # for j in range(3):
            #     dice.remove(i)
        elif count > 3 and not triple:
            triple = True
            points += scores[i]
            count -= 3
            if i == 1:
                points += (count * 100)
            elif i == 5:
                points += (count * 50)
            
            # for j in range(3):
                # dice.remove(i)

        
    return points


print( score( [5, 1, 3, 4, 1] )) #250
print(score([1, 1, 1, 3, 1])) #1100
print(score( [2, 3, 4, 6, 2] )) #0
print(score( [3, 4, 5, 3, 3] )) #350
print(score( [4,4,4,3,3])) #400
print(score([2,4,4,5,4])) #450