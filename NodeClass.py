class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self._head = None

    def set_head(self, head):
        self._head = head

    def get_head(self):
        return self._head

    def add(self, val):
        """ Adds a node containing val to the linked list. """
        if self._head is None:
            self.set_head(Node(val))
            return
        return self.add_helper(val, self._head)

    def add_helper(self, val, current_node):
        if current_node.next is None:
            current_node.next = Node(val)
            return
        return self.add_helper(val, current_node.next)

    def insert(self, val, pos):

        if self._head is None:
            self._head = Node(val)
            return
        return self.insert_helper(val, self._head, pos, 0)

    def insert_helper(self, val, current_node, pos, current_pos):

        if current_pos + 1 == pos:
            temp = current_node.next
            new_node = Node(val)
            current_node.next = new_node
            new_node.next = temp
            return
        return self.insert_helper(val, current_node.next, pos, current_pos + 1)

    def remove(self, value):
        """ Removes the node containing val from the linked list. """
        if self._head is None:
            return None
        elif self._head.data is value and self._head.next is not None:      # removes only the first instance of data
            self._head = self._head.next
            return
        else:
            return self.remove_helper(value, self._head)

    def remove_helper(self, value, current_node):
        if current_node.next.data == value:
            current_node.next = current_node.next.next
            return current_node
        return self.remove_helper(value, current_node.next)

    def contains(self, key):
        """ Returns True if the list contains a node with the value key, otherwise return False. """
        return self.contains_helper(key, self._head)

    def contains_helper(self, key, current_node):
        if current_node is None:
            return False
        if current_node.data == key:
            return True
        return self.contains_helper(key, current_node.next)

    def to_plain_list(self):
        """ Returns a regular Python list containing the same values in the same order as the linked list. """
        result_list = []
        return self.to_plain_list_helper(result_list, self._head)

    def to_plain_list_helper(self, result_list, current_node):

        if current_node is None:
            return result_list
        result_list.append(current_node.data)
        return self.to_plain_list_helper(result_list, current_node.next)