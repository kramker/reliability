import os
path = os.getcwd()
print(path)


def test_files():
    path1 = path[0:-5] + "reliability\\cli\\user"
    path2 = path[0:-5] + "reliability\\math\\api\\request"
    assert os.path.isdir(path1) == True, "Отсудствует папка по пути reliability\\cli\\user"
    assert os.path.isdir(path2) == True, "Отсудствует папка по пути reliability\\math\\api\\request"