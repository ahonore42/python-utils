def sort_list(unsorted_list: list[int]) -> list[int]:
    n = len(unsorted_list)
    for i in range(n):
        # Assume the current position as minimum
        min_index = i

        # Find the minimum element's index from the rest of the list
        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j

        # Swap the minimum element with the first element
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list

if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(" ".join(map(str, res)))