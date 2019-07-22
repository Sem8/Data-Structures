class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements? - Array
    self.storage = []

  def enqueue(self, item):    
    self.storage.append(item)
    # pass
  
  def dequeue(self):
    if not self.storage:
      return None
    else:
      return self.storage.pop(0)
    # pass

  def len(self):
    return len(self.storage)
    # pass

  # def len(self):
  #   count = 0
  #   current = self.storage

  #   if not self.storage:
  #     return 0
  #   else:
  #     while current:
  #       count += 0

  #   return count
  #   # pass
