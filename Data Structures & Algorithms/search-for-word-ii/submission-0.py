class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Fill prefix tree
        prefixTree = TrieNode()
        for word in words:
            prefixTree.addWord(word)

        results = set()
        visited = set()
        numRows = len(board)
        numCols = len(board[0])

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == numRows or c == numCols or (r, c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                results.add(word)
            
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for r in range(numRows):
            for c in range(numCols):
                dfs(r, c, prefixTree, "")
        
        return list(results)