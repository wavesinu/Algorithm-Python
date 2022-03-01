N, M = map(int, input().split())
# 2차원 list의 정보를 입력
graph = []
for i in range(N):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 주어진 좌표를 벗어날 경우 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드를 방문으로 처리
        graph[x][y] = 1
        # 상하 좌우의 좌표를 재귀적으로 호출, 탐색
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 dfs 탐색 수행
        if dfs(i, j) is True:
            result += 1

print(result)
