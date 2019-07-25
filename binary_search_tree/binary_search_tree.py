class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

# contains method with cleaner code:
  # def contains(self, target):
  #   if target > self.value and self.right:
  #     return self.right.contains(target)    
  #   elif target < self.value and self.left:
  #     return self.left.contains(target)
  #   elif target == self.value:
  #     return True
  #   else:
  #     return False

# contains method that makes more sense to me:
  def contains(self, target):
    if target > self.value and self.right:
      is_found = self.right.contains(target)
      if is_found:
        return True
      return False
    elif target < self.value and self.left:
      is_found = self.left.contains(target)
      if is_found:
        return True
      return False
    if target == self.value:
      return True
    else:
      return None

  def get_max(self):
    max_value = self.value

    if self.right:      
      max_value = self.right.get_max()
          
    return max_value


  # def get_max(self):
  #   max_value = self.value
  #   if not self.right:
  #     if self.left:
  #       self.left.get_max()
  #       max_value = self.left.value
  #   elif self.right:
  #     self.right.get_max()
  #     max_value = self.right.value
  #   return max_value
    

  def for_each(self, cb):
    pass