"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, 'value': 123, 'left': {...}, 'right':{...}})
"""

from typing import Any


class BinarySearchTree:

    def __init__(self):
        self.root = None

    class TreeNode:
        def __init__(self, key: int, value: Any):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return f'{self.key}-{self.left}-{self.right}'

    def insert(self,  key: int, value: Any, root=None):
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :param root: default value is None
        :return: None
        """
        if root is None:
            root = self.root
        if self.root:
            if key == root.key:
                root.value = value
            if key > root.key:
                if root.right is None:
                    new_node = self.TreeNode(key, value)
                    root.right = new_node
                else:
                    self.insert(key, value, root.right)
            if key < root.key:
                if root.left is None:
                    new_node = self.TreeNode(key, value)
                    root.left = new_node
                else:
                    self.insert(key, value, root.left)
        else:
            self.root = self.TreeNode(key, value)

    def remove(self, key: int, root=None):
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :param root: default value is None
        :return: deleted (key, value) pair or None
        """
        if root is None:
            root = self.root
        while root:
            if key > root.key:
                root = root.right
            elif key < root.key:
                root = root.left
            else:
                if root.left is None and root.right is None:
                    temp = self.TreeNode(root.key, root.value)
                    del root
                    return temp.key, temp.value
                elif root.left is None:
                    root.key = root.right.key
                    root.value = root.right.value
                elif root.right is None:
                    root.key = root.left.key
                    root.value = root.left.value
                else:
                    right_min = root.right
                    node = root.right
                    while node is not None:
                        if node > node.right:
                            right_min = node.right
                        node = node.right
                    root.key = right_min.key
                    self.remove(right_min.key, right_min)
            root.is_empty()

    def find(self, key: int):
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        root = self.root
        while root:
            if key == root.key:
                return root.value
            elif key < root.key:
                root = root.left
            elif key > root.key:
                root = root.right
        raise KeyError

    def __str__(self):
        return str(self.root)


if __name__ == '__main__':
    bst = BinarySearchTree()
    print(bst)
