 N,K=[int(i) for i in input().split()]
l=sorted(list(set([int(i) for i in input().split()])))
print(l[-(K)])
