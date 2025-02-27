def average(numbers):
    total = 0
    for avg in numbers:
        total+=int(avg)
    total=total/len(numbers)
    "Return the average of a list of numbers"
    # YOUR CODE HERE
    return total

print(average([32, 78, 48, 71, 93, 71, 79, 44, 5, 42])) #56.3
print(average([5, 4, 3, 2, 1])) # 3.0
print(average([8.0, 3.14159, 17])) # 9.38053