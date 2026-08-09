class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = set()
        visiting = set()

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
            result.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return result
        