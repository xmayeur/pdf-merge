# PDF  MERGE

This script allows combining multiple PDF files into a single PDF document

There are two basic alternatives:

### 1- Append merge (option -a)

Files are simply appended one after each others.


    pdf-merge -a file1.pdf file2.pdf file3.pdf ... -o merged_doc.pdf

or

    pdf-merge -a file_pattern*.pdf -o merged_doc.pdf

### 2- Combined merge (two files only, option -c)

Files are combined, each page of the second document is added after each corresponding page of the first one.

This is essentially used to recombine into a single document the consecutive scans of all odd, then all even pages
stored into two separate documents.
This is the case when a scanner is not able to perform double-face scan operation.

Of course, when the user starts scanning the even pages, he will scan the document by flipping the stack of pages,
therefore the stack shows even pages in reverse order, from the last page to the first one.

This tool reverses by default the page order of the even-page document before merging.


    pdf-merge -c odd-pages.pdf even-pages.pdf -o combined_doc.pdf

### USAGE

```
usage: pdf-merge [-h] [-o OUTPUT] [--no-reverse] [-a] [-c] [-e] [-p PASSWORD] files [files ...]

positional arguments:
  files                 the two (odd pages, even pages) PDF files to combine

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output pdf file
  --no-reverse          do not reverse second document page order
  -a, --append          Just append files after each others
  -c, --combined        Combined ood and even pages files
  -e, --encrypt         Encrypt output file
  -p PASSWORD, --password PASSWORD
```

---

    --no-reverse

This option, in conjunction with the `-c` option does not reverse the page of the even-pages documents

---
    --encrypt, -e

Encrypt the output document with the provided password.

Algorithm is `AES-256-R5`

---
    --password, -p

Provide an encryption password. If omitted when using the `-e` option, a password will be prompted

---