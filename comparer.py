"""

comparer.py

Function:
* Compares two files.

Usage:
* python3 comparer.py ... ...
                   ...add/Add.cack ...add/Add.hack
* or import comparer.py and use the compare function

"""


def compare(file_path1, file_path2):
    """Takes into two file paths and compares the two files line by line."""
    file1, file2 = open(file_path1), open(file_path2)

    lines1, lines2 = file1.readlines(), file2.readlines()

    for i, line1 in enumerate(lines1):
        if line1 != lines2[i]:
            print("Comparison failure at line", i+1)
            return False
    print("Comparison success.")
    return True

def main():
    import sys

    args = sys.argv
    file_path1, file_path2 = args[1], args[2]

    compare(file_path1, file_path2)

if __name__ == "__main__":
    main()
