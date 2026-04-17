class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.node = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.node
        for c in word:
            pos = ord(c) - ord("a") 
            if curr.children[pos] == None:
                curr.children[pos] = TreeNode()
            curr = curr.children[pos]
        curr.endOfWord = True

        

    def search(self, word: str) -> bool:
        curr = self.node
        for c in word:
            pos = ord(c) - ord("a") 
            if curr.children[pos] == None :
                return False
            curr = curr.children[pos]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.node
        for c in prefix:
            pos = ord(c) - ord("a")  
            if curr.children[pos] == None:
                return False
            curr = curr.children[pos]
        return True
        
        