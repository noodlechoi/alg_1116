edges = [ 
  (0, 6, 304), (0, 10, 460), (0, 22, 326), (1, 3, 75), (1, 13, 56), 
  (1, 18, 104), (1, 19, 463), (1, 21, 421), (2, 8, 89), (2, 12, 234), 
  (2, 15, 389), (2, 16, 118), (3, 15, 386), (4, 5, 186), (4, 10, 259), 
  (4, 14, 455), (4, 15, 347), (4, 19, 357), (4, 21, 249), (5, 10, 157), 
  (5, 14, 285), (5, 15, 413), (5, 19, 189), (6, 7, 285), (6, 22, 123), 
  (6, 24, 123), (7, 22, 176), (7, 24, 350), (8, 15, 443), (8, 16, 86), 
  (8, 17, 205), (9, 15, 413), (9, 18, 184), (9, 19, 378), (9, 21, 361), 
  (9, 23, 65), (10, 14, 376), (11, 17, 398), (11, 20, 228), (12, 16, 288), 
  (12, 17, 300), (12, 24, 405), (13, 18, 107), (13, 21, 448), (14, 23, 307), 
  (15, 19, 444), (15, 23, 369), (16, 17, 209), (17, 20, 430), (18, 23, 247), 
  (19, 21, 267), (22, 24, 227), 
]
num_vertex = 25

INF = float('inf')
# inf가 들어있는 25 * 25 2차원 배열
D = [[INF for _ in range(num_vertex)] for _ in range(num_vertex)]
# 직접 갈 수 있는 것
V = [[ -1 for _ in range(num_vertex)] for _ in range(num_vertex)]

for s, e, w in edges:
  D[s][e] = w
  D[e][s] = w

# print(D)

# k = 경유지
for k in range(num_vertex):
  for s in  range(num_vertex):
    if s == k: continue
    for e in range(num_vertex):
      if e == s or e == k: continue
      v = D[s][k]+ D[k][e] # s에서 e 갈 때 k 경유하는 비용
      if D[s][e] > v:
        D[s][e] = v
        # s에서  e갈 때는 k를 반드시 들렸다 가야한다는 것을 기록한다.
        V[s][e] = k

def getPath(s, e):
  k = V[s][e]
  # 한번도 V[s][e] = k 코드가 실행되지 않은 것
  if k == -1: return f'->{e}'
  return getPath(s, k) + getPath(k, e)



for s in range(num_vertex):
  for e in range(num_vertex):
    if s == e: continue
    path = getPath(s, e)
    cost = D[s][e]
    print(f'{s}{path} ({cost})')