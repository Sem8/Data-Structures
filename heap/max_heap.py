class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 2)
    

  def delete(self):
    pass

  def get_max(self):
    if self.storage[0]:
      return self.storage[0]
    else:
      return False
    

  def get_size(self):
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
    pass
