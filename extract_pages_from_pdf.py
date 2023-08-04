import argparse
import fitz
import os

def extract_page_to_png(pdf_file, chapter, test, page_nums):
    doc = fitz.open(pdf_file) # type: ignore

    # Create the output directory if it doesn't exist
    output_dir = f"images/chapter{chapter}/test{test}"
    os.makedirs(output_dir, exist_ok=True)

    for page_num in page_nums:
        page = doc.load_page(page_num + 20)
        pix = page.get_pixmap(dpi=200)
        output = os.path.join(output_dir, f"{page_num}.png")
        print(output)
        pix.save(output)
    
    doc.close()

def parse_page_nums(page_num_arg):
    if '-' in page_num_arg:
        start, end = map(int, page_num_arg.split('-'))
        return list(range(start, end+1))
    else:
        return [int(page_num_arg)]

def main():
    parser = argparse.ArgumentParser(description='Extract pages from a PDF file and save them as PNG')
    parser.add_argument('pdf_file', type=str, help='The location of the PDF file')
    # parser.add_argument('output_dir', type=str, help='The directory to save the output PNG files')
    parser.add_argument('chapter', type=str, help='chapter number')
    parser.add_argument('test', type=str, help='test number')

    parser.add_argument('page_nums', type=parse_page_nums, help='The page number or range of pages to extract (e.g. 5 or 3-7)')

    args = parser.parse_args()

    extract_page_to_png(args.pdf_file, args.chapter, args.test, args.page_nums)

if __name__ == "__main__":
    main()
