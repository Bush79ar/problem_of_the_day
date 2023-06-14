def get_total_length(arr):
    total_length = 0
    for item in arr:
        if isinstance(item, list):
            total_length += get_total_length(item)
        else:
            total_length += len(str(item))
    return total_length
input_array = [1,2,3,[4,5,[6,7]]]
result = get_total_length(input_array)
print(result)
