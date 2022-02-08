def dfs2(graph, start_node):
    # deque 패키지 불러오기
    from collections import deque
    visited = []
    not_visited = deque()

    # 시작 노드 설정
    not_visited.append(start_node)

    # 방문이 필요한 리스트가 아직 존재한다면
    while not_visited:
        # 시작 노드를 지정하고
        node = not_visited.popleft()

        # 만약 방문한 리스트에 없다면
        if node not in visited:
            # 방문 리스트에 노드를 추가
            visited.append(node)
            # 인접 노드들을 방문 예정 리스트에 추가
            not_visited.extend(graph[node])

    return visited
