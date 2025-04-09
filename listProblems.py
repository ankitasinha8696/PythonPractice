

# # Using list comprehension to sum each inner list
# output = [sum(column) for column in zip(*nested_list)]

# print(output)

# my_list = [1, 2, 3] + [4, 5] * 2
# print(my_list)

def flatten_list(input_list):
    flat_list = []
    for item in input_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def main():
    nested_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    nested_list_2 = [1, [2, 3], [4, [5, 6, [7, 8], 9]]]
    print(flatten_list(nested_list_2))

if __name__ == "__main__":
    main()

