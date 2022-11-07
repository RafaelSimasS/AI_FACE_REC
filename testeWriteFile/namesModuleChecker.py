import os, fnmatch


def find(type, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, type):
                result.append(os.path.join(root, name))
    return result
