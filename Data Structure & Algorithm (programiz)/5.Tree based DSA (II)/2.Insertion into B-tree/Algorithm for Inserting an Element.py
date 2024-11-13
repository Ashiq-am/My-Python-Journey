''''''
"""
BreeInsertion(T, k)
r  root[T]
if n[r] = 2t - 1
    s = AllocateNode()
    root[T] = s
    leaf[s] = FALSE
    n[s] <- 0
    c1[s] <- r
    BtreeSplitChild(s, 1, r)
    BtreeInsertNonFull(s, k)
else BtreeInsertNonFull(r, k)
BtreeInsertNonFull(x, k)
i = n[x]
if leaf[x]
    while i ≥ 1 and k < keyi[x]
        keyi+1 [x] = keyi[x]
        i = i - 1
    keyi+1[x] = k
    n[x] = n[x] + 1
else while i ≥ 1 and k < keyi[x]
        i = i - 1
    i = i + 1
    if n[ci[x]] == 2t - 1
        BtreeSplitChild(x, i, ci[x])
        if k &rt; keyi[x]
            i = i + 1
    BtreeInsertNonFull(ci[x], k)
BtreeSplitChild(x, i)
BtreeSplitChild(x, i, y)
z = AllocateNode()
leaf[z] = leaf[y]
n[z] = t - 1
for j = 1 to t - 1
    keyj[z] = keyj+t[y]
if not leaf [y]
    for j = 1 to t
        cj[z] = cj + t[y]
n[y] = t - 1
for j = n[x] + 1 to i + 1
    cj+1[x] = cj[x]
ci+1[x] = z
for j = n[x] to i
    keyj+1[x] = keyj[x]
keyi[x] = keyt[y]
n[x] = n[x] + 1



"""