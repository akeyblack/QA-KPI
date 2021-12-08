from directory import Directory
from binary import Binary
from buffer import Buffer
from log import Log


if __name__ == '__main__':
    root = Directory("root")
    dir1 = Directory('dir1')

    root.append(dir1)
    root.append(Directory("dir2"))

    buffer = Buffer("buff")
    buffer.push(123)

    dir1.append(Buffer("buff"))

    dir3 = Directory('dir3')

    dir1.append(dir3)
    dir3.append(Binary("bin", "haha"))
    dir3.append(Log("log", "1.Something\n2.Something new"))
    root.get_content()
