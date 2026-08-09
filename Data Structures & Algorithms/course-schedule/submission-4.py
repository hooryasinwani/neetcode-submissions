class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for course, pre in prerequisites:
            graph[course].append(pre)
        visiting = set()
        visited = set()
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for pre in graph[course]:
                if dfs(pre) == False:
                    return False
            visiting.remove(course)
            visited.add(course)
            graph[course]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True