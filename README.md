#### LRU get method algorithm:

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

#### LRU put method algorithm:

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
