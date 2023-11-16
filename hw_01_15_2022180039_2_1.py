d = [2,5,9,3,7,2,3,8,2,3]

mc = len(d) - 1

# 10 X 10개의 0을 넣은 이차원 배열
C = [[0 for _ in range(mc + 1) for _ in range(mc + 1)]]
# 마지막 곱셈의 위치?
P = [[0 for _ in range(mc + 1) for _ in range(mc + 1)]]

INF = float('INF')

# 부분 문제 크기 : 1일 때는 0이기 때문에 2부터 루프 돌기
for sps in range(2, mc + 1): # Sub-Problem Size
    # 부분 문제의 개수
    spc = mc - sps + 1# Sub-Problem Count
    for beg in range(1, spc + 1):
        end = beg + sps - 1 # end is inclusive
        C[beg][end] = INF
        for k in range(beg, end):
            t = C[beg][k] + C[k + 1][end] + d[beg - 1] * d[k] * d[end]
            if C[beg][end] > t:
                C[beg][end] = t
                P[beg][end] = k

def getMultStr(s, e):
    if s == e: return f'A{s}'
    p = P[s][e]
    return f'({getMultStr(s, p)}x{getMultStr(p+1,e)})'

print(f'mult = {C[1][mc]} expression = {getMultStr(1, mc)}')