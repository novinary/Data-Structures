'''
- A queue is nothing more than a list which is limited 
to only allow data to be inserted from one end, and 
retrieved from the other. 

- Known as FIFO data structure - First In - First Out!
- Data is pushed in at the Back end which is called enqueue
- Data is popped out at the Front end which is called dequeue
- There is no ability to insert or retrieve from any other location
  in the list 
'''

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    return self.storage.append(item)  # Push/append an item to the end of queue
  
  def dequeue(self):
    if len(self.storage):
      return self.storage.pop(0)     # Pop an item to the other end of the queue(first item in the list)

  def len(self):
    return len(self.storage)
