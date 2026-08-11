class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j]!=w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        visiting = set()
        visited = set()
        result = []

        def dfs(char):
            if char in visiting:
                return False
            if char in visited:
                return True
            visiting.add(char)

            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False
            visiting.remove(char)
            visited.add(char)
            result.append(char)
            return True
        
        for char in graph:
            if not dfs(char):
                return ""
        return "".join(reversed(result))