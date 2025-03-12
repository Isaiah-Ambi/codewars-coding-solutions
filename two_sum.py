def two_sum(numbers, target):
    l = len(numbers)

    for i in range(l):

        for j in range(i + 1, l):
            if numbers[i] + numbers[j] == target:
                return (i, j)

print(two_sum([1, 2, 3], 4))
print(two_sum([3, 2, 4], 6))