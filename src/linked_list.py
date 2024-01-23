class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        """Конструктор класса LinkedList"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными
        в начало связанного списка
        """

        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными
        в конец связанного списка"""
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""

        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        """Метод возвращает список с данными,
        содержащимися в односвязном списке"""

        result_list = []
        if not self.head:
            return []
        else:
            result_list.append(self.head.data)
            current_node = self.head.next_node
            while current_node:
                result_list.append(current_node.data)
                current_node = current_node.next_node
            return result_list

    def get_data_by_id(self, v_id: int):
        """ Метод возвращает первый найденный в односвязном списке
            словарь с ключом 'id'
            или пустой список, если ключ не найден
        """
        ll_list = self.to_list()

        for next_dict in ll_list:
            try:
                value = next_dict['id']

            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
                continue
            else:
                if value == v_id:
                    return next_dict
                continue
        return {}
