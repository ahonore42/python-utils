from heapq import heappop, heappush

def k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    heap: list[tuple[int, list[int]]] = []

    for pt in points:
        heappush(heap, (pt[0] ** 2 + pt[1] ** 2, pt))

    res = []
    for _ in range(k):
        _, pt = heappop(heap)
        res.append(pt)

    return res

if __name__ == "__main__":
    points = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = k_closest_points(points, k)
    for row in res:
        print(" ".join(map(str, row)))