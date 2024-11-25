import argparse
import logging
from sys import exit

import pypdf

log = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs=2, help="the two (odd pages, even pages) PDF files to combine")
    parser.add_argument("-o", "--output", help="output pdf file")
    parser.add_argument("--no-reverse", help="do not reverse second document page order", action="store_true")
    args = parser.parse_args()

    # read PDF documents
    try:
        inp1 = pypdf.PdfReader(args.files[0])
    except FileNotFoundError:
        log.error(f"File {args.files[0]} not found")
        exit(-1)
    try:
        inp2 = pypdf.PdfReader(args.files[1])
    except FileNotFoundError:
        log.error(f"File {args.files[1]} not found")
        exit(-1)

    out = pypdf.PdfWriter()

    pages = zip(inp1.pages, inp2.pages if args.no_reverse else inp2.pages[::-1])
    for page in pages:
        out.add_page(page[0])
        out.add_page(page[1])

    with open(args.output, "wb") as f:
        out.write(f)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
