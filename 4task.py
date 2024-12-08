def binary(arr, value):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= value:
            left = mid + 1
        else:
            right = mid - 1
    return left

if __name__ == "__main__":
    N, M = map(int, input().split())
    U, V = map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    q = int(input())

    u.sort()
    v.sort()

    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())

        region_x1 = binary(u, x1)
        region_x2 = binary(u, x2)

        region_y1 = binary(v, y1)
        region_y2 = binary(v, y2)

        if region_x1 == region_x2 and region_y1 == region_y2:
            print("YES")
        else:
            print("NO")


