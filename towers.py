n = int(input())
li = list(map(int,input().split()))
cnt = [0]*1001
maxBuilt = 0
count = 0
for i in range(n):
    cnt[li[i]] += 1
    if cnt[li[i]] == 1:
        count += 1
    if maxBuilt < cnt[li[i]]:
        maxBuilt = cnt[li[i]]
print(maxBuilt,count)

