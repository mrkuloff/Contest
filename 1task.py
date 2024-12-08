if __name__ == "__main__":
    N = int(input())
    target_points = list()
    hit_points = list()
    for _ in range(N):
        points = input().split()
        target_points.append(tuple(
            map(int,
                points)
        ))

    for _ in range(N):
        points = input().split()
        hit_points.append(tuple(
            map(int,
                points)
        ))

    u = (sum(x for x, y in hit_points) - sum(x for x, y in target_points)) // N
    v = (sum(y for x, y in hit_points) - sum(y for x, y in target_points)) // N

    print(u, v)