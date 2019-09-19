import copy
n = int(input())
arr = list(map(int,input().split()))
arrSorted = sorted(arr)
left = 0
right = 0
for i in range(n):
    if arr[i] != arrSorted[i]:
        left = i
        break
for i in range(n-1,-1,-1):
    if arr[i] != arrSorted[i]:
        right = i
        break
if arr == arrSorted:
    print("yes")
    print("1 1")
else:
    fakeArr = copy.deepcopy(arr)
    j = 0
    for i in range(left,right + 1):
        fakeArr[i] = arr[right - j]
        j += 1
    if fakeArr == arrSorted:
        print("yes")
        print(str(left + 1),str(right + 1))
    else:
        print("no")
