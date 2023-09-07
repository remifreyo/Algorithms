# A Timer for showing the amount of time a block of code takes to execute
import time
class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""
class Timer:
    def __init__(self):
        self._start_time = None
    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        self._start_time = time.perf_counter()
    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.6f} seconds")
t = Timer()

#Algorithms

#Test Cases
tests = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}
    ]

#Linear Search Function
def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

#Binary Search Functions
def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def locate_card_binary(cards, query):
    
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    
    return binary_search(0, len(cards) - 1, condition)

new_tests = [
    {'input': {'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, 'output': 3}, 
    {'input': {'nums': [0]}, 'output': 0},
    {'input': {'nums': [5, 6, 7, 1, 3]}, 'output': 3},
    {'input': {'nums': [7, 1, 3, 5, 6]}, 'output': 1}
]

#Linear Search Function
def count_rotations_linear(nums):
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
          return position
        
        position +=1
    return 0.
    
#Binary Search Function
def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
      if len(nums) - 1 == 0:
          return 0
      mid = (lo + hi) // 2
      if nums[mid] < nums[mid - 1]:
          return mid
      elif nums[mid] > nums[mid-1] and nums[mid] < nums[len(nums) - 1]:
          hi = mid - 1
      elif nums[mid] > nums[mid-1] and nums[mid] > nums[len(nums) - 1]:
          lo = mid + 1
    return 0

#Function for Evaluating Test Cases
def evaluate_test_cases(function, tests):
    for test in tests:
      t.start()
      if function == locate_card_linear or function == locate_card_binary:
          result = function(test['input']['cards'], test['input']['query'])
      elif function == count_rotations_linear or function == count_rotations_binary:
          result = function(test['input']['nums'])
      print('Function:', function)
      print('Input:', test['input'])
      print('Expected Output:', test['output'])
      print('Actual Output:', result)
      print('Test Passed:', (result == test['output']))
      t.stop()
      print('')

# evaluate_test_cases(locate_card_linear, tests)
# evaluate_test_cases(locate_card_binary, tests)
# evaluate_test_cases(count_rotations_linear, new_tests)
# evaluate_test_cases(count_rotations_binary, new_tests)

#Python Classes 
# Insert, Find, Update, and List (Brute Force|Sorted|Linear)
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User Created!')
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    def __str__(self):
        return self.__repr__()
    
class UserDatabase:
    def __init__(self):
        self.users = []
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
    def list_all(self):
        return self.users

#Test User and Username Classes and Methods
# John = User('John','John Doe', 'john@doe.com' )
# Jorge = User('Jorge','Jorge Doe', 'jorge@doe.com' )
# Jane = User('Jane','Jane Doe', 'jane@doe.com' )
# database = UserDatabase()
# database.insert(John)
# database.insert(Jane)
# database.insert(Jorge)
# user = database.find('Jorge')
# print(user)
# database.update(User('Jorge', name='Jorge Smith', email='jorge@doe.com' ))
# print(user)
# print(database.list_all())
# Allie = User('Allie', 'Allie Gordon', 'allie@gordon.com')
# database.insert(Allie)
# print(database.list_all())

# Insert, Find, Update, and List (Binary Search Tree)

class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, key, value):
        if self is None:
            self = TreeNode(key, value)
        elif key < self.key:
            self.left = TreeNode.insert(self.left, key, value)
            self.left.parent = self
        elif key > self.key:
            self.right = TreeNode.insert(self.right, key, value)
            self.right.parent = self

    def height(self):
      if self is None: 
        return 0
      return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
      if self is None:
        return 0
      return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)
   
    def traverse_in_order(self):
      if self is None:
        return []
      return(TreeNode.traverse_in_order(self.left) + 
           [self.key] + 
           TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space ='\t', level=0):
      if self is None:
        print(space*level + 'ø')
        return
      if self.left is None and self.right is None:
        print(space*level + str(self.key))
        return
      TreeNode.display_keys(self.right, space, level+1)
      print(space*level + str(self.key))
      TreeNode.display_keys(self.left, space, level+1)
   
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
   
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
   
    @staticmethod
    #Turn a tuple into a BST
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
          node = TreeNode(data[1])
          node.left = TreeNode.parse_tuple(data[0])
          node.right = TreeNode.parse_tuple(data[2])
        else: 
            node = TreeNode(data)
        return node
    
def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    is_bst_node = (is_bst_l and is_bst_r and 
                   (max_l is None or node.key > max_l) and 
                   (min_r is None or node.key < min_r))
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    return is_bst_node, min_key, max_key

Amber = User('Amber', 'Amber Graham', 'amber@graham.com')
Billy = User('Billy', 'Billy Bob', 'billy@bob.com')
Herman = User('Herman', 'Herman Anderson', 'herman@anderson.com')
Jeremy = User('Jeremy', 'Jeremy Cox', 'jeremy@cox.com')
Sally = User('Sally', 'Sally Sue', 'sally@sue.com')
Simone = User('Simone', 'Simone Hicks', 'simone@hicks.com')
Veronica = User('Veronica', 'Veronica Sanchez', 'veronica@sanchez.com')

tree = TreeNode(Jeremy.username, Jeremy)
tree.left = TreeNode(Billy.username, Billy)
tree.left.parent = tree
tree.right = TreeNode(Simone.username, Simone)
tree.right.parent = tree
print(())
