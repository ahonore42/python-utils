from heapq import heappop, heappush

def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    res: list[int] = []
    heap: list[tuple[int, list[int], int]] = []
    for current_list in lists:
        # push first number of each list into the heap
        heappush(heap, (current_list[0], current_list, 0))  # 1

    while heap:
        val, current_list, head_index = heappop(heap)
        res.append(val)
        head_index += 1
        # if there are more numbers in the list, push into the heap
        if head_index < len(current_list):
            heappush(heap, (current_list[head_index], current_list, head_index))

    return res

if __name__ == "__main__":
    lists = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_k_sorted_lists(lists)
    print(" ".join(map(str, res)))