# vector_database.py
class GlassVector:
    def __init__(self):
        self._data = {}

    def insert(self, id, vector):
        self._data[id] = vector

    def remove(self, id):
        del self._data[id]

    def get(self, id):
        return self._data.get(id)

    def update(self, id, vector):
        self._data[id] = vector

    def size(self):
        return len(self._data)
    