# The binary decision we must make when we look at an element is:

# If the element is false, we discard everything to the left and the current element itself.
# If the element is true, the current element could be the first true although there may be other 
# true to the left. We discard everything to the right but what about the current element?
# We can either keep the current element in the range or record it somewhere and then discard it. 
# Here we choose the latter.

# We keep a variable boundary_index that represents the currently recorded leftmost true's index.
# If the current element is true, then we update boundary_index with its index and discard everything 
# to the right including the current element itself since its index has been recorded by the variable.

def find_boundary(arr: list[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

if __name__ == "__main__":
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)