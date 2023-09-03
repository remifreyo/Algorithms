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
      if function == locate_card_linear or function == locate_card_binary:
          result = function(test['input']['cards'], test['input']['query'])
      elif function == count_rotations_linear or function == count_rotations_binary:
          result = function(test['input']['nums'])
      print('Input:', test['input'])
      print('Expected Output:', test['output'])
      print('Actual Output:', result)
      print('Test Passed:', (result == test['output']))
      print('')

# evaluate_test_cases(locate_card_linear, tests)
# evaluate_test_cases(locate_card_binary, tests)
# evaluate_test_cases(count_rotations_linear, new_tests)
evaluate_test_cases(count_rotations_binary, new_tests)
