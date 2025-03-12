def tribonacci(signature, n):
    if n == 0:
        return []
    if n <= 3:
        return signature[:n]
    new = signature
    for i in range(n-3):
        new.append(sum(new[-3:])) 
    return new[:n]


print(tribonacci([1, 1, 1], 10))