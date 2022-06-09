class LinkList:
    def __init__(self, head = None):
      # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
      self.length = 0
      self.head = head
    
  
    def add(self, data):
      # write your code to ADD an element to the Linked List
      if self.head == None:
        self.head = Node(data)
        self.length += 1
        return
      
      # Allows us to move through the list
      current = self.head
    
      # If the next node is "None", we add the new node to the end
      while current.next != None:
        current = current.next
      self.length += 1
      current.next = Node(data)

      
    

    def remove(self, data):
      # write your code to REMOVE an element from the Linked List
      if head == None:
        return
      
      # This makes the head the next node, if you remove the first node
      if head.data == data:
        head = head.next
        length -= 1

      # Allows you to move through the list
      current = self.head

      # If the node next to the current node has the requested data to be removed, we set the next node to the one after it
      while current.next != None:
        if current.next.data == data:
          current.next = current.next.next
          length -= 1
          return
        current = current.next

    def get(self, element_to_get):
      # write you code to GET and return an element from the Linked List
      if self.head == None:
        return "No data available"
      if self.head.data == element_to_get:
        return element_to_get

      # Allows us to move through the list
      current = self.head

      # If the node contains the data requested, we return the data
      while current.next != None:
        if current.next.data == element_to_get:
          return element_to_get
        else:
          current = current.next
      

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  
    def __init__(self, data, next = None):
      
      self.data = data
      self.next = next

# Testing Add method
ls = LinkList()
print(ls.length)
ls.add(2)
ls.add(5)
ls.add(6)
ls.add(10)
print(ls.get(5))
