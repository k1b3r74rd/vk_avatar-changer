from pathlib import Path
import os

counter = 0
directories = 0
path = Path(input('Enter your file directory: '))
filename = str(input('Enter yot file name:'))

for f in os.listdir(path):
    counter += 1
    os.rename(os.path.join(path, f),
              os.path.join(path, filename + str(counter) + '.jpg'))

