# The idea of a merge sort is divide and conquer: We divide 
# the array into two almost equally, sort them (usually another 
# merge sort), and merge the two sorted lists into one. To merge 
# the two sorted lists, have two pointers pointing towards the 
# bottom of the two lists, and in each step, add the smaller 
# element from those two into the list and move the pointer of 
# that item up by one until elements from both lists are fully added.

def sort_list(unsorted_list: list[int]) -> list[int]:
    n = len(unsorted_list)

    # Base case: A list of size 1 or 0 is already sorted
    if n <= 1:
        return unsorted_list

    # Split the list into left and right halves
    midpoint = n // 2
    left_list = sort_list(unsorted_list[:midpoint])
    right_list = sort_list(unsorted_list[midpoint:])

    result_list = []
    left_pointer, right_pointer = 0, 0

    # Merge the sorted left and right lists with two pointers
    while left_pointer < midpoint or right_pointer < n - midpoint:
        if left_pointer == midpoint:
            # If left list is empty, append element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint:
            # If right list is empty, append element from left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]:
            # Append smaller element from left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:  # Append smaller element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1

    return result_list

if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(" ".join(map(str, res)))