import os


def cat(*args):
    """Simulate the cat command in Linux"""
    s = ""
    for filename in args:
        if not os.path.exists(filename):
            raise FileNotFoundError(filename)
        with open(filename, "rt") as f:
            s += f.read()

    lines = s.split("\n")
    lines = [l.strip() for l in lines]

    return lines


def write_list(lines: list, path: str):
    """Write a list of string to a file, with each element on each line"""
    with open(path, "wt") as f:
        for line in lines:
            f.write(str(line) + "\n") 
