class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data},{self.next}'