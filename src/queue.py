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
        pass

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if self.head is None:
            self.head = node
            self.tail = node
            self.all.append(data)
        else:
            self.tail.next_node = node
            self.tail = node
            self.all.append(data)
        def enqueue(self, data):
            new_data = Node(data)
            if self.head is None:
                self.head = new_data
                self.tail = self.head
            else:
                self.tail.next = new_data
                self.tail = new_data

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        pass
