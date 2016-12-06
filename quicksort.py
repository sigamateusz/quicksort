def quick_sort(array=[12, 4, 5, 6, 7, 3, 1, 15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quick_sort(less)+equal+quick_sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:   # when you only have one element in your array, just return the array.
        return array


input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 4546, 0, 5]
sorted_list = quick_sort(input_list)
print(sorted_list)
