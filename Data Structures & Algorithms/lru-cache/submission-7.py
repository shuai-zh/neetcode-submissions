class ListNode:
    def __init__(self, val=0, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.cache = {}
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.pre = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            cur = self.head
            while cur.val != key:
                cur = cur.next
            
            pre_temp = cur.pre
            next_temp = cur.next
            pre_temp.next = next_temp
            next_temp.pre = pre_temp

            cur.next = self.head.next
            self.head.next.pre = cur
            self.head.next = cur
            cur.pre = self.head

            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cur = self.head
            while cur.val != key:
                cur = cur.next
            
            pre_temp = cur.pre
            next_temp = cur.next
            pre_temp.next = next_temp
            next_temp.pre = pre_temp

            cur.next = self.head.next
            self.head.next.pre = cur
            self.head.next = cur
            cur.pre = self.head
        else:
            
            if len(self.cache) >= self.capacity:
                
                remove_node = self.tail.pre
                
                remove_node.pre.next = self.tail
                
                self.tail.pre = remove_node.pre
                
                del self.cache[remove_node.val]
                
            new_node = ListNode(key, self.head.next, self.head)
            self.head.next.pre = new_node
            self.head.next = new_node

        self.cache[key] = value


        
