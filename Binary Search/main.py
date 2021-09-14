def binary_search(array, key):
    start_index = 0
    final_index = len(array) - 1
    index = None

    while start_index <= final_index:
        mid = int((start_index + final_index) / 2)

        if array[mid] == key:
            index = mid
            final_index = mid - 1
        elif array[mid] < key:
            start_index = mid + 1
        else:
            final_index = mid - 1

    return index


def search_lower_bound(array, key):
    start_index = 0
    final_index = len(array) - 1

    while start_index <= final_index:
        mid = int((start_index + final_index) / 2)

        if array[mid] == key:
            final_index = mid - 1
        elif array[mid] < key:
            start_index = mid + 1
        else:
            final_index = mid - 1

    return start_index


numbers = [35, -1, 0, 34, 12, 5, 3, 0, 5, 12, 100, -45, 100, 3, 5, 4, 3]
numbers = sorted(numbers)

if __name__ == '__main__':
    print(numbers, end="\n\n")  # Print the sorted list

    search_list = [12, 120, 3, 9, -45]  # Search for these numbers in the list
    for number in search_list:
        idx = binary_search(numbers, number)
        if idx is not None:
            print("{} is Found at index {}".format(number, idx))
        else:
            print("{} is Not Found".format(number))

    print("\n")

    for number in search_list:
        idx = search_lower_bound(numbers, number)
        print("Lower bound for {} is {}".format(number, idx))
