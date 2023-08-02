from paddleocr import PaddleOCR
from .utils import is_alpha_string


ocr = PaddleOCR(lang="en", show_log=False)
# img_path = 'chapter3_test1_page1.png'
img_path = '29.png'

result = ocr.ocr(img_path)

items = []
nltked_items = []
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        location, result = line
        word,confidence = result
        left_top,right_top,right_bottom,left_bottom = location
        x,y = left_top

        if is_alpha_string(word):
            items.append((x, y, word))

# Sort items by x-coordinate then y-coordinate
items.sort(key=lambda item: (item[1], item[0]))

# Create list of lines
lines = []
current_line = []

# Threshold for y-coordinate difference
threshold = 10

for item in items:
    if not current_line or abs(item[1] - current_line[-1][1]) <= threshold:
        current_line.append(item)
    else:
        lines.append(current_line)
        current_line = [item]

if current_line:
    lines.append(current_line)

page_words = []
for line in lines:
    line.sort(key=lambda item: item[0])
    # print(', '.join(item[2] for item in line))
    page_words.append([item[2] for item in line])
