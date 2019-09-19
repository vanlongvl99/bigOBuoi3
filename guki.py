n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
for i in range(n):
    for j in range(n-1,-1,-1):
        if a[i] == b[j]:
            print(n - j,end=" ")
            break
