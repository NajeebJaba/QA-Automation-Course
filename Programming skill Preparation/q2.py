# Question 2

##################  Linked Lists: ##################

#2.Linked Lists:

#a. Write a program to reverse a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def disp(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

# Testing the function to verify if it's running well
#linked_list = LinkedList()
#elements = [1, 2, 3, 4, 5]
#for element in elements:
#    linked_list.append(element)

#print("Original_Linked_List:")
#linked_list.disp()

#linked_list.reverse()

#print("\nReverse_Linked_List:")
#linked_list.disp()

##############################################################
##############################################################

#b.Write a program to find the middle element of a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def find_middle(self):
        if not self.head:
            return None

        slow_ptr = fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr.data

# Testing the function to verify if it's running well
#linked_list = LinkedList()
#elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for element in elements:
#    linked_list.append(element)

#print("Original_Linked_List:")
#linked_list.display()

#middle_element = linked_list.find_middle()

#print(f"\nThe middle element is: {middle_element}")

##############################################################
##############################################################

#c.Write a program to detect if a linked list has a cycle.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def create_cycle(self, position):
        if position < 0 or not self.head:
            return

        current_node = self.head
        cycle_start = None

        for i in range(position):
            if not current_node.next:
                return
            current_node = current_node.next
            if i == position - 1:
                cycle_start = current_node

        while current_node.next:
            current_node = current_node.next

        current_node.next = cycle_start

    def has_cycle(self):
        if not self.head:
            return False

        slow_ptr = fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True

        return False

# Testing the function to verify if it's running well
#linked_list = LinkedList()
#elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for element in elements:
#    linked_list.append(element)

#has_cycle = linked_list.has_cycle()

#print("linked list has a cycle:" if has_cycle else "Linked List has'nt Cycle")



