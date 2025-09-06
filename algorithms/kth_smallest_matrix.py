from heapq import heappop, heappush

def kth_smallest(matrix: list[list[int]], k: int) -> int:
    n = len(matrix)
    # Keeps track of items in the heap, and their row and column numbers
    heap = [(matrix[0][0], 0, 0)]
    # Keeps track of the top of each row that is not processed
    column_top = [0] * n
    # Keeps track of the first number each row not processed
    row_first = [0] * n
    # Repeat the process k - 1 times.
    while k > 1:
        k -= 1
        min_val, row, column = heappop(heap)
        row_first[row] = column + 1
        # Add the item on the right to the heap if everything above it is processed
        if column + 1 < n and column_top[column + 1] == row:
            heappush(heap, (matrix[row][column + 1], row, column + 1))
        column_top[column] = row + 1
        # Add the item below it to the heap if everything before it is processed
        if row + 1 < n and row_first[row + 1] == column:
            heappush(heap, (matrix[row + 1][column], row + 1, column))
    return heap[0][0]

if __name__ == "__main__":
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = kth_smallest(matrix, k)
    print(res)