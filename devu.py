n, x = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
total = 0
for i in range(n):
    total = total + arr[i]*x
    if x > 1:
        x = x -1
print(total)