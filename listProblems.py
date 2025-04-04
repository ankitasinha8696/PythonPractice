nested_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

# Using list comprehension to sum each inner list
output = [sum(column) for column in zip(*nested_list)]

print(output)

my_list = [1, 2, 3] + [4, 5] * 2
print(my_list)