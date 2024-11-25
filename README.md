# PDF SCAN MERGE

This script allows to combine into a single PDF document the result of the scan of a double sided document, when the
scanner has not option to scan both faces.

The user have to scan the odd pages, then the even pages into two separate batches, then combine both using this tool.

Of course, when the user starts scanning the even pages, he will scan the document by flipping the stack of pages,
therefore the stack shows even pages in reverse order, from the last page to the first one.

This tool reverses by default the page order of the even-page document before merging.

Usage:

```
pdf-merge odd-pages.pdf even-pages.pdf -o combined_doc.pdf [--no-reverse]
```

