class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        # Time: O(n)
        # Space: O(t + n)
        # n = length of string, t = # nodes

        cur = self.root
        for c in word:
            if cur.hasChild(c):
                cur = cur.getChild(c)
            else:
                newChild = Node()
                cur.children[c] = newChild
                cur = newChild
        cur.word = True

    def search(self, word: str) -> bool:
        # Time: O(26 * 26 * n)
        # Space: O(t + n)

        cands = [self.root]
        for c in word:
            newCands = []
            for cand in cands:
                if c == '.':
                    newCands.extend(list(cand.children.values()))
                else:
                    child = cand.getChild(c)
                    if child is not None:
                        newCands.append(child)
            cands = newCands
        
        return any(cand.word for cand in cands)
        
class Node:

    def __init__(self):
        self.children = {}
        self.word = False
    
    def hasChild(self, c: str):
        return c in self.children

    def getChild(self, c: str):
        if c in self.children:
            return self.children[c]
    
    def __repr__(self):
        return f'Node(children={list(self.children.keys())})'
        