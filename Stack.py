# Example 1: Using the class
my_stack = Stack()
my_stack.push(100)
my_stack.push(200)
my_stack.push(100)
my_stack.push(300)
print(my_stack)         # Stack: [100, 200, 100, 300]
print(my_stack.pop())   # 300
print(my_stack.peek())  # 100