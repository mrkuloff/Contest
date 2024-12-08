if __name__ == "__main__":
    N = int(input())
    lines = []
    for _ in range(N):
        line = input()
        lines.append(line)
    unique_line = ''
    unique_count = -1
    for i in range(len(lines)):
        unique_symbols = set(lines[i].strip())
        if len(unique_symbols) > unique_count:
            unique_line = lines[i]
            unique_count = len(unique_symbols)
    print(unique_count, unique_line)