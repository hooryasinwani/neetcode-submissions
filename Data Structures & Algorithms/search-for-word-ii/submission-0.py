class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def addWord(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char]= TrieNode()
            node = node.children[char]
        node.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        res = set()

        def dfs(node, r, c, word):
            if (r<0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] not in node.children):
                return
            char = board[r][c]
            node = node.children[char]
            word += char
            
            if node.end:
                res.add(word)
            board[r][c] = "#"
            dfs(node, r+1, c , word)
            dfs(node, r-1, c, word)
            dfs(node, r, c+1, word)
            dfs(node, r, c-1, word)

            board[r][c]= char
        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(root, r, c, "")
        return list(res)

            


        
