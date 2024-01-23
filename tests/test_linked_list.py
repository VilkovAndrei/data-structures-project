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

    def test_to_list(self):
        ll3 = LinkedList()
        self.assertEqual(ll3.to_list(), [])

        ll3.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll3.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(ll3.to_list(), [{'id': 0, 'username': 'serebro'}, {'id': 2, 'username': 'mik.roz'}])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(10), {})
