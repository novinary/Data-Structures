'''
In a max heap, each child node is less than or equal to parent node
'''

class Heap:
  def __init__(self):
    self.storage = []

# insert adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)
    print(self.storage)

# delete removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has bee
  def delete(self):
    deleted_value = self.storage[0]
    self.storage[0] = self.storage[len(self.storage)-1]
    self.storage.pop(len(self.storage)-1)
    if len(self.storage) > 0:
      self._sift_down(0)
    return deleted_value

# get_max returns the maximum value in the heap in constant time.
  def get_max(self):
    return self.storage[0]

# get_size returns the number of elements stored in the heap.
  def get_size(self):
    return len(self.storage)

# _bubble_up moves the element at the specified index "up" the heap by swapping it with its parent
# if the parent's value is less than the value at the specified index.
  def _bubble_up(self, index):
     # in worst case elem will need to make way to top of heap
    while index > 0:
      # get parent elem of this index
      parent = (index - 1) // 2
      # check if elem at index is higher priority than parent elem
      if self.storage[index] > self.storage[parent]:
        # if it is then swap them
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

        # update index to be new spot that swapped elem now resides at
        index = parent
      else:
        # otherwise, our elem is at a valid spot in the heap
        # we no longer need to bubble up
        break

# _sift_down grabs the indices of this element's children and determines which child has a larger value.
# If the larger child's value is larger than the parent's value, the child element is swapped with the parent.
  def _sift_down(self, index):
       while index * 2 + 1 <= len(self.storage) - 1:
            if index * 2 + 2 > len(self.storage) - 1:
                biggest_child = index * 2 + 1
            else:
                biggest_child = index * 2 + \
                    1 if self.storage[index * 2 +
                                      1] > self.storage[index * 2 + 2] else index * 2 + 2
            if self.storage[index] < self.storage[biggest_child]:
                self.storage[index], self.storage[biggest_child] = self.storage[biggest_child], self.storage[index]
            index = biggest_child
