"""
[Description]
LRU Cache
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

  LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
  int get(int key) Return the value of the key if the key exists, otherwise return -1.
  void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

 
Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

 
Constraints:

  1 <= capacity <= 3000
  0 <= key <= 104
  0 <= value <= 105
  At most 2 * 105 calls will be made to get and put.

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, Linked List, Design, Doubly-Linked List
- Slug: lru-cache
"""

// [Solution]
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.d = {}              # key -> Node
        self.capacity = capacity

        self.head = Node()       # dummy head
        self.tail = Node()       # dummy tail

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def add_to_tail(self, node):
        # insert node before dummy tail
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def move_to_recent(self, node):
        self.remove_node(node)
        self.add_to_tail(node)

    def delete_from_head(self):
        # least recently used node is after dummy head
        lru = self.head.next
        self.remove_node(lru)
        del self.d[lru.key]

    def get(self, key):
        if key not in self.d:
            return -1

        node = self.d[key]
        self.move_to_recent(node)
        return node.val

    def put(self, key, value):
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.move_to_recent(node)
        else:
            node = Node(key, value)
            self.d[key] = node
            self.add_to_tail(node)

            if len(self.d) > self.capacity:
                self.delete_from_head()