# Question 4

##################  Trees and Graphs: ##################

#a. Write a program to find the lowest common ancestor of two nodes in a binary tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_lowest_common_ancestor(root, node1, node2):
    if not root:
        return None

    # If either node1 or node2 is the root, the root is the LCA
    if root.value == node1 or root.value == node2:
        return root

    # Recursively search in the left and right subtrees
    left_lca = find_lowest_common_ancestor(root.left, node1, node2)
    right_lca = find_lowest_common_ancestor(root.right, node1, node2)

    # If both nodes are found in different subtrees, the current root is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise, return the non-None result from the left or right subtree
    return left_lca if left_lca else right_lca


# Constructing the binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Testing the function to verify if it's running well
# node1 = 5
# node2 = 1
# lca = find_lowest_common_ancestor(root, node1, node2)
#
# print(f"The lowest common ancestor of nodes {node1} and {node2} is {lca.value}")


##############################################################
##############################################################

#b. Write a program to find the shortest path between two nodes in a graph.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return None  # Nodes are not present in the graph

        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current, path = queue.popleft()

            if current == end:
                return path  # Return the shortest path

            if current not in visited:
                visited.add(current)
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None  # No path found between the nodes



# Constructing the graph
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(3, 4)

# Testing the function to verify if it's running well
# start_node = 0
# end_node = 2
#
# shortest_path_result = graph.shortest_path(start_node, end_node)
#
# if shortest_path_result:
#     print(f"The shortest path between nodes {start_node} and {end_node} is: {shortest_path_result}")
# else:
#     print(f"No path found between nodes {start_node} and {end_node}")


##############################################################
##############################################################


#c. Implement a binary search tree and write functions to insert, delete and search for elements.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children: Get the inorder successor (smallest
            # in the right subtree) or the inorder predecessor (largest
            # in the left subtree)
            root.key = self._min_value_node(root.right).key
            root.right = self._delete(root.right, root.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)

# Testing the function to verify if it's running well
# bst = BinarySearchTree()
# elements = [50, 30, 20, 40, 70, 60, 80]
#
# for element in elements:
#     bst.insert(element)
#
# print("Inorder Traversal:", bst.inorder_traversal())
#
# search_key = 60
# search_result = bst.search(search_key)
# print(f"Search for key {search_key}: {'Found' if search_result else 'Not Found'}")
#
# delete_key = 30
# bst.delete(delete_key)
# print(f"Deleted key {delete_key}. Inorder Traversal:", bst.inorder_traversal())
