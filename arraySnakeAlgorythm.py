test_array = [
    [1, 2, 3, 48, 96],
    [4, 5, 6, 101, 201],
    [7, 8, 9, 555, 952],
    [10, 11, 12, 1599, 2788],


]

result = []

for i in range(0, len(test_array), 2):
    result += test_array[i]+test_array[i+1][::-1]

print(result)
