from paddleocr import PaddleOCR
from utils import is_english_compound_word, is_english_word, is_alpha_string

def process_image(img_path, printable=False):
    ocr = PaddleOCR(lang="en", show_log=False, use_angle_cls=False)
    result = ocr.ocr(img_path)

    items = []
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            location, result = line
            word,confidence = result
            word = word.strip()
            left_top,right_top,right_bottom,left_bottom = location
            x,y = left_top
            # print(word)
            if is_alpha_string(word) and len(word) in [3,4]:
                print(word, is_alpha_string(word), img_path)
            # if is_english_compound_word(word) or is_english_word(word):
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
        page_words.append([item[2] for item in line])
        if printable:
            print(', '.join([item[2] for item in line]))
    return page_words

# process_image('test_images/29.png',True)
# process_image('images/chapter3/test4/40.png')