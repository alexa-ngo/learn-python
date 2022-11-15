import unittest
from NodeClass import Node, LinkedList


class TestNodeClass(unittest.TestCase):

    def test_node(self):
        test_node = Node(8).data
        self.assertEqual(test_node, 8)

    def test_node_next(self):
        one_node = Node(3)
        test_node_next_none = one_node.next
        self.assertEqual(test_node_next_none, None)

    def test_get_head_empty(self):
        alexa_linked_list = LinkedList()
        self.assertEqual(alexa_linked_list is not None, True)

    def test_contains_one_node(self):
        alexa_linked_list = LinkedList()
        alexa_linked_list._head = Node(9)
        self.assertEqual(alexa_linked_list.get_head().data, 9)

    def test_make_list(self):
        first_node = Node(1)
        second_node = Node(2)
        third_node = Node(3)

        alexa_linked_list = LinkedList()
        alexa_linked_list._head = first_node
        first_node.next = second_node
        second_node.next = third_node
        self.assertEqual(second_node.next.data, 3)

    def test_to_plain_list_none(self):
        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(None)
        self.assertEqual(alexa_linked_list.to_plain_list(), [])


    def test_to_plain_list_4(self):
        first_node = Node(1)
        second_node = Node(2)
        third_node = Node(3)
        fourth_node = Node(4)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node
        self.assertEqual(alexa_linked_list.to_plain_list(), [1, 2, 3, 4])


    def test_to_plain_list_4(self):
        first_node = Node(0)
        second_node = Node(0)
        third_node = Node(4)
        fourth_node = Node(2)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node
        self.assertEqual(alexa_linked_list.to_plain_list(), [0,0,4,2])


    def test_to_plain_list_five_nodes(self):
        first_node = Node(1)
        second_node = Node(2)
        third_node = Node(3)
        forth_node = Node(4)
        fifth_node = Node(5)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = forth_node
        forth_node.next = fifth_node
        self.assertEqual(third_node.data, 3)

    def test_contains_none(self):
        first_node = Node(1)
        second_node = Node(2)
        third_node = Node(3)
        forth_node = Node(4)
        fifth_node = Node(5)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = forth_node
        forth_node.next = fifth_node

        test_contains_none = alexa_linked_list.contains(None)
        test_contains_488 = alexa_linked_list.contains(488)
        test_contains_4 = alexa_linked_list.contains(4)
        test_contains_99 = alexa_linked_list.contains(99)

        self.assertEqual(test_contains_none, False)
        self.assertEqual(test_contains_488, False)
        self.assertEqual(test_contains_4, True)
        self.assertEqual(test_contains_99, False)


    def test_add_one(self):
        first_node = Node(1)
        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)

        alexa_linked_list.add(1)
        self.assertEqual(first_node.data, 1)

    def test_add_two_nodes(self):
        first_node = Node(1)
        second_node = Node(2)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        alexa_linked_list.add(2)

        self.assertEqual(second_node.data, 2)

    def test_add_four_nodes(self):
        first_node = Node(3)
        second_node = Node(26)
        third_node = Node(88)
        fourth_node = Node(91)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)

        alexa_linked_list.add(third_node)
        alexa_linked_list.add(fourth_node)

        self.assertEqual(fourth_node.data, 91)

    def test_insert_first_node_in_empty(self):
        alexa_linked_list = LinkedList()
        alexa_linked_list.insert(99, 4)
        self.assertEqual(alexa_linked_list.get_head().data, 99)

    def test_insert_second_node_in_list_with_one_node(self):
        first_node = Node(3)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        alexa_linked_list.add(26)
        alexa_linked_list.insert(9,1)
        self.assertEqual(first_node.next.data, 9)

    def test_insert_into_last(self):
        first_node = Node(2)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        alexa_linked_list.add(33)
        alexa_linked_list.add(11)

        alexa_linked_list_head = alexa_linked_list.get_head()

        alexa_linked_list.insert(888, 2)
        self.assertEqual(alexa_linked_list_head.next.next.data, 888)

    def test_insert_into_between(self):
        first_node = Node(2)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        alexa_linked_list.add(33)

        alexa_linked_list_head = alexa_linked_list.get_head()

        alexa_linked_list.insert(999, 1)
        self.assertEqual(alexa_linked_list_head.next.data, 999)

    def test_remove_no_node(self):
        alexa_linked_list = LinkedList()

        alexa_linked_list_head = alexa_linked_list.get_head()
        alexa_linked_list.remove(None)
        self.assertEqual(alexa_linked_list_head, None)

    def test_remove_first_node_of_two_nodes(self):
        first_node = Node(2)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        alexa_linked_list.add(4)

        alexa_linked_list.remove(2)
        alexa_linked_list_head = alexa_linked_list.get_head()
        self.assertEqual(alexa_linked_list_head.data, 4)

    def test_remove_node_four(self):
        first_node = Node(2)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        alexa_linked_list.add(4)
        alexa_linked_list.add(5)
        alexa_linked_list.add(99)
        alexa_linked_list.remove(99)
        alexa_linked_list_head = alexa_linked_list.get_head()
        self.assertEqual(alexa_linked_list_head.next.next.data, 5)

    def test_remove_second_node_of_three(self):
        first_node = Node(2)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        alexa_linked_list.add(33)
        alexa_linked_list.add(44)

        alexa_linked_list.remove(33)
        alexa_linked_list_head = alexa_linked_list.get_head()
        self.assertEqual(alexa_linked_list_head.next.data, 44)

    def test_remove_second_node_of_three(self):
        first_node = Node(2)

        alexa_linked_list = LinkedList()
        alexa_linked_list.set_head(first_node)
        alexa_linked_list.add(33)
        alexa_linked_list.add(44)

        alexa_linked_list.remove(44)
        alexa_linked_list_head = alexa_linked_list.get_head()
        self.assertEqual(alexa_linked_list_head.next.next, None)


if __name__ == '__main__':
    unittest.main()