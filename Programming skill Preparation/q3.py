# Question 3

##################  Stacks and Queues: ##################

#a.Implement a stack using two queues.

from queue import Queue

class StackUsingQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        # Push the item to queue1
        self.queue1.put(item)

    def pop(self):
        # Move all items from queue1 to queue2 except the last one
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        # Pop the last item from queue1 (which is the top of the stack)
        if not self.queue1.empty():
            popped_item = self.queue1.get()

        # Swap the names of queue1 and queue2 for the next operation
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_item

    def is_empty(self):
        return self.queue1.empty() and self.queue2.empty()

# Testing the function to verify if it's running well
# stack = StackUsingQueues()
#
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# print("Pop:", stack.pop())  # Output: 3
# print("Pop:", stack.pop())  # Output: 2
#
# stack.push(4)
#
# print("Is Empty:", stack.is_empty())  # Output: False
# print("Pop:", stack.pop())  # Output: 4
# print("Is Empty:", stack.is_empty())  # Output: True



##############################################################
##############################################################

#b. Implement a queue using two stacks.

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        # Push the item onto stack1
        self.stack1.append(item)

    def dequeue(self):
        # If stack2 is empty, transfer all items from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop the item from stack2 (which is the front of the queue)
        if self.stack2:
            dequeued_item = self.stack2.pop()
            return dequeued_item
        else:
            # If both stacks are empty, the queue is empty
            return None

    def is_empty(self):
        return not self.stack1 and not self.stack2

# Testing the function to verify if it's running well
# queue = QueueUsingStacks()
#
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
#
# print("Dequeue:", queue.dequeue())  # Output: 1
# print("Dequeue:", queue.dequeue())  # Output: 2
#
# queue.enqueue(4)
#
# print("Is Empty:", queue.is_empty())  # Output: False
# print("Dequeue:", queue.dequeue())  # Output: 3
# print("Is Empty:", queue.is_empty())  # Output: False
# print("Dequeue:", queue.dequeue())  # Output: 4
# print("Is Empty:", queue.is_empty())  # Output: True

##############################################################
##############################################################

#c.Write a program to check if a given string of parentheses is balanced.

def is_balance_parenthes(s):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return False

    return not stack

# Testing the function to verify if it's running well
# test_string = "{[()]}"
#
# if is_balance_parenthes(test_string):
#     print(f"The string {test_string} is balance.")
# else:
#     print(f"The string {test_string} is not balance.")


