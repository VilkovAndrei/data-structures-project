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
            return popped_node.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""

        result_list = []
        if self.head == None:
            return ""
        else:
            result_list.append(self.head.data)
            current_node = self.head.next_node
            while current_node != None:
                result_list.append(current_node.data)
                current_node = current_node.next_node

            result = "\n".join(result_list)
            return result
