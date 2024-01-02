# 1. Understand how LLs are created#
# 2. CRUD operations
# 3. Loops in LLs
# 4. Sort the LLs (merge sort)
# 5. Intersection in LLs
# 6. Some Intersecting Problems

# Recall: Every class: Data + Functions

class Node:
    # Data 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.haed = None

    # Functions
    def append(self, data):
        new_node = Node(data)
        # If my head is empty
        if self.head is None:
            self.head = new_node
            return
        # If head is not empty
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print(self):
        print(self, )
        while a:
            

for i in range(1, 100):
    print()