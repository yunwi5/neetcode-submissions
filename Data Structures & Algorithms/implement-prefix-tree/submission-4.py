class PrefixTree:

    def __init__(self):
        self.nodeDict = {}

    def insert(self, word: str) -> None:
        # Time: O(n)
        # Space: O(t)
        if word[0] not in self.nodeDict:
            rootNode = Node(word[0])
            node = rootNode
            for char in word[1:]:
                nextNode = Node(char)
                node.addChild(nextNode)
                node = nextNode
            node.hasEnd = True
            self.nodeDict[word[0]] = rootNode
        else:
            currentNode = self.nodeDict[word[0]]
            wordIndex = 1
            while wordIndex < len(word):
                char = word[wordIndex]
                childNode = currentNode.getChildOfLetter(char)
                if not childNode:
                    newChild = Node(word[wordIndex])
                    currentNode.addChild(newChild)
                    currentNode = newChild
                else:
                    currentNode = childNode
                wordIndex += 1

            currentNode.hasEnd = True


    def search(self, word: str) -> bool:
        matchingNode = self.getFurthestMatchingNode(word)
        return matchingNode is not None and matchingNode.hasEnd        

    def startsWith(self, prefix: str) -> bool:
        matchingNode = self.getFurthestMatchingNode(prefix)
        return matchingNode is not None
    
    def getFurthestMatchingNode(self, prefix: str) -> Optional[Node]:
        if not prefix or prefix[0] not in self.nodeDict:
            return None

        node = self.nodeDict[prefix[0]]
        if len(prefix) == 1:
            return node

        for char in prefix[1:]:
            childNode = node.getChildOfLetter(char)
            if not childNode:
                return None
            node = childNode

        return node

class Node:
    def __init__(self, letter: str):
        self.letter = letter
        self.children = {} # key:letter, value: node
        self.hasEnd = False
    
    def addChild(self, childNode: Node):
        self.children[childNode.letter] = childNode

    def getChildOfLetter(self, letter: str):
        return self.children[letter] if letter in self.children else None

    def hasChildOfLetter(self, letter: str):
        return letter in self.children
    
    def __str__(self):
        return f'Node(Letter: {self.letter}, hasEnd: {self.hasEnd})'
    
    def __repr__(self):
        return str(self)
