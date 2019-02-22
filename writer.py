# writer.py
# Writes to a file

class Writer:

    def __init__(self, path):
        """Creates or overwrites (cleans) the file that will be written to."""
        self.path = path
        self.file = open(self.path, "w")
        print("Opened file:", self.path)

    def write_line(self, line):
        """Writes string to file and moves to next line."""
        self.file.write(line + "\n")

    def __del__(self):
        """Required deconstructor to close the file stream."""
        self.file.close()
        print("Closing file:", self.path)