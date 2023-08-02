import os
from process import process_image
from utils import save_to_file, natural_keys



from pathlib import Path

chapter = 3
test = 2

img_dir = f'images/chapter{chapter}_test{test}/'

# specify the directory you want to scan
directory = Path(img_dir)

# get a list of all files in the directory
files = [str(item) for item in directory.iterdir() if item.is_file()]
print(files)
files = sorted(files, key=natural_keys)

chapter_words = []

for f in files:
    output = process_image(str(f))
    chapter_words.append(output)

output_location = f'words/chapter{chapter}/test{test}.json'

output_directory = Path(output_location).parent
os.makedirs(str(output_directory), exist_ok=True)

save_to_file(chapter_words, output_location)
