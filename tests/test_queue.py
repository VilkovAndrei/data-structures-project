import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def test_Queue(self):
        queue1 = Queue()
        queue1.enqueue('data1')
        queue1.enqueue('data2')
        queue1.enqueue('data3')
        queue1.enqueue('data4')
        self.assertEqual(str(queue1), 'data1\ndata2\ndata3\ndata4')
        self.assertEqual(queue1.head.data, 'data1')
        self.assertEqual(queue1.tail.data, 'data4')
        self.assertEqual(queue1.head.next_node.data, 'data2')
        self.assertEqual(queue1.head.next_node.next_node.data, 'data3')
        self.assertEqual(queue1.dequeue(), 'data1')
        self.assertEqual(queue1.del_node_queue(1), 'data3')
        self.assertEqual(str(queue1), 'data2\ndata4')
        self.assertEqual(queue1.del_node_queue(1), 'data4')
        self.assertEqual(str(queue1), 'data2')
