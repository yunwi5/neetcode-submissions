class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Key: key, value: node object
        self.nodeDict = {}
        self.itemCount = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.nodeDict:
            return -1
        
        node = self.nodeDict[key]
        prev = node.prev
        nextNode = node.next
        if prev and nextNode:
            # prev <-> node <-> next
            # prev <-> next
            # remove node and connect prev and next
            prev.next = nextNode
            nextNode.prev = prev
            node.prev = None
            node.next = None

        # node <-> tail
        currentTailPrev = self.tail.prev
        if currentTailPrev:
            currentTailPrev.next = node
            node.prev = currentTailPrev
        self.tail.prev = node
        node.next = self.tail

        return node.value
    

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.nodeDict:
            oldNode = self.nodeDict[key]
            prev = oldNode.prev
            nextNode = oldNode.next
            if prev and nextNode:
                # prev <-> node <-> next
                # prev <-> next
                # remove node and connect prev and next
                prev.next = nextNode
                nextNode.prev = prev
                node.prev = None
                node.next = None
            self.itemCount -= 1


        if self.itemCount >= self.capacity:
            nextHead = self.head.next
            if nextHead:
                nextHead.prev = None
                if nextHead.key in self.nodeDict:
                    del self.nodeDict[nextHead.key]
                if nextHead.next:
                    self.head.next = nextHead.next
                    nextHead.next.prev = self.head
                else:
                    self.head.next = None
                self.itemCount -= 1
    
    
        self.nodeDict[key] = node
        self.itemCount += 1
        currentTailPrev = self.tail.prev
        if currentTailPrev:
            currentTailPrev.next = node
            node.prev = currentTailPrev

        node.next = self.tail
        self.tail.prev = node
        

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
