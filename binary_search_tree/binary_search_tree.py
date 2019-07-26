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
      # return self.right.get_max()      
      max_value = self.right.get_max()

    return max_value
    
# I did a pre-order traversal I believe
# post order traversal would just invoke cb(self.value) all the way at the bottom
# inorder traversal would invoke cb(self.value) between left and right if statements
  def for_each(self, cb):    
    if self.value != None:
      cb(self.value)
      if self.left:
        self.left.for_each(cb)
      if self.right:
        self.right.for_each(cb)


    
    