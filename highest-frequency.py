def highest_frequency (arr):
    frequency={}
    for number in arr:
        if number not in frequency:
            frequency[number] = 1
        else:
            frequency[number] += 1
    try:
        highest = max(frequency.values())
    except ValueError:
        print("arr is an empty array")
        pass
    result = []
    for number in frequency:
        if frequency[number] == highest:
            result.append(number)
    return result
print(highest_frequency([2,3,2,7,7,7,7,2,3,3,3]))


    