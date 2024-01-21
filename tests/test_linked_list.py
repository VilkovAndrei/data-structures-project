import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_LinkedList_insert_beginning(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1})
        self.assertEqual(str(ll), "{'id': 1} -> None")

        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> None")

    def test_LinkedList_insert_at_end(self):
        ll2 = LinkedList()

        ll2.insert_at_end({'id': 2})
        self.assertEqual(str(ll2), "{'id': 2} -> None")

        ll2.insert_at_end({'id': 3})
        self.assertEqual(str(ll2), "{'id': 2} -> {'id': 3} -> None")
