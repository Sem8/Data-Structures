class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)
    

  def delete(self):
    if len(self.storage) >= 2:
      self.storage[0], self.storage[(len(self.storage) - 1)] = self.storage[(len(self.storage) - 1)], self.storage[0]
      max = self.storage.pop()
      self._sift_down(0)
    # elif len(self.storage) == 2:
    #   max = self.storage.pop()
    elif len(self.storage) == 1:
      max = self.storage.pop()
    else:
      max = False
    return max
    

  def get_max(self):
    if self.storage[0]:
      return self.storage[0]
    else:
      return False
    

  def get_size(self):
    return len(self.storage)
    pass    
    

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2

      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

        index = parent
      else:
        break
    

  def _sift_down(self, index):
    left_child_i = index * 2 + 1
    right_child_i = index * 2 + 2
    largest = index

    if len(self.storage) > left_child_i and self.storage[largest] < self.storage[left_child_i]:
      largest = left_child_i

    if len(self.storage) > right_child_i and self.storage[largest] < self.storage[right_child_i]:
      largest = right_child_i
    if largest != index:
      self.storage[index], self.storage[largest] = self.storage[largest], self.storage[index]
      self._sift_down(largest)
    
