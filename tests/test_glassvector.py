import unittest
from glassvector import GlassVector

class GlassVectorTests(unittest.TestCase):
    def setUp(self):
        self.db = GlassVector()

    def test_insert(self):
        self.db.insert('vector1', [1.0, 2.0, 3.0])
        self.assertEqual(self.db.size(), 1)

    def test_get(self):
        self.db.insert('vector1', [1.0, 2.0, 3.0])
        vector = self.db.get('vector1')
        self.assertEqual(vector, [1.0, 2.0, 3.0])

    def test_update(self):
        self.db.insert('vector1', [1.0, 2.0, 3.0])
        self.db.update('vector1', [4.0, 5.0, 6.0])
        vector = self.db.get('vector1')
        self.assertEqual(vector, [4.0, 5.0, 6.0])

    def test_remove(self):
        self.db.insert('vector1', [1.0, 2.0, 3.0])
        self.db.remove('vector1')
        vector = self.db.get('vector1')
        self.assertIsNone(vector)

    def test_size(self):
        self.assertEqual(self.db.size(), 0)
        self.db.insert('vector1', [1.0, 2.0, 3.0])
        self.assertEqual(self.db.size(), 1)
        self.db.insert('vector2', [4.0, 5.0, 6.0])
        self.assertEqual(self.db.size(), 2)
        self.db.remove('vector1')
        self.assertEqual(self.db.size(), 1)

if __name__ == '__main__':
    unittest.main()
