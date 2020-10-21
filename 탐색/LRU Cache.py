"""
146. LRU Cache in LeetCode
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.
"""

"""
Follow up:
Could you do both operations in O(1) time complexity?
"""

"""
Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capa = capacity
        self.nodeList = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        idx, value  = self.search(key)
        if (idx != None):
            del self.nodeList[idx]
            self.nodeList.insert(0, [key, value])
          
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """                        
        idx, _ = self.search(key)
        
        if(idx != None):            
            del self.nodeList[idx]            
        else:
            if(len(self.nodeList) == self.capa):
                self.nodeList.pop()
                    
        self.nodeList.insert(0, [key, value])

        return None

    def search(self, key):
        """
        :type key: int
        :rtype: int, int
        """
        idx = None
        value = -1
        for i in range(len(self.nodeList)):
            if (self.nodeList[i][0] == key):
                value = self.nodeList[i][1]
                idx = i         

        return [idx, value]

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Input
["LRUCache","put","put","put","put","get","get"]
[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
Output
[null,null,null,null,null,1,-1]
Expected
[null,null,null,null,null,-1,3]
"""


def main():
    capacity = 2
    cache = LRUCache(capacity)
        
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)

    print(cache.get(1))
    print(cache.get(2))        

if __name__ == "__main__":
    main()

"""
I sovled this problem with Linked List.
When we use any element, this element move to first place in LinkedList.
So, when we remove any element, we just remove final place element.
Because final place element is the last used element.
"""