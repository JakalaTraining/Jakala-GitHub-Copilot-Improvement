class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)  # Nodo meno recente (LRU)
        self.right = Node(0, 0) # Nodo più recente (MRU)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Esempio di utilizzo della LRU Cache
if __name__ == "__main__":
    lruCache = LRUCache(2)

    lruCache.put(1, 10)
    lruCache.put(2, 20)
    
    print(lruCache.get(1))  # Stampa 10

    lruCache.put(3, 30)
    
    print(lruCache.get(2))  # Stampa -1
    print(lruCache.get(1))  # Stampa 10