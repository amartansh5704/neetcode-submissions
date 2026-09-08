class TrieNode:

    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False
        self.word = None

class Solution:

    def __init__(self):
        self.root = TrieNode("")
    
    def insertWord(self, w: str) -> None:
        curr = self.root
        for c in w:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.end = True
        curr.word = w
    

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        
        for w in words:
            self.insertWord(w)

        res = []

        def dfs(i, j, curr, parent):
            if min(i,j) < 0 or i >= n or j >= m or board[i][j] == "@" or board[i][j] not in curr.children:
                return

            parent = curr
            curr = curr.children[board[i][j]]
            if curr.end:
                res.append(curr.word)
                curr.end = False

            char = board[i][j]
            board[i][j] = "@"
            dfs(i+1, j, curr, parent)
            dfs(i-1, j, curr, parent)
            dfs(i, j+1, curr, parent)
            dfs(i, j-1, curr, parent)
            board[i][j] = char
            if not curr.end and not curr.children:
                del parent.children[curr.val]
            return

        for i in range(n):
            for j in range(m):
                dfs(i, j, self.root, None)
        return res