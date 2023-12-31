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

#Linear Search Function
def count_rotations_linear(nums):
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
          return position
        
        position +=1
    return 0
    
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
        elif function in [bucket_sort, quick_sort, merge_sort, count_rotations_binary, count_rotations_linear, bubble_sort, insertion_sort, counting_sort, selection_sort, heap_sort]:
            result = function(test['input']['nums'])
        print('Function:', function)
        print('Input:', test['input'])
        print('Expected Output:', test['output'])
        print('Actual Output:', result)
        print('Test Passed:', (result == test['output']))
        t.stop()
        print('')

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

tests2 = [
    {'input': {'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, 'output': 3}, 
    {'input': {'nums': [0]}, 'output': 0},
    {'input': {'nums': [5, 6, 7, 1, 3]}, 'output': 3},
    {'input': {'nums': [7, 1, 3, 5, 6]}, 'output': 1}
]

# evaluate_test_cases(locate_card_linear, tests)
# evaluate_test_cases(locate_card_binary, tests)
# evaluate_test_cases(count_rotations_linear, tests2)
# evaluate_test_cases(count_rotations_binary, tests2)

#Python Classes 
# Insert, Find, Update, and List (Brute Force/Linear)
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

# Binary Search Tree + Useful Methods
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
        return self

    def find(self, key):
        if self is None:
            return None
        if key == self.key:
            return self
        if key < self.key:
            return TreeNode.find(self.left, key)
        if key > self.key:
            return TreeNode.find(self.right, key)
        
    def update(self, key, value):
        target = TreeNode.find(self, key)
        if target is not None:
            target.value = value

    def list_all(self):
        if self is None:
            return []
        return TreeNode.list_all(self.left) + [(self.key, self.value)] + TreeNode.list_all(self.right)
    
    def is_balanced(self):
        if self is None:
            return True, 0
        balanced_l, height_l = TreeNode.is_balanced(self.left)
        balanced_r, height_r = TreeNode.is_balanced(self.left)
        balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
        height = 1 + max(height_l, height_r)
        return balanced, height

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
    
    def is_bst(self):
        def remove_none(nums):
          return [x for x in nums if x is not None]
        if self is None:
            return True, None, None
        is_bst_l, min_l, max_l = TreeNode.is_bst(self.left)
        is_bst_r, min_r, max_r = TreeNode.is_bst(self.right)
        is_bst_self = (is_bst_l and is_bst_r and 
                      (max_l is None or self.key > max_l) and 
                      (min_r is None or self.key < min_r))
        min_key = min(remove_none([min_l, self.key, min_r]))
        max_key = max(remove_none([max_l, self.key, max_r]))
        return is_bst_self, min_key, max_key
    
    def make_balanced_bst(data, lo=0, hi=None, parent=None):
        if hi is None:
            hi = len(data) - 1
        if lo > hi:
            return None
        
        mid = (lo + hi) // 2
        key, value = data[mid]

        root = TreeNode(key, value)
        root.parent = parent
        root.left = TreeNode.make_balanced_bst(data, lo, mid-1, root)
        root.right = TreeNode.make_balanced_bst(data, mid+1, hi, root)

        return root
    def balance_bst(self):
        return TreeNode.make_balanced_bst(TreeNode.list_all(self))

#Test Cases
# Amber = User('Amber', 'Amber Graham', 'amber@graham.com')
# Billy = User('Billy', 'Billy Bob', 'billy@bob.com')
# Herman = User('Herman', 'Herman Anderson', 'herman@anderson.com')
# Jeremy = User('Jeremy', 'Jeremy Cox', 'jeremy@cox.com')
# Sally = User('Sally', 'Sally Sue', 'sally@sue.com')
# Simone = User('Simone', 'Simone Hicks', 'simone@hicks.com')
# Veronica = User('Veronica', 'Veronica Sanchez', 'veronica@sanchez.com')

# users = [Amber, Billy, Herman, Jeremy, Sally, Simone, Veronica]
# data = [(user.username, user) for user in users]

# tree = TreeNode.make_balanced_bst(data)
# tree2 = None
# for username, user in data:
#     tree2 = TreeNode.insert(tree2, username, user)
# tree2 = TreeNode.balance_bst(tree2)

#Hash Tables
MAX_HASH_TABLE_SIZE = 4096

class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size
    def insert(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = (key, value)
        return '({}, {}) was inserted.'.format(key, value)
    def find(self, key):
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return key, value
    def update(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = (key, value)
        return self.data_list[idx]
    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]

def get_index(data_list, a_string):
        result = 0
        for a_character in a_string:
            a_number = ord(a_character)
            result += a_number
        list_index = result % len(data_list)
        return list_index

def get_valid_index(data_list, key):
    idx = get_index(data_list, key)
    while True:
        kv = data_list[idx]
        if kv is None:
            return idx
        k, v = kv
        if kv[0] == key:
            return idx
        idx +=1
        if idx == len(data_list):
            idx = 0


table = HashTable()
table.insert('Jeremy', '3811675')

#Sorting
def bubble_sort(nums):
    nums = list(nums)
    for _ in range(len(nums)-1):
        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -=1
        nums.insert(j+1, cur)
    return nums

def merge(nums1, nums2):
    merged = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j +=1
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    return merged + nums1_tail + nums2_tail

def merge_sort(nums):
    if len(nums) <=1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    sorted_nums = merge(left_sorted, right_sorted)
    return sorted_nums

def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    l, r = start, end - 1
    while r > l:
        if nums[l] <= nums[end]:
            l += 1
        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else: 
        return end
    
def quick_sort(nums, start=0, end=None):
    if end is None:
        nums=list(nums)
        end = len(nums) - 1
    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)
    return nums

def counting_sort(nums):
    nums = list(nums)
    if len(nums) == 0:
        return []
    # Find the maximum and minimum values in the list
    max_value = max(nums)
    min_value = min(nums)

    # Create a counting array to store the frequency of each element
    count_array_size = max_value - min_value + 1
    count = [0] * count_array_size

    # Count the frequency of each element
    for num in nums:
        count[num - min_value] += 1

    # Reconstruct the sorted list
    sorted_nums = []
    for i in range(len(count)):
        sorted_nums.extend([i + min_value] * count[i])

    return sorted_nums

def bucket_sort(nums):
    nums = list(nums)
    if len(nums) == 0:
        return []
    # Find the maximum and minimum values in the list
    max_value = max(nums)
    min_value = min(nums)

    # Determine the range of integers
    range_of_integers = max_value - min_value + 1

    # Create empty buckets
    buckets = [[] for _ in range(range_of_integers)]

    # Place elements into buckets
    for num in nums:
        buckets[num - min_value].append(num)

    # Sort each bucket individually (using any sorting algorithm)
    sorted_nums = []
    for bucket in buckets:
        # Sort each bucket using any sorting algorithm (e.g., Python's built-in sorted)
        sorted_bucket = sorted(bucket)
        sorted_nums.extend(sorted_bucket)

    return sorted_nums

def selection_sort(nums):
    nums = list(nums)
    # Traverse through all array elements starting from 0
    for i in range(len(nums)):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

def heapify(nums, n, i):
    largest = i  # Initialize the largest element as the root
    left_child = 2 * i + 1  # Left child
    right_child = 2 * i + 2  # Right child

    # Compare the left child with the root
    if left_child < n and nums[left_child] > nums[largest]:
        largest = left_child

    # Compare the right child with the largest so far
    if right_child < n and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is not the root, swap them
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(nums, n, largest)

def heap_sort(nums):
    nums = list(nums)
    n = len(nums)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]  # Swap the root (max element) with the last element
        heapify(nums, i, 0)  # Call heapify on the reduced heap
    return nums

#Test Cases
#List of numbers in random order
test0 = {
    'input': {
        'nums': [4,2,6,3,4,6,2,1]
    },
    'output': [1,2,2,3,4,4,6,6]
}
#List of numbers in random order
test1 = {
    'input': {
        'nums': [5,2,6,1,23,7,-12,12,-243,0]
    },
    'output': [-243,-12,0,1,2,5,6,7,12,23]
}
#List of numbers already sorted
test2 = {
    'input': {
        'nums': [3,5,6,8,9,10,99]
    },
    'output': [3,5,6,8,9,10,99]
}
#List of numbers in descending order
test3 = {
    'input': {
        'nums': [99,10,9,8,6,5,3]
    },
    'output': [3,5,6,8,9,10,99]
}
#List containing repeating elements
test4 = {
    'input': {
        'nums': [5,-12,2,6,1,23,7,7,-12,6,12,1,-243,1,0]
    },
    'output': [-243,-12,-12,0,1,1,1,2,5,6,6,7,7,12,23]
}
#An Empty List
test5 = {
    'input': {
        'nums': []
    },
    'output': []
}
#A list Containing just one element
test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}
#A list containing one elemenet repeated many times
test7 = {
    'input': {
        'nums': [42,42,42,42,42,42,42,42]
    },
    'output': [42,42,42,42,42,42,42,42]
}
#A really long list
import random
in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)
test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}
tests3 = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

# evaluate_test_cases(bubble_sort, tests3)
# evaluate_test_cases(insertion_sort, tests3)
# evaluate_test_cases(merge_sort, tests3)
# evaluate_test_cases(quick_sort, tests3)
# evaluate_test_cases(counting_sort, tests3)
# evaluate_test_cases(bucket_sort, tests3)
# evaluate_test_cases(selection_sort, tests3)
# evaluate_test_cases(heap_sort, tests3)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
# n = 5
# print(f"The factorial of {n} (iterative) is {factorial_iterative(n)}")

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
# n = 5
# print(f"The factorial of {n} (recursive) is {factorial_recursive(n)}")

def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
        print(b)
    return a

# Example usage:
# num1 = 48
# num2 = 18
# print(f"The GCD of {num1} and {num2} (iterative) is {gcd_iterative(num1, num2)}")

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

# Example usage:
# num1 = 48
# num2 = 18
# print(f"The GCD of {num1} and {num2} (recursive) is {gcd_recursive(num1, num2)}")

def fibonacci_recursive(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return a

# Example usage:
n = 8
result = fibonacci_recursive(n)
print(f"The {n}-th Fibonacci number is {result}")