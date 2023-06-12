def progress(distances):
    count = 0
    for i in range(1, len(distances)):
        if distances[i] > distances[i - 1]:
            count += 1
    return count
distances = [2, 4, 7, 10, 8, 11]
distances1 = [5,7,6,9,8]
improvements = progress(distances)
improvements1 = progress(distances1)
print("Number of times Mohammed improved: ", improvements)
print("Number of times Mohammed improved: ", improvements1)