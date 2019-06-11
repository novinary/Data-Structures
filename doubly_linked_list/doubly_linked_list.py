'''
Regular linked list has a pointer to the root node or first node in the list.
Each node has a piece of data and a pointer to next node.

With doubly linked list, every node has 3 parts:
- pointer to its previous node
- pointer to next node
- and a piece of data
This enables to us navigate either forward or backward through the linked list.

Adavantages over regukar(singly) linked lists:
- Can iterate the list in either direction
- Can delete a node without iterating through the entire list(if given a pointer to the node)
  Whereas with single linked list, you'd have to iterate through all the list.
  However, this means doubly use up more memory and bit more coding invole as
  each time you insert or delete a node, you also have to update prev/ next node.
'''

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  # replaces the head of thae list with a new value that is passed in.
  '''
  If there is atleast one node in the linked list already,
  Then as we add a new item to the top/front of the list
  We have to add a pointer to that node pointing to the previous ones
  '''

  def add_to_head(self, value):
  # If there's a head node then we know there's one node at least in the list so we assign the head node previous node to new node
    new_node = ListNode(value)
    if self.head:                  
      self.head.insert_before(value)
      self.head = self.head.prev
    else:
       self.head = new_node
       self.tail = new_node
    self.length += 1  #increment by 1

  # replaces the tail of the list with a new value that is passed in.
  def remove_from_head(self):
    #Delete last item by setting tail to be None if there is only one item in the list
    if self.head is None:
      return None
    old_head = self.head
    self.head.delete()
    self.head = old_head.next
        
    if self.length == 1:
      self.tail = None
    self.length -= 1
    return old_head.value

  # removes the head node and returns the value stored in it.
  def add_to_tail(self, value):
    new_node = ListNode(value)
    if self.tail:                  
      self.tail.insert_after(value)
      self.tail = self.tail.next
    else:
       self.head = new_node
       self.tail = new_node
    self.length += 1

  # removes the tail node and returns the value stored in it.
  def remove_from_tail(self):
    removed = self.tail.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.tail = self.head.prev
      self.tail.next.delete()
      self.length -= 1
    return removed

  def move_to_front(self, node):
    self.add_to_head(node.value)
    self.length -= 1 #decrement by 1

  # takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up.
  def move_to_end(self, node):
    self.tail.insert_after(node.value)
    self.tail = self.tail.next
    if node is self.head:
      self.head = self.head.next
    node.delete()

  # takes a reference to a node in the list and removes it from the list. The deleted node's previous and next pointers should point to each afterwards.
  def delete(self, node):
    if node is self.head:
      self.head = self.head.next
    if node is self.tail:
      self.tail = self.tail.prev
    node.delete()
    self.length -= 1 

  # returns the maximum value in the list.
  def get_max(self):
    pass
  