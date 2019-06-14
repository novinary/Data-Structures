'''
Binary Search tree exhibits a special behavior. 
A node's left child must have a value less than its parent's value 
and the node's right child must have a value greater than its parent value.
'''

# insert adds the input value to the binary search tree, 
# adhering to the rules of the ordering of elements in a binary search tree.
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Check new node val < current nodes val
    if value < self.value:
      # if no left child place new node
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        #otherwise repeat process
        self.left.insert(value)
    # check new node val >= current nodes val
    if value >= self.value:
      # if no right child place new node
      if not self.right:
        self.right = BinarySearchTree(value)
      # otherwise repeat process
      else:
        self.right.insert(value)

# contains searches the binary search tree for the input value,
# returning a boolean indicating whether the value exists in the tree or not.
  def contains(self, target):
    # Check target val < current nodes val
    if target < self.value:
      # if no left child return false else return the target value from left child
      if self.left is None:
        return False
      return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return False
      return self.right.contains(target)
    else:
      return True


# get_max returns the maximum value in the binary search tree.
  def get_max(self):
    while self.right is not None:
      self = self.right
    return self.value


# for_each performs a traversal of every node in the tree,
# executing the passed-in callback function on each tree node value.
# There is a myriad of ways to perform tree traversal; in this case any of them should work.
  def for_each(self, cb):
    # run cb for each node
    cb(self.value)
    if self.right != None:
      self.right.for_each(cb)
    if self.left != None:
      self.left.for_each(cb)

#testing
bst = BinarySearchTree(66)
bst.insert(5)
print(bst.contains(66))
print(bst.get_max())

def cb(value):
  print(value)  
bst.for_each(cb)