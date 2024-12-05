from collections import deque, defaultdict


def levit_algorithm(graph, start):
    # Количество вершин
    n = len(graph)

    # Массив расстояний (инициализируется бесконечностями)
    inf = float('inf')
    distances = [inf] * n
    distances[start] = 0

    # Буфер для вершин
    buffer = deque([start])

    # Множества вершин
    in_queue = {start}  # Множество вершин в буфере
    not_used = set(range(n)) - {start}  # Непосещённые вершины
    used = set()  # Вершины, обработанные окончательно

    while buffer:
        u = buffer.popleft()
        in_queue.discard(u)

        # Обработка всех смежных вершин
        for v, weight in graph[u]:
            if distances[v] > distances[u] + weight:
                distances[v] = distances[u] + weight
                if v in not_used:
                    buffer.append(v)
                    in_queue.add(v)
                    not_used.discard(v)
                elif v in used:
                    buffer.appendleft(v)
                    in_queue.add(v)
                    used.discard(v)

        # После обработки добавляем вершину в множество обработанных
        used.add(u)

    return distances


# Пример использования:
if __name__ == "__main__":
    # Граф представлен списком смежности: graph[вершина] = [(сосед, вес), ...]
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }

    start_vertex = 0
    result = levit_algorithm(graph, start_vertex)
    print(f"Кратчайшие пути от вершины {start_vertex}: {result}")




graph = {
    0: [(1, 1)],
    1: [(2, 2)],
    2: [(0, 3)]
}
