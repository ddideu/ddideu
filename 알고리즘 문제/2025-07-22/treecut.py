import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
l_p = 0
r_p = max(trees)
# 2분탐색 하듯이 해봤지만 시간 초과가 걸린다. 아마 2중 반복문 때문인것 같다.
while l_p <= r_p:
    m_p = (l_p + r_p) // 2
    ins = 0
    for tree in trees:
        if m_p < tree:
            ins += tree - m_p
    if ins < M:
        r_p = m_p - 1
    else:
        l_p = m_p + 1
print(r_p)
