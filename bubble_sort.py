def bubble_sort(unsorted_list: list):
    for i in range(len(unsorted_list)):

        for j in range(len(unsorted_list) - 1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

    return unsorted_list


unsorted_list = [3, 45, 12, 78, 79, 19, 61]

print(bubble_sort(unsorted_list))