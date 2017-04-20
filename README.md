pyQuickFileRenamer
==================
  A quick file renamer, use it to rename multiple files at once, remove unwanted characters or remove files with certain name constraints. It's useful for working with batch operations for renaming files, fileformats, etc. It also has functionalities to work with folders and to perform actions recursively.

## Usage ##
```bash
qfr.py [-h] [-R] [-F] (-rm string | -rs string | -rp string) dir
```

## Positional arguments: ##
  <b>dir</b>                   Directory to search for files.

## Optional arguments: ##
  <b>-h, --help</b>:            show this help message and exit

  <b>-R, --recursive</b>:       Operates recursively into the directory tree.

  <b>-F, --folder</b>:          Operates on folders as well.

  <b>-rm string, --removefile string</b>:
                        Removes a file based on a string search.

  <b>-rs string, --removestring string</b>:
                        Removes a string from the filename based on a string
                        search

  <b>-rp string, --replacestring string</b>:
                        Replaces a string in the filename based on a string
                        search

