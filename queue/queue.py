class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements? - Array
    self.storage = []    

  # Methods WITHOUT Python built in methods
  # def enqueue(self, item):
  #   if self.storage is None:
  #     self.storage = [item]
    
  #   pass
  
  # def dequeue(self):
    
  #   pass

  # def len(self):
  #   current = self.storage

  #   if current is None:
  #     self.size = 0
  #     # return self.size
  #   else:
  #     while current:
  #       self.size += 1 
  #       break 
  #   return self.size -1
    # pass

  # Methods with Python built in methods
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
