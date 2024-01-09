
class AllOne:
    
    # DoublyLinkedList Node
    # Encapsulates a set of all keys with the same count
    class AllOneNode:
        def __init__(self):
            self.prev = None
            self.next = None
            self.count = -1
            self.keys = set()

    # Initialize DoublyLinkedList Head/Tail and our HashMaps
    def __init__(self):
        self.head_ = self.AllOneNode()
        self.tail_ = self.AllOneNode()
        self.head_.next = self.tail_
        self.tail_.prev = self.head_
        self.count2Node_ = {}
        self.key2Count_ = {}

    # Utility function for inserting a new node inbetween predecessor and successor
    def insertNodeBetween(self, predecessor, successor, node):
        predecessor.next = node
        node.prev = predecessor
        successor.prev = node
        node.next = successor

    # Utility function for deleting a node when it has no more keys
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count2Node_[node.count]
        del node

    def inc(self, key: str) -> None:
        # - Key doesn't exist
        if key not in self.key2Count_:
            count = 1
            if count not in self.count2Node_:
                node = self.AllOneNode()
                node.count = 1
                self.insertNodeBetween(self.tail_.prev, self.tail_, node)
                self.count2Node_[count] = node
            self.key2Count_[key] = count
            self.count2Node_[count].keys.add(key)
        # - Key exists
        else:
            currentCount = self.key2Count_[key]
            updatedCount = currentCount+1

            self.key2Count_[key] = updatedCount

            # Get handle to currentCountNode
            currentCountNode = self.count2Node_[currentCount]

            # Insert key at updatedCountNode
            if updatedCount not in self.count2Node_:
                node = self.AllOneNode()
                node.count = updatedCount
                self.insertNodeBetween(currentCountNode.prev, currentCountNode, node)
                self.count2Node_[updatedCount] = node
            updatedCountNode = self.count2Node_[updatedCount]
            updatedCountNode.keys.add(key)

            # Remove key from currentCount
            currentCountNode = self.count2Node_[currentCount]
            currentCountNode.keys.remove(key)
            # Check if removal left the node empty
            if len(currentCountNode.keys) == 0:
                self.removeNode(currentCountNode)

    def dec(self, key: str) -> None:
        # - Key doesn't exist
        if key not in self.key2Count_:
            pass
        # - Key exists
        else:
            currentCount = self.key2Count_[key]
            updatedCount = currentCount-1

            # Get handle to currentCountNode
            currentCountNode = self.count2Node_[currentCount]

            if updatedCount != 0:
                self.key2Count_[key] = updatedCount
                # Insert key at updatedCountNode
                if updatedCount not in self.count2Node_:
                    node = self.AllOneNode()
                    node.count = updatedCount
                    self.insertNodeBetween(currentCountNode, currentCountNode.next, node)
                    self.count2Node_[updatedCount] = node
                updatedCountNode = self.count2Node_[updatedCount]
                updatedCountNode.keys.add(key)
            else:
                del self.key2Count_[key]

            # Remove key from currentCount
            currentCountNode = self.count2Node_[currentCount]
            currentCountNode.keys.remove(key)
            # Check if removal left the node empty
            if len(currentCountNode.keys) == 0:
                self.removeNode(currentCountNode)
        

    def getMaxKey(self) -> str:
        maxNode = self.getMaxNode()
        if maxNode is self.tail_:
            return ""
        for key in maxNode.keys:
            return key
        
    def getMinKey(self) -> str:
        minNode = self.getMinNode()
        if minNode is self.head_:
            return ""
        for key in minNode.keys:
            return key

    def getMaxNode(self):
        return self.head_.next

    def getMinNode(self):
        return self.tail_.prev

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()