from binary import Binary
from buffer import Buffer
from directory import Directory
from log import Log


def test_directory():
    root = Directory('root')
    dir1 = Directory('dir1')
    root.append(dir1)
    assert root.name == 'root' and root.items[0].name == 'dir1'

    dir2 = Directory('dir2')
    dir1.append(dir2)
    assert dir1.items[0].name == 'dir2'

    dir1.move(dir2, root)
    assert len(root.items) == 2

    root.append(Binary("123", "123"))
    assert len(root.items) == 2

    root.delete(dir1)
    assert len(root.items) == 1

    root.append(123)
    assert len(root.items) == 1

    delete_test = False
    try:
        root.delete(dir1)
    except ValueError:
        delete_test = True

    assert delete_test


def test_binary():
    root = Directory('root')
    binary = Binary("123", "321")
    root.append(binary)
    assert binary.name == "123" and binary.readfile() == "321"
    error_test = False
    try:
        root.append(Binary(123, 123))
    except ValueError:
        error_test = True
    assert error_test


def test_log():
    log = Log("123", "321")
    assert log.name == "123" and log.readfile() == "321"

    log.append("456")
    assert log.readfile() == "321456"


def test_buffer():
    buffer = Buffer("123")
    assert buffer.consume() is None

    buffer.push(4355)
    assert buffer.consume() == 4355

    assert buffer.consume() is None
