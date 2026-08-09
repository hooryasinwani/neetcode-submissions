class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
        for u,v, w in times:
            graph[u].append((v, w))
        
        heap = [(0, k)]
        visited = {}

        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited[node] = cost

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost+weight, neighbor))
        if len(visited) == n:
            return max(visited.values())
        return -1
        