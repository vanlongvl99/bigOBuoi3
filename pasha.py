def getMaxlWater(n,w,a):
    a.sort()
    minCup = min(a[0],a[n]/2)
    if minCup*3*n > w:
        print(w)
        exit()
    return minCup*3*n


if __name__ == "__main__":
    n, w = map(int,input().split())
    a = list(map(int,input().split()))
    result = getMaxlWater(n,w,a)
    if result%1 != 0:
        print(result)
    else:
        print(int(result))