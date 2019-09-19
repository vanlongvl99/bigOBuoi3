n, a, b = map(int,input().split())
arrH = list(map(int,input().split()))
arrH.sort()
print(arrH[n - a] - arrH[b -1])