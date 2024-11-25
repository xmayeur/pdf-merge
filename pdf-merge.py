import argparse
import logging
import warnings
from getpass import getpass
from glob import glob
from sys import exit

import pypdf

warnings.filterwarnings("ignore")
log = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='+', help="the two (odd pages, even pages) PDF files to combine")
    parser.add_argument("-o", "--output", help="output pdf file", default="merged-pdf.pdf")
    parser.add_argument("--no-reverse", help="do not reverse second document page order", action="store_true")
    parser.add_argument("-a", "--append", help="Just append files after each others", action="store_true")
    parser.add_argument("-c", "--combined", help="Combined ood and even pages files", action="store_true")
    parser.add_argument('-e', '--encrypt', help="Encrypt output file", action="store_true")
    parser.add_argument('-p', '--password')
    args = parser.parse_args()

    out = pypdf.PdfWriter()
    if args.encrypt:
        if not args.password:
            p1 = getpass("Enter password: ")
            p2 = getpass("Re-enter password: ")
            if p1 != p2:
                log.error("Passwords do not match")
                exit(-1)
            args.password = p1
        out.encrypt(args.password, algorithm="AES-256-R5")

    if args.combined:
        # read PDF documents
        try:
            inp1 = pypdf.PdfReader(args.files[0], strict=True)
        except FileNotFoundError:
            log.error(f"File {args.files[0]} not found")
            exit(-1)
        except Exception as e:
            log.warning(f'Invalid PDF file {args.files[0]} - {e}')
            exit(-1)

        try:
            inp2 = pypdf.PdfReader(args.files[1], strict=True)
        except FileNotFoundError:
            log.error(f"File {args.files[1]} not found")
            exit(-1)
        except Exception as e:
            log.warning(f'Invalid PDF file {args.files[1]} - {e}')
            exit(-1)

        pages = zip(inp1.pages, inp2.pages if args.no_reverse else inp2.pages[::-1])
        for page in pages:
            out.add_page(page[0])
            out.add_page(page[1])

    elif args.append:
        if len(args.files) > 1:
            files = args.files
        else:
            files = glob(args.files[0])

        for pdf in files:
            try:
                out.append(pdf)
            except Exception as e:
                log.warning(f'Invalid PDF file {pdf} - {e}')
                continue

    with open(args.output, "wb") as f:
        out.write(f)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
