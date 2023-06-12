numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    current_number = numbers[i]
    is_greater = True
    
    # Compare with numbers to the right
    for j in range(i + 1, len(numbers)):
        if current_number < numbers[j]:
            is_greater = False
            break
    
    if is_greater:
        print(current_number)
