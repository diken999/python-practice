def find_amicable(n: int) -> list[tuple[int, int]]:
    # s[x] 记录 x 的真因数之和
    s = [0] * (n + 1)
    # 倍数标记法: 把 i 累加到它所有的倍数 j 上
    # j 从 2i 起步 -> 只累加"真"因数; i 到 n//2 为止 -> 大于一半的真因数不存在
    for i in range(1, n // 2 + 1):
        for j in range(2 * i, n + 1, i):
            s[j] += i
    # 单层扫描配对: a < b 同时排除完全数(s[a]==a)和重复对
    pairs = []
    for a in range(1, n + 1):
        b = s[a]
        if a < b <= n and s[b] == a:
            pairs.append((a, b))
    return pairs


if __name__ == "__main__":
    n = int(input())
    for a, b in find_amicable(n):
        print(a, b)
