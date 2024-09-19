import importlib


def getModules(path):
    """get and import a list of python modules in the given path
    it is assumed that this method is called within a module
    (in most cases, __init__.py) in the given path.
    """
    import os

    rt = []
    for entry in os.listdir(path):
        f = os.path.join(path, entry)
        if os.path.isdir(f):
            continue
        if entry == "__init__.py":
            continue
        modulename, ext = os.path.splitext(entry)
        if ext not in [".py", ".pyc"]:
            continue
        m = importlib.import_module(
            ".{}".format(modulename), "histogram.ndarray.converters"
        )
        rt.append(m)
        continue
    return rt


def test_getModules():
    print(getModules("."))
    return


def main():
    test_getModules()
    return


if __name__ == "__main__":
    main()
