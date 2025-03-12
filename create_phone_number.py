def create_phone_number(numbers):
    if len(numbers) != 10 or not all(0 <= n <= 9 for n in numbers):
        raise ValueError("Input must be an array of 10 integers between 0 and 9.")
    
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)

# Example usage:
# print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))
# Output: "(123) 456-7890"