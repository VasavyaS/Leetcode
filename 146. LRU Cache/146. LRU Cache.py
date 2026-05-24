#
# Problem: 146. LRU Cache
# Difficulty: Medium
# Link: https://leetcode.com/problems/lru-cache/submissions/2012067389/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-all
# Language: python3
# Date: 2026-05-24


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prv

    def remove(self, node):
        prv , nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
