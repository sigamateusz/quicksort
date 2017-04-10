import sys
import os
import time


os.system('clear')


def open_file(file_name):
    output_list = []
    with open(file_name) as f:
        reader = f.readlines()
    for line in reader:
        output_list.append(int(line))
    return output_list


def write_to_file(file_name, sorted_list):
    new_name = file_name.split('.')[0] + '_sorted.' + file_name.split('.')[1]
    print(new_name)

    with open(new_name, 'w+') as file:
        for number in sorted_list:
            file.write("%s\n" % number)


def quick_sort(array=None):
    if array is None:
        array = [12, 4, 5, 6, 7, 3, 1, 15]
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


def main():
    try:
        file_name = sys.argv[1]
        list_to_sort = open_file(file_name)
        start_time = time.time()
        sorted_list = quick_sort(list_to_sort)
        end_time = time.time() - start_time
        print('........', end_time, 'sec........')
        write_to_file(file_name, sorted_list)
    except IndexError:
        print('You don\'t give me any file name')


if __name__ == '__main__':
    main()
