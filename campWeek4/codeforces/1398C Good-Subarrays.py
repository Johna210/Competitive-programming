t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int,input()))
    prefix = {0:1}
    cummulative = 0
    count = 0
    for i, num in enumerate(lst):
        cummulative += num
        diff = cummulative-i-1
        if diff in prefix:
            count += prefix[diff]
            prefix[diff] += 1
        else:
            prefix[diff] = 1

    print(count)