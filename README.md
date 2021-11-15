### LRU get method algorithm:

1. Search the key into a hash map.
2. If not found in hash map then return None
3. If key is found into the hash map then get the node from dubly link list.
4. Delete the node from dubly link list.
5. Insert the node after the head into dubly link list.
6. Return the node value


Source code:
```
def get(key):
    if not hash_map.find(key):
        return "Not found"
    
    current_node = cache[key]
    DublyLinkList.delete_node(current_node)
    DublyLinkList.insert_after_head(current_node)
    
    return current_node.value
```

### LRU put method algorithm:

1. Search the key into hash map.
2. If found,
    1. Get the node from dubly link list.
    2. Update the value of that node.
    3. Delete the node from dubly link list.
    4. Insert the node into dubly link list after head.

3. If not found,
     1. Create a new node.
     2. Assing that node to the hash map key.
     3. Insert that node after dubly link list's head.

4. Check the capacity of hash map.
5. If exceed,
    1. Get the last node from dubly link list.
    2. Delete the last node from hash map.


Source code:
```
def put(key, value):
    if hash_map.find(key):
        curr_node = hash_map[key]
        curr_node.value = value
        DublyLinkList.delete_node(curr_node)
        DublyLinkList.insert_after_head(curr_node)
        
    new_node = DublyLinkList(key, value)
    hash_map[key] = new_node
    DublyLinkList.insert_after_head(new_node)
        
    if hash_map.size() > capacity:
        last_node = DublyLinkList.get_last_node()
        hash_map.remove(last_node.key)
```

### Dubly Linked List Insertion
A node can be inserted into a dubly linked list in four ways.
1. Insert before head.
2. Insert after a given node.
3. Insert at the end of dubly linked list.
4. Insert before a given node.

#### Insert a node before head algorithm:
1. Make a new node.
2. Assign head node to its next node.
3. Assing None to its previous node. (Because head node hasn't any previous node)
4. Assing new node as previous node to head.
5. Finally make new node as head.

Source code:
```
class Node(object):
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data
           
    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = Node
        
        if self.head is not Node:
            self.head.prev = new_node
            
        self.head = new_node
```

#### Insert a node after a given node algorithm:
1. Make a new node.
2. Assign previous node's next node to new node's next node.
3. Assign previous node as the new node's previous node.
4. Assign previous node's next node to new node.
5. Assing new nodes's next node's privous node to new node.

This scenario is slightly tricky, if previous node is A, new node is B and next node is C then,
1. B.next = A.next  (B -> C)
2. B.prev = A       (A <- B)
3. A.next = B       (A -> B)
4. B.next.prev = B  (B <- C)

```
class Node(object):
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data
        
    def insert_after_given_node(self, previous_node, new_data):
        new_node = Node(data=new_data)
        
        new_node.next = previous_node.next
        new_node.prev = previous_node
        
        previous_node.next = new_node
        previous_node.next.prev = new_node
```

#### Insert a node at the end of dubly linked list algorithm:
1. Make a new node.
2. Assign next pointer to None because this node is the last node.
3. Traverse and find the last node.
4. Assing last node to new node's previous pointer.
5. Assign new node to last node's next pointer.
6. Make new node as last node.

Source code:
```
class Node(object):
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data
        
    def insert_before_last(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        
        # First i assume the head is the last node. Then i have to find the last node through traversal till the end.
        last = self.head
        while last.next is not None:
            last = last.next
        
        last.prev = new_node
        new_node.prev = last 
```

