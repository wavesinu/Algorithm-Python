def dfs(graph, start_node):
    # 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    not_visited, visited = list(), list()

    # 시작 노드를 설정
    not_visited.append(start_node)

    # 만약 아직도 방문이 필요한 노드가 있다면,
    while not_visited:

        # 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = not_visited.pop()

        # 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            # 방문한 목록에 추가하기
            visited.append(node)

            not_visited.extend(graph[node])

    return visited
