# Quick sort is a divide-and-conquer algorithm that sorts a list by partitioning 
# it around a chosen element called the "pivot." The main idea is to rearrange the 
# list so that all elements less than the pivot come before it, and all elements 
# greater than or equal to the pivot come after it. This process is called partitioning.

# Select a pivot element from the list (the choice can be arbitrary).
# Rearrange the elements so that everything less than the pivot is on its 
# left, and everything greater than or equal to the pivot is on its right.
# The pivot is now in its final sorted position.
# Recursively apply the same process to the sublists on the left and right of the pivot.

# One common way to partition is to use two pointers: one starting just before the beginning 
# of the interval, and one at the end. Move the left pointer forward until you find an 
# element greater than or equal to the pivot, and move the right pointer backward until you 
# find an element less than or equal to the pivot. If the pointers haven't crossed, swap 
# these two elements and continue. When the pointers meet or cross, swap the pivot into its 
# correct position. This ensures that after partitioning, the pivot separates the list into 
# two parts that can be sorted independently.

def sort_list_interval(unsorted_list: list[int], start: int, end: int) -> None:
    # If segment is 1 or 0, it's sorted
    if end - start <= 1:
        return

    # Using last element as the pivot
    pivot = unsorted_list[end - 1]
    start_ptr, end_ptr = start, end - 1

    # Partitioning process
    while start_ptr < end_ptr:
        # Find the next element from the left that is larger than the pivot
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1

        # Find the next element from the right that is smaller than or equal to the pivot
        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1

        # Swap if pointers haven't met
        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]

    # Place pivot in its final position
    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]

    # Sort left and right of the pivot
    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)

def sort_list(unsorted_list: list[int]) -> list[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
    return unsorted_list

if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(" ".join(map(str, res)))