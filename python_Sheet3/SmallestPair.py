t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    ans = 10**18

    for i in range(n):
        for j in range(i + 1, n):
            value = A[i] + A[j] + (j + 1) - (i + 1)
            if value < ans:
                ans = value

    print(ans)
