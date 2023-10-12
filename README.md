# GlassVector
is a Python package that provides a simple and efficient way to store and retrieve vectors in a database.

## Features
- Store vectors with associated metadata in a database.
- Efficiently query vectors based on similarity or other criteria.
- Supports various distance metrics for similarity search.
- Easy-to-use API for adding, updating, and querying vectors.

## Installation

You can install VectorDatabase using pip:
```sh 
pip install glassvector
```

## Usage

Here's a simple example of how to use GlassVector:

```python
from glassvector import GlassVector
```
### Create a new database

```python
db = VectorDatabase()
```
### Add vectors to the database

```python
db.insert('vector1', [1.0, 2.0, 3.0])
```

### Print the results

```python
print(db.get('vector1'))  # Output: [1.0, 2.0, 3.0]
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.



