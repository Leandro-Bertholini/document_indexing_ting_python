from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        return self._queue.pop(0)

    def search(self, index):
        queue_data = len(self._queue)

        if index < 0 or index >= queue_data:
            raise IndexError("Índice Inválido ou Inexistente")
        return self._queue[index]
