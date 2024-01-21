class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.all = []
        self.head = None
        self.tail = None

    def __iter__(self):
        """Возвращает итератор."""
        self.current_value = self.head
        return self

    def __next__(self):
        """Возвращает следующий элемент.

        Returns:
            int: Следующее четное число.

        Raises:
            StopIteration: Если достигнут последний элеммент.
        """
        if not self.current_value.next_node:
            self.current_value = self.current_value.next_node
            return self.current_value
        else:
            raise StopIteration

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.all.append(data)
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.tail.next_node = None
            self.all.append(data)

    def dequeue(self):
        """
        Метод для удаления элемента из головы очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            popped_node = self.head
            self.head = self.head.next_node
            del self.all[0]

            return popped_node.data

    def del_node_queue(self, deleted_index=0):
        """
        Метод для удаления элемента из очереди по индексу. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            if deleted_index >= len(self.all):
                raise ValueError(f'Число должно быть меньше {len(self.all)}')
            elif deleted_index < 0:
                raise ValueError('Число должно быть неотрицательным')
            deleted_node = self.head
            forward_node = None
            for index in range(0, deleted_index):
                forward_node = deleted_node
                deleted_node = deleted_node.next_node
            if deleted_node == self.tail:
                self.tail = forward_node
                self.tail.next_node = None
            if forward_node:
                forward_node.next_node = deleted_node.next_node
            del self.all[deleted_index]

            return deleted_node.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""

        result_list = []
        if not self.head:
            return ""
        else:
            result_list.append(self.head.data)
            current_node = self.head.next_node
            while current_node:
                result_list.append(current_node.data)
                current_node = current_node.next_node
            result = "\n".join(result_list)
            return result
