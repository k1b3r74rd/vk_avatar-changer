import os, glob
from pathlib import Path


class Program:
    def __init__(self, path: Path):
        self.path = path

    @staticmethod
    def counter(self):
        count = 0
        for f in os.listdir(self.path):
            count += 1
        print(count)


print(Program(r'E:\program\memes'))



