#!/usr/bin/python3

class Node:
    """A node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data value to be stored in the node.
            next_node (Node, optional): The next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node.

        Args:
            value (int): The new data value to be set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Get the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The new next node to be set.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """A singly linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList with an empty head."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list (in increasing order).

        Args:
            value (int): The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Convert the linked list to a string representation.

        Returns:
            str: The string representation of the linked list.
        """
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
