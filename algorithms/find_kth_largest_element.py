from heapq import heapify, heappop

def find_kth_largest(nums: list[int], k: int) -> int:
    # max heap
    nums = [-x for x in nums]
    heapify(nums)
    for _ in range(k - 1):
        heappop(nums)
    return -nums[0]

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = find_kth_largest(nums, k)
    print(res)
