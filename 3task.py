if __name__ == "__main__":
    def solve(N, k, q, heights):
        left = 0
        count_to_change = 0
        max_count = 0

        for right in range(N):
            if heights[right] >= k:
                count_to_change += 1

            while count_to_change > q:
                if heights[left] >= k:
                    count_to_change -= 1
                left += 1

            max_count = max(max_count, right - left + 1)

        return max_count

    N, k, q = map(int, input().split())
    heights = list(map(int, input().split()))

    print(solve(N, k, q, heights))