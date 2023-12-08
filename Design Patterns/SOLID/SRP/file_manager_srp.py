import os
from pathlib import Path
from zipfile import ZipFile

"""The class has two different responsibilities. It uses the .read() and .write() methods to manage the file. It also deals with ZIP archives by providing the .compress() and .decompress() methods. """


class FileZIPManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding=encoding)

    def write(self, data, encoding="utf-8"):
        return self.path.write_text(data=data, encoding=encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


"""This class violates the single-responsibility principle because it has two reasons for changing its internal implementation.
To fix this issue and make your design more robust, you can split the class into two smaller, more focused classes, each with its own specific concern:"""


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding=encoding)

    def write(self, data, encoding="utf-8"):
        return self.path.write_text(data=data, encoding=encoding)


class ZipFileManager:
    def __init__(self, filename) -> None:
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file = FileManager(f"{BASE_DIR}/example.txt")

print(file.read())

file.write("TEST MESSAGE UPDATED")

print(file.read())
