import pytest
from MySet import MySet

def test_init():
    s = MySet()
    assert s.size() == 0

def test_init_with_list():
    s = MySet([1, 2, 3])
    assert s.size() == 3

def test_init_with_duplicates():
    s = MySet([1, 2, 2, 3, 3])
    assert s.size() == 3

def test_has():
    s = MySet([1, 2, 3])
    assert s.has(1)
    assert not s.has(4)

def test_add():
    s = MySet()
    s.add(1)
    assert s.has(1)
    assert s.size() == 1

def test_add_duplicate():
    s = MySet([1, 2, 3])
    s.add(1)
    assert s.size() == 3

def test_delete():
    s = MySet([1, 2, 3])
    s.delete(2)
    assert s.size() == 2
    assert not s.has(2)

def test_delete_nonexistent():
    s = MySet([1, 2, 3])
    s.delete(4)
    assert s.size() == 3

def test_size():
    s = MySet([1, 2, 3])
    assert s.size() == 3

def test_clear():
    s = MySet([1, 2, 3])
    s.clear()
    assert s.size() == 0