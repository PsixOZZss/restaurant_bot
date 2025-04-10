class DoubleWrite:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def write(self, s):
        self.file1.write(s)
        self.file2.write(s)

    def flush(self):
        self.file1.flush()
        self.file2.flush()
