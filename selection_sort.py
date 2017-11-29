def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in xrange(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    new_array = list()
    for i in xrange(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array


def main():
    list = [1, 7, 4, 9, 2, 14, 67, 32, 11]
    print selection_sort(list)

if __name__ == '__main__':
    main()